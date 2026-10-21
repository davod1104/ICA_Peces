/* =====================================================================
   Configuración de entorno · carga y valida variables .env
   ===================================================================== */
import dotenv from "dotenv";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const raiz = path.resolve(__dirname, "..", "..");

dotenv.config({ path: path.join(raiz, ".env") });

const aNumero = (v, def) => {
  const n = Number(v);
  return Number.isFinite(n) ? n : def;
};
const aBooleano = (v, def) => {
  if (v === undefined || v === "") return def;
  return /^(1|true|si|sí|yes)$/i.test(String(v));
};

const entorno = process.env.NODE_ENV || "development";

export const config = {
  entorno,
  produccion: entorno === "production",
  puerto: aNumero(process.env.PORT, 4000),

  db: {
    cadena: process.env.DATABASE_URL || "",
    host: process.env.PGHOST || "localhost",
    puerto: aNumero(process.env.PGPORT, 5432),
    usuario: process.env.PGUSER || "postgres",
    clave: process.env.PGPASSWORD || "postgres",
    base: process.env.PGDATABASE || "bienestar_acuatico",
  },

  jwt: {
    secreto: process.env.JWT_SECRET || "desarrollo_inseguro_cambiar",
    expira: process.env.JWT_EXPIRA || "8h",
  },

  cors: {
    origenes: (process.env.CORS_ORIGEN || "*")
      .split(",")
      .map((x) => x.trim())
      .filter(Boolean),
  },

  uploads: {
    dir: path.resolve(raiz, process.env.UPLOADS_DIR || "./uploads"),
    maxMB: aNumero(process.env.MAX_UPLOAD_MB, 15),
  },

  modoOfflinePermitido: aBooleano(process.env.MODO_OFFLINE_PERMITIDO, true),

  raiz,
  version: "2.0.0",
};

export function avisarConfiguracion() {
  const avisos = [];
  if (!config.db.cadena && !process.env.PGDATABASE) {
    avisos.push("No se definió DATABASE_URL ni PGDATABASE; se usarán los valores por defecto.");
  }
  if (!config.produccion && config.jwt.secreto.startsWith("desarrollo")) {
    avisos.push("JWT_SECRET no está definido; se usa un valor de desarrollo. No lo uses en producción.");
  }
  if (config.cors.origenes.includes("*") && config.produccion) {
    avisos.push("CORS_ORIGEN='*' en producción no es recomendable.");
  }
  return avisos;
}

export default config;
