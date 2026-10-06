# 🚀 ONCOP - Production Deployment & Operations Guide

> **One Nation One Complaint Portal (ONCOP)**  
> Full-Stack Civic Grievance Redressal Engine with AI-Driven Routing, High-Precision GPS, and Official Government Portals Integration.

---

## 📋 Pre-Deployment Checklist

- [x] Node.js **>= 22.0.0** installed (required for native `node:sqlite`).
- [x] Dependencies installed (`npm install`).
- [x] Database initialized with SQLite WAL mode and high-performance indexes.
- [x] Rate limiting and security headers enabled in `server.js`.
- [x] Environment configured (`.env`).
- [x] Verified zero sample complaints in production database.

---

## ⚡ Option 1: 1-Click Docker Deployment (Recommended)

Docker provides an isolated, production-grade container with all native SQLite dependencies, persistent volumes for citizen proof uploads, and automated health checks.

### 1. Build and Start Container
```bash
docker compose up -d --build
```

### 2. Verify Container Health
```bash
# Check running status
docker ps -f name=oncop_server

# View live application logs
docker logs -f oncop_server

# Query internal healthcheck
curl http://localhost:3000/api/health
```

### 3. Stop Container
```bash
docker compose down
```

---

## 🌐 Option 2: Cloud PaaS Deployment

### A. Deploy to **Render.com** (Free/Standard)
1. Push your repository to **GitHub** or **GitLab**.
2. Go to [Render Dashboard](https://dashboard.render.com/) and click **New + > Web Service**.
3. Connect your GitHub repository.
4. Fill in the build settings:
   - **Environment**: `Node`
   - **Node Version**: `22` (Set environment variable `NODE_VERSION=22.8.0`)
   - **Build Command**: `npm install`
   - **Start Command**: `node server.js`
5. Under **Disks**, add a Persistent Disk (e.g. Mount Path: `/app/data`, Size: 1 GB) and set Environment Variable:
   ```env
   DB_PATH=/app/data/oncop.db
   NODE_ENV=production
   ```
6. Click **Deploy Web Service**. Render provides a free SSL HTTPS domain automatically.

---

### B. Deploy to **Railway.app**
1. Sign up at [Railway.app](https://railway.app/).
2. Select **New Project > Deploy from GitHub repo**.
3. In Service Settings:
   - Add a Volume mounted at `/app` for persistent database storage.
   - Set environment variable `PORT=3000`.
4. Click **Deploy**.

---

### C. Deploy to **Fly.io**
1. Install Flyctl CLI:
   ```bash
   # Windows PowerShell
   iwr https://fly.io/install.ps1 -useb | iex
   ```
2. Launch the app:
   ```bash
   fly launch
   ```
3. Create a persistent volume for the SQLite database:
   ```bash
   fly volumes create oncop_data --size 1
   ```
4. Deploy:
   ```bash
   fly deploy
   ```

---

## 🖥️ Option 3: Traditional Linux VM / VPS (Ubuntu + PM2 + Nginx)

For self-hosting on AWS EC2, DigitalOcean Droplet, Hetzner, or a government intranet server.

### 1. Install Node.js 22 LTS
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs nginx
```

### 2. Copy Code to Server
```bash
sudo mkdir -p /var/www/oncop
sudo chown -R $USER:$USER /var/www/oncop
# Copy project files into /var/www/oncop
cd /var/www/oncop
npm install --production
```

### 3. Start with PM2 Process Manager
```bash
# Install PM2 globally
sudo npm install -g pm2

# Start ONCOP application
pm2 start server.js --name "oncop-portal" --time

# Configure auto-restart on system reboot
pm2 startup
pm2 save
```

### 4. Configure Nginx Reverse Proxy
Edit `/etc/nginx/sites-available/oncop`:
```nginx
server {
    listen 80;
    server_name your-domain.gov.in www.your-domain.gov.in;

    # Allow up to 20MB photo uploads
    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable site and test configuration:
```bash
sudo ln -s /etc/nginx/sites-available/oncop /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 5. Install Free SSL with Let's Encrypt
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.gov.in
```

---

## 🔍 Monitoring & Health Verification

| Endpoint | Method | Purpose |
| :--- | :--- | :--- |
| `/api/health` | `GET` | Health check (Uptime, SQLite DB connection status) |
| `/api/stats` | `GET` | Central KPI counters (Total, Resolved, Breached) |
| `/api/complaints` | `GET` | Grievance registry & active queue |
| `/api/notifications` | `GET` | Real-time SMS & escalation broadcast logs |

### Health Check Response Example:
```json
{
  "status": "UP",
  "uptimeSeconds": 1420,
  "timestamp": "2026-09-29T09:55:00.000Z",
  "database": "connected",
  "version": "1.0.0",
  "environment": "production"
}
```

---

## 💾 Database Backups

Because ONCOP uses SQLite in **WAL (Write-Ahead Logging)** mode, you can safely create zero-downtime hot backups anytime without stopping the server:

```bash
# Hot backup command
sqlite3 oncop.db ".backup 'backups/oncop_backup_$(date +%Y%m%d_%H%M%S).db'"
```

Add to cron for automated nightly backups:
```bash
0 2 * * * cd /var/www/oncop && sqlite3 oncop.db ".backup 'backups/oncop_$(date +\%F).db'"
```

---

## 🏛️ Government Portal Integration Gateway

ONCOP includes pre-configured adapters that automatically dispatch tickets and generate external reference numbers with:
- **CPGRAMS** (`https://pgportal.gov.in`)
- **Swachh Bharat Urban / Swachhata** (`https://swachhbharatmission.gov.in`)
- **Delhi Jal Board Grievance Portal** (`https://delhijalboard.delhi.gov.in`)
- **Urja Mitra / National Power Portal** (`https://urjamitra.in` / 1912)

All external sync attempts are audited in the `external_sync_logs` table for public transparency.
