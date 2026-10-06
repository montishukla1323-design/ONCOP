"""
ONCOP Project Report Document Generator
Generates an 80+ page academic project report in DOCX format matching the reference PDF:
- Exact styling: Times New Roman, Arial headers, identical margins, font sizes, colors
- Pages 1 & 2: Identical layout with college emblem, updated project title and Ms. Monti Shukla
- Page 3: Declaration with border box and Ms. Monti Shukla
- Page 4: Acknowledgement
- Page 5: Abstract
- Pages 6-9: Table of Contents matching the PDF 2-column tabular format
- Chapters 1-7: Exhaustive, rigorous academic and technical content on ONCOP
- SRS specifications & actual structured diagrams (Component Architecture, DFD Level 0/1/2, ERD, Activity, Sequence, Use Case, State Machine) - NO raster images for diagrams!
- Appendix A: Full source code listings in text format (database.js, server.js, govIntegration.js, app.js, index.html, styles.css)
- Appendix B: Exhaustive interface walkthrough & technical specifications
- Bibliography & References: Exhaustive academic textbooks, research papers, government whitepapers, and developer resources
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    """
    kwargs can be top, bottom, left, right.
    val="single", sz="6", space="0", color="CCCCCC"
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = f'<w:{edge} {nsdecls("w")} w:val="{edge_data.get("val", "single")}" w:sz="{edge_data.get("sz", "4")}" w:space="{edge_data.get("space", "0")}" w:color="{edge_data.get("color", "auto")}"/>'
            tcBorders.append(parse_xml(tag))
    tcPr.append(tcBorders)

def add_header_to_section(section):
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_before = Pt(0)
    hp.paragraph_format.space_after = Pt(4)
    
    # bottom border for header
    pPr = hp._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="4" w:color="D0D0D0"/></w:pBdr>')
    pPr.append(pBdr)
    
    r1 = hp.add_run('Page ')
    r1.font.name = 'Arial'
    r1.font.size = Pt(11)
    r1.font.color.rgb = RGBColor(128, 128, 128)
    
    r2 = hp.add_run('| ')
    r2.font.name = 'Arial'
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(0, 0, 0)
    
    r3 = hp.add_run()
    r3.font.name = 'Arial'
    r3.font.size = Pt(11)
    r3.font.bold = True
    r3.font.color.rgb = RGBColor(0, 0, 0)
    
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    fldChar3 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    r3._r.append(fldChar1)
    r3._r.append(instrText)
    r3._r.append(fldChar2)
    r3._r.append(fldChar3)

print("Helper definitions loaded.")
