# -*- coding: utf-8 -*-
"""Contenido (requerimientos) del Manual de Usuario.

Fuente: "Requerimientos Aplicación ICA.docx" (PhD. Paola Andrea Valencia A.).
El documento define RF01-RF36, dos veces RF38 y RF40; no define RF37 ni RF39.
"""

MODULOS = []


def rf(cod, nombre, desc, shot, exp):
    return {"cod": cod, "nombre": nombre, "desc": desc, "shot": shot, "exp": exp}


def mod(numero, titulo, intro, rfs):
    MODULOS.append({"numero": numero, "titulo": titulo, "intro": intro, "rfs": rfs})


# ---------------------------------------------------------------- Módulo 1
mod(1, "Módulo 1 · Seguridad y usuarios",
    "Agrupa los requerimientos relacionados con el ingreso al sistema, la "
    "administración de roles y usuarios, y la recuperación de acceso.",
    [
        rf("RF01", "Gestión de autenticación",
           "El sistema debe permitir el inicio de sesión de usuarios mediante "
           "credenciales seguras.",
           "Pantalla de inicio de sesión, señalando los campos «Correo» y "
           "«Contraseña», el botón «Iniciar sesión» y el enlace «¿Olvidó su "
           "contraseña?».",
           "Abra la aplicación en el navegador; lo primero que verá es la pantalla "
           "de inicio de sesión. Escriba su correo electrónico y su contraseña en "
           "los campos «Correo» y «Contraseña» y presione el botón «Iniciar "
           "sesión». Si los datos son correctos, el sistema lo llevará al panel "
           "principal y habilitará el menú con los módulos que correspondan a su "
           "rol. Si el correo o la contraseña no coinciden, aparecerá un mensaje "
           "de error; verifique que el correo esté bien escrito y sin espacios "
           "adicionales, o use el enlace «¿Olvidó su contraseña?». Por seguridad, "
           "si permanece inactivo durante un tiempo la sesión se cierra y deberá "
           "ingresar de nuevo; también puede salir cuando quiera con la opción "
           "«Cerrar sesión» del menú superior."),
        rf("RF02", "Gestión de roles",
           "El sistema debe permitir administrar roles como administrador, "
           "docente, estudiante evaluador y consultor externo.",
           "Pantalla «Usuarios» del módulo de administración, con el listado y el "
           "desplegable de asignación de rol resaltado.",
           "El administrador es quien asigna el rol a cada persona. Ingrese con un "
           "perfil de administrador, abra el módulo «Administración» y entre a la "
           "sección «Usuarios»; allí verá el listado de usuarios registrados. Al "
           "crear o editar un usuario, seleccione en la lista desplegable el rol "
           "correspondiente: administrador (control total del sistema), docente "
           "(acompaña y supervisa los grupos), estudiante evaluador (diligencia "
           "las evaluaciones) o consultor externo (consulta resultados y "
           "reportes). Al guardar, cada usuario verá únicamente las opciones "
           "permitidas para su rol cuando inicie sesión; por ejemplo, un "
           "estudiante no podrá administrar catálogos ni gestionar usuarios."),
        rf("RF03", "Registro de usuarios",
           "El sistema debe permitir crear, editar, activar e inactivar usuarios.",
           "Formulario de creación de usuario y el interruptor «Activo / Inactivo» "
           "visible en la lista de usuarios.",
           "En «Administración» → «Usuarios», presione el botón «Nuevo usuario» "
           "para registrar una persona: complete el nombre, el correo, el rol y "
           "una contraseña inicial, y guarde. Para modificar datos, haga clic en "
           "el ícono de edición del usuario y actualice los campos. Si una persona "
           "deja de participar (por ejemplo, un estudiante que termina el curso), "
           "no elimine el registro: use el interruptor «Activo / Inactivo» para "
           "inactivarlo, así se conserva el historial de sus evaluaciones pero no "
           "podrá iniciar sesión. El mismo interruptor permite reactivarlo cuando "
           "sea necesario."),
        rf("RF04", "Recuperación de acceso",
           "El sistema debe permitir la recuperación de contraseña mediante correo "
           "electrónico.",
           "Ventana «Recuperar contraseña» con el campo de correo y el botón "
           "«Enviar enlace».",
           "Si olvidó su contraseña, en la pantalla de inicio de sesión presione "
           "el enlace «¿Olvidó su contraseña?». Escriba el correo con el que está "
           "registrado y confirme. El sistema enviará a esa dirección un mensaje "
           "con un enlace o una contraseña temporal para restablecer el acceso. "
           "Abra el correo, siga el enlace y defina una nueva contraseña. Si no "
           "recibe el mensaje, revise la carpeta de correo no deseado y confirme "
           "con el administrador que su correo está registrado correctamente."),
    ])

# ---------------------------------------------------------------- Módulo 2
mod(2, "Módulo 2 · Gestión de fincas",
    "Reúne el registro de las fincas, su ubicación geográfica, las especies "
    "presentes y el inventario animal.",
    [
        rf("RF05", "Gestión de fincas",
           "El sistema debe permitir registrar, consultar, editar y eliminar la "
           "información básica de una finca.",
           "Listado de fincas con los botones «Nueva finca», editar y eliminar, y "
           "el formulario de registro de una finca.",
           "Abra el módulo «Fincas». Para registrar una nueva, presione «Nueva "
           "finca» y complete los datos básicos: nombre o razón social, número de "
           "identificación (NIT o cédula), nombre del propietario, teléfono y "
           "correo de contacto. Guarde con el botón «Guardar». En la lista podrá "
           "consultar las fincas registradas, abrir el detalle de cada una, "
           "editarlas con el ícono de lápiz o eliminarlas con el ícono de "
           "papelera (el sistema pedirá confirmación antes de borrar). "
           "Recomendación: antes de eliminar, verifique que la finca no tenga "
           "evaluaciones asociadas, para no perder el historial."),
        rf("RF06", "Registro de ubicación de finca",
           "El sistema debe permitir registrar la ubicación geográfica de la "
           "finca: departamento, municipio, vereda, dirección y coordenadas "
           "opcionales.",
           "Sección «Ubicación» del formulario de finca, con los desplegables de "
           "departamento y municipio y los campos de vereda, dirección y "
           "coordenadas.",
           "Dentro del formulario de la finca, en la sección «Ubicación», "
           "seleccione el departamento y luego el municipio en las listas "
           "desplegables (el municipio se filtra según el departamento elegido). "
           "Escriba la vereda y la dirección. Si lo desea, registre las "
           "coordenadas geográficas (latitud y longitud) tomadas con un GPS o "
           "desde un mapa; son opcionales, pero facilitan ubicar la finca. Guarde "
           "los cambios. La ubicación quedará visible en el detalle de la finca y "
           "se usará en los reportes y en los filtros por zona."),
        rf("RF07", "Asociación de especies a la finca",
           "El sistema debe permitir asociar una o varias especies animales a una "
           "finca.",
           "Sección «Especies» dentro del detalle de la finca, con el botón "
           "«Agregar especie» y la lista de especies asociadas.",
           "Ingrese al detalle de la finca y abra la sección «Especies». Presione "
           "«Agregar especie» y seleccione de la lista la especie que se cría en "
           "esa finca (por ejemplo, peces, aves o cerdos). Puede repetir la "
           "operación para asociar varias especies a la misma finca. Cada especie "
           "asociada aparecerá en la lista y podrá retirarse si se deja de "
           "trabajar con ella. Esta asociación es la que permitirá, más adelante, "
           "generar la evaluación con la lista de chequeo correcta para cada "
           "especie."),
        rf("RF08", "Registro de inventario animal",
           "El sistema debe permitir registrar el inventario por especie, "
           "incluyendo el número de animales por categoría o grupo etario (edades).",
           "Formulario de inventario por especie, con las casillas por categoría "
           "etaria y el total calculado por el sistema.",
           "Con la especie ya asociada, abra la sección «Inventario». Seleccione la "
           "especie y registre cuántos animales hay en cada categoría o grupo de "
           "edad (por ejemplo, alevines, juveniles y adultos, o crías, levante y "
           "ceba, según la especie). Escriba la cantidad en cada casilla y guarde. "
           "El sistema sumará automáticamente el total de animales de la especie y "
           "mostrará el inventario consolidado de la finca. Mantenga este dato "
           "actualizado, porque sirve de contexto para interpretar los resultados "
           "de la evaluación."),
    ])

# ---------------------------------------------------------------- Módulo 3
mod(3, "Módulo 3 · Parametrización de especies",
    "Cada grupo de estudiantes configura su especie: la lista de verificación, "
    "los criterios e indicadores, las ponderaciones y los tipos de respuesta.",
    [
        rf("RF09", "Parametrización de especies",
           "El sistema debe permitir configurar listas de verificación "
           "diferenciadas por especie animal. Cada grupo de estudiantes parametriza "
           "su especie animal.",
           "Módulo de parametrización de especies, con la opción de habilitar la "
           "lista de verificación por especie.",
           "Abra el módulo «Parametrización» → «Especies». Cada grupo de "
           "estudiantes trabaja con una especie. Cree o seleccione la especie y "
           "habilite su lista de verificación propia: esta define qué se va a "
           "evaluar en esa especie. Guarde la configuración. A partir de ese "
           "momento, cuando se cree una evaluación para esa especie, el sistema "
           "cargará automáticamente su lista de verificación, sin afectar las "
           "listas de las demás especies."),
        rf("RF10", "Parametrización de criterios de evaluación",
           "El sistema debe permitir definir criterios, subcriterios, indicadores "
           "y preguntas para cada especie.",
           "Editor de criterios mostrando la jerarquía criterio → subcriterio → "
           "indicador → pregunta.",
           "Dentro de la parametrización de una especie, abra «Criterios». Cree los "
           "criterios de bienestar animal (por ejemplo, alimentación, sanidad o "
           "instalaciones) y, dentro de cada uno, agregue los subcriterios, los "
           "indicadores y las preguntas que se evaluarán. Para cada pregunta "
           "escriba el enunciado que verá el evaluador. Puede reordenar los "
           "elementos y agruparlos por secciones para que la evaluación se "
           "diligencie en el orden del documento de referencia. Guarde los "
           "cambios; la estructura quedará lista para usarse en las evaluaciones "
           "de esa especie."),
        rf("RF11", "Parametrización de ponderaciones",
           "El sistema debe permitir asignar pesos o ponderaciones a criterios, "
           "indicadores y dimensiones de bienestar animal.",
           "Pantalla de ponderaciones con la columna de peso (%) por criterio y el "
           "indicador de suma total.",
           "En la parametrización de la especie, abra «Ponderaciones». Asigne un "
           "peso a cada criterio, indicador o dimensión, según su importancia en "
           "el concepto de bienestar animal. Los pesos se expresan en porcentaje "
           "y, en cada nivel, el sistema verifica que la suma sea 100%. Presione "
           "«Guardar» cuando la suma sea correcta; si no, aparecerá una advertencia "
           "indicando el faltante o el exceso. Estas ponderaciones son las que el "
           "sistema usará después para calcular el puntaje final de la evaluación."),
        rf("RF12", "Parametrización de tipos de respuesta",
           "El sistema debe permitir definir preguntas con respuesta de tipo sí/no, "
           "selección única, selección múltiple, escala, numérica, textual y carga "
           "de evidencia, de acuerdo con el manual de Bienestar Animal asignado "
           "para la especie de cada grupo de estudiantes.",
           "Editor de pregunta con el desplegable «Tipo de respuesta» y los campos "
           "específicos de cada tipo.",
           "Al crear o editar una pregunta (dentro de los criterios), elija el "
           "«Tipo de respuesta» en la lista: Sí/No, selección única, selección "
           "múltiple, escala, numérica, textual o carga de evidencia. Según el "
           "tipo elegido, el sistema mostrará los campos necesarios: por ejemplo, "
           "las opciones disponibles en selección única o múltiple, los valores y "
           "las etiquetas de la escala, o el límite de números en la respuesta "
           "numérica. Si la pregunta admite evidencia, active la opción «Permitir "
           "adjuntar archivo». Guarde; el evaluador verá en cada pregunta el "
           "control correspondiente al tipo definido. Use el manual de Bienestar "
           "Animal asignado a la especie como guía para escoger el tipo adecuado."),
    ])

# ---------------------------------------------------------------- Módulo 4
mod(4, "Módulo 4 · Evaluación",
    "Comprende la creación de la evaluación, el diligenciamiento por secciones, "
    "el guardado parcial, las validaciones, las observaciones y las evidencias.",
    [
        rf("RF13", "Creación de evaluación",
           "El sistema debe permitir crear una evaluación nueva asociada a una "
           "finca y a una especie específica.",
           "Formulario «Nueva evaluación» con los selectores de finca y especie y "
           "el botón «Crear».",
           "Abra el módulo «Evaluaciones» y presione «Nueva evaluación». Seleccione "
           "la finca y la especie que va a evaluar (solo aparecerán las especies "
           "asociadas a esa finca), asígnele un nombre o identifíquela por la "
           "fecha y confirme. El sistema crea la evaluación en estado «Borrador» y "
           "abre la primera sección del formulario. Guarde para conservarla o "
           "continúe diligenciando de inmediato."),
        rf("RF14", "Selección de checklist por especie",
           "El sistema debe cargar automáticamente la lista de chequeo "
           "correspondiente a la especie seleccionada.",
           "Encabezado de la evaluación mostrando el nombre de la lista de chequeo "
           "cargada según la especie.",
           "Una vez elegida la especie al crear la evaluación, el sistema carga de "
           "manera automática la lista de chequeo parametrizada para esa especie: "
           "no es necesario elegirla manualmente. En la parte superior del "
           "formulario verá el nombre de la lista activa y el número de secciones o "
           "preguntas. Si la lista no aparece o está vacía, significa que la "
           "especie aún no tiene criterios parametrizados; en ese caso, regrese a "
           "«Parametrización» y complétela antes de continuar."),
        rf("RF15", "Registro secuencial de evaluación",
           "El sistema debe permitir diligenciar la evaluación por etapas o "
           "secciones, de acuerdo con el documento del ICA.",
           "Formulario por secciones con el menú de etapas y la barra de progreso "
           "de la evaluación.",
           "El formulario se presenta por secciones o etapas (por ejemplo, una por "
           "cada criterio del documento). Diligencie la sección actual respondiendo "
           "cada pregunta y avance con el botón «Siguiente» o seleccionando la "
           "sección en el menú lateral. Una barra de progreso le indicará cuánto "
           "lleva completado y cuánto falta. Puede moverse hacia adelante y hacia "
           "atrás entre secciones sin perder las respuestas ya registradas. Al "
           "llegar a la última sección, el botón «Finalizar» se habilitará "
           "únicamente cuando no falten campos obligatorios."),
        rf("RF16", "Guardado parcial de evaluación",
           "El sistema debe permitir guardar una evaluación parcialmente para "
           "continuarla después, registrando la fecha y la hora.",
           "Botón «Guardar borrador» y mensaje con la fecha y la hora del último "
           "guardado.",
           "Durante el diligenciamiento puede presionar «Guardar borrador» en "
           "cualquier momento para no perder el avance. El sistema registra la "
           "fecha y la hora del guardado y conserva las respuestas como evaluación "
           "«En proceso». Para continuar después, abra «Evaluaciones», busque la "
           "evaluación en el listado y presione «Continuar»; el formulario se "
           "abrirá en la última sección donde trabajó, con las respuestas ya "
           "diligenciadas. El sistema también guarda de forma automática y "
           "periódica mientras usted trabaja."),
        rf("RF17", "Validación de obligatoriedad",
           "El sistema debe validar que los campos obligatorios de la evaluación "
           "estén diligenciados antes de finalizarla.",
           "Aviso de validación con la lista de preguntas obligatorias pendientes "
           "resaltadas en rojo.",
           "Al presionar «Finalizar», el sistema revisa que todas las preguntas "
           "marcadas como obligatorias estén respondidas. Si falta alguna, no "
           "permitirá finalizar: mostrará un aviso y resaltará las preguntas "
           "pendientes, con un acceso directo a la sección correspondiente. "
           "Complete lo indicado y vuelva a presionar «Finalizar». Cuando todo esté "
           "diligenciado, el sistema cerrará la evaluación y pasará al cálculo de "
           "resultados."),
        rf("RF18", "Registro de observaciones",
           "El sistema debe permitir ingresar observaciones textuales por pregunta, "
           "criterio o evaluación general.",
           "Campo «Observaciones» bajo una pregunta y el campo de observaciones "
           "generales de la evaluación.",
           "Cada pregunta incluye un campo «Observaciones» donde puede escribir "
           "notas, aclaraciones o justificaciones de la respuesta. También hay un "
           "campo de observaciones generales al final de cada sección o de la "
           "evaluación. Escriba el texto y guárdelo; las observaciones quedarán "
           "asociadas a la pregunta o al criterio y aparecerán luego en el "
           "diagnóstico y en el reporte, como soporte de lo evaluado."),
        rf("RF19", "Carga de evidencias",
           "El sistema debe permitir adjuntar evidencias como fotografías, "
           "documentos o videos cortos asociados a preguntas o criterios.",
           "Zona de carga de evidencias con archivos adjuntos y sus miniaturas.",
           "Cuando una pregunta lo permita, use el botón «Adjuntar evidencia» para "
           "subir una fotografía, un documento o un video corto (según el tamaño "
           "máximo permitido). Seleccione el archivo de su equipo o dispositivo y "
           "espere a que termine la carga; verá una miniatura o el nombre del "
           "archivo con la opción de verlo, reemplazarlo o eliminarlo. Puede "
           "adjuntar varias evidencias por pregunta. Estas evidencias respaldan la "
           "evaluación y quedarán incluidas en el reporte."),
    ])

# ---------------------------------------------------------------- Módulo 5
mod(5, "Módulo 5 · Diagnóstico",
    "Presenta los resultados calculados: puntajes, nivel de bienestar, "
    "diagnóstico automático y hallazgos críticos.",
    [
        rf("RF20", "Cálculo automático de puntajes",
           "El sistema debe calcular automáticamente los puntajes parciales y "
           "totales de la evaluación según las reglas definidas.",
           "Pantalla de resultados con el puntaje total y el desglose por criterio.",
           "Al finalizar la evaluación, el sistema calcula los puntajes sin "
           "intervención del usuario. Primero obtiene un puntaje por cada criterio "
           "o dimensión, aplicando las ponderaciones definidas, y luego un puntaje "
           "total. Los resultados aparecen en la pantalla de «Resultados», con el "
           "detalle por criterio. Si más adelante corrige una respuesta (y la "
           "evaluación lo permite), el sistema recalcula automáticamente al "
           "guardar."),
        rf("RF21", "Clasificación del nivel de bienestar",
           "El sistema debe clasificar el resultado de la evaluación en niveles de "
           "desempeño o cumplimiento.",
           "Indicador de nivel de bienestar (etiqueta o semáforo) en la pantalla de "
           "resultados.",
           "Junto con el puntaje, la pantalla de resultados muestra el nivel de "
           "bienestar obtenido (por ejemplo, Bajo, Medio, Alto o Excelente, según "
           "la escala definida). El nivel se representa con un color y un ícono "
           "para identificarlo rápidamente. El usuario no asigna el nivel "
           "manualmente: lo determina el sistema a partir del puntaje total, de "
           "acuerdo con los rangos configurados en la parametrización."),
        rf("RF22", "Generación de diagnóstico",
           "El sistema debe generar un diagnóstico automático indicando fortalezas, "
           "incumplimientos, alertas críticas y oportunidades de mejora.",
           "Sección de diagnóstico con los bloques de fortalezas, incumplimientos, "
           "alertas críticas y oportunidades de mejora.",
           "Debajo de los resultados, el sistema presenta un diagnóstico redactado "
           "automáticamente. Se organiza en cuatro bloques: fortalezas (lo que "
           "cumple satisfactoriamente), incumplimientos (lo que no cumple), alertas "
           "críticas (los aspectos de mayor riesgo) y oportunidades de mejora. Lea "
           "cada bloque para entender en qué está bien la finca y qué debe "
           "corregirse. El diagnóstico se genera a partir de las respuestas y las "
           "reglas definidas, y sirve de base para las recomendaciones."),
        rf("RF23", "Identificación de hallazgos críticos",
           "El sistema debe identificar y resaltar los aspectos con mayor nivel de "
           "incumplimiento o riesgo.",
           "Listado de hallazgos críticos resaltados, con acceso al detalle de cada "
           "uno.",
           "El sistema resalta los hallazgos críticos, es decir, las preguntas o "
           "criterios con mayor incumplimiento o riesgo. Estos aparecen listados al "
           "inicio del diagnóstico y también señalados dentro del detalle de la "
           "evaluación. Haga clic en un hallazgo para ver la pregunta, su respuesta "
           "y las observaciones asociadas. Atienda estos puntos con prioridad, "
           "porque son los que más afectan el nivel de bienestar de la finca."),
    ])

# ---------------------------------------------------------------- Módulo 6
mod(6, "Módulo 6 · Recomendaciones con IA",
    "Genera, contextualiza y permite editar recomendaciones automáticas, y las "
    "convierte en un plan de mejora.",
    [
        rf("RF24", "Generación de recomendaciones con IA",
           "El sistema debe consumir una API de IA para generar recomendaciones "
           "automáticas a partir de los hallazgos detectados.",
           "Botón «Generar recomendaciones» y la lista de recomendaciones "
           "propuestas por la IA.",
           "En la pantalla de resultados, presione el botón «Generar "
           "recomendaciones». El sistema analizará los hallazgos detectados y, "
           "mediante un servicio de inteligencia artificial, propondrá "
           "recomendaciones automáticas para mejorar el bienestar animal. Mientras "
           "se generan, verá un indicador de progreso; al terminar, las "
           "recomendaciones aparecerán en una lista. Estas recomendaciones son un "
           "apoyo a la decisión y deben revisarse con criterio técnico; no "
           "reemplazan el juicio del evaluador."),
        rf("RF25", "Recomendaciones contextualizadas",
           "El sistema debe generar recomendaciones diferenciadas según especie, "
           "tipo de sistema productivo y resultados obtenidos.",
           "Lista de recomendaciones mostrando el contexto (especie, sistema "
           "productivo y criterio) que las origina.",
           "Las recomendaciones que genera el sistema no son genéricas: tienen en "
           "cuenta la especie evaluada, el tipo de sistema productivo de la finca y "
           "los resultados obtenidos. Por eso verá recomendaciones distintas para "
           "una finca de peces que para otra de aves, o según el nivel alcanzado en "
           "cada criterio. Revise que la información de especie y sistema "
           "productivo de la finca esté correctamente registrada, ya que de ello "
           "depende la pertinencia de las recomendaciones."),
        rf("RF26", "Edición de recomendaciones",
           "El sistema debe permitir que el evaluador revise, ajuste o complemente "
           "las recomendaciones generadas por IA.",
           "Recomendación en modo edición, con las opciones de modificar, eliminar "
           "y añadir recomendación manual.",
           "Cada recomendación generada por la IA es editable. Presione el ícono de "
           "edición para ajustar el texto, adaptarlo a las condiciones reales de la "
           "finca, complementarlo o eliminar las recomendaciones que no apliquen. "
           "También puede agregar recomendaciones propias con el botón «Añadir "
           "recomendación». Los cambios quedan a cargo del evaluador, de modo que "
           "el conjunto final de recomendaciones refleje su criterio profesional. "
           "Guarde cuando termine de revisar."),
        rf("RF27", "Generación de plan de mejora",
           "El sistema debe permitir convertir recomendaciones en acciones de "
           "mejora con responsable, prioridad y plazo.",
           "Tabla del plan de mejora con las columnas de acción, responsable, "
           "prioridad y plazo.",
           "Con las recomendaciones ya revisadas, presione «Crear plan de mejora». "
           "El sistema convierte cada recomendación en una acción de mejora. Para "
           "cada acción, asigne un responsable, establezca una prioridad (alta, "
           "media o baja) y fije un plazo o fecha límite. Puede editar el texto, "
           "agregar acciones adicionales y ajustar el orden. Guarde el plan; "
           "quedará asociado a la evaluación y podrá consultarse y actualizarse a "
           "medida que se cumplan las acciones."),
    ])

# ---------------------------------------------------------------- Módulo 7
mod(7, "Módulo 7 · Reportes y análisis",
    "Consulta del historial, comparación de evaluaciones, tablero de indicadores, "
    "reportes descargables, exportación y búsqueda.",
    [
        rf("RF28", "Consulta de historial",
           "El sistema debe permitir consultar el histórico de evaluaciones "
           "realizadas por finca y por especie.",
           "Pantalla de historial con los filtros de finca y especie y la lista "
           "cronológica de evaluaciones.",
           "Abra el módulo «Historial». Use los filtros para seleccionar la finca y "
           "la especie; el sistema mostrará las evaluaciones realizadas, ordenadas "
           "por fecha, con su puntaje y nivel de bienestar. Haga clic en cualquier "
           "registro para ver el detalle o abrir el reporte. También puede filtrar "
           "por rango de fechas o por estado. Así podrá ver la evolución de una "
           "finca a lo largo del tiempo."),
        rf("RF29", "Comparación entre evaluaciones",
           "El sistema debe permitir comparar resultados de distintas evaluaciones "
           "realizadas a la misma finca.",
           "Vista de comparación de dos evaluaciones con puntajes lado a lado y "
           "diferencias resaltadas.",
           "En el «Historial», marque dos o más evaluaciones de la misma finca con "
           "la casilla de selección y presione «Comparar». El sistema mostrará una "
           "vista lado a lado con los puntajes de cada evaluación, el nivel de "
           "bienestar y las diferencias por criterio, resaltando las mejoras y los "
           "retrocesos. Use esta comparación para verificar si las acciones de "
           "mejora aplicadas están dando resultado. Puede descargar la comparación "
           "como reporte."),
        rf("RF30", "Tablero de indicadores",
           "El sistema debe mostrar dashboards con indicadores agregados por finca, "
           "especie, zona o periodo.",
           "Tablero con gráficos de indicadores y filtros por finca, especie, zona "
           "y periodo.",
           "El módulo «Tablero» presenta gráficos e indicadores agregados. "
           "Seleccione los filtros de finca, especie, zona o periodo y el tablero "
           "se actualizará mostrando, por ejemplo, el promedio de puntaje, la "
           "distribución por nivel de bienestar y la cantidad de evaluaciones. Pase "
           "el cursor sobre los gráficos para ver los valores detallados. Este "
           "tablero le da una visión general rápida para tomar decisiones o "
           "presentar resultados."),
        rf("RF31", "Reporte descargable",
           "El sistema debe permitir generar reportes en PDF con el resumen de la "
           "evaluación, el diagnóstico y las recomendaciones.",
           "Botón «Generar reporte PDF» y vista previa del reporte generado.",
           "Abra la evaluación que desee y presione «Generar reporte PDF». El "
           "sistema armará un documento con el resumen de la evaluación, los "
           "resultados, el diagnóstico, las recomendaciones y el plan de mejora. "
           "Cuando esté listo, el archivo se descargará a su equipo o se abrirá en "
           "una nueva pestaña para verlo e imprimirlo. Verifique el nombre del "
           "archivo (incluye la finca y la fecha) y guárdelo donde lo necesite."),
        rf("RF32", "Exportación de datos",
           "El sistema debe permitir exportar datos a Excel o CSV para análisis "
           "posterior.",
           "Menú «Exportar» con las opciones Excel y CSV sobre un listado de "
           "resultados.",
           "En las pantallas con listados o resultados (historial, tablero), "
           "presione «Exportar» y elija el formato: Excel (.xlsx) o CSV. El sistema "
           "descargará un archivo con los datos que están en pantalla, respetando "
           "los filtros aplicados. Puede abrir el archivo en Excel o en otra "
           "herramienta para hacer análisis, gráficos o cruces de información. Si "
           "aplicó filtros, recuerde que la exportación solo incluye lo filtrado."),
        rf("RF33", "Búsqueda y filtrado",
           "El sistema debe permitir buscar y filtrar fincas, evaluaciones y "
           "resultados por diferentes criterios.",
           "Barra de búsqueda y panel de filtros, con etiquetas de los filtros "
           "activos.",
           "Cada módulo con listados incluye una barra de búsqueda y filtros. "
           "Escriba en el buscador el nombre de la finca o un texto relacionado y "
           "presione la lupa o la tecla Enter. Use los filtros (por especie, "
           "estado, fecha o zona) para acotar los resultados; puede combinarlos. "
           "Los filtros activos se muestran como etiquetas que puede quitar con un "
           "clic. Presione «Limpiar filtros» para volver a ver todo el listado."),
    ])

# ---------------------------------------------------------------- Módulo 8
mod(8, "Módulo 8 · Administración y notificaciones",
    "Trazabilidad, catálogos, estados de evaluación, certificación, gestión "
    "multi-especie y notificaciones del sistema.",
    [
        rf("RF34", "Trazabilidad de acciones",
           "El sistema debe registrar auditoría sobre creación, modificación y "
           "cierre de evaluaciones.",
           "Pantalla de auditoría con las columnas de usuario, acción, entidad y "
           "fecha y hora.",
           "El sistema guarda automáticamente un registro de auditoría de las "
           "acciones importantes (creación, modificación, finalización y cierre de "
           "evaluaciones, entre otras). Los administradores pueden consultarlo en "
           "«Administración» → «Auditoría», donde se ve quién hizo la acción, qué "
           "cambió y en qué fecha y hora. Este registro no se edita ni se elimina "
           "desde la interfaz; sirve para verificar el historial y respaldar la "
           "validez de las evaluaciones."),
        rf("RF35", "Gestión de catálogos",
           "El sistema debe permitir administrar catálogos como especies, "
           "municipios, tipos de productor, sistemas productivos y estados de "
           "evaluación.",
           "Módulo de catálogos con la lista de catálogos disponibles y el editor "
           "de valores.",
           "En «Administración» → «Catálogos» encontrará las listas maestras del "
           "sistema: especies, municipios, tipos de productor, sistemas productivos "
           "y estados de evaluación, entre otras. Seleccione el catálogo que desea "
           "gestionar y use «Agregar» para crear nuevos valores, el ícono de "
           "edición para corregirlos o el de eliminar para retirarlos (siempre que "
           "no estén en uso). Estos catálogos alimentan los formularios de toda la "
           "aplicación, así que manténgalos actualizados y consistentes."),
        rf("RF36", "Gestión de estados de evaluación",
           "El sistema debe manejar estados como borrador, en proceso, finalizada, "
           "validada y cerrada.",
           "Listado de evaluaciones con la etiqueta de estado y los botones "
           "«Validar» y «Cerrar».",
           "Cada evaluación tiene un estado que cambia según su avance: «Borrador» "
           "(recién creada), «En proceso» (con respuestas, aún sin finalizar), "
           "«Finalizada» (diligenciada y calculada), «Validada» (revisada y "
           "aprobada por un docente o administrador) y «Cerrada» (concluida, sin "
           "más cambios). El estado se muestra como una etiqueta de color en los "
           "listados. Según su rol, podrá cambiar el estado con los botones "
           "«Validar» o «Cerrar»; una evaluación cerrada queda bloqueada para "
           "edición y solo puede reabrirse con permisos especiales."),
        rf("RF38a", "Certificación",
           "El sistema debe permitir la generación de certificación si la finca "
           "cumple a satisfacción los criterios evaluados, y enviarla por correo "
           "electrónico.",
           "Botón «Generar certificación» habilitado y la ventana de envío por "
           "correo.",
           "Cuando una evaluación está «Validada» y la finca alcanza el nivel de "
           "cumplimiento satisfactorio definido, se habilita la opción «Generar "
           "certificación». Presiónela para producir el documento de certificación, "
           "que incluye los datos de la finca, la especie, la fecha y el nivel "
           "obtenido. Luego use la opción «Enviar por correo», indique el "
           "destinatario y confirme; el sistema enviará la certificación adjunta. "
           "Si la finca no cumple los criterios, la opción aparecerá deshabilitada "
           "con un mensaje que indica los requisitos faltantes."),
        rf("RF38b", "Módulo administrativo multi-especie",
           "El sistema debe permitir activar o desactivar especies en la plataforma "
           "sin afectar la operación general.",
           "Listado de especies con el interruptor «Habilitada / Deshabilitada» en "
           "la administración.",
           "El administrador puede controlar qué especies están habilitadas en la "
           "plataforma desde «Administración» → «Especies». Cada especie tiene un "
           "interruptor «Habilitada / Deshabilitada». Si deshabilita una especie, "
           "esta dejará de ofrecerse para nuevas evaluaciones, pero las evaluaciones "
           "ya realizadas y su historial se conservan intactos. Al habilitarla de "
           "nuevo, volverá a estar disponible. Este control permite incorporar o "
           "retirar especies sin afectar el funcionamiento general del sistema."),
        rf("RF40", "Notificaciones",
           "El sistema debe enviar notificaciones por correo o dentro de la "
           "plataforma sobre evaluaciones pendientes, aprobaciones y "
           "observaciones.",
           "Panel de notificaciones (ícono de campana) con la lista de avisos y su "
           "contador de novedades.",
           "El sistema notifica los eventos importantes por dos vías: dentro de la "
           "plataforma (ícono de campana en la barra superior, con un contador de "
           "novedades) y por correo electrónico. Recibirá avisos sobre evaluaciones "
           "pendientes por diligenciar, aprobaciones o validaciones y observaciones "
           "o devoluciones. Presione la campana para ver la lista de notificaciones "
           "y abra cualquiera para ir directamente a la evaluación o al registro "
           "relacionado. Puede marcar las notificaciones como leídas y, si lo "
           "desea, configurar en su perfil qué avisos recibir por correo."),
    ])

# ---------------------------------------------------------------- Anexo RNF
RNF = [
    ("RNF01", "Arquitectura web", "La solución debe implementarse como aplicación web con frontend en Angular."),
    ("RNF02", "Infraestructura en la nube", "La solución debe desplegarse sobre servicios de Google Cloud."),
    ("RNF03", "Escalabilidad", "Debe soportar el crecimiento en número de especies, usuarios, fincas y evaluaciones sin rediseño estructural."),
    ("RNF04", "Disponibilidad", "La plataforma debe estar disponible al menos el 99% del tiempo, exceptuando mantenimientos programados."),
    ("RNF05", "Seguridad de autenticación", "La autenticación debe realizarse con mecanismos seguros, con cifrado de credenciales y manejo de sesiones o token."),
    ("RNF06", "Cifrado de datos", "La información sensible debe protegerse en tránsito y en almacenamiento mediante cifrado."),
    ("RNF07", "Control de acceso", "Los usuarios solo deben visualizar y modificar la información autorizada según su rol."),
    ("RNF08", "Trazabilidad", "Todas las acciones críticas del sistema deben quedar registradas en bitácoras de auditoría."),
    ("RNF09", "Rendimiento de navegación", "Las pantallas principales deben cargar idealmente en menos de 3 segundos en condiciones normales."),
    ("RNF10", "Rendimiento de cálculo", "El sistema debe calcular resultados y diagnósticos en menos de 5 segundos por evaluación estándar."),
    ("RNF11", "Disponibilidad de evidencias", "Los archivos adjuntos deben almacenarse de forma segura, persistente y accesible desde la nube."),
    ("RNF12", "Usabilidad", "La interfaz debe ser intuitiva, consistente y fácil de usar sin entrenamiento técnico avanzado."),
    ("RNF13", "Diseño responsivo", "La plataforma debe adaptarse a computadores, tabletas y dispositivos móviles."),
    ("RNF14", "Accesibilidad", "La interfaz debe contemplar contraste adecuado, navegación clara y compatibilidad con teclado."),
    ("RNF15", "Mantenibilidad", "El código debe ser modular, documentado y reutilizable para facilitar su mantenimiento y evolución."),
    ("RNF16", "Reutilización", "Los componentes de Angular deben diseñarse para permitir reutilización entre especies y tipos de evaluación."),
    ("RNF17", "Parametrización", "Las listas de chequeo no deben quedar codificadas de forma rígida; deben configurarse desde catálogos o estructuras de datos."),
    ("RNF18", "Interoperabilidad", "La solución debe integrarse con APIs externas, incluyendo servicios de IA y almacenamiento en la nube."),
    ("RNF19", "Compatibilidad de navegadores", "La aplicación debe funcionar correctamente en los navegadores modernos más usados."),
    ("RNF20", "Respaldo de información", "El sistema debe contar con mecanismos de respaldo y recuperación de datos."),
    ("RNF21", "Calidad de datos", "El sistema debe validar formatos, obligatoriedad y consistencia de los datos ingresados."),
    ("RNF22", "Observabilidad", "La solución debe permitir el monitoreo de errores, eventos y consumo de recursos en la nube."),
    ("RNF23", "Despliegue continuo", "La arquitectura debe permitir integración y despliegue continuo para facilitar las actualizaciones."),
    ("RNF24", "Portabilidad", "La solución debe poder migrarse o evolucionar entre ambientes de desarrollo, pruebas y producción."),
    ("RNF25", "Fiabilidad de IA", "Las recomendaciones de IA deben presentarse como apoyo a la decisión, no como sustituto del criterio técnico del evaluador."),
    ("RNF26", "Tolerancia a fallos", "Si el servicio de IA no está disponible, el sistema debe seguir operando con diagnóstico estructurado sin bloquear la evaluación."),
    ("RNF27", "Protección de información personal", "El tratamiento de datos de usuarios y propietarios debe ajustarse a principios de privacidad y protección de datos."),
    ("RNF28", "Versionamiento", "La plataforma debe soportar versionamiento de formularios, criterios y listas de chequeo por especie."),
    ("RNF29", "Consistencia visual", "La solución debe mantener una línea gráfica homogénea en todos los módulos."),
    ("RNF30", "Soporte para crecimiento académico", "La plataforma debe permitir que nuevos grupos agreguen especies, reglas o funcionalidades sin afectar lo ya construido."),
    ("RNFG01", "Despliegue en Google Cloud", "La solución debe poder desplegarse en servicios administrados de Google Cloud."),
    ("RNFG02", "Almacenamiento de evidencias en la nube", "Las evidencias deben almacenarse en un servicio cloud escalable y seguro."),
    ("RNFG03", "Base de datos administrada", "La información estructurada debe almacenarse en un motor gestionado en Google Cloud o en un servicio compatible en la nube."),
    ("RNFG04", "Integración con servicios de IA", "La solución debe integrarse con servicios de inteligencia artificial consumidos desde la nube."),
    ("RNFG05", "Monitoreo cloud", "La solución debe contar con monitoreo, registro de eventos y seguimiento de errores en la infraestructura cloud."),
    ("RNFG06", "Gestión de credenciales", "Las credenciales y llaves de acceso a servicios cloud deben almacenarse de forma segura, no embebidas en el código."),
    ("RNFG07", "Separación de ambientes", "La solución debe contemplar ambientes independientes de desarrollo, pruebas y producción en la nube."),
]
