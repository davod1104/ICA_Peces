/* =====================================================================
   Dominio · reglas de muestreo por modalidad
   PMG: <4 → todos · 4–9 → 3 · >9 → 4
   AREL: <4 → todos · ≥4 → sin definir (requiere verificación metodológica)
   ===================================================================== */

/**
 * @param {number} nLotes lotes sembrados
 * @param {"PMG"|"AREL"} modalidad
 * @returns {number|null} lotes a muestrear (n = todos) o null si no está definido
 */
export function muestreo(nLotes, modalidad = "PMG") {
  const n = Number(nLotes);
  if (!(n > 0) || !Number.isFinite(n)) return null;
  if (modalidad === "AREL") return n < 4 ? n : null;
  if (n < 4) return n;
  if (n <= 9) return 3;
  return 4;
}

/** Aplica una tabla de reglas (regla_muestreo) si se dispone de ella. */
export function muestreoDesdeReglas(nLotes, reglas) {
  const n = Number(nLotes);
  if (!(n > 0) || !reglas || !reglas.length) return null;
  const regla = reglas.find(
    (r) => n >= r.min_lotes && (r.max_lotes === null || n <= r.max_lotes)
  );
  if (!regla) return null;
  return regla.lotes_a_muestrear === null || regla.lotes_a_muestrear === undefined
    ? n
    : regla.lotes_a_muestrear;
}

export default { muestreo, muestreoDesdeReglas };
