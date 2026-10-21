/* =====================================================================
   Servicio · evaluaciones (creación, diligenciamiento, cierre)
   ===================================================================== */
import evaluacionRepo from "../repositories/evaluacion.repo.js";
import cat from "../repositories/indicador.repo.js";
import auditoriaRepo from "../repositories/auditoria.repo.js";
import { calcularEvaluacion } from "./calculo.service.js";
import { clasificar } from "../domain/clasificacion.js";
import { noEncontrado, validacion, conflicto } from "../utils/errores.js";
import { query } from "../config/db.js";

async function idModalidad(codigo) {
  const { rows } = await query("SELECT id FROM modalidad WHERE codigo = $1", [codigo]);
  return rows[0] ? rows[0].id : null;
}
async function idEspecie(nombreOCodigo) {
  if (!nombreOCodigo) return null;
  const { rows } = await query(
    "SELECT id FROM especie WHERE lower(codigo) = lower($1) OR lower(nombre_comun) = lower($1)",
    [nombreOCodigo]
  );
  return rows[0] ? rows[0].id : null;
}
async function idUsuarioPorNombre(nombre) {
  if (!nombre) return null;
  const { rows } = await query("SELECT id FROM usuario WHERE lower(nombre) = lower($1)", [nombre]);
  return rows[0] ? rows[0].id : null;
}

export async function listar(filtros = {}) {
  return evaluacionRepo.listar(filtros);
}

export async function porId(id) {
  const e = await evaluacionRepo.porId(id);
  if (!e) throw noEncontrado("Evaluación");
  return e;
}

export async function porIdConCalculo(id) {
  const e = await porId(id);
  return { evaluacion: e, calculo: await calcularEvaluacion(e) };
}

/** Respuestas crudas de una evaluación (sin calcular). */
export async function respuestas(id) {
  await porId(id); // valida existencia
  return evaluacionRepo.respuestasDe(id);
}

export async function crear(payload, usuario) {
  const predioId = payload.predioId || payload.pid;
  if (!predioId) throw validacion("Selecciona un predio.");
  if (!payload.fecha) throw validacion("Indica la fecha.");
  if (!payload.reg) throw validacion("Indica el tipo de evaluación.");

  const modalidadId = await idModalidad(payload.reg);
  if (!modalidadId) throw validacion("Modalidad no válida.");
  const especieId = await idEspecie(payload.esp || (payload.peces && payload.peces.esp));
  if (!especieId) throw validacion("Selecciona la especie.");
  if (!(Number(payload.lotes) > 0)) throw validacion("Indica el número de lotes sembrados.");

  const evaluadorId = (payload.ev && (await idUsuarioPorNombre(payload.ev))) || usuario.id;

  const id = await evaluacionRepo.crear({
    predioId,
    evaluadorId,
    modalidadId,
    especieId,
    fecha: payload.fecha,
    evaluadorNombre: payload.ev || usuario.nombre,
    lotes: Number(payload.lotes) || 0,
    estado: "en_proceso",
    sel: payload.sel || [],
    peces: payload.peces || null,
  });
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Evaluación creada (predio ${predioId})`, entidad: "evaluacion", entidadId: id });
  return porId(id);
}

export async function actualizar(id, payload, usuario) {
  const e = await porId(id);
  const campos = {};
  if (payload.fecha) campos.fecha = payload.fecha;
  if (payload.lotes !== undefined) campos.lotes = Number(payload.lotes) || 0;
  if (payload.estado) campos.estado = payload.estado;
  if (payload.etapa) campos.etapa = payload.etapa;
  if (payload.reg) campos.modalidadId = await idModalidad(payload.reg);
  await evaluacionRepo.actualizarCabecera(id, campos);
  if (Array.isArray(payload.sel)) await evaluacionRepo.reemplazarLotes(id, payload.sel);
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Evaluación editada: ${e.predio_nombre}`, entidad: "evaluacion", entidadId: id });
  return porId(id);
}

export async function eliminar(id, usuario) {
  const e = await porId(id);
  await evaluacionRepo.eliminar(id);
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Evaluación eliminada: ${e.predio_nombre}`, entidad: "evaluacion", entidadId: id });
  return { ok: true };
}

export async function guardarRespuesta(evalId, indicadorCodigo, datos, usuario) {
  const e = await porId(evalId);
  if (["validada", "cerrada"].includes(e.est))
    throw conflicto("La evaluación está validada o cerrada; no admite cambios.");
  const lista = await cat.indicadores({ modalidad: e.reg });
  const ind = lista.find((i) => i.codigo === indicadorCodigo);
  if (!ind) throw noEncontrado(`Indicador ${indicadorCodigo}`);

  const score = datos.score;
  const noAplica = datos.no_aplica === true || score === "NA";
  let puntaje = null;
  if (!noAplica) {
    if (score === undefined || score === null || score === "") throw validacion("Selecciona un resultado.");
    puntaje = Number(score);
    const validos = (ind.niveles || []).map((nv) => Number(nv.puntaje));
    if (!validos.includes(puntaje)) throw validacion("Puntaje no permitido para este indicador.");
  }

  await evaluacionRepo.upsertRespuesta(evalId, ind.id, {
    puntaje,
    noAplica,
    observacion: datos.obs || "",
    calc: datos.calc || null,
  });
  if (e.est === "borrador" || e.est === "en_proceso") {
    await evaluacionRepo.actualizarCabecera(evalId, { estado: "en_proceso" });
  }
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Indicador ${indicadorCodigo} guardado`, entidad: "respuesta", entidadId: evalId });
  return porId(evalId);
}

export async function finalizar(id, usuario, { reabrir = false } = {}) {
  const e = await porId(id);
  if (reabrir) {
    if (["validada", "cerrada"].includes(e.est)) throw conflicto("No se puede reabrir una evaluación validada o cerrada.");
    await evaluacionRepo.actualizarCabecera(id, { estado: "en_proceso" });
    await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Evaluación reabierta: ${e.predio_nombre}`, entidad: "evaluacion", entidadId: id });
    return porId(id);
  }
  const calc = await calcularEvaluacion(e);
  if (calc.pend) throw validacion("No se puede finalizar: hay indicadores pendientes o con puntuación inválida.");
  if (calc.gruposSinDato.length)
    throw validacion("No se puede finalizar: falta puntuación válida en " + calc.gruposSinDato.join(", ") + ".");
  await evaluacionRepo.actualizarCabecera(id, {
    estado: "finalizada",
    puntaje: Number(calc.total.toFixed(2)),
    clasificacion: clasificar(calc.total),
    cerrado: true,
  });
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Evaluación finalizada: ${e.predio_nombre}`, entidad: "evaluacion", entidadId: id });
  return { evaluacion: await porId(id), calculo: calc };
}

export async function cambiarEstado(id, nuevoEstado, usuario) {
  const permitidos = ["borrador", "en_proceso", "finalizada", "validada", "cerrada"];
  if (!permitidos.includes(nuevoEstado)) throw validacion("Estado no válido.");
  const e = await porId(id);
  const campos = { estado: nuevoEstado };
  if (["finalizada", "validada", "cerrada"].includes(nuevoEstado)) {
    const calc = await calcularEvaluacion(e);
    if (calc.isFinal) {
      campos.puntaje = Number(calc.total.toFixed(2));
      campos.clasificacion = clasificar(calc.total);
    }
  }
  await evaluacionRepo.actualizarCabecera(id, campos);
  await auditoriaRepo.registrar({ usuarioId: usuario.id, accion: `Estado → ${nuevoEstado}: ${e.predio_nombre}`, entidad: "evaluacion", entidadId: id });
  return porId(id);
}

/** Recalcula y almacena el puntaje global (sin cambiar de estado). */
export async function recalcular(id, usuario) {
  const e = await porId(id);
  const calc = await calcularEvaluacion(e);
  if (calc.isFinal) {
    await evaluacionRepo.actualizarCabecera(id, {
      puntaje: Number(calc.total.toFixed(2)),
      clasificacion: clasificar(calc.total),
    });
  }
  void usuario;
  return calc;
}

export default {
  listar, porId, porIdConCalculo, respuestas, crear, actualizar, eliminar, guardarRespuesta,
  finalizar, cambiarEstado, recalcular,
};
