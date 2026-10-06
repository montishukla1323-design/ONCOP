/**
 * ONCOP Database Management Layer
 * Using Node.js native DatabaseSync (node:sqlite)
 * SQLite persistent file: oncop.db
 */

const { DatabaseSync } = require('node:sqlite');
const path = require('path');

const DB_PATH = process.env.DB_PATH || path.join(__dirname, 'oncop.db');
const db = new DatabaseSync(DB_PATH);

// Enable WAL mode & foreign keys for high performance
db.exec(`
  PRAGMA journal_mode = WAL;
  PRAGMA foreign_keys = ON;
  PRAGMA busy_timeout = 5000;
  PRAGMA synchronous = NORMAL;

  -- 1. Complaints Main Table
  CREATE TABLE IF NOT EXISTS complaints (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    category_name TEXT NOT NULL,
    description TEXT NOT NULL,
    citizen_name TEXT NOT NULL,
    citizen_phone TEXT NOT NULL,
    ward TEXT NOT NULL,
    landmark TEXT NOT NULL,
    urgency TEXT NOT NULL DEFAULT 'Normal',
    sla_hours INTEGER NOT NULL DEFAULT 48,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    assigned_dept TEXT NOT NULL,
    assigned_officer TEXT NOT NULL,
    officer_phone TEXT NOT NULL,
    escalation_level TEXT NOT NULL DEFAULT 'None',
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    photo_before TEXT,
    photo_after TEXT,
    rating INTEGER,
    feedback TEXT,
    gov_portal_name TEXT,
    gov_reference_no TEXT,
    gov_portal_url TEXT,
    gov_sync_status TEXT DEFAULT 'Synced'
  );

  -- 2. Complaint Progression Timeline
  CREATE TABLE IF NOT EXISTS timeline (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complaint_id TEXT NOT NULL,
    status TEXT NOT NULL,
    time TEXT NOT NULL,
    note TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(complaint_id) REFERENCES complaints(id) ON DELETE CASCADE
  );

  -- 3. Government Portal & External API Sync Logs
  CREATE TABLE IF NOT EXISTS external_sync_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complaint_id TEXT NOT NULL,
    portal_name TEXT NOT NULL,
    external_ack_id TEXT NOT NULL,
    sync_status TEXT NOT NULL,
    response_payload TEXT,
    synced_at TEXT NOT NULL
  );

  -- 4. Simulated SMS & WhatsApp Notification History
  CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel TEXT NOT NULL,
    recipient TEXT NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    sent_at TEXT NOT NULL
  );

  -- 5. Civic Users & Role-Based Authentication
  CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    department TEXT,
    designation TEXT,
    avatar TEXT
  );

  -- High-Performance Production Indexes
  CREATE INDEX IF NOT EXISTS idx_complaints_status ON complaints(status);
  CREATE INDEX IF NOT EXISTS idx_complaints_dept ON complaints(assigned_dept);
  CREATE INDEX IF NOT EXISTS idx_complaints_phone ON complaints(citizen_phone);
  CREATE INDEX IF NOT EXISTS idx_complaints_created ON complaints(created_at);
  CREATE INDEX IF NOT EXISTS idx_timeline_complaint ON timeline(complaint_id);
`);

// Seed Users for Authentication
function seedUsers() {
  const userCount = db.prepare('SELECT COUNT(*) as count FROM users').get();
  if (userCount.count > 0) return;

  console.log('Seeding authentication users (Citizens, Department Officers, Admin)...');

  const defaultUsers = [
    {
      id: "CIT-001",
      name: "Ramesh Sharma",
      email: "ramesh.citizen@gmail.com",
      phone: "9876543210",
      password: "citizen123",
      role: "citizen",
      department: "Citizen",
      designation: "Verified Citizen",
      avatar: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150"
    },
    {
      id: "OFF-PWD-01",
      name: "Er. V. K. Saxena",
      email: "pwd@oncop.gov.in",
      phone: "9412044911",
      password: "pwd123",
      role: "officer",
      department: "roads",
      designation: "Divisional Road Engineer (PWD)",
      avatar: "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=150"
    },
    {
      id: "OFF-SWM-02",
      name: "Dr. Sandeep Rawat",
      email: "sanitation@oncop.gov.in",
      phone: "9415522019",
      password: "clean123",
      role: "officer",
      department: "sanitation",
      designation: "Chief Sanitary Inspector",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150"
    },
    {
      id: "OFF-PWR-03",
      name: "Er. Amit Chhabra",
      email: "power@oncop.gov.in",
      phone: "9871133200",
      password: "power123",
      role: "officer",
      department: "electricity",
      designation: "Senior Electrical Inspector",
      avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150"
    },
    {
      id: "OFF-JAL-04",
      name: "Er. Rajesh Meena",
      email: "water@oncop.gov.in",
      phone: "9810912345",
      password: "water123",
      role: "officer",
      department: "water",
      designation: "Executive Water Engineer",
      avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150"
    },
    {
      id: "ADM-001",
      name: "Sh. Rajeshwar Singh, IAS",
      email: "admin@oncop.gov.in",
      phone: "9800011100",
      password: "admin123",
      role: "admin",
      department: "all",
      designation: "Municipal Commissioner & Nodal Head",
      avatar: "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=150"
    }
  ];

  const insertUserStmt = db.prepare(`
    INSERT INTO users (id, name, email, phone, password, role, department, designation, avatar)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  for (const u of defaultUsers) {
    insertUserStmt.run(u.id, u.name, u.email, u.phone, u.password, u.role, u.department, u.designation, u.avatar);
  }
}

seedUsers();

// Clean any old sample/demo complaints to keep the system 100% original
function cleanSampleComplaints() {
  db.exec(`
    DELETE FROM timeline;
    DELETE FROM external_sync_logs;
    DELETE FROM complaints;
    DELETE FROM notifications;
  `);
  console.log('Database cleaned: 0 sample complaints. Ready for 100% genuine citizen complaints.');
}

// cleanSampleComplaints(); // Disabled so original citizen grievances persist across server restarts

module.exports = {
  db
};

