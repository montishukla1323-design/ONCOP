"""
Master Project Report Generator for ONCOP
Assembles the complete 80+ page project report DOCX file:
- Matching reference PDF format, styling, margins, headers, and colors
- Cover page & Certificate exactly matching PDF with college logo and Ms. Monti Shukla
- Chapters 1 to 7 with exhaustive academic content
- Software Requirements Specification (SRS) & native UML diagrams (NOT images)
- Full source code listings in text format (Appendix A)
- Exhaustive interface walkthrough & technical specifications (Appendix B)
- Comprehensive Bibliography and References
- Computes exact page count via Word COM automation
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from build_report_helpers import add_header_to_section
from report_content_front import build_front_matter
from report_content_ch1_ch3 import build_chapters_1_to_3
from report_content_ch4_ch7 import build_chapters_4_to_7
from report_content_appendices import build_appendices_and_refs
from verify_word import get_word_page_count

def generate_report(output_filename="ONCOP_Project_Report.docx"):
    print(f"Initializing document generation: {output_filename}")
    doc = docx.Document()
    
    # Configure A4 Page Setup and Margins matching reference PDF
    section = doc.sections[0]
    section.page_width = Inches(8.27)   # A4 Width: 210mm
    section.page_height = Inches(11.69) # A4 Height: 297mm
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)
    section.header_distance = Inches(0.4)
    section.footer_distance = Inches(0.4)
    
    # Configure Header with "Page | <PAGE>" matching reference PDF
    add_header_to_section(section)
    
    # 1. Front Matter: Pages 1 to 9 (Cover, Certificate, Declaration, Acknowledgement, Abstract, TOC)
    print("Building Front Matter (Pages 1 to 9)...")
    build_front_matter(doc)
    
    # 2. Chapters 1 to 3: Introduction, System Analysis & SRS, System Design & UML (Pages 10 to 37)
    print("Building Chapters 1 to 3 (Pages 10 to 37)...")
    build_chapters_1_to_3(doc)
    
    # 3. Chapters 4 to 7: Implementation, Modules, Testing, Conclusion (Pages 38 to 58)
    print("Building Chapters 4 to 7 (Pages 38 to 58)...")
    build_chapters_4_to_7(doc)
    
    # 4. Appendices & Bibliography: Source Code in Text, Walkthrough, References (Pages 59 to 81)
    print("Building Appendices & Bibliography (Pages 59 to 81)...")
    build_appendices_and_refs(doc)
    
    # Save the document
    print(f"Saving completed document to {output_filename}...")
    doc.save(output_filename)
    print(f"Successfully generated {output_filename}!")
    
    # Verify exact page count via Word COM
    print("Verifying page count via Word COM Automation...")
    page_count = get_word_page_count(output_filename)
    print(f"==================================================")
    print(f"TOTAL COMPUTED PAGE COUNT: {page_count} PAGES")
    print(f"==================================================")
    return page_count

if __name__ == "__main__":
    generate_report()
