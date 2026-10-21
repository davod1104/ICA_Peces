# Bienestar Acuático — Neon Aquaculture

Prototipo académico para registrar predios, diligenciar evaluaciones de bienestar en peces de cultivo, visualizar resultados, gestionar recomendaciones e imprimir informes/constancias simuladas. Está basado en la Metodología ICA v2.0 (2024); **no es un sistema oficial del ICA**.

El proyecto se puede usar de dos formas: **solo frontend** (abriendo `index.html`, con persistencia en el navegador) o con el **backend opcional** Node.js + Express + PostgreSQL que añade autenticación real, base de datos relacional y API REST. En ambos casos la interfaz y las reglas de cálculo son las mismas.

## Abrir el proyecto (solo frontend)

1. Descomprime el ZIP completo en una carpeta.
2. Abre `index.html` en un navegador moderno (Chrome, Edge o Firefox).
3. Para persistencia local, utiliza siempre el mismo navegador y perfil. Si el navegador limita el almacenamiento al abrir `file://`, sirve la carpeta con un servidor estático local. No requiere backend ni base de datos remota.

## Ejecutar con backend (Node.js + Express + PostgreSQL)

Requiere Node.js ≥ 20 y PostgreSQL ≥ 14 (o Docker). Desde la raíz del proyecto:

1. Levanta PostgreSQL. Con Docker: `docker compose up -d` (publica la base en `localhost:5432`).
2. En `backend/`, copia el entorno y arranca:

   ```bash
   cd backend
   cp .env.example .env      # PowerShell: Copy-Item .env.example .env
   npm install
   npm run setup             # migra el esquema y siembra catálogos + datos demo
   npm start                 # API y frontend en http://localhost:4000
   ```

3. Abre `http://localhost:4000/`. La API queda en `http://localhost:4000/api` y el estado en `http://localhost:4000/api/salud`.

El detalle de variables de entorno, endpoints, roles y modo offline está en `backend/README.md` y `docs/PLAN_IMPLEMENTACION.md`. El frontend detecta la API automáticamente (`APP_CONFIG.MODO = "auto"`); si no responde, sigue funcionando en local. Se puede forzar con `index.html?modo=local`.

## Usuarios de demostración

Estas cuentas son ficticias y se cargan al inicializar los datos de demostración:

| Perfil | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin@ica.demo` | `admin123` |
| Docente | `docente@ica.demo` | `docente123` |
| Estudiante evaluador | `evaluador@ica.demo` | `1234` |
| Consultor externo | `consultor@ica.demo` | `consultor123` |

Son credenciales públicas para probar el prototipo, no para reutilizar como contraseñas reales. El inicio de sesión y los roles funcionan solo en el frontend local; no representan una frontera de seguridad robusta. **No publiques esta versión como servicio productivo ni guardes datos reales o sensibles en ella.**

## Datos y respaldos

Los datos de prueba y registros se guardan en `localStorage`; las evidencias se almacenan en `IndexedDB` cuando el navegador lo permite. Desde la administración se pueden utilizar las funciones disponibles para exportar/importar respaldos JSON y exportar el historial CSV. El almacenamiento local depende del navegador, puede borrarse y no equivale a una copia de seguridad remota.

Con el backend activo, la fuente de verdad pasa a ser PostgreSQL mediante la API REST; el `localStorage` actúa como caché y respaldo sin conexión. La interfaz se puede forzar a modo local con `index.html?modo=local`.

## Fotografías y modo sin conexión

El proyecto conserva la fotografía de peces `Im/Peces.JPG` aportada con el ZIP original e incorpora dos imágenes locales extraídas de la página inicial del PDF de metodología: un estanque de producción (`Im/sistemas/estanque-ica.jpg`) y un cardumen (`Im/peces/cardumen-ica.jpg`), con crédito fotográfico al ICA (2023), tal como aparece en el documento. La galería incluye además enlaces a imágenes de especies y sistemas en Wikimedia Commons con créditos y licencias documentados en `docs/CREDITOS_IMAGENES.md`.

El cardumen se usa como escena de fondo del hero de la landing y como tarjeta de la galería; el estanque aparece como cabecera de la sección de sistemas y como fondo de la guía visual de la metodología (botón «¿Cómo se evalúa?»).

Las imágenes locales funcionan sin conexión. Las fotos remotas de Wikimedia Commons requieren Internet; si un archivo no carga, algunas tarjetas muestran un respaldo visual local y otras dejan una superficie ilustrada en lugar de atribuir una foto incorrecta a una especie.

## Ejecutar las comprobaciones incluidas

Desde la carpeta raíz del proyecto, ejecuta `node tests/validation.js` para probar la lógica principal de cálculo y `python tests/check_assets.py` para revisar referencias locales. Los scripts usan herramientas estándar de Node.js y Python; no requieren instalar paquetes.

Desde `backend/`, `npm test` ejecuta las pruebas del servidor: cálculo ICA, muestreo, reglas y **equivalencia backend ↔ frontend** (mismos insumos, mismos puntajes) más comprobaciones HTTP. Las pruebas no necesitan una base de datos en marcha.

## Metodología

Consulta `docs/Metodologia_ICA_Bienestar_Peces_v2.pdf` y `docs/REVISION_METODOLOGIA.md`. El apartado general del PDF menciona 24 indicadores, mientras el conjunto detallado utilizado por el prototipo contiene 23 para PMG y 15 para AREL. Esta diferencia queda documentada para revisión académica; no se inventa un indicador adicional.

Ponderaciones configuradas: PMG 35/35/30 (MBR/MBA/MBG) y AREL 40/40/20. Los límites de clasificación son Bajo < 50 %, Medio desde 50 % y menor que 75 %, Alto desde 75 % y menor que 90 %, y Excelente desde 90 %.

## Limitaciones conocidas

- El muestreo AREL con cuatro o más lotes requiere confirmación del criterio académico aplicable: la tabla 30 consultada solo especifica qué hacer cuando hay menos de cuatro lotes.
- El documento combina una nota general de máximo 15 ejemplares por lote con una indicación específica de mínimo 15 ejemplares para tamaño y peso. Para este indicador el prototipo registra 15 y documenta la interpretación.
- Los parámetros del agua son referencias por especie y modalidad; no sustituyen una medición en el predio ni asesoría técnica profesional.
- Las constancias e informes impresos son simulaciones académicas y no documentos emitidos o avalados por el ICA.
- Debido a que no se pudo ejecutar un navegador real con acceso local en el entorno de construcción, se realizaron comprobaciones estáticas y pruebas de lógica en Node.js, pero no se afirma haber superado una revisión visual manual completa en Chrome.
