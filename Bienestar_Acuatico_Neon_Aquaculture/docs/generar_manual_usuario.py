# -*- coding: utf-8 -*-
"""
Generador del "Manual de Usuario - Aplicación ICA Bienestar Animal".

Construye un PDF profesional (portada, índice, módulos y requerimientos
funcionales RF01-RF40) a partir del documento fuente
"Requerimientos Aplicación ICA.docx".

Uso:  python generar_manual_usuario.py
Salida: Manual_Usuario_ICA_Bienestar_Animal.pdf (en la misma carpeta)
"""
import os
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents

# ----------------------------------------------------------------------------
#  Paleta y medidas
# ----------------------------------------------------------------------------
AZUL      = colors.HexColor("#0B3C49")   # azul profundo (barras de módulo)
TEAL      = colors.HexColor("#0E7C86")   # acento principal
NEON      = colors.HexColor("#12CBC4")   # acento brillante
NEON2     = colors.HexColor("#7DE2D1")   # acento claro
GRIS      = colors.HexColor("#33474E")   # texto
GRIS_CLARO= colors.HexColor("#6B7A80")   # texto secundario
FONDO     = colors.HexColor("#F1FBFB")   # fondo de caja
LINEA     = colors.HexColor("#CBE9E8")   # líneas suaves
BANDA     = colors.HexColor("#12505E")   # decoración

A4W, A4H = A4
MARGEN   = 20 * mm
FECHA    = date.today().strftime("%d/%m/%Y")

RUTA_SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "Manual_Usuario_ICA_Bienestar_Animal.pdf")

# ----------------------------------------------------------------------------
#  Estilos de párrafo
# ----------------------------------------------------------------------------
def estilo(nombre, **kw):
    base = dict(fontName="Helvetica", fontSize=10.2, leading=15,
                textColor=GRIS, alignment=TA_JUSTIFY)
    base.update(kw)
    return ParagraphStyle(nombre, **base)

S_BODY      = estilo("Body", spaceAfter=7)
S_DEF       = estilo("Def", fontName="Helvetica-Oblique", fontSize=8.8,
                     leading=12, textColor=GRIS_CLARO, spaceAfter=7)
S_MODULE    = estilo("ModuleTitle", fontName="Helvetica-Bold", fontSize=15,
                     leading=19, textColor=colors.white, backColor=AZUL,
                     borderPadding=(8, 10, 9, 10), alignment=TA_LEFT,
                     spaceBefore=16, spaceAfter=12)
S_REQ       = estilo("ReqTitle", fontName="Helvetica-Bold", fontSize=12.5,
                     leading=16, textColor=TEAL, alignment=TA_LEFT,
                     spaceBefore=8, spaceAfter=2)
S_MINIH     = estilo("MiniHead", fontName="Helvetica-Bold", fontSize=10,
                     leading=13, textColor=AZUL, alignment=TA_LEFT,
                     spaceBefore=7, spaceAfter=2)
S_SHOT_H    = estilo("ShotHead", fontName="Helvetica-Bold", fontSize=9.6,
                     leading=12, textColor=TEAL, alignment=TA_LEFT,
                     spaceAfter=1)
S_SHOT_T    = estilo("ShotText", fontSize=9.2, leading=12.5,
                     textColor=GRIS, alignment=TA_LEFT)
S_TITLE     = estilo("DocTitle", fontName="Helvetica-Bold", fontSize=22,
                     leading=26, textColor=AZUL, alignment=TA_LEFT, spaceAfter=4)
S_H1        = estilo("H1", fontName="Helvetica-Bold", fontSize=16,
                     leading=20, textColor=AZUL, alignment=TA_LEFT,
                     spaceBefore=6, spaceAfter=8)
S_COVER_TXT = estilo("CoverTxt", fontSize=10.5, leading=15,
                     textColor=GRIS, alignment=TA_LEFT, spaceAfter=6)

# ----------------------------------------------------------------------------
#  Caja de "espacio para pantallazo"
# ----------------------------------------------------------------------------
def caja_pantallazo(texto):
    contenido = [
        Paragraph("[ INSERTAR PANTALLAZO ]", S_SHOT_H),
        Paragraph(texto, S_SHOT_T),
    ]
    t = Table([[contenido]], colWidths=[A4W - 2 * MARGEN - 2])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), FONDO),
        ("BOX",         (0, 0), (-1, -1), 0.8, LINEA),
        ("LINEBEFORE",  (0, 0), (0, -1), 3.2, NEON),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",(0, 0), (-1, -1), 12),
        ("TOPPADDING",  (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 9),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t

# ----------------------------------------------------------------------------
#  Plantilla de documento (TOC + marcadores + encabezado/pie)
# ----------------------------------------------------------------------------
class ManualDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="normal")
        self.addPageTemplates([PageTemplate(id="main", frames=[frame],
                                            onPage=self._decorar)])

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        nombre = flowable.style.name
        texto = flowable.getPlainText()
        if nombre == "ModuleTitle":
            clave = "mod%d" % id(flowable)
            self.notify("TOCEntry", (0, texto, self.page))
            self.canv.bookmarkPage(clave)
            self.canv.addOutlineEntry(texto, clave, level=0, closed=False)
        elif nombre == "ReqTitle":
            clave = "req%d" % id(flowable)
            self.notify("TOCEntry", (1, texto, self.page))
            self.canv.bookmarkPage(clave)
            self.canv.addOutlineEntry(texto, clave, level=1, closed=True)

    def _decorar(self, canvas, doc):
        canvas.saveState()
        if doc.page == 1:
            self._portada(canvas)
        else:
            canvas.setStrokeColor(LINEA)
            canvas.setLineWidth(0.8)
            canvas.line(MARGEN, A4H - 38, A4W - MARGEN, A4H - 38)
            canvas.setFont("Helvetica", 7.8)
            canvas.setFillColor(GRIS_CLARO)
            canvas.drawString(MARGEN, A4H - 33,
                              "Manual de Usuario - Aplicación ICA Bienestar Animal")
            canvas.drawRightString(A4W - MARGEN, A4H - 33, "RF01 - RF40")
            canvas.setStrokeColor(LINEA)
            canvas.line(MARGEN, 44, A4W - MARGEN, 44)
            canvas.setFont("Helvetica", 7.8)
            canvas.setFillColor(GRIS_CLARO)
            canvas.drawString(MARGEN, 32, "Documento de apoyo académico")
            canvas.setFillColor(TEAL)
            canvas.setFont("Helvetica-Bold", 8.5)
            canvas.drawRightString(A4W - MARGEN, 32, "Página %d" % doc.page)
        canvas.restoreState()

    def _portada(self, canvas):
        c = canvas
        c.setFillColor(colors.white)
        c.rect(0, 0, A4W, A4H, fill=1, stroke=0)
        banda = 335
        c.setFillColor(AZUL)
        c.rect(0, A4H - banda, A4W, banda, fill=1, stroke=0)
        c.setFillColor(BANDA)
        c.circle(A4W - 70, A4H - 60, 130, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#0F4653"))
        c.circle(A4W - 20, A4H - 235, 85, fill=1, stroke=0)
        c.setFillColor(NEON)
        c.rect(0, A4H - banda, A4W, 6, fill=1, stroke=0)
        c.setFillColor(NEON2)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(48, A4H - 74, "MANUAL DE USUARIO")
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 33)
        c.drawString(48, A4H - 126, "Aplicación ICA")
        c.setFillColor(NEON)
        c.drawString(48, A4H - 166, "Bienestar Animal")
        c.setStrokeColor(NEON)
        c.setLineWidth(2.4)
        c.line(48, A4H - 188, 210, A4H - 188)
        c.setFillColor(colors.HexColor("#CFEDE9"))
        c.setFont("Helvetica", 11.5)
        c.drawString(48, A4H - 214, "Guía de uso de la plataforma")
        c.drawString(48, A4H - 232, "Requerimientos funcionales RF01 - RF40")

        y = A4H - banda - 46
        c.setFillColor(AZUL)
        c.setFont("Helvetica-Bold", 12.5)
        c.drawString(48, y, "Contenido de este manual")
        lineas = [
            "Recorrido por los 39 requerimientos funcionales del documento fuente,",
            "organizados en ocho módulos de trabajo.",
            "",
            "Cada requerimiento incluye su descripción, un espacio reservado para el",
            "pantallazo correspondiente y la explicación de uso paso a paso.",
        ]
        c.setFont("Helvetica", 10.5)
        c.setFillColor(GRIS)
        yy = y - 22
        for ln in lineas:
            c.drawString(48, yy, ln)
            yy -= 15

        bx, by, bw, bh = 48, 138, A4W - 96, 150
        c.setFillColor(FONDO)
        c.setStrokeColor(LINEA)
        c.setLineWidth(1)
        c.roundRect(bx, by, bw, bh, 9, fill=1, stroke=1)
        c.setFillColor(NEON)
        c.rect(bx, by + bh - 3.5, bw, 3.5, fill=1, stroke=0)
        filas = [
            ("Documento base", "Requerimientos Aplicación ICA - Bienestar Animal"),
            ("Autor del documento base", "PhD. Paola Andrea Valencia A."),
            ("Alcance", "Requerimientos funcionales RF01 - RF40"),
            ("Versión del manual", "1.0"),
            ("Fecha", FECHA),
        ]
        fy = by + bh - 30
        for etiqueta, valor in filas:
            c.setFillColor(AZUL)
            c.setFont("Helvetica-Bold", 9.5)
            c.drawString(bx + 18, fy, etiqueta)
            c.setFillColor(GRIS)
            c.setFont("Helvetica", 9.5)
            c.drawString(bx + 175, fy, valor)
            fy -= 24

        c.setFillColor(AZUL)
        c.rect(0, 0, A4W, 42, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#CFEDE9"))
        c.setFont("Helvetica", 8.6)
        c.drawString(48, 17,
                     "Documento de carácter académico y de apoyo  ·  "
                     "Los recuadros para pantallazos deben reemplazarse por capturas reales.")


# ----------------------------------------------------------------------------
#  Construcción del manual
# ----------------------------------------------------------------------------
import _manual_contenido as C   # noqa: E402


def bloque_rf(r):
    """Devuelve los flowables de un requerimiento funcional."""
    cod = r["cod"]
    cod_disp = "RF38" if cod in ("RF38a", "RF38b") else cod
    titulo = "%s. %s" % (cod_disp, r["nombre"])
    return [
        Paragraph(titulo, S_REQ),
        HRFlowable(width="100%", thickness=0.8, color=LINEA,
                   spaceBefore=1, spaceAfter=6),
        Paragraph("<i>Descripción del requerimiento:</i> %s" % r["desc"], S_DEF),
        caja_pantallazo(r["shot"]),
        Spacer(1, 6),
        Paragraph("Explicación del funcionamiento", S_MINIH),
        Paragraph(r["exp"], S_BODY),
    ]


def seccion_presentacion():
    f = []
    f.append(Paragraph("Presentación", S_H1))
    f.append(HRFlowable(width="100%", thickness=1.2, color=NEON, spaceAfter=10))
    f.append(Paragraph(
        "Este manual describe, de forma práctica y orientada al usuario final, "
        "el funcionamiento de la aplicación <b>Aplicación ICA - Bienestar "
        "Animal</b>. Su contenido se elaboró a partir del documento de "
        "requerimientos funcionales y no funcionales del proyecto, y recorre "
        "cada uno de los requerimientos funcionales (RF01 a RF40) explicando "
        "cómo se usa la plataforma, qué botones debe presionar el usuario, qué "
        "información debe registrar y qué resultados puede esperar en pantalla.",
        S_BODY))
    f.append(Paragraph(
        "El manual está dirigido a administradores, docentes, estudiantes "
        "evaluadores y consultores externos que interactúan con el sistema.",
        S_BODY))

    f.append(Paragraph("Cómo leer este manual", S_MINIH))
    f.append(Paragraph(
        "Cada requerimiento se presenta siempre con la misma estructura: "
        "<b>título</b> con el código y el nombre del requerimiento; un "
        "<b>espacio reservado para el pantallazo</b>, que indica exactamente "
        "qué imagen o captura de pantalla debe insertarse allí; y una "
        "<b>explicación del funcionamiento</b> redactada paso a paso para el "
        "usuario final.", S_BODY))
    f.append(Paragraph(
        "Los recuadros de color claro con la etiqueta «INSERTAR PANTALLAZO» son "
        "marcadores de posición: deben reemplazarse por capturas de pantalla "
        "reales de la aplicación antes de publicar el manual.", S_BODY))

    f.append(Paragraph("Organización por módulos", S_MINIH))
    f.append(Paragraph(
        "Los requerimientos se agrupan en ocho módulos de trabajo que siguen el "
        "flujo natural de uso de la aplicación:", S_BODY))
    filas = []
    for m in C.MODULOS:
        filas.append([m["titulo"]])
    t = Table(filas, colWidths=[A4W - 2 * MARGEN])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), FONDO),
        ("BOX", (0, 0), (-1, -1), 0.8, LINEA),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, NEON),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.6),
        ("TEXTCOLOR", (0, 0), (-1, -1), AZUL),
    ]))
    f.append(t)

    f.append(Paragraph("Nota sobre la numeración de los requerimientos", S_MINIH))
    f.append(Paragraph(
        "El documento fuente define los requerimientos <b>RF01 a RF36</b>, un "
        "<b>RF38</b> (Certificación), un segundo <b>RF38</b> (Módulo "
        "administrativo multi-especie) y un <b>RF40</b> (Notificaciones). No "
        "define los requerimientos RF37 ni RF39. Este manual respeta la "
        "numeración original: por eso no incluye secciones para RF37 y RF39, y "
        "presenta los dos RF38 con sus nombres diferenciados.", S_BODY))
    f.append(Paragraph(
        "En total se documentan <b>39 requerimientos funcionales</b>. Como "
        "información complementaria, el Anexo A resume los requerimientos no "
        "funcionales (RNF y RNFG).", S_BODY))
    f.append(PageBreak())
    return f


def seccion_anexo():
    f = []
    f.append(Paragraph("Anexo A · Requerimientos no funcionales", S_MODULE))
    f.append(Paragraph(
        "Los siguientes requerimientos no funcionales, tomados del documento "
        "fuente, describen las cualidades y restricciones técnicas que debe "
        "cumplir la plataforma (rendimiento, seguridad, usabilidad, "
        "infraestructura en la nube, entre otras). No corresponden a pantallas "
        "de uso, por lo que se presentan como listado de referencia.", S_BODY))
    f.append(Spacer(1, 4))
    datos = [["Código", "Requerimiento no funcional"]]
    for cod, nombre, desc in C.RNF:
        datos.append([cod, Paragraph("<b>%s.</b> %s" % (nombre, desc),
                                     ParagraphStyle("rnf", parent=S_SHOT_T,
                                                    fontSize=9.0, leading=12))])
    t = Table(datos, colWidths=[58, A4W - 2 * MARGEN - 58], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 1), (0, -1), TEAL),
        ("FONTSIZE", (0, 1), (0, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, FONDO]),
        ("GRID", (0, 0), (-1, -1), 0.5, LINEA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    f.append(t)
    return f


def construir():
    doc = ManualDoc(
        RUTA_SALIDA, pagesize=A4,
        leftMargin=MARGEN, rightMargin=MARGEN,
        topMargin=52, bottomMargin=56,
        title="Manual de Usuario - Aplicación ICA Bienestar Animal",
        author="Manual de Usuario",
        subject="Requerimientos funcionales RF01 - RF40",
    )
    # Ajustes finos de estilo
    S_REQ.keepWithNext = 1
    S_MINIH.keepWithNext = 1

    story = []
    story.append(Spacer(1, 1))   # la portada se dibuja en el canvas (página 1)
    story.append(PageBreak())

    # ---- Índice de contenidos (página 2) ----
    story.append(Paragraph("Índice de contenidos", S_H1))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NEON,
                            spaceAfter=10))
    indice = TableOfContents()
    indice.dotsMinLevel = 0
    indice.levelStyles = [
        ParagraphStyle(name="TOC0", fontName="Helvetica-Bold", fontSize=11,
                       leading=16.5, textColor=AZUL, spaceBefore=8),
        ParagraphStyle(name="TOC1", fontName="Helvetica", fontSize=9.6,
                       leading=13.6, textColor=GRIS, leftIndent=16),
    ]
    story.append(indice)
    story.append(PageBreak())

    # ---- Presentación ----
    story += seccion_presentacion()

    # ---- Módulos y requerimientos ----
    for m in C.MODULOS:
        story.append(Paragraph(m["titulo"], S_MODULE))
        story.append(Paragraph(m["intro"], S_BODY))
        for r in m["rfs"]:
            story += bloque_rf(r)

    # ---- Anexo ----
    story.append(PageBreak())
    story += seccion_anexo()

    doc.multiBuild(story)
    return RUTA_SALIDA


if __name__ == "__main__":
    ruta = construir()
    print("PDF generado:", ruta)
    print("Existe:", os.path.exists(ruta), "| bytes:", os.path.getsize(ruta))
