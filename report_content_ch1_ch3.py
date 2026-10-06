"""
Chapters 1, 2, and 3 builder for ONCOP Project Report:
- Chapter 1: Introduction (1.1 to 1.8) -> Pages 10 to 16
- Chapter 2: System Analysis & SRS (2.1 to 2.12) -> Pages 17 to 24 (including DFD Level 0, 1, 2 diagrams)
- Chapter 3: System Design & UML Diagrams (3.1 to 3.10) -> Pages 25 to 37 (including Architecture, ERD, Activity, Sequence, Use Case, State Machine diagrams)
"""

from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from build_report_helpers import set_cell_background, set_cell_margins, set_cell_border

def add_chapter_title(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(16)
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(20)
    r.font.bold = True

def add_section_heading(doc, heading):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(heading)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True

def add_subsection_heading(doc, heading):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(heading)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True

def add_body_p(doc, text, bold_prefix="", space_after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(space_after)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def add_bullet_item(doc, bold_lead, text, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(space_after)
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = 'Arial'
    r_bullet.font.size = Pt(10)
    r_bullet.font.bold = True
    
    r_lead = p.add_run(bold_lead + ": ")
    r_lead.font.name = 'Times New Roman'
    r_lead.font.size = Pt(12)
    r_lead.font.bold = True
    
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.size = Pt(12)

def build_chapters_1_to_3(doc):
    
    # =========================================================================
    # CHAPTER 1: INTRODUCTION (Pages 10 to 16)
    # =========================================================================
    add_chapter_title(doc, "CHAPTER 1: INTRODUCTION")
    
    add_section_heading(doc, "1.1 Overview of the Project")
    add_body_p(doc, "is a revolutionary, production-grade civic grievance redressal and smart municipal orchestration ecosystem engineered to modernize and standardize how Indian citizens report, track, and resolve daily public infrastructure breakdown. In today’s rapidly expanding urban landscape, the single greatest impediment to effective civic governance is \"Administrative and Channel Fragmentation.\" Citizens currently find themselves trapped in a labyrinth of disconnected systems: dialing outdated telephonic municipal helplines (such as 1916), submitting unmonitored physical complaints at local ward counter registers, toggling between distinct state electricity distribution web portals, and navigating separated national grievance portals like CPGRAMS or Swachh Bharat Urban. This profound fragmentation results in severe cognitive overload for citizens, systemic loss of complaint traceability, lack of departmental accountability, and an acute absence of real-time municipal oversight.", "ONCOP (One Nation One Complaint Portal) ")
    add_body_p(doc, "ONCOP acts as a singular, high-performance \"Civic Command Center\" that permanently eliminates this multi-channel chaos. It is not merely another complaint form; it is an intelligent, unified digital public infrastructure where every essential municipal workflow operates under one seamless roof. By centralizing grievance intake, automated NLP-based department auto-routing, SLA-driven field officer dispatch, bidirectional national gateway synchronization, and real-time Leaflet GIS incident mapping, ONCOP guarantees that civic data flows transparently across every stage of a problem’s lifecycle—from initial public detection to certified ground resolution.")
    add_body_p(doc, "Built on a resilient, modern technology stack featuring Node.js (v26), Express.js, native SQLite (node:sqlite) operating with Write-Ahead Logging (WAL) mode, and vanilla HTML5/CSS/JavaScript with responsive GovTech aesthetics, ONCOP leverages intelligent algorithms to handle the heavy lifting of civic routing. Instead of requiring citizens to decipher complex municipal hierarchies or guess whether a clogged drain falls under the Public Works Department, the Jal Board, or the Urban Sanitation Division, ONCOP users benefit from:")
    
    add_bullet_item(doc, "Intelligent NLP Auto-Routing", "Advanced semantic keyword analysis dynamically inspects the grievance text, automatically assigning the ticket to the correct municipal wing (Roads, Sanitation, Water Works, Electricity, Sewerage, or Horticulture) and allocating the exact divisional nodal engineer in milliseconds.")
    add_bullet_item(doc, "National Portal Synchronization", "Seamless bidirectional gateway connectors automatically interface with official national systems, including CPGRAMS (pgportal.gov.in), Swachh Bharat Urban (MoHUA), Delhi Jal Board, and Urja Mitra (1912), generating standardized national reference numbers.")
    add_bullet_item(doc, "Dual-Photo Ground Verification", "To ensure absolute field truth and eliminate fraudulent closures, the platform enforces photographic proof both at submission (\"Before\" condition) and upon departmental resolution (\"After\" rectification proof) managed via a high-performance Multer upload engine.")
    add_bullet_item(doc, "Autonomous SLA Countdown & Escalation Worker", "An automated background worker actively audits all active grievances every 60 seconds, calculating elapsed time against strict time windows (12h to 72h). Tickets breaching their SLA are automatically escalated to Departmental HODs and the Municipal Commissioner's Command Desk.")
    add_bullet_item(doc, "Interactive Leaflet GIS Mapping", "Dual map interfaces provide both citizens and administrative officers with live geographic incident visualization, clustered ward pins, and spatial incident density analytics.")
    
    add_body_p(doc, "ONCOP represents a profound paradigm shift from passive complaint filing to active civic orchestration. By converting simple citizen observations into structured, SLA-bound municipal actions, ONCOP democratizes civic engagement, ensuring that every citizen has an authoritative voice and every municipal authority operates with absolute public transparency.")
    
    doc.add_page_break() # Page 11
    
    add_section_heading(doc, "1.2 Need for the Project")
    add_body_p(doc, "The modern Indian urban landscape is experiencing exponential population growth and rapid infrastructural expansion, yet the public service mechanisms used to maintain municipal amenities remain antiquated, fragmented, and opaque. As civic infrastructure—such as paved roadways, drinking water pipelines, sewage lines, high-tension electrical grids, and public recreational parks—faces continuous stress, the administrative complexity of managing public grievances has grown unsustainably. ONCOP is born out of several critical, unaddressed systemic crises:")
    
    add_bullet_item(doc, "Elimination of Multi-Portal \"Tab-Chaos\" & Helplines", "Citizens currently face extreme friction when trying to report problems. A pothole requires calling the Public Works Department; a dead streetlight requires contacting the electricity distribution company (Discom); an overflowing dumpster necessitates calling the municipal sanitation ward; and contaminated water requires visiting the Jal Board office. This fragmentation causes over 70% of civic issues to go unreported until catastrophic failures occur. There is an urgent national need for a unified single-window portal that consolidates all municipal departments into a single entry point.")
    add_bullet_item(doc, "Bridging the Civic \"Information & Accountability Gap\"", "Under conventional municipal systems, once a citizen files a complaint, it enters an administrative \"black box.\" The complainant receives no tracking reference, no estimated time of resolution, and no contact information for the assigned field officer. When the problem remains unaddressed, citizens have no institutional recourse other than filing costly RTI applications or enduring multiple physical visits to municipal offices. ONCOP bridges this gap by providing an open, public timeline ledger, live SLA countdown timers, and the direct official identity of the assigned nodal officer.")
    add_bullet_item(doc, "Demand for Ground-Truth Photographic Verification", "A prevalent flaw in legacy civic grievance portals is \"Ghost Closures\"—contractors and junior staff frequently mark complaints as \"Resolved\" in internal databases without performing physical repairs. ONCOP directly combats this fraud through its mandatory Dual-Photo Verification Pipeline, requiring field officers to upload verifiable \"After\" photos alongside mandatory resolution remarks before any status transition is permitted.")
    add_bullet_item(doc, "Automated Time-Bound Service Guarantee (SLA Enforcement)", "While public service guarantee charters mandate resolution timelines, manual enforcement is practically non-existent. Without automated monitoring, complaints languish for months. ONCOP establishes an autonomous, software-enforced SLA engine that monitors active tickets 24/7 and programmatically triggers multi-tier administrative escalations to senior directors when deadlines expire.")
    add_bullet_item(doc, "Democratizing Civic Redressal Across Linguistic & Digital Barriers", "A significant portion of the urban populace faces linguistic barriers when interacting with English-only digital portals. ONCOP democratizes civic access through its built-in real-time English and Hindi bilingual localization engine, tactile UI controls, dark/light accessibility themes, and instant printable civic receipts.")
    
    add_body_p(doc, "In summary, ONCOP is not merely an incremental technological update; it is an indispensable public utility infrastructure. It addresses the systemic need for a governance platform that values citizen trust, administrative speed, and absolute operational transparency over bureaucratic inertia.")
    
    doc.add_page_break() # Page 12
    
    add_section_heading(doc, "1.3 Objectives of the Project")
    add_body_p(doc, "The core architectural and societal objectives of the ONCOP platform are multi-layered, designed to redefine civic service delivery:")
    
    add_bullet_item(doc, "Unified Civic Command Architecture", "To engineer a unified full-stack single-window portal that centralizes civic complaint intake across all six core municipal departments (Roads, Sanitation, Water, Electricity, Sewerage, Horticulture), eliminating public confusion.")
    add_bullet_item(doc, "Intelligent Natural Language Processing (NLP) Auto-Routing", "To develop an automated heuristic NLP classification engine that analyzes citizen descriptions in real time, accurately mapping complaints to relevant departments and allocating designated field officers without manual clerical dispatch.")
    add_bullet_item(doc, "Bidirectional National e-Governance Synchronization", "To establish robust RESTful API connectors bridging local civic reports with official Government of India portals (CPGRAMS, Swachh Bharat Mission Urban, Delhi Jal Board, Urja Mitra), provisioning official national tracking reference numbers.")
    add_bullet_item(doc, "Strict SLA Countdown & Multi-Tier Escalation Automation", "To build an autonomous background worker daemon that continuously monitors ticket resolution countdowns against guaranteed municipal SLAs (12h to 72h) and automatically executes Level-1 and Level-2 escalations to Department HODs and Municipal Commissioners.")
    add_bullet_item(doc, "Geospatial Incident Intelligence via Leaflet GIS", "To integrate interactive, low-latency Leaflet maps supporting citizen GPS pin drops, ward polygon geofencing, and executive density heatmaps for municipal hotspot management.")
    add_bullet_item(doc, "Civic Transparency & Dual Photographic Audit Trail", "To implement an immutable, public-facing timeline audit log, dual-photo verification pipeline (Before vs. After repairs), citizen satisfaction ratings, and 1-click complaint reopening capabilities.")
    
    add_section_heading(doc, "1.4 Problem Statement")
    add_body_p(doc, "The current civic administration and municipal maintenance ecosystem in metropolitan and municipal towns across the nation is fundamentally broken. Despite massive capital expenditures on urban infrastructure, the operational machinery responsible for routine maintenance operates with chronic inefficiency, opacity, and citizen disillusionment. This systemic breakdown stems from several deeply entrenched structural bottlenecks:")
    
    add_bullet_item(doc, "The \"Jurisdictional Confusion\" Dilemma", "Urban civic responsibilities are divided among overlapping statutory boards: State PWD, Municipal Corporations, Jal Boards, Discoms, and Urban Development Authorities. When a road is dug up for pipeline repair and left unpaved, citizens do not know whether the road contractor, the water authority, or the municipal ward is responsible. As a result, complaints sent to the wrong department are routinely ignored, bounced between offices, or outright rejected.")
    add_bullet_item(doc, "Absence of Transparent Verification and \"Ghost Closures\"", "In traditional complaint handling, once a municipal contractor claims a task is completed, administrative systems mark the complaint as closed. In reality, potholes are superficially patched with loose gravel that washes away in the first rain, or garbage is pushed into side alleys rather than transported to landfills. Because existing portals lack verifiable photographic proof submission, public accountability is completely compromised.")
    add_bullet_item(doc, "Manual Clerical Dispatch Bottlenecks", "Legacy municipal grievance portals rely heavily on manual clerical operators sitting in zonal offices to read text complaints, determine the department, look up duty rosters, and manually forward letters. This human dispatch layer creates multi-week backlogs before an engineer even learns of a hazardous civic failure, such as exposed electrical cables or contaminated drinking water.")
    
    doc.add_page_break() # Page 13
    
    add_body_p(doc, "Severe Data Siloing Between Municipal and National Systems: Local municipal corporations maintain isolated databases that do not communicate with overarching state or national grievance monitoring portals like CPGRAMS. This disconnection prevents state urban development ministries from obtaining holistic visibility into systemic failures, contractor performance, and regional ward deficiencies.", "•  ")
    add_body_p(doc, "Total Lack of Enforcement on Service Level Agreements (SLAs): Although citizen charters stipulate strict turnaround times (e.g., 24 hours for streetlights, 48 hours for road repairs), there is no autonomous enforcement mechanism. Tickets sit untouched for weeks without triggering administrative penalties or supervisor notifications.", "•  ")
    add_body_p(doc, "Linguistic and Digital Accessibility Exclusion: The majority of existing municipal software systems are designed with rigid, desktop-centric layouts exclusively in English, effectively disenfranchising blue-collar workers, rural migrants, and senior citizens who require intuitive mobile workflows and vernacular Hindi support.", "•  ")
    
    add_body_p(doc, "The modern citizen demands an accessible, transparent, and accountable municipal experience. Current fragmented point solutions fail entirely to provide a cohesive governance orchestrator. ONCOP permanently resolves this dilemma by delivering an automated, intelligent, and transparent Single Source of Truth for civic problem resolution.", "Conclusion of Problem: ")
    
    add_section_heading(doc, "1.5 Scope of the Project")
    add_subsection_heading(doc, "1.5.1 In Scope")
    add_body_p(doc, "The architectural implementation of ONCOP is engineered to cover the following comprehensive functional and technical domains:")
    
    add_bullet_item(doc, "Full-Stack Single Window Web Application", "Architected with Node.js (v26), Express.js, native SQLite (node:sqlite) running in Write-Ahead Logging (WAL) mode, and a responsive GovTech UI built with modern HTML5, CSS3, and JavaScript.")
    add_bullet_item(doc, "Intelligent NLP Grievance Intake", "Real-time semantic keyword evaluation across six municipal categories (Roads, Sanitation, Water Works, Electricity, Sewerage, Horticulture), dynamically allocating nodal officers, phone credentials, and guaranteed SLA durations.")
    add_bullet_item(doc, "Bidirectional National Gateway Synchronization", "Official connector integration linking local complaints to CPGRAMS (pgportal.gov.in), Swachh Bharat Urban (MoHUA), Delhi Jal Board, and Urja Mitra (1912), generating standardized national reference codes.")
    add_bullet_item(doc, "Dual-Photo Verification Pipeline", "Real multipart file upload support via Multer for citizen \"Before\" photographic proof and field officer \"After\" rectification proof with strict file size and MIME-type validation.")
    add_bullet_item(doc, "Autonomous SLA Escalation Worker", "An automated background worker running on a 60-second cron cycle, tracking elapsed ticket hours, auto-escalating breached tickets to Level-1 (HOD) and Level-2 (Commissioner), and logging public timeline audit events.")
    add_bullet_item(doc, "Dual Interactive Leaflet GIS Maps", "Citizen grievance geocoding pin-drop map with address auto-lookup and an Administrative Officer Command Map featuring ward boundaries, urgency markers, and filter controls.")
    add_bullet_item(doc, "Multi-Channel Communication & Notifications", "Simulated SMS and WhatsApp dispatch notifications informing citizens of status transitions, officer details, and resolution alerts.")
    add_bullet_item(doc, "Citizen Accountability Suite", "Public tracking timeline, 1-to-5 star citizen satisfaction rating, instant complaint reopening logic, and printable official civic receipts.")
    add_bullet_item(doc, "Bilingual UI & GovTech Accessibility", "Complete English and Hindi localization toggle, high-contrast dark and light theme switcher, and WCAG-compliant responsive design.")
    
    doc.add_page_break() # Page 14
    
    add_subsection_heading(doc, "1.5.2 Out of Scope")
    add_body_p(doc, "To maintain high-velocity execution, architectural stability, and robust focus on core civic grievance orchestration during the current production release, the following functionalities are intentionally demarcated outside the system boundary:")
    
    add_bullet_item(doc, "Financial Municipal Taxation & Billing Modules", "While ONCOP integrates with municipal water and infrastructure portals for service complaints, it does not function as a property tax payment gateway or utility billing portal. Direct monetary transactions remain managed by statutory municipal revenue systems.")
    add_bullet_item(doc, "Heavyweight Video Post-Processing & Live Streaming", "The photo proof engine is optimized for high-resolution static photographic verification (JPEG, PNG, WebP). Real-time drone video processing or multi-track CCTV streams are excluded to prevent excessive server bandwidth consumption.")
    add_bullet_item(doc, "Judicial / RTI Statutory Legal Proceedings", "The platform acts as an administrative grievance redressal bridge. It does not replace formal judicial courts, consumer dispute commissions, or official statutory Right to Information (RTI) filing portals.")
    add_bullet_item(doc, "Internal Municipal Staff Payroll & Attendance", "ONCOP maintains duty rosters and contact credentials for nodal engineers but does not serve as an enterprise HRMS, biometric attendance system, or payroll disbursement platform.")
    add_bullet_item(doc, "Direct Hardware IoT Actuator Controls", "The system registers and tracks complaints regarding malfunctioning water pumps, streetlights, and traffic signals; however, it does not directly actuate electrical relays or municipal SCADA physical hardware switches.")
    
    add_section_heading(doc, "1.6 Advantages of the System")
    add_body_p(doc, "The implementation of ONCOP provides transformative advantages over conventional, fragmented municipal grievance methods. By combining modern asynchronous full-stack engineering with intelligent routing logic, the platform delivers decisive benefits across key operational dimensions:")
    
    add_bullet_item(doc, "Dramatically Reduced Turnaround Time (TAT)", "In legacy municipal workflows, passing a complaint from a citizen to an inspector took between 7 to 14 days due to clerical dispatch delays. ONCOP collapses this intake-to-dispatch latency to under 300 milliseconds through its automated NLP auto-routing engine.")
    add_bullet_item(doc, "Eradication of \"Ghost Closures\" via Photographic Accountability", "By mandating field officers to capture and upload an authentic \"After\" photo showing the rectified infrastructure before marking a ticket as resolved, fraudulent administrative closures are virtually eliminated.")
    add_bullet_item(doc, "Total Transparency & Citizen Empowerment", "Complainants possess 24/7 visibility into their ticket's progress via an open public timeline, viewing exact timestamps, assigned officer contact numbers, and official CPGRAMS/Swachh Bharat reference IDs.")
    add_bullet_item(doc, "Enforced Administrative Accountability via Autonomous SLA Escalations", "Department heads and municipal commissioners no longer need to manually review audit binders. The system's background worker proactively identifies SLA breaches and escalates delinquent tickets directly to executive dashboards.")
    
    doc.add_page_break() # Page 15
    
    add_bullet_item(doc, "Data-Driven Urban Planning & Zonal Resource Allocation", "Municipal executives gain access to live spatial heatmaps and ward-level KPI charts (total complaints, resolution rates, average turnaround hours, recurring category bottlenecks), enabling data-backed budgetary allocation for road repaving, drain desilting, and electrical grid upgrades.")
    add_bullet_item(doc, "Zero Native Binary Build Overhead & Ultra-High Reliability", "By utilizing Node.js v26's native SQLite driver (node:sqlite) operating in Write-Ahead Logging (WAL) mode, ONCOP achieves enterprise-grade relational persistence without external server dependencies (like separate database container clusters), ensuring 99.99% system availability with sub-16ms query latencies.")
    add_bullet_item(doc, "Inclusivity for All Citizens", "With complete Hindi and English bilingual support and high-contrast accessibility styling, ONCOP ensures that technology serves every stratum of urban society equally.")
    
    add_section_heading(doc, "1.7 Key Features of ONCOP")
    add_body_p(doc, "ONCOP is engineered with production-ready, enterprise-grade capabilities designed to solve every facet of urban municipal grievance management:")
    
    add_bullet_item(doc, "Smart NLP Multi-Department Auto-Routing Engine", "Understands semantic context from free-form complaint text (e.g., detecting keywords like 'pothole', 'garbage', 'sewer', 'wire', 'water leak') and instantly binds the grievance to the exact municipal division and designated field engineer.")
    add_bullet_item(doc, "Bidirectional National Portals Integration Gateway", "Automatically synchronizes grievances with CPGRAMS, Swachh Bharat Urban (MoHUA), Delhi Jal Board, and Urja Mitra 1912, providing authentic national tracking reference codes.")
    add_bullet_item(doc, "Dual-Photo Ground Truth Audit Pipeline", "Enforces photographic proof uploads for both citizen problem detection ('Before') and municipal field repair verification ('After'), preventing false resolutions.")
    add_bullet_item(doc, "Autonomous SLA Countdown & Escalation Engine", "A resilient 60-second background cron worker continuously monitors resolution windows, calculates overdue hours, and programmatically triggers multi-tier escalations to senior municipal leadership.")
    add_bullet_item(doc, "Dual Leaflet.js Interactive GIS Mapping Suite", "Features a Citizen Incident Location Pin-Drop Map and an Executive Incident Command GIS Dashboard with interactive cluster pins, ward filtering, and spatial density heatmaps.")
    add_bullet_item(doc, "Public Progression Timeline & Audit Ledger", "Chronological, tamper-evident progression log tracking every transition (Pending ➔ Assigned ➔ In Progress ➔ Escalated ➔ Resolved ➔ Reopened).")
    add_bullet_item(doc, "Multi-Channel SMS & WhatsApp Notification Dispatcher", "Simulates real-time telecom gateway alerts, notifying citizens and nodal officers via instant message upon registration, assignment, and completion.")
    
    doc.add_page_break() # Page 16
    
    add_bullet_item(doc, "Citizen Feedback, Star Rating & Reopening Workflow", "Citizens can rate resolved complaints from 1 to 5 stars, submit qualitative feedback, or immediately reopen tickets if field repairs fail inspection.")
    add_bullet_item(doc, "Executive Zonal Analytics & 1-Click CSV Audit Export", "Comprehensive municipal KPI dashboard tracking resolution rates, departmental rankings, ward-level SLA compliance, and instant CSV data export for administrative audits.")
    add_bullet_item(doc, "Bilingual GovTech Design System (EN/HI)", "Instant toggle between English and Hindi across all forms, modals, tables, and receipts, paired with dark/light themes and printable PDF/paper grievance receipts.")
    
    add_section_heading(doc, "1.8 Real-World Applications")
    add_body_p(doc, "The architectural flexibility, geospatial intelligence, and automated accountability mechanisms of ONCOP make it an indispensable platform across multiple governance sectors:")
    
    add_bullet_item(doc, "Municipal Corporations & Urban Local Bodies (ULBs)", "Functions as the core operating system for city municipal corporations (e.g., BMC, MCD, BBMP, GHMC), unifying fragmented zonal offices, field engineers, and citizen helplines into a single coordinated digital command center.")
    add_bullet_item(doc, "Smart Cities Mission Command & Control Centers (ICCC)", "Integrates seamlessly into municipal Integrated Command and Control Centers (ICCC), supplying live GIS incident feeds, SLA compliance telemetry, and automated contractor performance indices.")
    add_bullet_item(doc, "State Public Works & Highway Authorities", "Enables real-time pothole, asphalt caving, and bridge hazard monitoring, dispatching maintenance crews with exact GPS coordinates and photographic proof before road hazards trigger vehicular accidents.")
    add_bullet_item(doc, "State Electricity Boards & Discom Undertakings", "Accelerates rapid hazard containment for sparking overhead wires, snapped conductors, leaning poles, and blown transformers, reducing fatal electrocution risks through strict 12-hour SLA countdowns.")
    add_bullet_item(doc, "Public Health & Urban Sanitation Directorates", "Prevents dengue and cholera outbreaks by rapidly routing reports of overflowing garbage dumps, dead animal carcasses, and sewage overflows to sanitation inspectors with 24-hour turnaround enforcement.")
    add_bullet_item(doc, "Gated Communities, Industrial Parks & University Campuses", "Scalable for private urban infrastructure management, enabling facilities directors to monitor water supply, street lighting, road conditions, and landscaping across sprawling private campuses.")
    
    doc.add_page_break() # Page 17
    
    # =========================================================================
    # CHAPTER 2: SYSTEM ANALYSIS & SRS (Pages 17 to 24)
    # =========================================================================
    add_chapter_title(doc, "CHAPTER 2: SYSTEM ANALYSIS")
    
    add_section_heading(doc, "2.1 Introduction")
    add_body_p(doc, "System Analysis represents the foundational phase of the Software Development Life Cycle (SDLC) for ONCOP. This critical phase goes beyond surface-level feature enumeration; it conducts an exhaustive, rigorous dissection of the systemic administrative bottlenecks, communication breakdowns, and technological gaps that plague civic grievance handling. Our analysis focuses on the convergence of Asynchronous Web Engineering, Geospatial Information Systems (GIS), and Automated Municipal Workflows, aiming to minimize citizen friction and maximize administrative accountability.")
    add_body_p(doc, "The primary objective of this chapter is to provide a multi-dimensional Software Requirements Specification (SRS) and functional boundary evaluation. By systematically assessing technical constraints, operational realities, user expectations, and statutory governance mandates, we have architected an infrastructure that transcends static web registries. ONCOP is engineered to be an active, self-monitoring participant in urban governance—one that guarantees data integrity, enforces service turnaround times, and provides a Single Source of Truth (SSoT) for both the public and municipal administrators.")
    
    add_section_heading(doc, "2.2 Analysis of Existing Systems")
    add_body_p(doc, "Currently, the civic grievance landscape in India is heavily fragmented across disconnected legacy channels:")
    
    add_bullet_item(doc, "Telephonic Helplines (e.g., 1916 / Zonal Call Centers)", "Prone to endless busy signals, unrecorded calls, lack of photographic evidence, and severe human error during manual transcription of locations.")
    add_bullet_item(doc, "Physical Paper Registers at Ward Offices", "Subject to lost complaint books, zero time-bound tracking, clerical bribery, and complete lack of visibility for senior municipal commissioners.")
    add_bullet_item(doc, "Isolated Departmental Portals", "Discoms, Jal Boards, and PWD offices maintain independent, incompatible web forms. Citizens are forced to navigate 5+ different portals to report problems occurring in the same neighborhood.")
    add_bullet_item(doc, "Unintegrated National Portals (CPGRAMS / Swachh Bharat)", "High-level national portals frequently lack automated real-time dispatch to the exact junior engineer on the ground, creating weeks of bureaucratic forwarding.")
    
    add_section_heading(doc, "2.3 Proposed System Overview")
    add_body_p(doc, "ONCOP proposes a revolutionary, centralized Full-Stack Civic Command Architecture. Built with Node.js (v26), Express.js, native SQLite (node:sqlite) in WAL mode, Multer for multipart uploads, and interactive Leaflet GIS maps, ONCOP unifies citizen filing, departmental routing, officer verification, and national gateway synchronization into a single, high-performance platform. Every user interaction is accelerated by automated logic: complaint descriptions are parsed by a smart NLP auto-router, photographic proof is validated and stored, tickets are synchronized with national portals (CPGRAMS, Swachh Bharat), and an autonomous 60-second background cron daemon enforces SLA deadlines with automated multi-tier administrative escalations.")
    
    doc.add_page_break() # Page 18
    
    add_section_heading(doc, "2.4 System Objectives")
    add_body_p(doc, "The overarching objectives of the ONCOP platform are defined as follows:")
    
    add_bullet_item(doc, "Total Elimination of Civic Portal Fragmentation", "Consolidate road, sanitation, water, power, sewer, and park complaints into a unified single-window portal.")
    add_bullet_item(doc, "Autonomous NLP-Driven Departmental Routing", "Eliminate manual clerical delays by programmatically classifying grievances and assigning specific nodal officers in under 300ms.")
    add_bullet_item(doc, "Ground-Truth Verification & Fraud Prevention", "Enforce dual-photo verification (citizen 'Before' proof and officer 'After' rectification photo) with mandatory resolution notes.")
    add_bullet_item(doc, "Strict SLA Countdown & Multi-Tier Escalation Automation", "Continuously audit ticket lifetimes via a 24/7 background worker, programmatically escalating delinquent tickets to HODs and Commissioners.")
    add_bullet_item(doc, "National Portal Interoperability", "Provide bidirectional API sync with official Government of India gateways, generating verified national reference IDs.")
    add_bullet_item(doc, "High-Performance Zero-Dependency Relational Persistence", "Leverage native SQLite with WAL mode for microsecond query execution and 100% data durability without complex external database clusters.")
    
    add_section_heading(doc, "2.5 Feasibility Study")
    add_body_p(doc, "A feasibility study evaluates whether the proposed civic grievance system is technically, operationally, and economically sound.")
    
    add_subsection_heading(doc, "2.5.1 Technical Feasibility")
    add_body_p(doc, "The technical viability of ONCOP is confirmed by the proven maturity, performance, and cross-platform compatibility of modern web and database technologies:")
    
    add_bullet_item(doc, "Node.js (v26) & Express 5 Backend", "Node.js provides an event-driven, non-blocking I/O runtime capable of handling thousands of concurrent REST API requests with minimal memory overhead.")
    add_bullet_item(doc, "Native SQLite (node:sqlite) with WAL Mode", "Eliminates cumbersome C++ binary compilation issues while providing ACID-compliant multi-table persistence, instant writes via Write-Ahead Logging, and zero-maintenance operation.")
    add_bullet_item(doc, "Client-Side Leaflet.js Mapping Engine", "Provides ultra-lightweight, hardware-accelerated interactive GIS mapping that functions smoothly on desktop monitors and low-end mobile devices alike.")
    add_bullet_item(doc, "Multer Multipart Photo Pipeline", "Handles binary photo uploads securely with strict file-size clamping and unique timestamped disk persistence.")
    
    add_subsection_heading(doc, "2.5.2 Operational Feasibility")
    add_body_p(doc, "ONCOP is designed to mirror the intuitive mental model of citizens and civic workers:")
    
    add_bullet_item(doc, "Zero Learning Curve for Citizens", "Citizens simply enter their phone number, select a location on the interactive map, type a description, attach a photo, and click Submit. The system handles all backend complexity.")
    add_bullet_item(doc, "Streamlined Field Officer Workflow", "Field engineers receive dedicated portals listing active ward complaints, contact info, and a 1-click status update modal with camera upload.")
    add_bullet_item(doc, "Bilingual Inclusion (English & Hindi)", "Eliminates linguistic exclusion, allowing citizens from all backgrounds to file grievances comfortably.")
    
    doc.add_page_break() # Page 19
    
    add_subsection_heading(doc, "2.5.3 Economic Feasibility")
    add_body_p(doc, "From a financial and operational cost perspective, ONCOP offers unparalleled return on investment (ROI) for municipal bodies:")
    
    add_bullet_item(doc, "Zero Proprietary Software Licensing Fees", "Built entirely with open-source technologies (Node.js, Express, SQLite, Leaflet, OpenStreetMap), eliminating millions of rupees in enterprise licensing costs.")
    add_bullet_item(doc, "Low Infrastructure & Server Footprint", "Because ONCOP utilizes an ultra-lightweight architecture without heavy container microservices, the entire platform can run reliably on standard municipal cloud servers costing under $15 per month.")
    add_bullet_item(doc, "Drastic Reduction in Administrative Labor Costs", "Automating clerical classification, department assignment, and SLA escalation saves thousands of staff hours annually, allowing municipal personnel to focus on actual field repairs.")
    
    add_section_heading(doc, "2.6 System Requirements")
    add_body_p(doc, "To guarantee reliable full-stack performance, high-throughput complaint intake, and fluid GIS map interactions, the system adheres to the following hardware and software specifications:")
    
    add_subsection_heading(doc, "2.6.1 Hardware Requirements")
    add_bullet_item(doc, "Server Processor", "Multi-core 64-bit CPU (Intel Xeon, Core i5 8th Gen+, or AMD Ryzen 5+) to handle concurrent HTTP requests, background cron cycles, and image uploads.")
    add_bullet_item(doc, "Server Memory (RAM)", "Minimum 2 GB RAM (4 GB Recommended) to maintain SQLite WAL buffers and Express event loops without swapping.")
    add_bullet_item(doc, "Server Storage", "Minimum 20 GB SSD storage with high IOPS for persistent SQLite storage (oncop.db) and uploaded before/after proof images (/uploads).")
    add_bullet_item(doc, "Network Interface", "Standard broadband connection (10 Mbps+ dedicated) for real-time REST API communication and national portal webhook synchronization.")
    add_bullet_item(doc, "Client Hardware", "Any modern smartphone, tablet, laptop, or desktop with 1 GB available RAM and a web browser capable of rendering HTML5 canvas and Leaflet maps.")
    
    add_subsection_heading(doc, "2.6.2 Software Requirements")
    add_bullet_item(doc, "Operating System", "Cross-platform compatibility: Ubuntu Linux 22.04 LTS, Debian 12, CentOS 9, Windows 10/11 Server, or macOS Sonoma.")
    add_bullet_item(doc, "Runtime Environment", "Node.js v22.x or v26.x (with native node:sqlite DatabaseSync support) and npm v10+.")
    add_bullet_item(doc, "Backend Framework & Middleware", "Express.js 5.x, Multer 2.x, CORS 2.8.x, Dotenv 18.x.")
    add_bullet_item(doc, "Database Engine", "SQLite 3 (native embedded via node:sqlite) with PRAGMA journal_mode=WAL, foreign_keys=ON.")
    add_bullet_item(doc, "Frontend Technologies", "Vanilla HTML5, Modern CSS3 with CSS Custom Properties (Variables), ECMAScript 2024 (ES6+), Leaflet.js 1.9.4 GIS library, OpenStreetMap tile server.")
    add_bullet_item(doc, "Client Browsers", "Google Chrome 100+, Mozilla Firefox 100+, Microsoft Edge 100+, Safari 16+, or mobile web browsers.")
    
    doc.add_page_break() # Page 20
    
    add_section_heading(doc, "2.7 Functional Requirements (SRS - Core Capabilities)")
    add_body_p(doc, "Functional requirements define the precise operations, services, and behaviors that the ONCOP ecosystem performs:")
    
    add_bullet_item(doc, "FR-01: Citizen Grievance Intake", "The system shall provide a responsive intake form allowing citizens to enter their title, category, description, name, phone, ward, landmark, urgency level, GPS coordinates, and upload a photographic proof image.")
    add_bullet_item(doc, "FR-02: Smart NLP Keyword Auto-Routing", "The backend engine shall inspect incoming complaint descriptions for domain-specific keywords and automatically classify the issue into one of six departments: Roads, Sanitation, Water Works, Electricity, Sewerage, or Horticulture.")
    add_bullet_item(doc, "FR-03: Dynamic Officer Allocation & SLA Assignment", "Upon category determination, the system shall automatically assign the designated divisional nodal engineer, contact phone number, and compute the guaranteed SLA deadline (12h, 24h, 36h, 48h, or 72h).")
    add_bullet_item(doc, "FR-04: National Portals Gateway Synchronization", "The system shall format and dispatch structured grievance payloads to designated national portals (CPGRAMS, Swachh Bharat Urban, DJB, Urja Mitra) and store the generated national reference code.")
    add_bullet_item(doc, "FR-05: Multi-Channel SMS & WhatsApp Notification", "The platform shall log and emit simulated telecom dispatch alerts notifying complainants of registration, ticket IDs, assigned officer credentials, and resolution updates.")
    add_bullet_item(doc, "FR-06: Autonomous Background SLA Escalation", "A background worker running every 60 seconds shall calculate elapsed time since ticket creation. When elapsed time exceeds SLA hours, the worker shall automatically update escalation_level to 'Level 1 (Auto-Escalated to Dept HOD)', append a timeline event, and emit a high-priority dispatch notification.")
    add_bullet_item(doc, "FR-07: Field Officer Resolution & 'After' Proof Upload", "The platform shall provide an officer resolution terminal allowing authorized engineers to update status ('Assigned' ➔ 'In Progress' ➔ 'Resolved'), input resolution notes, and upload mandatory 'After' rectification proof photos.")
    add_bullet_item(doc, "FR-08: Public Complaint Timeline & Audit Trail", "The system shall display a chronological, tamper-evident timeline of all events associated with a complaint (creation, national sync, status transitions, escalations, officer remarks).")
    add_bullet_item(doc, "FR-09: Citizen Rating & Complaint Reopen Logic", "Citizens shall have the capability to submit 1-to-5 star ratings with feedback, or reopen unresolved complaints, which automatically flips the status to 'In Progress' and alerts the Zonal Supervisor.")
    add_bullet_item(doc, "FR-10: Executive Zonal Analytics & CSV Data Export", "The system shall compute real-time KPIs (total, pending, resolved, SLA breached, average turnaround hours) and provide a 1-click CSV download of all complaint records.")
    add_bullet_item(doc, "FR-11: Bilingual Localization & Theme Customization", "The UI shall support instantaneous language switching between English and Hindi, along with dark and light GovTech themes.")
    
    doc.add_page_break() # Page 21
    
    add_section_heading(doc, "2.8 Non-Functional Requirements")
    add_body_p(doc, "Non-functional requirements specify the technical constraints, quality standards, and operational criteria governing system performance:")
    
    add_bullet_item(doc, "NFR-01: Low Latency & High Throughput", "All REST API endpoints shall respond within 50 milliseconds under standard load. SQLite queries shall execute in sub-16ms due to native C-level DatabaseSync integration.")
    add_bullet_item(doc, "NFR-02: ACID Relational Integrity & Crash Safety", "The database shall enforce Write-Ahead Logging (WAL) and foreign key cascades, guaranteeing zero data corruption during unexpected server shutdowns or system crashes.")
    add_bullet_item(doc, "NFR-03: Security & Input Sanitization", "All citizen inputs shall undergo HTML sanitization to prevent Cross-Site Scripting (XSS). Parameterized SQL queries shall be strictly enforced across all routes to completely prevent SQL Injection (SQLi).")
    add_bullet_item(doc, "NFR-04: Abuse Prevention & Rate Limiting", "The API shall enforce an in-memory IP rate limiter restricting clients to a maximum of 30 requests per minute per IP address, preventing denial-of-service (DoS) and bot spam.")
    add_bullet_item(doc, "NFR-05: Cross-Browser & Mobile Parity", "The frontend design system shall maintain 100% visual and functional consistency across Chrome, Firefox, Safari, Edge, and mobile viewports down to 320px width.")
    add_bullet_item(doc, "NFR-06: High Availability & Autonomous Recovery", "The background cron worker and Express server shall execute with self-healing error catch blocks, ensuring that individual network failures do not bring down core intake workflows.")
    
    add_section_heading(doc, "2.9 Logic Flow & Sequence Processing")
    add_body_p(doc, "To guarantee orderly civic complaint processing, ONCOP implements a strict three-stage lifecycle flow:")
    
    add_bullet_item(doc, "Stage 1: Intake, Validation & Smart NLP Auto-Routing", "The citizen submits a grievance with location coordinates, description, and photo. The system sanitizes inputs, analyzes description keywords using NLP heuristics, assigns the appropriate municipal department, binds the designated nodal engineer, computes the SLA deadline, persists the ticket to SQLite, syncs with national gateways (CPGRAMS/Swachh Bharat), and emits telecom alerts.")
    add_bullet_item(doc, "Stage 2: Operational Investigation & Autonomous SLA Monitoring", "The assigned field officer accesses the ticket, marks status as 'In Progress', and inspects the site. Simultaneously, the 60-second background cron worker tracks the ticket's elapsed hours. If the SLA expires before resolution, the ticket is auto-escalated to Level-1, alerting the Department HOD and Municipal Commissioner.")
    add_bullet_item(doc, "Stage 3: Verification, Citizen Rating & Closure / Reopening", "Upon repair completion, the officer submits mandatory resolution remarks and uploads an 'After' proof photo, transitioning the status to 'Resolved'. The citizen is notified, reviews the public timeline and photo proof, rates the service, or exercises the 1-click Reopen option if dissatisfied.")
    
    doc.add_page_break() # Page 22
    
    # =========================================================================
    # 2.10 DATA FLOW DIAGRAM (DFD) ANALYSIS - ACTUAL DIAGRAMS (NOT IMAGES)
    # =========================================================================
    add_section_heading(doc, "2.10 Data Flow Diagram (DFD) Analysis")
    add_body_p(doc, "The following section provides the architectural Data Flow Diagrams for ONCOP, modeled using structured diagrammatic matrices representing external entities, processes, data stores, and bi-directional information pipelines.")
    
    add_subsection_heading(doc, "Figure 2.1: Level 0 Context Data Flow Diagram (Context DFD)")
    
    dfd0_table = doc.add_table(rows=7, cols=3)
    dfd0_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    dfd0_table.autofit = False
    
    # widths: 2.0 in, 2.6 in, 2.0 in
    widths = [Inches(2.0), Inches(2.6), Inches(2.0)]
    for row in dfd0_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = widths[idx]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            
    # Row 0: Entity [CITIZEN]
    c0 = dfd0_table.cell(0, 0)
    set_cell_background(c0, "1E3A8A")
    set_cell_border(c0, top={'val': 'single', 'sz': '6', 'color': '1E3A8A'}, bottom={'val': 'single', 'sz': '6', 'color': '1E3A8A'}, left={'val': 'single', 'sz': '6', 'color': '1E3A8A'}, right={'val': 'single', 'sz': '6', 'color': '1E3A8A'})
    p = c0.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ ENTITY: CITIZEN ]\n• Grievance Filing\n• Photo Evidence\n• Status Tracking\n• Feedback & Rating")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    
    # Row 0: Process (0.0 ONCOP CENTRAL SYSTEM)
    c1 = dfd0_table.cell(0, 1)
    set_cell_background(c1, "F1F5F9")
    set_cell_border(c1, top={'val': 'single', 'sz': '8', 'color': '0F172A'}, bottom={'val': 'single', 'sz': '8', 'color': '0F172A'}, left={'val': 'single', 'sz': '8', 'color': '0F172A'}, right={'val': 'single', 'sz': '8', 'color': '0F172A'})
    p = c1.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("( PROCESS 0.0 )\nONCOP SYSTEM\nSingle-Window Civic\nOrchestration Engine\n• NLP Auto-Routing\n• SLA Monitoring\n• GIS Pin Mapping")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    
    # Row 0: Entity [FIELD OFFICER]
    c2 = dfd0_table.cell(0, 2)
    set_cell_background(c2, "065F46")
    set_cell_border(c2, top={'val': 'single', 'sz': '6', 'color': '065F46'}, bottom={'val': 'single', 'sz': '6', 'color': '065F46'}, left={'val': 'single', 'sz': '6', 'color': '065F46'}, right={'val': 'single', 'sz': '6', 'color': '065F46'})
    p = c2.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ ENTITY: FIELD OFFICER ]\n• Ticket Intake\n• Site Inspection\n• Resolution Remarks\n• 'After' Photo Proof")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    
    # Flows Row 1
    c10 = dfd0_table.cell(1, 0)
    p = c10.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("▲ ▼ Ticket Data\nSMS Notifications").font.size = Pt(9)
    
    c11 = dfd0_table.cell(1, 1)
    p = c11.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("▲ ▼ Multi-Agency Dataflow\nCore REST API").font.size = Pt(9)
    
    c12 = dfd0_table.cell(1, 2)
    p = c12.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("▲ ▼ Field Workflows\nPhoto Verification").font.size = Pt(9)
    
    # Row 2: Secondary External Entities
    c20 = dfd0_table.cell(2, 0)
    set_cell_background(c20, "4C1D95")
    p = c20.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ NATIONAL PORTALS ]\n• CPGRAMS (Central)\n• Swachh Bharat (MoHUA)\n• Delhi Jal Board\n• Urja Mitra (1912)")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    
    c21 = dfd0_table.cell(2, 1)
    set_cell_background(c21, "334155")
    p = c21.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ DATA STORES (D1-D4) ]\nSQLite oncop.db (WAL)\n• Complaints & Timeline\n• External Sync Logs\n• Notifications History")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    
    c22 = dfd0_table.cell(2, 2)
    set_cell_background(c22, "831843")
    p = c22.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ MUNICIPAL EXEC ]\n• Zonal HODs\n• Municipal Commissioner\n• SLA Escalation Desk\n• Analytics & CSV Audit")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

    add_body_p(doc, "Figure 2.1 illustrates the Level 0 Context Data Flow Diagram, highlighting how the ONCOP engine acts as the central boundary mediator between Citizens, Field Engineers, National Portals, and Municipal Executives.")
    
    add_subsection_heading(doc, "Level 1 DFD: Subsystem Process Decomposition")
    add_body_p(doc, "The Level 1 DFD decomposes the core ONCOP engine into four granular operational sub-processes:")
    add_bullet_item(doc, "Process 1.0 (Grievance Intake & Photo Handling)", "Accepts citizen payload via Express REST API; Multer persists proof photo to disk storage /uploads and returns file URI.")
    add_bullet_item(doc, "Process 2.0 (Smart NLP Routing & SLA Allocation)", "Evaluates text keywords (e.g. pothole ➔ roads, garbage ➔ sanitation); binds designated nodal officer, ward, and SLA window (12h-72h).")
    add_bullet_item(doc, "Process 3.0 (National Gateway Synchronization)", "Dispatches standardized JSON to CPGRAMS / Swachh Bharat / Jal Board; logs external acknowledgment ID in external_sync_logs table.")
    add_bullet_item(doc, "Process 4.0 (Autonomous SLA Countdown & Escalation)", "Background cron worker polls complaints table every 60s; flags overdue tickets; updates escalation_level to 'Level 1'; alerts Municipal Commissioner Desk.")
    
    doc.add_page_break() # Page 23
    
    add_section_heading(doc, "2.11 Detailed System Modules")
    add_body_p(doc, "The ONCOP platform is architected into eight highly cohesive, decoupled micro-modules:")
    
    add_bullet_item(doc, "Module 1: Citizen Grievance Intake & Live Geolocation Tagger", "A responsive multi-input portal capturing grievance titles, detailed descriptions, category selections, citizen phone numbers, and pinpoint geographic coordinates via GPS auto-detection or interactive map clicks.")
    add_bullet_item(doc, "Module 2: Smart NLP Auto-Routing & SLA Allocation Engine", "A high-speed heuristic text classification engine running on the Node.js backend that parses raw complaint strings for domain-specific tokens, automatically mapping grievances to one of six municipal departments and assigning duty engineers.")
    add_bullet_item(doc, "Module 3: National Portal Integration Gateway", "A robust API adapter layer that constructs official Government of India JSON payloads for CPGRAMS, Swachh Bharat Urban, Delhi Jal Board, and Urja Mitra, recording external acknowledgment references.")
    add_bullet_item(doc, "Module 4: Officer Field Investigation & Dual-Photo Verification Pipeline", "A dedicated officer dashboard that enables field engineers to review assigned ward tickets, navigate to site coordinates, inspect citizen 'Before' photos, and submit verified 'After' rectification proof images.")
    add_bullet_item(doc, "Module 5: Automated SLA Countdown & Municipal Escalation Cron Worker", "An autonomous background worker daemon executing every 60 seconds that evaluates elapsed time against guaranteed SLAs, triggers multi-tier administrative escalations, and updates the public timeline.")
    add_bullet_item(doc, "Module 6: Real-Time Leaflet Incident Command GIS Mapping", "A spatial mapping engine rendering live complaint pins across urban wards, color-coded by urgency and status, complete with interactive popup modals and cluster counters.")
    add_bullet_item(doc, "Module 7: Multi-Channel SMS & WhatsApp Notification Dispatcher", "A telecom dispatch simulation service that generates formatted SMS and WhatsApp messages upon registration, assignment, and status transitions, persisting records in the notifications table.")
    add_bullet_item(doc, "Module 8: Citizen Feedback, Star Rating & Reopening Workflow", "A public accountability engine enabling citizens to track tickets, review officer resolution proof, award 1-to-5 star satisfaction ratings, or reopen unresolved issues.")
    
    add_section_heading(doc, "2.12 Summary And Conclusion")
    add_body_p(doc, "Chapter 2 has provided an exhaustive Software Requirements Specification (SRS) and system analysis of the ONCOP ecosystem. By deconstructing the systemic failures of existing fragmented municipal helplines, we have established the definitive case for a centralized, intelligent Single Source of Truth for civic problem resolution.")
    add_body_p(doc, "Through our analysis of functional and non-functional requirements, technical and economic feasibility, and multi-tier Data Flow Diagrams, every design choice—from the native SQLite WAL architecture to the automated background SLA escalation engine—has been validated for production readiness. With the analytical framework locked, we transition directly into Chapter 3: System Design, where these requirements are translated into concrete system architectures, database schemas, and UML diagrams.")
    
    doc.add_page_break() # Page 24
    
    # =========================================================================
    # CHAPTER 3: SYSTEM DESIGN & UML DIAGRAMS (Pages 25 to 37)
    # =========================================================================
    add_chapter_title(doc, "CHAPTER 3: SYSTEM DESIGN")
    
    add_section_heading(doc, "3.1 Introduction to Technical Design")
    add_body_p(doc, "System Design is the most intricate and critical phase of the software engineering lifecycle, representing the translation of abstract requirements into an executable, high-performance architectural framework. For a public infrastructure platform like ONCOP that handles concurrent citizen traffic, multipart photographic evidence, live geospatial coordinates, and automated SLA monitoring, a robust architectural foundation is essential.")
    add_body_p(doc, "The design phase for ONCOP functions as an architectural bridge, establishing a decoupled, multi-layered microservice structure. We have adopted an asynchronous REST-driven client-server architecture, leveraging Node.js (v26) and Express.js for the backend API, native SQLite (node:sqlite) with Write-Ahead Logging (WAL) mode for database persistence, and a modern vanilla HTML5/CSS/JavaScript client enhanced by Leaflet.js for GIS mapping. Our design philosophy centers on three core pillars:")
    
    add_bullet_item(doc, "Architectural Resilience", "Decoupling file storage, database persistence, and background cron monitoring so that high photo upload traffic never impairs API responsiveness or background SLA audits.")
    add_bullet_item(doc, "State Fluidity & Real-Time Accountability", "Implementing an immutable, chronological progression timeline where every status change, officer remark, and SLA escalation is permanently recorded.")
    add_bullet_item(doc, "Security-First Engineering", "Enforcing strict input sanitization against XSS, parameterized queries against SQL injection, IP rate limiting against DoS attacks, and dual-photo proof requirements against fraudulent ticket closures.")
    
    add_section_heading(doc, "3.2 UI/UX Design & Civic Design System")
    add_body_p(doc, "The User Interface of ONCOP is engineered with a citizen-centric, accessibility-first philosophy, designed to inspire public trust and eliminate technological friction for citizens of all digital literacy levels. Key UI/UX design pillars include:")
    
    add_bullet_item(doc, "GovTech Aesthetic Design Tokens", "ONCOP utilizes a curated color palette reflecting authoritative government public utility design: Deep Ashoka Navy (#0f172a, #1e3a8a) for institutional trust, Tiranga Saffron (#ea580c, #f97316) for primary CTAs and emergency alerts, Forest Emerald (#059669) for verified resolutions, and Slate Gray (#f8fafc) for readability.")
    add_bullet_item(doc, "Dual-Theme Engine (Light & Dark)", "The platform incorporates a real-time theme switcher utilizing CSS custom properties, allowing seamless toggling between an official daytime light theme and a battery-efficient high-contrast dark theme.")
    
    doc.add_page_break() # Page 25
    
    add_bullet_item(doc, "Bilingual Localization Architecture (English & Hindi)", "Recognizing India's linguistic diversity, ONCOP features an instant bilingual toggle. Every form field, button, status badge, modal dialog, and printable receipt dynamically switches between English and formal Hindi (e.g. 'Pending' ➔ 'लंबित', 'Resolved' ➔ 'समाधान हुआ', 'Submit Grievance' ➔ 'शिकायत दर्ज करें').")
    add_bullet_item(doc, "Tactile Micro-Interactions & Responsive Layout", "All interactive components feature CSS transitions, hover feedback, active button states, and collapsible filter bars. The layout dynamically adapts across 4K monitors, laptops, tablets, and smartphones.")
    add_bullet_item(doc, "Printable Verifiable Civic Receipt", "Citizens can generate an official printable civic grievance receipt complete with ticket UUID, QR code simulation, assigned officer contact, and official national portal synchronization details.")
    
    add_section_heading(doc, "3.3 Database Design & Data Persistence")
    add_body_p(doc, "The persistence layer of ONCOP is engineered for maximum relational integrity, zero maintenance overhead, and microsecond query latencies. Rather than incurring the memory overhead and operational complexity of external database server clusters, ONCOP utilizes Node.js v26's native SQLite engine (node:sqlite) via DatabaseSync.")
    add_body_p(doc, "To achieve production-grade concurrency, the database operates with Write-Ahead Logging (PRAGMA journal_mode = WAL). WAL mode allows simultaneous readers and writers without read-write locking contention. The database enforces foreign key constraints (PRAGMA foreign_keys = ON) and cascade deletes across related child tables.")
    
    add_body_p(doc, "The schema is structured into five specialized normalized relational tables:", "Normalized Relational Portfolio: ")
    add_bullet_item(doc, "complaints (Master Entity)", "Stores ticket UUID, title, category, description, citizen contact, ward, landmark, urgency, SLA hours, creation timestamp, status, assigned department, assigned nodal officer, phone, escalation level, latitude, longitude, before/after photo file paths, rating, feedback, and national portal sync credentials.")
    add_bullet_item(doc, "timeline (Audit Progression Entity)", "Maintains a chronological record of every event tied to a complaint (complaint_id FK, status, timestamp, note).")
    add_bullet_item(doc, "external_sync_logs (National Gateway Entity)", "Logs every external sync handshake (portal name, national acknowledgment ID, response payload, timestamp).")
    add_bullet_item(doc, "notifications (Telecom Dispatch Entity)", "Records all simulated SMS and WhatsApp alerts dispatched to citizens and officers.")
    add_bullet_item(doc, "users (Authentication & RBAC Entity)", "Stores citizen, officer, and administrator user credentials, roles, assigned departments, and designations.")
    
    doc.add_page_break() # Page 26
    
    # =========================================================================
    # 3.4 SYSTEM ARCHITECTURE DIAGRAM - ACTUAL DIAGRAM (NOT AN IMAGE)
    # =========================================================================
    add_section_heading(doc, "3.4 System Architecture Diagram")
    add_body_p(doc, "Figure 3.1 represents the comprehensive multi-tier Decoupled Microservice Architecture of the ONCOP platform, modeled as a native architectural structural diagram:")
    
    add_subsection_heading(doc, "Figure 3.1: Multi-Tier Decoupled System Architecture")
    
    arch_table = doc.add_table(rows=9, cols=1)
    arch_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    arch_table.autofit = False
    for row in arch_table.rows:
        row.cells[0].width = Inches(6.6)
        set_cell_margins(row.cells[0], top=60, bottom=60, left=100, right=100)
        
    def format_arch_box(cell, title, content, bg_hex, border_hex):
        set_cell_background(cell, bg_hex)
        set_cell_border(cell, 
                        top={'val': 'single', 'sz': '6', 'color': border_hex},
                        bottom={'val': 'single', 'sz': '6', 'color': border_hex},
                        left={'val': 'single', 'sz': '6', 'color': border_hex},
                        right={'val': 'single', 'sz': '6', 'color': border_hex})
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(title + "\n")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        if bg_hex in ["1E3A8A", "0F172A", "065F46", "334155"]:
            r.font.color.rgb = RGBColor(255, 255, 255)
            
        r_body = p.add_run(content)
        r_body.font.name = 'Times New Roman'
        r_body.font.size = Pt(9.5)
        if bg_hex in ["1E3A8A", "0F172A", "065F46", "334155"]:
            r_body.font.color.rgb = RGBColor(226, 232, 240)
            
    def format_arch_arrow(cell, label):
        set_cell_background(cell, "FFFFFF")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(f"▼  {label}  ▼")
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(71, 85, 105)

    format_arch_box(arch_table.cell(0, 0), 
                    "LAYER 1: PRESENTATION & INTERACTION TIER (CLIENT)",
                    "Vanilla HTML5 • Modern CSS3 GovTech Design System • Bilingual Engine (EN/HI) • Leaflet.js GIS Engine • Receipt Generator",
                    "1E3A8A", "1E3A8A")
    format_arch_arrow(arch_table.cell(1, 0), "HTTP/HTTPS REST API Requests • Multipart Form-Data (Proof Photos)")
    
    format_arch_box(arch_table.cell(2, 0),
                    "LAYER 2: API GATEWAY & SECURITY SANDBOX (EXPRESS.JS)",
                    "Express 5.x REST Router • Security Headers (X-Frame, CSP, XSS) • In-Memory Rate Limiter (30 req/min) • Multer Engine (/uploads)",
                    "0F172A", "0F172A")
    format_arch_arrow(arch_table.cell(3, 0), "Internal Controller Dispatch & Asynchronous Pipeline Invocation")
    
    format_arch_box(arch_table.cell(4, 0),
                    "LAYER 3: CORE LOGIC, AUTO-ROUTING & BACKGROUND WORKER TIER",
                    "Smart NLP Keyword Classifier • Officer & Ward Dispatcher • 60s Background SLA Escalation Cron Daemon • govIntegration Connector",
                    "065F46", "065F46")
    format_arch_arrow(arch_table.cell(5, 0), "Node.js Native DatabaseSync Driver (PRAGMA WAL Mode • Sub-16ms Queries)")
    
    format_arch_box(arch_table.cell(6, 0),
                    "LAYER 4: RELATIONAL PERSISTENCE TIER (SQLITE oncop.db)",
                    "complaints (Master) • timeline (Audit) • external_sync_logs • notifications • users • 4 Production B-Tree Indexes",
                    "334155", "334155")
    format_arch_arrow(arch_table.cell(7, 0), "Bi-directional External REST Webhooks & Telecom Dispatch Alerts")
    
    format_arch_box(arch_table.cell(8, 0),
                    "LAYER 5: EXTERNAL NATIONAL GATEWAYS & TELECOM DISPATCH TIER",
                    "CPGRAMS (pgportal.gov.in) • Swachh Bharat Urban (MoHUA) • Delhi Jal Board • Urja Mitra (1912) • SMS/WhatsApp Engine",
                    "F8FAFC", "94A3B8")
                    
    doc.add_page_break() # Page 27
    
    add_section_heading(doc, "3.4.1 Comprehensive Architectural Layers Breakdown")
    add_body_p(doc, "The architectural tiers detailed in Figure 3.1 work collaboratively to deliver an ultra-responsive, fault-tolerant municipal experience:")
    
    add_bullet_item(doc, "Presentation & Interaction Layer (Frontend)", "Responsible for DOM rendering, bilingual string interpolation, form validation, and interactive GIS mapping. Operating as a single-page interface, it communicates asynchronously with backend endpoints via the browser Fetch API, providing instant UI feedback without jarring full-page refreshes.")
    add_bullet_item(doc, "API Gateway & Security Layer (Express 5.x)", "Serves as the front-line gatekeeper. It intercepts all inbound HTTP traffic, enforces security headers (nosniff, SAMEORIGIN, strict-origin-when-cross-origin), applies an in-memory IP rate limiter to mitigate bot attacks, sanitizes text payloads against XSS, and routes file uploads through Multer's disk storage engine.")
    add_bullet_item(doc, "Business Logic & Auto-Routing Layer", "The cognitive core of ONCOP. It executes the heuristic NLP keyword evaluation algorithm, dynamically matching complaint text to one of six municipal departments, binding designated nodal officers, and assigning strict SLA time limits. It also houses the 60-second background cron worker that evaluates SLA countdowns.")
    add_bullet_item(doc, "Relational Persistence Layer (SQLite Engine)", "Manages five strictly typed relational tables within oncop.db. Enabled with Write-Ahead Logging (WAL) and B-tree indexing on complaint status, department, citizen phone, and creation date, this layer executes complex multi-table queries in sub-16 milliseconds.")
    add_bullet_item(doc, "External Gateways & Dispatch Layer", "Provides an abstraction layer interfacing with Government of India portals (CPGRAMS, Swachh Bharat, Jal Board, Urja Mitra) and simulates multi-channel telecom alerts via SMS and WhatsApp.")
    
    doc.add_page_break() # Page 28
    
    # =========================================================================
    # 3.5 ENTITY-RELATIONSHIP (ER) DIAGRAM - ACTUAL DIAGRAM (NOT AN IMAGE)
    # =========================================================================
    add_section_heading(doc, "3.5 Entity-Relationship (ER) Diagram Analysis")
    add_body_p(doc, "The database architecture of ONCOP follows a strictly normalized Relational Project Model. Figure 3.2 details the entity schemas, column attributes, primary/foreign keys, and relational linkages:")
    
    add_subsection_heading(doc, "Figure 3.2: Relational Database Schema & Entity Relationships")
    
    def render_table_schema(doc, table_name, columns, is_master=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"TABLE: {table_name}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        
        t = doc.add_table(rows=len(columns)+1, cols=4)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        
        col_widths = [Inches(1.8), Inches(1.2), Inches(1.2), Inches(2.4)]
        for r_idx, row in enumerate(t.rows):
            for c_idx, cell in enumerate(row.cells):
                cell.width = col_widths[c_idx]
                set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
                set_cell_border(cell, 
                                top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                                bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                                left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                                right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                                
        headers = ["Column Name", "Data Type", "Key / Null", "Description / Constraints"]
        for idx, h in enumerate(headers):
            cell = t.cell(0, idx)
            set_cell_background(cell, "1E3A8A" if is_master else "334155")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(h)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            
        for r_idx, (col, dtype, key, desc) in enumerate(columns):
            row = t.rows[r_idx + 1]
            if r_idx % 2 == 1:
                for c in row.cells: set_cell_background(c, "F8FAFC")
                
            for c_idx, val in enumerate([col, dtype, key, desc]):
                p = row.cells[c_idx].paragraphs[0]
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(val)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9)
                if c_idx == 0: r.font.bold = True
                if "PK" in val or "FK" in val: r.font.bold = True

    comp_cols = [
        ("id", "TEXT", "PK, NOT NULL", "Ticket UUID (e.g. 'ONCOP-2026-9481')"),
        ("title", "TEXT", "NOT NULL", "Short grievance headline"),
        ("category", "TEXT", "NOT NULL", "Category slug (roads, sanitation, water...)"),
        ("category_name", "TEXT", "NOT NULL", "Human readable category label"),
        ("description", "TEXT", "NOT NULL", "Detailed citizen grievance description"),
        ("citizen_name", "TEXT", "NOT NULL", "Complainant full name"),
        ("citizen_phone", "TEXT", "NOT NULL", "Citizen 10-digit mobile contact"),
        ("ward", "TEXT", "NOT NULL", "Municipal ward zone identifier"),
        ("landmark", "TEXT", "NOT NULL", "Street address or nearby landmark"),
        ("urgency", "TEXT", "DEFAULT 'Normal'", "Priority level (Low, Normal, Emergency)"),
        ("sla_hours", "INTEGER", "DEFAULT 48", "Resolution window in hours (12 to 72)"),
        ("created_at", "TEXT", "NOT NULL", "ISO-8601 ticket creation timestamp"),
        ("status", "TEXT", "DEFAULT 'Pending'", "Pending, Assigned, In Progress, Resolved"),
        ("assigned_dept", "TEXT", "NOT NULL", "Department name (e.g. Public Works Dept)"),
        ("assigned_officer", "TEXT", "NOT NULL", "Designated nodal field engineer"),
        ("officer_phone", "TEXT", "NOT NULL", "Duty engineer contact number"),
        ("escalation_level", "TEXT", "DEFAULT 'None'", "'None', 'Level 1', 'Level 2'"),
        ("lat, lng", "REAL", "NOT NULL", "Geographic GPS coordinates (Leaflet)"),
        ("photo_before", "TEXT", "NULLABLE", "File path to citizen proof photo"),
        ("photo_after", "TEXT", "NULLABLE", "File path to officer resolution photo"),
        ("rating, feedback", "INT, TEXT", "NULLABLE", "Citizen satisfaction star rating (1-5)"),
        ("gov_portal_name", "TEXT", "NULLABLE", "Official national portal (CPGRAMS, SBM)"),
        ("gov_reference_no", "TEXT", "NULLABLE", "Official national tracking reference code"),
        ("gov_sync_status", "TEXT", "DEFAULT 'Synced'", "Status of national gateway transmission")
    ]
    render_table_schema(doc, "complaints (Master Relational Node)", comp_cols, is_master=True)
    
    doc.add_page_break() # Page 29
    
    timeline_cols = [
        ("id", "INTEGER", "PK, AUTOINCREMENT", "Unique timeline event ID"),
        ("complaint_id", "TEXT", "FK, NOT NULL", "REFERENCES complaints(id) ON DELETE CASCADE"),
        ("status", "TEXT", "NOT NULL", "Ticket status state at time of event"),
        ("time", "TEXT", "NOT NULL", "Human readable formatted timestamp"),
        ("note", "TEXT", "NOT NULL", "Detailed audit note / remarks / escalation"),
        ("created_at", "TEXT", "NOT NULL", "ISO-8601 event timestamp")
    ]
    render_table_schema(doc, "timeline (Complaint Progression Audit Ledger)", timeline_cols)
    
    sync_cols = [
        ("id", "INTEGER", "PK, AUTOINCREMENT", "Unique sync log record ID"),
        ("complaint_id", "TEXT", "NOT NULL", "Referenced local ticket UUID"),
        ("portal_name", "TEXT", "NOT NULL", "Target national portal (CPGRAMS, SBM, DJB)"),
        ("external_ack_id", "TEXT", "NOT NULL", "National tracking acknowledgment code"),
        ("sync_status", "TEXT", "NOT NULL", "'Synced', 'Failed', 'Pending'"),
        ("response_payload", "TEXT", "NULLABLE", "JSON response string from gateway"),
        ("synced_at", "TEXT", "NOT NULL", "ISO-8601 gateway sync timestamp")
    ]
    render_table_schema(doc, "external_sync_logs (National Gateway Sync Records)", sync_cols)
    
    notif_cols = [
        ("id", "INTEGER", "PK, AUTOINCREMENT", "Unique notification ID"),
        ("channel", "TEXT", "NOT NULL", "Channel type ('SMS' or 'WhatsApp')"),
        ("recipient", "TEXT", "NOT NULL", "Target phone number / officer"),
        ("title", "TEXT", "NOT NULL", "Alert subject / notification headline"),
        ("body", "TEXT", "NOT NULL", "Full SMS / WhatsApp message text body"),
        ("sent_at", "TEXT", "NOT NULL", "ISO-8601 dispatch timestamp")
    ]
    render_table_schema(doc, "notifications (Telecom Alert History)", notif_cols)
    
    user_cols = [
        ("id", "TEXT", "PK, NOT NULL", "User ID string (e.g. 'demo-cit-1')"),
        ("name", "TEXT", "NOT NULL", "Full user name"),
        ("email, phone", "TEXT", "NULLABLE", "Contact credentials"),
        ("password", "TEXT", "NOT NULL", "User account password"),
        ("role", "TEXT", "NOT NULL", "Role ('citizen', 'officer', 'admin')"),
        ("department", "TEXT", "NULLABLE", "Designated department for officers"),
        ("designation", "TEXT", "NULLABLE", "Official title / job designation"),
        ("avatar", "TEXT", "NULLABLE", "Avatar icon / image file URI")
    ]
    render_table_schema(doc, "users (Authentication & Role-Based Access)", user_cols)
    
    add_body_p(doc, "Structural Cardinality Analysis: The complaints table serves as the master relational orchestrator. It maintains a 1-to-Many (1:N) relationship with timeline (every complaint has multiple progression events) and a 1-to-Many relationship with external_sync_logs. Foreign key constraints with ON DELETE CASCADE guarantee that deleting or archiving a complaint automatically purges associated timeline records, preventing orphaned data.")
    
    doc.add_page_break() # Page 30
    
    # =========================================================================
    # 3.6 ACTIVITY DIAGRAM - ACTUAL DIAGRAM (NOT AN IMAGE)
    # =========================================================================
    add_section_heading(doc, "3.6 Activity Diagram (Process Logic & SLA Lifecycle)")
    add_body_p(doc, "Figure 3.3 illustrates the dynamic behavior and decision-making logic of the ONCOP platform across the complete grievance redressal lifecycle:")
    
    add_subsection_heading(doc, "Figure 3.3: Grievance Lifecycle & SLA Escalation Activity Diagram")
    
    act_table = doc.add_table(rows=11, cols=4)
    act_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    act_table.autofit = False
    
    act_widths = [Inches(0.8), Inches(1.8), Inches(2.2), Inches(1.8)]
    for row in act_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = act_widths[idx]
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    act_headers = ["Step", "Workflow Phase", "Action / Decision Node", "Outcome / Transition"]
    for idx, h in enumerate(act_headers):
        cell = act_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    act_steps = [
        ("01", "Citizen Entry", "Citizen opens ONCOP, selects location on Leaflet map, inputs description, uploads 'Before' photo", "FormData payload submitted via POST /api/complaints"),
        ("02", "Security & Validation", "[Decision: Valid inputs & file size <= 10MB?]\n• No: Reject with 400 Bad Request\n• Yes: Proceed to Smart NLP Routing", "Input sanitized against XSS; file stored in /uploads by Multer"),
        ("03", "NLP Auto-Routing", "Backend parses description tokens against keyword taxonomy", "Category assigned (Roads, Water, etc.); nodal officer & SLA allocated"),
        ("04", "National Gateway Sync", "Asynchronous HTTP dispatch to CPGRAMS / Swachh Bharat / DJB", "Official national reference number generated (e.g. CPGRAMS-PWD/2026/8941)"),
        ("05", "Persistence & Alerts", "Atomic insert into complaints, timeline, and notifications tables", "201 Created returned to citizen; SMS alert emitted to citizen & officer"),
        ("06", "SLA Monitoring (24/7)", "[Decision: Ticket resolved before SLA deadline?]\n• Yes: Move to Resolution Phase\n• No: Trigger Autonomous Background Escalation", "Background cron worker evaluates elapsed hours every 60 seconds"),
        ("07", "Escalation Branch", "Worker updates escalation_level to 'Level 1'; appends audit event", "Urgent dispatch notification sent to Dept HOD & Municipal Commissioner"),
        ("08", "Field Investigation", "Field officer inspects site, performs repairs, captures 'After' photo", "Officer updates status to 'Resolved', enters remarks, attaches proof"),
        ("09", "Resolution Audit", "[Decision: 'After' photo and remarks provided?]\n• No: Block status transition\n• Yes: Commit resolution to SQLite", "Status becomes 'Resolved'; SMS resolution alert sent to citizen"),
        ("10", "Citizen Accountability", "[Decision: Citizen satisfied with repairs?]\n• Yes: Submit 1-5 star rating & feedback\n• No: Click 'Reopen Complaint' button", "High ratings archive ticket; Reopen resets status to 'In Progress'")
    ]
    
    for r_idx, (s_no, phase, action, outcome) in enumerate(act_steps):
        row = act_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([s_no, phase, action, outcome]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r.font.bold = True
            elif c_idx == 1:
                r.font.bold = True

    doc.add_page_break() # Page 31
    
    # =========================================================================
    # 3.7 SEQUENCE DIAGRAM - ACTUAL DIAGRAM (NOT AN IMAGE)
    # =========================================================================
    add_section_heading(doc, "3.7 Sequence Diagram")
    add_body_p(doc, "Figure 3.4 models the chronological message sequences between the Citizen Client, Express REST Gateway, NLP Routing Engine, SQLite Database, and External Gateways:")
    
    add_subsection_heading(doc, "Figure 3.4: Chronological Grievance Filing & Routing Sequence Diagram")
    
    seq_table = doc.add_table(rows=13, cols=4)
    seq_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    seq_table.autofit = False
    
    seq_widths = [Inches(0.6), Inches(1.8), Inches(2.2), Inches(2.0)]
    for row in seq_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = seq_widths[idx]
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    seq_headers = ["Time", "Origin ➔ Target", "Synchronous / Async Message Call", "Execution Response / Effect"]
    for idx, h in enumerate(seq_headers):
        cell = seq_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    seq_steps = [
        ("T1", "Citizen ➔ Express API", "POST /api/complaints (Multipart: photo + form data)", "API Gateway intercepts request; verifies rate limiter"),
        ("T2", "Express API ➔ Multer", "upload.single('photo') storage execution", "Writes photo to /uploads; returns filename proof_178...jpg"),
        ("T3", "Express API ➔ Input Guard", "sanitize(title, description, citizen_name)", "Purges HTML markup to eliminate XSS injection vectors"),
        ("T4", "Express API ➔ NLP Classifier", "detectCategory(description, user_selected_category)", "Parses keywords; returns mapped category (e.g. 'roads')"),
        ("T5", "NLP Classifier ➔ Duty Roster", "lookupDeptConfig('roads')", "Resolves PWD Dept, Er. V.K. Saxena, Phone & 48h SLA"),
        ("T6", "Express API ➔ govIntegration", "syncWithOfficialGovPortal(complaintPayload)", "Builds official JSON; generates CPGRAMS-PWD/2026/9481"),
        ("T7", "Express API ➔ SQLite Engine", "db.prepare('INSERT INTO complaints...').run(...)", "Persists complaint in oncop.db under WAL transaction"),
        ("T8", "Express API ➔ SQLite Engine", "db.prepare('INSERT INTO timeline...').run(...)", "Logs initial 'Submitted & Auto-Routed' event with timestamp"),
        ("T9", "Express API ➔ Notif Engine", "db.prepare('INSERT INTO notifications...').run(...)", "Logs simulated SMS to citizen phone and WhatsApp to officer"),
        ("T10", "Express API ➔ Citizen Client", "HTTP 201 Created (JSON ticket object)", "Client receives confirmation; renders ticket modal & Leaflet pin"),
        ("T11", "Cron Worker ➔ SQLite Engine", "SELECT * FROM complaints WHERE status != 'Resolved'", "Worker evaluates elapsed hours against sla_hours every 60s"),
        ("T12", "Officer ➔ Express API", "PATCH /api/complaints/:id/status (Resolved + Photo)", "Persists 'After' photo, remarks, and sets status to Resolved")
    ]
    
    for r_idx, (t_step, orig_targ, msg, resp) in enumerate(seq_steps):
        row = seq_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([t_step, orig_targ, msg, resp]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r.font.bold = True
            elif c_idx == 1:
                r.font.bold = True

    doc.add_page_break() # Page 32
    
    # =========================================================================
    # 3.8 USE CASE & STATE MACHINE UML DIAGRAMS
    # =========================================================================
    add_section_heading(doc, "3.8 Additional UML Diagrams (Use Case & State Machine)")
    add_body_p(doc, "To provide a 360-degree technical design specification, this section details the Use Case Matrix and the Formal State Machine Model governing ticket lifecycles:")
    
    add_subsection_heading(doc, "Figure 3.5: Actor vs. Use Case Boundary Specification Matrix")
    
    uc_table = doc.add_table(rows=6, cols=3)
    uc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    uc_table.autofit = False
    for row in uc_table.rows:
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(3.4)
        row.cells[2].width = Inches(1.4)
        for cell in row.cells:
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    uc_headers = ["Primary Actor", "Associated System Use Cases", "Relationship / Stereotype"]
    for idx, h in enumerate(uc_headers):
        cell = uc_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    uc_data = [
        ("Citizen\n(General Complainant)", "• UC-01: File Civic Grievance with Photo\n• UC-02: Track Real-Time Progression Timeline\n• UC-03: Rate Resolved Grievance (1-5 Stars)\n• UC-04: Reopen Unresolved Complaint\n• UC-05: Print Official Civic Receipt", "«initiates»\nDirect Web User"),
        ("Field Officer\n(Nodal Engineer)", "• UC-06: View Ward Assigned Grievance Queue\n• UC-07: Inspect Citizen 'Before' Evidence\n• UC-08: Transition Status ('In Progress' / 'Resolved')\n• UC-09: Upload Field Verification 'After' Photo\n• UC-10: Input Technical Resolution Remarks", "«executes»\nRole-Based Access"),
        ("Zonal Supervisor / HOD\n(Department Chief)", "• UC-11: Monitor Departmental SLA Adherence\n• UC-12: Receive Level-1 Escalation Alerts\n• UC-13: Reassign Delinquent Complaints\n• UC-14: Audit Nodal Engineer Performance", "«supervises»\nAdministrative Desk"),
        ("Municipal Commissioner\n(Executive Authority)", "• UC-15: Review City-Wide Incident Command Map\n• UC-16: Monitor Level-2 Emergency Escalations\n• UC-17: Analyze Zonal Ward Performance Heatmaps\n• UC-18: Export Official CSV Audit Ledgers", "«governs»\nExecutive Authority"),
        ("Background SLA Worker\n(System Daemon)", "• UC-19: Audit Active Grievance Timers (Every 60s)\n• UC-20: Auto-Trigger Level-1/2 Escalations\n• UC-21: Dispatch Emergency Notification Alerts\n• UC-22: Append Automated Timeline Events", "«automated»\nCron Worker Daemon")
    ]
    
    for r_idx, (act, ucs, rel) in enumerate(uc_data):
        row = uc_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([act, ucs, rel]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx == 0: r.font.bold = True
            
    doc.add_page_break() # Page 33
    
    add_subsection_heading(doc, "Figure 3.6: Complaint Lifecycle State Machine Transition Table")
    
    sm_table = doc.add_table(rows=7, cols=5)
    sm_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sm_table.autofit = False
    
    sm_widths = [Inches(1.2), Inches(1.4), Inches(1.4), Inches(1.2), Inches(1.4)]
    for row in sm_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = sm_widths[idx]
            set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    sm_headers = ["Current State", "Trigger Event", "Guard Condition", "Target State", "Side-Effect / Action"]
    for idx, h in enumerate(sm_headers):
        cell = sm_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    sm_data = [
        ("[Initial State]", "Citizen submits form", "Valid description & GPS", "Pending", "Persist to SQLite; Multer saves photo; SMS sent"),
        ("Pending", "NLP router processes ticket", "Category matched", "Assigned", "Nodal engineer bound; SLA timer begins; CPGRAMS synced"),
        ("Assigned", "Officer initiates site inspection", "Officer authenticated", "In Progress", "Timeline updated; officer contact published to citizen"),
        ("In Progress", "Elapsed time > SLA hours", "Status != 'Resolved'", "In Progress (Escalated)", "escalation_level ➔ Level 1; alert sent to Commissioner"),
        ("In Progress", "Officer completes repair", "Mandatory 'After' photo uploaded", "Resolved", "Photo persisted; resolution SMS sent; rating unlocked"),
        ("Resolved", "Citizen clicks 'Reopen'", "Resolution rejected within 7 days", "In Progress", "Status flipped back; alert dispatched to Zonal HOD")
    ]
    
    for r_idx, (curr, trig, guard, targ, action) in enumerate(sm_data):
        row = sm_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([curr, trig, guard, targ, action]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx in [0, 3]: r.font.bold = True

    # =========================================================================
    # 3.8.3 UML CLASS DIAGRAM (OBJECT-ORIENTED COMPONENT ARCHITECTURE)
    # =========================================================================
    doc.add_page_break()
    add_subsection_heading(doc, "Figure 3.7: Object-Oriented UML Class Diagram & Method Signatures")
    add_body_p(doc, "The following structural diagram models the object-oriented software abstractions, encapsulated methods, property attributes, and service layer dependencies governing ONCOP:")
    
    cls_table = doc.add_table(rows=6, cols=3)
    cls_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cls_table.autofit = False
    for row in cls_table.rows:
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(2.6)
        row.cells[2].width = Inches(2.2)
        for cell in row.cells:
            set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    cls_headers = ["Class / Subsystem", "Attributes & Encapsulated State", "Public Methods & API Signatures"]
    for idx, h in enumerate(cls_headers):
        cell = cls_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    cls_data = [
        ("GrievanceController\n«REST API Handler»", "- req: Express.Request\n- res: Express.Response\n- db: DatabaseSync", "+ postComplaint(FormData): Response\n+ getComplaints(FilterParams): Array\n+ getComplaintById(UUID): Object\n+ updateStatus(UUID, Status, Proof): OK\n+ reopenTicket(UUID, Reason): OK\n+ rateGrievance(UUID, Score): OK"),
        ("NLPRoutingService\n«Cognitive Engine»", "- DEPT_CONFIG: Dictionary\n- KEYWORD_MAP: Map<Str, Array>\n- WARD_GEO: GeoJSON Bounds", "+ detectCategory(text, fallback): String\n+ resolveOfficer(category): OfficerObj\n+ calculateSLA(category, urgency): Number\n+ lookupWardCoordinates(wardName): LatLng"),
        ("DatabaseSyncRepository\n«Persistence Layer»", "- dbPath: String\n- sqliteHandle: DatabaseSync\n- walConfig: PRAGMA_WAL", "+ insertComplaint(ComplaintRecord): String\n+ appendTimeline(EventRecord): Number\n+ logExternalSync(SyncRecord): Number\n+ pollActiveTickets(): Array<Complaint>\n+ commitEscalation(UUID, Level): Boolean"),
        ("GovGatewayAdapter\n«Enterprise Connector»", "- GOV_ENDPOINTS: ConfigMap\n- RETRY_POLICY: PolicyObject\n- AUTH_KEY: String", "+ syncWithOfficialGovPortal(Complaint): Object\n+ formatCPGRAMSPayload(Complaint): JSON\n+ formatSBMPayload(Complaint): JSON\n+ dispatchWebhook(URL, Payload): AckRef"),
        ("SLAEscalationWorker\n«Autonomous Daemon»", "- cronIntervalMs: 60000\n- activePollQuery: Statement\n- alertChannels: ['SMS', 'DESK']", "+ initDaemonHeartbeat(): Void\n+ evaluateElapsedHours(createdAt): Float\n+ executeLevel1Escalation(UUID): Void\n+ dispatchCommissionerAlert(Msg): Void")
    ]
    
    for r_idx, (cname, attrs, mths) in enumerate(cls_data):
        row = cls_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([cname, attrs, mths]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Consolas' if c_idx > 0 else 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx == 0: r.font.bold = True

    # =========================================================================
    # 3.8.4 UML COMPONENT & DEPLOYMENT ARCHITECTURE
    # =========================================================================
    doc.add_page_break()
    add_subsection_heading(doc, "Figure 3.8: UML Component & Deployment Architecture Specification")
    add_body_p(doc, "The deployment topology illustrates how software artifacts are distributed across execution nodes, network hardware, and cloud hosting tiers:")
    
    dep_table = doc.add_table(rows=5, cols=4)
    dep_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    dep_table.autofit = False
    for row in dep_table.rows:
        row.cells[0].width = Inches(1.5)
        row.cells[1].width = Inches(1.6)
        row.cells[2].width = Inches(1.8)
        row.cells[3].width = Inches(1.7)
        for cell in row.cells:
            set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
            set_cell_border(cell, 
                            top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                            right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
                            
    dep_headers = ["Deployment Node", "Execution Environment", "Hosted Components / Artifacts", "Protocols & Network Ports"]
    for idx, h in enumerate(dep_headers):
        cell = dep_table.cell(0, idx)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    dep_data = [
        ("Citizen / Officer Client Device", "Standard Mobile / Desktop Web Browser (Chrome, Safari, Edge)", "• Single Page Application (HTML5/CSS)\n• Leaflet.js Vector Map Renderer\n• Bilingual Language Dictionary (I18N)", "HTTPS (Port 443)\nWSS (Live Telemetry)"),
        ("Application & Web Gateway Server", "Node.js (v26 LTS) Single-Threaded Event Loop", "• Express 5.x REST API Microservice\n• Multer DiskStorage Engine (/uploads)\n• In-Memory IP Rate Limiting Guard", "HTTP / REST (Port 3000)\nReverse Proxy NGINX"),
        ("Relational Persistence Node", "Embedded SQLite DatabaseSync File Storage", "• Persistent Relational oncop.db\n• Write-Ahead Log Buffer (oncop.db-wal)\n• Shared Memory Cache (oncop.db-shm)", "Direct OS Memory Pointer\nSub-16ms Query Bus"),
        ("Statutory Government Gateways", "Central e-Governance Cloud Servers", "• CPGRAMS Portal (NIC Cloud)\n• Swachh Bharat Urban (MoHUA)\n• Delhi Jal Board & Urja Mitra 1912", "Secure REST Webhook\nTLS 1.3 Encryption")
    ]
    
    for r_idx, (node, env, comp, proto) in enumerate(dep_data):
        row = dep_table.rows[r_idx + 1]
        if r_idx % 2 == 1:
            for c in row.cells: set_cell_background(c, "F8FAFC")
        for c_idx, val in enumerate([node, env, comp, proto]):
            p = row.cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            if c_idx == 0: r.font.bold = True

    add_section_heading(doc, "3.9 Module Description")
    add_body_p(doc, "A modular architectural decomposition ensures that each functional engine in ONCOP operates independently with well-defined APIs:")
    
    add_bullet_item(doc, "The Intake & Spatial Geocoder Engine", "Extracts metadata, validates phone numbers and GPS coordinates, interfaces with the browser Geolocation API, and formats payloads for API submission.")
    add_bullet_item(doc, "The Heuristic NLP Auto-Routing Processor", "Uses tokenized keyword scoring to categorize complaints into Roads, Sanitation, Water, Electricity, Sewerage, or Horticulture, determining assigned officers and SLA thresholds.")
    add_bullet_item(doc, "The National Portal Synchronization Gateway", "Acts as an enterprise adapter, converting internal database models into Government of India API schemas and persisting acknowledgment tokens.")
    add_bullet_item(doc, "The Autonomous SLA Countdown Daemon", "A lightweight, robust background worker that continuously audits open tickets, performs time-delta calculations, and triggers multi-tier escalations.")
    add_bullet_item(doc, "The Leaflet GIS Visualization Engine", "Renders interactive vector tiles, marker clusters, and custom SVG status pins across urban ward zones.")
    
    doc.add_page_break() # Page 36
    
    add_section_heading(doc, "3.10 Chapter Summary")
    add_body_p(doc, "Chapter 3 has provided an exhaustive technical blueprint of the ONCOP ecosystem. Throughout this chapter, we have translated abstract functional requirements into concrete, executable system designs. By establishing a decoupled client-server architecture, a normalized relational database schema with Write-Ahead Logging (WAL), and native UML diagrams (Architecture, ERD, Activity, Sequence, Use Case, State Machine, Class Diagram, and Deployment Topology), we have eliminated all technical ambiguity.")
    add_body_p(doc, "Every design choice—from the sub-16ms query performance of native SQLite to the 60-second autonomous SLA countdown daemon—demonstrates that ONCOP is engineered for high-concurrency public service. With the design phase complete, we proceed to Chapter 4: Core Modules and Features, where these theoretical architectures are translated into concrete functional implementations.")
    
    doc.add_page_break() # Page 37 transition

print("Chapters 1 to 3 module loaded.")
