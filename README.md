# 🏛️ ONCOP (One Nation One Complaint Portal)
### Production Full-Stack Civic Grievance Redressal & Smart Routing Platform
**Powered by Node.js, Express, SQLite (`node:sqlite`), Leaflet Maps & Official National Govt Gateways**

---

## 🏗️ Architecture & Technology Stack

| Component | Technology | Role & Functionality |
| :--- | :--- | :--- |
| **Backend Runtime** | **Node.js (v26)** & **Express.js** | High-performance RESTful API microservice, static file server, auto-routing engine, SLA countdown background worker. |
| **Database** | **SQLite (`oncop.db`)** via native `node:sqlite` | Persistent relational database storing `complaints`, `timeline`, `external_sync_logs`, and `notifications` with zero native binary build dependencies. |
| **File Storage** | **Multer Engine (`/uploads`)** | Real multipart photo uploads for citizen "Before" pictures and field officer "After" verification proof. |
| **Govt Gateways** | **Official National Portals Integration** | Bidirectional connector linking complaints to **CPGRAMS (pgportal.gov.in)**, **Swachh Bharat Urban (swachhbharatmission.gov.in)**, **Delhi Jal Board**, and **Urja Mitra (1912)**. |
| **Frontend UI** | **Vanilla HTML5 + Modern CSS + JS** | Responsive GovTech design system, bilingual support (EN/HI), dark/light theme, dual Leaflet.js interactive maps, printable receipts. |

---

## 🌐 Official Government Portals Connected

Every complaint registered on ONCOP is automatically synchronized with the relevant Government of India / State Municipal Portal and generates an official National Acknowledgment Reference:

1. **CPGRAMS (pgportal.gov.in)** - Centralized Public Grievance Redress and Monitoring System (Dept of Administrative Reforms & Public Grievances).
2. **Swachh Bharat Urban (swachhbharatmission.gov.in)** - Ministry of Housing & Urban Affairs (MoHUA) for solid waste and sanitation.
3. **Delhi Jal Board / Municipal Water Works (delhijalboard.delhi.gov.in)** - Clean drinking water pipelines, contaminated water, and trunk sewer leaks.
4. **Urja Mitra / National Power Portal (1912 / urjamitra.in)** - Ministry of Power for electrical hazards, sparking overhead wires, and streetlights.
5. **State PWD Infrastructure Gateway** - Road potholes, caved-in asphalt, and pedestrian footpaths.

---

## 📡 REST API Documentation

### Complaints
- `GET /api/complaints`: List all complaints. Supports filters: `?category=roads&status=Assigned&ward=Ward 14&escalated=true`
- `GET /api/complaints/:id`: Get full details of a grievance including timeline events, photo attachments, and official Govt portal sync credentials.
- `POST /api/complaints`: Create a new complaint. Accepts `multipart/form-data` with photo upload or JSON. Runs Smart NLP Auto-routing, calculates SLA, syncs with Govt Portal, and dispatches SMS/WhatsApp alerts.
- `PATCH /api/complaints/:id/status`: Update status (`Assigned` ➔ `In Progress` ➔ `Resolved`), attach field remarks and resolution "After" photo.
- `POST /api/complaints/:id/reopen`: Citizen re-opens an unresolved complaint. Automatically switches status to `In Progress` and alerts Zonal Supervisor.
- `POST /api/complaints/:id/rate`: Submit citizen satisfaction rating (1 to 5 stars) and feedback.

### Analytics & Reporting
- `GET /api/stats`: Live KPIs (Total complaints, resolved, pending, in progress, SLA breaches, average resolution time).
- `GET /api/export/csv`: Direct downloadable `.csv` report of all complaints.

### Notifications & Dispatch
- `GET /api/notifications`: List all simulated SMS, WhatsApp, and Escalation dispatch alerts.
- `POST /api/notifications/clear`: Clear notification history.

---

## ⚡ Background SLA Escalation Worker
The server includes an automated background cron worker running every 60 seconds:
- Automatically tracks elapsed hours against `sla_hours`.
- If a ticket breaches SLA:
  - Updates `escalation_level` to **Level 1 (SLA Breached - Auto-Escalated to Dept HOD)**.
  - Adds an automated event to the complaint's public timeline.
  - Emits a high-priority dispatch notification to the **Municipal Commissioner's Command Desk**.

---

## 🚀 Running the Application

To start the server:
```bash
npm start
```
The application will be live at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## 📂 Project Structure
```
oncop/
├── database.js          # SQLite schema, tables & seed records
├── govIntegration.js    # CPGRAMS, Swachh Bharat & Municipal API connector
├── server.js            # Express REST API, file upload & SLA worker
├── index.html           # Full-stack frontend single page app
├── styles.css           # Modern design system & responsive styling
├── app.js               # Frontend controller consuming REST APIs
├── uploads/             # Persistent directory for uploaded proof photos
├── oncop.db             # Persistent SQLite database file
├── package.json         # Node.js dependencies & scripts
└── README.md            # Comprehensive system documentation
```
