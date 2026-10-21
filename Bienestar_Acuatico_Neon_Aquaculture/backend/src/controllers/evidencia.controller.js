/* =====================================================================
   Controlador · evidencias
   ===================================================================== */
import evidenciaService from "../services/evidencia.service.js";
import { asyncHandler, ok, creado } from "../utils/http.js";

export const subir = asyncHandler(async (req, res) => {
  const respuestaId = Number(req.body.respuesta_id || req.query.respuesta_id);
  return creado(res, await evidenciaService.subir(respuestaId, req.file, req.usuario));
});

export const listar = asyncHandler(async (req, res) =>
  ok(res, await evidenciaService.listar(Number(req.params.respuestaId)))
);

export const eliminar = asyncHandler(async (req, res) =>
  ok(res, await evidenciaService.eliminar(Number(req.params.id), req.usuario))
);

export default { subir, listar, eliminar };
