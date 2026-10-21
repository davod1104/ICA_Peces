/* =====================================================================
   Pruebas HTTP mínimas: arranque de la app, salud, protección de rutas
   y 404. No requieren PostgreSQL (las rutas protegidas responden 401
   antes de tocar la base de datos).
   ===================================================================== */
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import app from "../src/app.js";

let servidor;
let base;

before(async () => {
  await new Promise((res) => {
    servidor = app.listen(0, () => {
      base = `http://127.0.0.1:${servidor.address().port}`;
      res();
    });
  });
});

after(async () => {
  await new Promise((res) => servidor.close(res));
});

test("GET /api/salud responde 200 con datos.ok", async () => {
  const r = await fetch(`${base}/api/salud`);
  assert.equal(r.status, 200);
  const j = await r.json();
  assert.equal(j.datos.ok, true);
  assert.ok(typeof j.datos.version === "string");
});

test("rutas protegidas sin token responden 401", async () => {
  for (const ruta of ["/api/predios", "/api/evaluaciones", "/api/usuarios", "/api/catalogos/indicadores"]) {
    const r = await fetch(`${base}${ruta}`);
    assert.equal(r.status, 401, `${ruta} debería ser 401`);
    const j = await r.json();
    assert.ok(j.error && j.error.codigo, `${ruta} debería devolver { error: { codigo } }`);
  }
});

test("ruta inexistente responde 404 con código", async () => {
  const r = await fetch(`${base}/api/no-existe`);
  assert.equal(r.status, 404);
  const j = await r.json();
  assert.equal(j.error.codigo, "RUTA_NO_ENCONTRADA");
});

test("el frontend estático se sirve en la raíz", async () => {
  const r = await fetch(`${base}/`);
  assert.equal(r.status, 200);
  const html = await r.text();
  assert.ok(html.includes("Bienestar Acuático"), "debe contener el título del prototipo");
});
