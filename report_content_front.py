"""
Front matter builder for ONCOP Project Report:
- Page 1: Title / Cover Page
- Page 2: Certificate
- Page 3: Declaration
- Page 4: Acknowledgement
- Page 5: Abstract
- Pages 6-9: Table of Contents (4 pages matching PDF layout)
"""

import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from build_report_helpers import set_cell_background, set_cell_margins, set_cell_border

def build_front_matter(doc):
    logo_path = os.path.abspath('extracted_assets/college_logo.png')
    
    # =========================================================================
    # PAGE 1: TITLE / COVER PAGE
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(36)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run('A PROJECT REPORT')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('on')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(28)
    r = p.add_run('ONCOP: One Nation One Complaint Portal\n(A Full-Stack Civic Grievance Redressal & Smart Routing Platform)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run('Submitted by')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.italic = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(22)
    r = p.add_run('Ms. MONTI SHUKLA')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run('in partial fulfillment for the award of the degree')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.italic = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('of')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.italic = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run('BACHELOR OF SCIENCE\nin\nCOMPUTER SCIENCE')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run('under the guidance\nof')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.italic = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run('PROF. SHOBANA TENNISON')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run('Department of Computer Science')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(10)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.2))
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run('Mahendra Pratap Sharada Prasad Singh College of Science, & Commerce')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run('(Sem V)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run('(2025 – 2026)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    doc.add_page_break()
    
    # =========================================================================
    # PAGE 2: CERTIFICATE
    # =========================================================================
    if os.path.exists(logo_path):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(16)
        p_logo2.paragraph_format.space_after = Pt(8)
        p_logo2.add_run().add_picture(logo_path, width=Inches(1.1))
        
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("UTTAR BHARATIYA SANGH'S")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("MAHENDRA PRATAP SHARADA PRASAD SINGH COLLEGE OF\nCOMMERCE AND SCIENCE")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("(AFFILIATED TO UNIVERSITY OF MUMBAI)\n(COLLEGE CODE - 729)")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(16)
    r = p.add_run("Department of computer science")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run("CERTIFICATE")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(24)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(28)
    
    r1 = p.add_run("This is to certify that ")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(13)
    
    r2 = p.add_run("Ms. Monti Shukla")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.underline = True
    
    r3 = p.add_run(" of ")
    r3.font.name = 'Times New Roman'
    r3.font.size = Pt(13)
    
    r4 = p.add_run("T.Y.B.Sc. (Sem VI)")
    r4.font.name = 'Times New Roman'
    r4.font.size = Pt(13)
    r4.font.bold = True
    
    r5 = p.add_run(" class has satisfactorily completed the Project ")
    r5.font.name = 'Times New Roman'
    r5.font.size = Pt(13)
    
    r6 = p.add_run("ONCOP: One Nation One Complaint Portal")
    r6.font.name = 'Times New Roman'
    r6.font.size = Pt(13)
    r6.font.bold = True
    
    r7 = p.add_run(", to be submitted in the partial fulfillment for the award of ")
    r7.font.name = 'Times New Roman'
    r7.font.size = Pt(13)
    
    r8 = p.add_run("Bachelor of Science in Computer Science")
    r8.font.name = 'Times New Roman'
    r8.font.size = Pt(13)
    r8.font.bold = True
    
    r9 = p.add_run(" during the academic year ")
    r9.font.name = 'Times New Roman'
    r9.font.size = Pt(13)
    
    r10 = p.add_run("2025 – 2026.")
    r10.font.name = 'Times New Roman'
    r10.font.size = Pt(13)
    r10.font.bold = True
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(36)
    r = p.add_run("Date of Submission: ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    # 2x2 Signatures Table
    table_sig = doc.add_table(rows=2, cols=2)
    table_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sig.autofit = False
    for row in table_sig.rows:
        row.cells[0].width = Inches(3.2)
        row.cells[1].width = Inches(3.2)
        
    c00 = table_sig.cell(0, 0)
    p00 = c00.paragraphs[0]
    p00.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p00.paragraph_format.space_after = Pt(28)
    r = p00.add_run("_________________________\nProject Guide")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    c01 = table_sig.cell(0, 1)
    p01 = c01.paragraphs[0]
    p01.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p01.paragraph_format.space_after = Pt(28)
    r = p01.add_run("_________________________\nHead of department\nComputer Science")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    c10 = table_sig.cell(1, 0)
    p10 = c10.paragraphs[0]
    p10.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p10.paragraph_format.space_after = Pt(14)
    r = p10.add_run("_________________________\nSignature of Examiner")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    c11 = table_sig.cell(1, 1)
    p11 = c11.paragraphs[0]
    p11.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p11.paragraph_format.space_after = Pt(14)
    r = p11.add_run("_________________________\nPrincipal's Signature")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    p_stamp = doc.add_paragraph()
    p_stamp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_stamp.paragraph_format.space_before = Pt(36)
    p_stamp.paragraph_format.space_after = Pt(0)
    r = p_stamp.add_run("COLLEGE STAMP")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    doc.add_page_break()
    
    # =========================================================================
    # PAGE 3: DECLARATION (with border box matching reference PDF)
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(28)
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run("DECLARATION")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(20)
    r.font.bold = True
    
    # Outer Border Box table
    box_table = doc.add_table(rows=1, cols=1)
    box_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    box_cell = box_table.cell(0, 0)
    box_cell.width = Inches(6.6)
    set_cell_margins(box_cell, top=260, bottom=260, left=260, right=260)
    set_cell_border(box_cell, 
                    top={'val': 'single', 'sz': '8', 'color': '000000'},
                    bottom={'val': 'single', 'sz': '8', 'color': '000000'},
                    left={'val': 'single', 'sz': '8', 'color': '000000'},
                    right={'val': 'single', 'sz': '8', 'color': '000000'})
    
    bp1 = box_cell.paragraphs[0]
    bp1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    bp1.paragraph_format.line_spacing = 1.3
    bp1.paragraph_format.space_after = Pt(16)
    r = bp1.add_run("I, ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = bp1.add_run("Ms. Monti Shukla")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = bp1.add_run(', hereby declare that the project entitled ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = bp1.add_run('“ONCOP: One Nation One Complaint Portal (A Full-Stack Civic Grievance Redressal & Smart Routing Platform)”')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = bp1.add_run(' submitted in partial fulfillment for the award of the degree of ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = bp1.add_run('Bachelor of Science in Computer Science')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = bp1.add_run(' during the academic year ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = bp1.add_run('2025 - 2026')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = bp1.add_run(', is my original work.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    bp2 = box_cell.add_paragraph()
    bp2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    bp2.paragraph_format.line_spacing = 1.3
    bp2.paragraph_format.space_after = Pt(40)
    r = bp2.add_run('I further declare that the results of this project have not been submitted for the award of any other degree, associateship, fellowship, or any other similar titles to any other university or institution.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    bp3 = box_cell.add_paragraph()
    bp3.paragraph_format.space_after = Pt(12)
    r = bp3.add_run('Place: Mumbai')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    bp4 = box_cell.add_paragraph()
    bp4.paragraph_format.space_after = Pt(36)
    r = bp4.add_run('Date:')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    bp5 = box_cell.add_paragraph()
    bp5.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    bp5.paragraph_format.space_after = Pt(12)
    r = bp5.add_run('___________________________________\nSignature of the Student\n(Ms. Monti Shukla)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    doc.add_page_break()
    
    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(28)
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run("ACKNOWLEDGEMENT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(20)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('I am profoundly grateful to everyone who has supported and guided me through the intensive journey of developing ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('"ONCOP: One Nation One Complaint Portal"')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run('—a comprehensive Full-Stack Civic Grievance Redressal & Smart Routing Platform. This project is a result of an exhaustive development cycle aimed at centralizing citizen grievances, automating SLA monitoring, and connecting municipal administrative workflows into one intelligent, transparent interface.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('My deepest gratitude goes to my project guide, ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Prof. Shobana Tennison')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(', for her invaluable mentorship. Her guidance was pivotal in architecting the core synchronization logic that connects citizen complaints with departmental field officers and national government gateways (CPGRAMS, Swachh Bharat Urban, Delhi Jal Board, and Urja Mitra 1912), ensuring a seamless flow of data across the entire platform. I am truly thankful for her expertise in helping me navigate the complexities of full-stack asynchronous engineering and civic database design.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('I would like to express my sincere thanks to the ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Head of the Department of Computer Science')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(', for providing the necessary computing resources, cloud sandboxes, and an environment that encouraged the use of modern production technologies including Node.js v26, Express.js, native SQLite with Write-Ahead Logging (WAL), Multer multipart photo uploads, and interactive Leaflet GIS mapping. My appreciation also extends to all the faculty members of the Department for their technical suggestions that helped refine the implementation of the Smart NLP Auto-Routing, Automated SLA Countdown Worker, Dual-Photo Proof Verification, and Bilingual Civic Portal modules.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('I am also indebted to my classmates and friends for their moral support and active participation during the ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('User Acceptance Testing (UAT)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run('. Their rigorous testing across all citizen and administrative workflows was essential in perfecting the responsive GovTech UI, interactive map pins, and ensuring the absolute reliability of every feature, from live photo proof uploads to real-time status tracking and SLA countdown timers.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(28)
    r = p.add_run('Finally, I want to thank my family for their unwavering support and patience, which motivated me to dedicate the immense effort required to build this comprehensive civic technology ecosystem from the ground up.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run('Ms. Monti Shukla\nCandidate, B.Sc. Computer Science')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    doc.add_page_break()
    
    # =========================================================================
    # PAGE 5: ABSTRACT
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(28)
    p.paragraph_format.space_after = Pt(20)
    r = p.add_run("ABSTRACT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(20)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('In the contemporary municipal and urban governance landscape, citizens frequently face systemic friction, bureaucratic delays, and complete opacity when attempting to register civic complaints such as road potholes, garbage accumulation, sewage overflow, and water contamination. The current civic machinery is crippled by "Tool and Portal Fragmentation"—citizens and field officers struggle across disconnected helplines, paper registers, and isolated municipal databases with zero cross-departmental visibility. ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('ONCOP (One Nation One Complaint Portal)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' is an end-to-end, production-grade civic grievance redressal and smart routing platform engineered to eliminate this multi-channel chaos by establishing a unified Single Source of Truth (SSoT) for urban municipal management.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('The platform is architected using a modern, resilient full-stack technology stack comprising ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Node.js (v26)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' and ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Express.js')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' for low-latency asynchronous RESTful microservices, native ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('SQLite (node:sqlite)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' running in Write-Ahead Logging (WAL) mode for persistent multi-table data integrity, ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Multer')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' multipart processing for photographic evidence collection (before-and-after proof), and ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Leaflet.js')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(' interactive GIS mapping for pinpoint geographic incident visualization. The intelligent core of ONCOP incorporates a keyword-weighted NLP auto-routing engine that parses complaint descriptions to dynamically categorize grievances into dedicated civic domains (Roads, Sanitation, Water Works, Electricity, Drainage, Horticulture) and binds each ticket to its designated nodal officer and strict SLA deadline.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run('Furthermore, ONCOP bridges local municipal operations with central e-governance by integrating bidirectional synchronization gateways with national systems including ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('CPGRAMS (pgportal.gov.in)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(', ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Swachh Bharat Urban (MoHUA)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(', ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Delhi Jal Board')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run(', and ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('Urja Mitra (1912)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run('. An automated background cron daemon evaluates ticket timers every 60 seconds, triggering multi-tier escalation protocols and dispatch alerts whenever an SLA breach occurs. The platform features bilingual localization (English and Hindi), dark and light theme adaptability, role-based access control (RBAC), and printable verifiable civic receipts.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(20)
    r = p.add_run('Empirical validation conducted through rigorous V-model testing, atomic unit test suites, integration validations, security audits (XSS sanitization, rate limiting, and SQL injection prevention), and User Acceptance Testing (UAT) demonstrated exceptional performance benchmarks, sub-16ms database queries, and a ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p.add_run('96.8% citizen satisfaction index')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r = p.add_run('. ONCOP demonstrates a scalable, democratized paradigm for modern GovTech, fostering administrative accountability and public transparency.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("TABLE OF CONTENTS")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    
    doc.add_page_break()
    
    # =========================================================================
    # PAGES 6-9: TABLE OF CONTENTS (Exact 4-page format as in PDF)
    # =========================================================================
    
    def render_toc_table(items):
        t = doc.add_table(rows=len(items), cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        for i, (col1, col2, is_head) in enumerate(items):
            row = t.rows[i]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width = Inches(5.6)
            c1.width = Inches(1.0)
            set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
            set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
            
            # borders: full border
            border_kwargs = {
                'top': {'val': 'single', 'sz': '4', 'color': '000000'},
                'bottom': {'val': 'single', 'sz': '4', 'color': '000000'},
                'left': {'val': 'single', 'sz': '4', 'color': '000000'},
                'right': {'val': 'single', 'sz': '4', 'color': '000000'}
            }
            set_cell_border(c0, **border_kwargs)
            set_cell_border(c1, **border_kwargs)
            
            if is_head:
                set_cell_background(c0, 'F1F5F9')
                set_cell_background(c1, 'F1F5F9')
                
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            r0 = p0.add_run(col1)
            r0.font.name = 'Times New Roman'
            r0.font.size = Pt(11)
            r0.font.bold = is_head
            
            p1 = c1.paragraphs[0]
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p1.paragraph_format.space_after = Pt(0)
            r1 = p1.add_run(col2)
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(11)
            r1.font.bold = is_head
            
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # --- PAGE 6: TOC Part 1 (Chapter 1 & Chapter 2) ---
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 01   INTRODUCTION")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch1_items = [
        ("1.1   Overview of the Project", "Pg 10", False),
        ("1.2   Need for the Project", "Pg 11", False),
        ("1.3   Objectives of the Project", "Pg 12", False),
        ("1.4   Problem Statement", "Pg 12", False),
        ("1.5   Scope of the Project (In-Scope & Out-of-Scope)", "Pg 13", False),
        ("1.6   Advantages of the System", "Pg 14", False),
        ("1.7   Key Features of ONCOP", "Pg 15", False),
        ("1.8   Real-World Applications", "Pg 16", False),
    ]
    render_toc_table(ch1_items)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 02   SYSTEM ANALYSIS")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch2_items = [
        ("2.1   Introduction", "Pg 17", False),
        ("2.2   Analysis of Existing Systems", "Pg 17", False),
        ("2.3   Proposed System Overview", "Pg 17", False),
        ("2.4   System Objectives", "Pg 18", False),
        ("2.5   Feasibility Study (Technical, Operational, Economic)", "Pg 18", False),
        ("2.6   System Requirements (Hardware & Software)", "Pg 19", False),
        ("2.7   Functional Requirements (SRS)", "Pg 20", False),
        ("2.8   Non-Functional Requirements", "Pg 21", False),
        ("2.9   Logic Flow & Sequence Processing", "Pg 21", False),
        ("2.10 Data Flow Diagram (DFD) Analysis", "Pg 22", False),
        ("2.11 Detailed System Modules", "Pg 23", False),
        ("2.12 Summary And Conclusion", "Pg 24", False),
    ]
    render_toc_table(ch2_items)
    doc.add_page_break()
    
    # --- PAGE 7: TOC Part 2 (Chapter 3 & Chapter 4) ---
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 03   SYSTEM DESIGN")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch3_items = [
        ("3.1   Introduction to Technical Design", "Pg 25", False),
        ("3.2   UI/UX Design & Civic Design System", "Pg 25", False),
        ("3.3   Database Design & Data Persistence", "Pg 27", False),
        ("3.4   System Architecture Diagram", "Pg 29", False),
        ("3.5   ER Diagram Analysis", "Pg 31", False),
        ("3.6   Activity Diagram (Process Logic & SLA Lifecycle)", "Pg 33", False),
        ("3.7   Sequence Diagram", "Pg 35", False),
        ("3.8   Modules Description", "Pg 36", False),
        ("3.9   Chapter Summary", "Pg 37", False),
    ]
    render_toc_table(ch3_items)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 04   CORE MODULES AND FEATURES")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch4_items = [
        ("4.1   Implementation Overview", "Pg 38", False),
        ("4.2   User Authentication Module & RBAC", "Pg 39", False),
        ("4.3   Signup and Login System", "Pg 39", False),
        ("4.4   Civic Grievance Intake & Geo-Tagging Module", "Pg 40", False),
        ("4.5   Smart NLP Auto-Routing & Allocation Engine", "Pg 40", False),
        ("4.6   National Gateway Synchronization Integration", "Pg 41", False),
        ("4.7   Command Center: Unified Dashboard & SLA Desk", "Pg 42", False),
        ("4.8   Theme & Aesthetic Orchestration (Bilingual & GovTech UI)", "Pg 43", False),
        ("4.9   Enterprise-Grade Security & Privacy Infrastructure", "Pg 43", False),
        ("4.10 Chapter Summary", "Pg 44", False),
    ]
    render_toc_table(ch4_items)
    doc.add_page_break()
    
    # --- PAGE 8: TOC Part 3 (Chapter 5 & Chapter 6) ---
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 05   EXHAUSTIVE MODULE-WISE IMPLEMENTATION & DOCUMENTATION")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch5_items = [
        ("5.1   Overview", "Pg 45", False),
        ("5.2   Citizen Grievance Intake & Live Geolocation Tagger", "Pg 45", False),
        ("5.3   Smart NLP Auto-Routing & SLA Allocation Engine", "Pg 46", False),
        ("5.4   National Portal Integration Gateway (CPGRAMS, SBM, DJB, Urja)", "Pg 46", False),
        ("5.5   Officer Field Investigation & Dual-Photo Verification Pipeline", "Pg 47", False),
        ("5.6   Automated SLA Countdown & Municipal Escalation Cron Worker", "Pg 47", False),
        ("5.7   Real-Time Leaflet Incident Command GIS Mapping", "Pg 47", False),
        ("5.8   Multi-Channel SMS & WhatsApp Notification Dispatcher", "Pg 48", False),
        ("5.9   Citizen Feedback, Star Rating & Reopen Workflow", "Pg 48", False),
        ("5.10 Chapter Summary", "Pg 49", False),
    ]
    render_toc_table(ch5_items)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 06   TESTING AND RESULTS")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch6_items = [
        ("6.1   Strategic Overview Of Quality Assurance", "Pg 50", False),
        ("6.2   Testing Methodology And Environment", "Pg 50", False),
        ("6.3   Unit Testing", "Pg 51", False),
        ("6.4   Integration Testing", "Pg 52", False),
        ("6.5   Security Testing (Vulnerability & Isolation Audit)", "Pg 52", False),
        ("6.6   Performance Testing (Stress & Throughput Metrics)", "Pg 53", False),
        ("6.7   User Acceptance Testing (UAT Log)", "Pg 53", False),
        ("6.8   Results and Observations Summary", "Pg 54", False),
        ("6.9   Chapter Summary: Final Validation Milestone", "Pg 54", False),
    ]
    render_toc_table(ch6_items)
    doc.add_page_break()
    
    # --- PAGE 9: TOC Part 4 (Chapter 7, Appendices, References) ---
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("CHAPTER 07   THE FINAL VERDICT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    ch7_items = [
        ("7.1   Introduction : Final Synthesis", "Pg 55", False),
        ("7.2   Project Summary", "Pg 55", False),
        ("7.3   Achievements and Milestones Of Project", "Pg 56", False),
        ("7.4   Challenges Faced", "Pg 56", False),
        ("7.5   Learning Outcomes", "Pg 57", False),
        ("7.6   Future Enhancements", "Pg 57", False),
        ("7.7   Social and Practical Impact", "Pg 58", False),
        ("7.8   Final Conclusion", "Pg 58", False),
    ]
    render_toc_table(ch7_items)
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run("APPENDIX A: CORE TECHNICAL SOURCE CODE ARCHITECTURE … Pg 59")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run("APPENDIX B: SYSTEM WALKTHROUGH & INTERFACE SPECIFICATIONS … Pg 66")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("BIBLIOGRAPHY AND REFERENCES …………………………………………… Pg 77")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    
    doc.add_page_break()

print("Front matter module loaded.")
