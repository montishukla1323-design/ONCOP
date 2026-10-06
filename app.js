/**
 * ONCOP (One Nation One Complaint Portal)
 * Full-Stack Client connecting to Express REST API & SQLite Database
 */

const API_BASE = '/api';

// Department and Routing Reference Mapping
const DEPT_ROUTING_CONFIG = {
  roads: {
    name: "Public Works Dept (Roads & Bridges)",
    officer: "Er. V. K. Saxena (Divisional Road Engineer)",
    phone: "+91 94120-44911",
    defaultSla: 48,
    escalateTo: "Chief Engineer (Roads) ➔ Municipal Commissioner"
  },
  sanitation: {
    name: "Solid Waste Management Division",
    officer: "Dr. Sandeep Rawat (Chief Sanitary Inspector)",
    phone: "+91 94155-22019",
    defaultSla: 24,
    escalateTo: "Director of Sanitation ➔ Municipal Commissioner"
  },
  water: {
    name: "Jal Board (Water Supply & Drainage)",
    officer: "Er. Rajesh Meena (Executive Engineer)",
    phone: "+91 98109-12345",
    defaultSla: 36,
    escalateTo: "Superintending Engineer ➔ Jal Board Secretary"
  },
  electricity: {
    name: "Municipal Power & Lighting Board",
    officer: "Er. Amit Chhabra (Senior Electrical Inspector)",
    phone: "+91 98711-33200",
    defaultSla: 12,
    escalateTo: "Superintending Electrical Engineer ➔ Commissioner"
  },
  sewer: {
    name: "Sewerage & Underground Drainage Dept",
    officer: "Er. K. L. Gautam (Drainage Zonal Officer)",
    phone: "+91 98100-55412",
    defaultSla: 48,
    escalateTo: "Director Drainage ➔ Commissioner"
  },
  parks: {
    name: "Horticulture & Public Parks Board",
    officer: "Smt. Neha Bansal (Deputy Director Horticulture)",
    phone: "+91 99112-88711",
    defaultSla: 72,
    escalateTo: "Director Horticulture ➔ Commissioner"
  }
};

const WARD_COORDINATES = {
  "Ward 14 - Central Market": { lat: 28.6328, lng: 77.2197 },
  "Ward 08 - South Extension": { lat: 28.5684, lng: 77.2215 },
  "Ward 22 - Industrial Area Phase 2": { lat: 28.5284, lng: 77.2715 },
  "Ward 05 - Green Park & Metro": { lat: 28.5589, lng: 77.2028 },
  "Ward 31 - East Enclave Housing": { lat: 28.6180, lng: 77.2950 }
};

// Bilingual Dictionary (English & Hindi)
const I18N = {
  en: {
    govBanner: "🇮🇳 राष्ट्रीय शिकायत निवारण पोर्टल | Govt. of India / Municipal Initiative",
    slaActivePill: "24x7 Active SLA Redressal",
    emergencySos: "Civic SOS (112)",
    brandTagline: "One Nation • One Complaint • Zero Confusion",
    navReport: "Report Complaint",
    navTrack: "Live Tracking",
    navAdmin: "Admin & SLA Desk",
    navMap: "Public Heatmap",
    btnFileGrievance: "File Grievance",
    kpiTotal: "Complaints Filed",
    kpiResolved: "Resolved On-Ground",
    kpiAvgTime: "Avg. Resolution Time",
    kpiEscalated: "Active SLA Escalations",
    aiRoutingActive: "Smart AI & Ward Auto-Routing Active",
    heroTitle: "Submit Your Civic Complaint",
    heroSubtitle: "Whether it is a pothole or a garbage pile—submit your complaint with text or photo. The system will automatically route it to the right department.",
    formTitle: "New Grievance Registration",
    lblFullName: "Full Name *",
    lblMobile: "Mobile Number (SMS Updates) *",
    lblTitle: "Issue Title *",
    lblCategory: "Problem Category *",
    lblUrgency: "Severity / Urgency",
    lblWard: "Ward / Colony Zone *",
    lblLandmark: "Specific Landmark / Address *",
    lblPinLocation: "Precision GPS & Ground Geolocation *",
    btnDetectGps: "Auto-Detect My GPS",
    lblDesc: "Detailed Description *",
    lblPhoto: "Upload Photo Proof (Optional but accelerates resolution)",
    dropzoneText: "Click to select photo or drag and drop from device / camera",
    btnSubmit: "Submit Grievance & Route Instantly",
    routingDesc: "Real-time prediction of assigned municipal department, nodal officer, and strict SLA deadline based on your inputs.",
    trackerTitle: "Live Grievance Tracking Engine",
    trackerSubtitle: "Check transparent status, assigned officer contact, ground progress timeline, and download official receipt.",
    btnTrack: "Track Status"
  },
  hi: {
    govBanner: "🇮🇳 राष्ट्रीय शिकायत निवारण पोर्टल | भारत सरकार / नगर निगम उपक्रम",
    slaActivePill: "24x7 सक्रिय समयबद्ध निवारण",
    emergencySos: "नागरिक आपातकाल (112)",
    brandTagline: "एक राष्ट्र • एक शिकायत पोर्टल • शून्य असमंजस",
    navReport: "शिकायत दर्ज करें",
    navTrack: "लाइव ट्रैकिंग",
    navAdmin: "अधिकारी एवं SLA डैशबोर्ड",
    navMap: "सार्वजनिक हीटमैप",
    btnFileGrievance: "शिकायत करें",
    kpiTotal: "कुल दर्ज शिकायतें",
    kpiResolved: "जमीनी स्तर पर हल",
    kpiAvgTime: "औसत निवारण समय",
    kpiEscalated: "सक्रिय SLA उल्लंघन",
    aiRoutingActive: "स्मार्ट AI एवं वार्ड ऑटो-रूटिंग सक्रिय",
    heroTitle: "अपनी नागरिक शिकायत दर्ज करें",
    heroSubtitle: "चाहे सड़क का गड्ढा हो या कचरे का ढेर—अपनी शिकायत टेक्स्ट या फोटो के साथ डालें। सिस्टम स्वतः सही विभाग और अधिकारी को भेजेगा।",
    formTitle: "नया शिकायत पंजीकरण",
    lblFullName: "पूरा नाम *",
    lblMobile: "मोबाइल नंबर (SMS सूचना हेतु) *",
    lblTitle: "शिकायत का विषय *",
    lblCategory: "समस्या की श्रेणी *",
    lblUrgency: "प्राथमिकता / गंभीरता",
    lblWard: "वार्ड / कॉलोनी क्षेत्र *",
    lblLandmark: "नजदीकी लैंडमार्क या पता *",
    lblPinLocation: "सटीक GPS एवं भू-स्थान (सैटेलाइट द्वारा) *",
    btnDetectGps: "मेरा GPS स्थान पहचानें",
    lblDesc: "विस्तृत विवरण *",
    lblPhoto: "फोटो प्रमाण अपलोड करें (वैकल्पिक परंतु समाधान तीव्र करता है)",
    dropzoneText: "फोटो चुनने के लिए क्लिक करें या डिवाइस / कैमरे से ड्रैग करें",
    btnSubmit: "शिकायत भेजें एवं तुरंत रूट करें",
    routingDesc: "आपके विवरण के आधार पर सही नगर निगम विभाग, अधिकारी एवं SLA समय-सीमा का वास्तविक समय पूर्वानुमान।",
    trackerTitle: "लाइव शिकायत ट्रैकिंग इंजन",
    trackerSubtitle: "पारदर्शी स्थिति, अधिकारी संपर्क, कार्य प्रगति टाइमलाइन देखें और आधिकारिक रसीद प्रिंट करें।",
    btnTrack: "स्थिति देखें"
  }
};

class OncopApp {
  constructor() {
    this.complaints = [];
    this.notifications = [];
    this.currentLanguage = "en";
    this.currentUser = null;
    
    // Maps
    this.leafletMap = null;
    this.mapMarkers = [];
    this.citizenPickerMap = null;
    this.pickerMarker = null;
    this.pickedCoordinates = { lat: 28.6328, lng: 77.2197 };

    this.currentSelectedPhoto = null;
    this.uploadedFileObj = null;
    this.activeFilter = "all";
    
    this.init();
  }

  async init() {
    this.setupTheme();
    this.setupLanguage();
    this.setupAuth();
    this.setupNavTabs();
    this.setupNotifications();
    this.setupSosModal();
    this.setupCitizenLocationPicker();
    this.setupSmartRoutingListener();
    this.setupPhotoUpload();
    this.setupComplaintForm();
    this.setupTracker();
    this.setupAdminDesk();
    this.setupHeatmap();
    this.setupModals();

    // Fetch initial data from backend SQLite database
    await this.fetchComplaints();
    await this.fetchStats();
    await this.fetchNotifications();
    
    // Automatically track first complaint if available, else show clean empty state
    if (this.complaints && this.complaints.length > 0) {
      this.renderTrackerResult(this.complaints[0].id);
    } else {
      this.renderTrackerEmptyState();
    }
    this.renderRecentChips();
  }

  /* ------------------------------------------------------------------------
     User Authentication & Role Management (SSO / Demo Logins)
     ------------------------------------------------------------------------ */
  setupAuth() {
    const loginTrigger = document.getElementById("btnLoginTrigger");
    const loginModal = document.getElementById("loginModal");
    const closeBtn = document.getElementById("btnCloseLoginModal");
    const logoutBtn = document.getElementById("btnLogout");

    const tabCitizen = document.getElementById("tabLoginCitizen");
    const tabOfficer = document.getElementById("tabLoginOfficer");
    const formCitizen = document.getElementById("formCitizenAuth");
    const formOfficer = document.getElementById("formOfficerAuth");
    const demoButtons = document.querySelectorAll(".btn-demo-user");

    const openModal = () => loginModal.classList.add("open");
    const closeModal = () => loginModal.classList.remove("open");

    if (loginTrigger) loginTrigger.addEventListener("click", openModal);
    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    loginModal.addEventListener("click", (e) => {
      if (e.target === loginModal) closeModal();
    });

    if (tabCitizen && tabOfficer) {
      tabCitizen.addEventListener("click", () => {
        tabCitizen.classList.add("active");
        tabOfficer.classList.remove("active");
        formCitizen.style.display = "flex";
        formOfficer.style.display = "none";
      });

      tabOfficer.addEventListener("click", () => {
        tabOfficer.classList.add("active");
        tabCitizen.classList.remove("active");
        formOfficer.style.display = "flex";
        formCitizen.style.display = "none";
      });
    }

    if (formCitizen) {
      formCitizen.addEventListener("submit", async (e) => {
        e.preventDefault();
        const phone = document.getElementById("citizenLoginPhone").value;
        const password = document.getElementById("citizenLoginPassword").value;
        await this.performLogin({ identifier: phone, password });
        closeModal();
      });
    }

    if (formOfficer) {
      formOfficer.addEventListener("submit", async (e) => {
        e.preventDefault();
        const email = document.getElementById("officerLoginEmail").value;
        const password = document.getElementById("officerLoginPassword").value;
        await this.performLogin({ identifier: email, password });
        closeModal();
      });
    }

    demoButtons.forEach(btn => {
      btn.addEventListener("click", async () => {
        const uid = btn.dataset.uid;
        await this.performLogin({ demoUserId: uid });
        closeModal();
      });
    });

    if (logoutBtn) {
      logoutBtn.addEventListener("click", () => this.logoutUser());
    }

    // Check saved session
    const savedUser = localStorage.getItem("oncop_auth_user");
    if (savedUser) {
      try {
        this.loginUser(JSON.parse(savedUser), false);
      } catch (e) {}
    }
  }

  async performLogin(credentials) {
    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials)
      });
      const json = await res.json();
      if (res.ok && json.success) {
        this.loginUser(json.user, true);
      } else {
        alert(json.message || "Authentication failed.");
      }
    } catch (e) {
      console.error("Login request failed:", e);
      alert("Failed to communicate with authentication server.");
    }
  }

  loginUser(user, notify = true) {
    this.currentUser = user;
    localStorage.setItem("oncop_auth_user", JSON.stringify(user));

    const trigger = document.getElementById("btnLoginTrigger");
    const badge = document.getElementById("userProfileBadge");
    const avatar = document.getElementById("headerUserAvatar");
    const nameEl = document.getElementById("headerUserName");
    const roleEl = document.getElementById("headerUserRole");

    if (trigger) trigger.style.display = "none";
    if (badge) badge.style.display = "flex";
    if (avatar && user.avatar) avatar.src = user.avatar;
    if (nameEl) nameEl.textContent = user.name;
    if (roleEl) roleEl.textContent = user.role.toUpperCase();

    // Auto-fill Citizen Form if Citizen
    if (user.role === "citizen") {
      const nameInput = document.getElementById("citizenName");
      const phoneInput = document.getElementById("citizenPhone");
      if (nameInput) nameInput.value = user.name;
      if (phoneInput) phoneInput.value = user.phone;
    }

    // If Officer or Admin, prioritize department queue
    if (user.role === "officer" && user.department) {
      this.switchTab("admin");
    }

    if (notify) {
      this.showToast(`👋 Welcome, ${user.name}! Authenticated as ${user.designation || user.role}.`);
    }
  }

  logoutUser() {
    this.currentUser = null;
    localStorage.removeItem("oncop_auth_user");

    const trigger = document.getElementById("btnLoginTrigger");
    const badge = document.getElementById("userProfileBadge");
    if (trigger) trigger.style.display = "inline-flex";
    if (badge) badge.style.display = "none";

    this.showToast("Logged out successfully.");
    this.switchTab("citizen");
  }

  /* ------------------------------------------------------------------------
     REST API Data Synchronizers
     ------------------------------------------------------------------------ */
  async fetchComplaints() {
    try {
      const res = await fetch(`${API_BASE}/complaints`);
      if (res.ok) {
        const json = await res.json();
        this.complaints = json.data || [];
        this.renderAdminTable();
        this.renderMapMarkers();
        this.updateKpiCounters();
      }
    } catch (err) {
      console.warn("Backend API offline, using local cache:", err);
    }
  }

  async fetchStats() {
    try {
      const res = await fetch(`${API_BASE}/stats`);
      if (res.ok) {
        const json = await res.json();
        const data = json.data || json;
        const elTotal = document.getElementById("kpiTotal");
        const elResolved = document.getElementById("kpiResolved");
        const elAvgTime = document.getElementById("kpiAvgTime");
        const elEscalated = document.getElementById("kpiEscalated");
        const elBadge = document.getElementById("adminAlertBadge");

        if (elTotal) elTotal.textContent = (data.total ?? 0).toString();
        if (elResolved) elResolved.textContent = (data.resolved ?? 0).toString();
        if (elAvgTime) elAvgTime.textContent = (data.avgResolutionHours ?? 0) > 0 ? `${data.avgResolutionHours} hrs` : "0 hrs";
        if (elEscalated) elEscalated.textContent = (data.escalated ?? 0).toString();
        if (elBadge) elBadge.textContent = (data.escalated ?? 0).toString();
      }
    } catch (e) {}
  }

  async fetchNotifications() {
    try {
      const res = await fetch(`${API_BASE}/notifications`);
      if (res.ok) {
        const json = await res.json();
        this.notifications = json.data || [];
        this.renderNotificationList();
        this.updateNotifBadge();
      }
    } catch (e) {}
  }

  /* ------------------------------------------------------------------------
     Theme Management (Dark / Light)
     ------------------------------------------------------------------------ */
  setupTheme() {
    const themeBtn = document.getElementById("themeToggle");
    const savedTheme = localStorage.getItem("oncop_theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);
    this.updateThemeIcon(savedTheme);

    themeBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("oncop_theme", next);
      this.updateThemeIcon(next);
      
      if (this.leafletMap) setTimeout(() => this.leafletMap.invalidateSize(), 150);
      if (this.citizenPickerMap) setTimeout(() => this.citizenPickerMap.invalidateSize(), 150);
    });
  }

  updateThemeIcon(theme) {
    const icon = document.querySelector("#themeToggle i");
    if (icon) {
      icon.className = theme === "dark" ? "fa-solid fa-sun" : "fa-solid fa-moon";
    }
  }

  /* ------------------------------------------------------------------------
     Bilingual Language Switcher (EN / HI)
     ------------------------------------------------------------------------ */
  setupLanguage() {
    const langBtn = document.getElementById("btnLangToggle");
    const langLabel = document.getElementById("langLabel");
    this.currentLanguage = localStorage.getItem("oncop_lang") || "en";
    
    if (langLabel) {
      langLabel.textContent = this.currentLanguage === "en" ? "हिन्दी" : "English";
    }
    this.applyTranslations();

    if (langBtn) {
      langBtn.addEventListener("click", () => {
        this.currentLanguage = this.currentLanguage === "en" ? "hi" : "en";
        localStorage.setItem("oncop_lang", this.currentLanguage);
        if (langLabel) {
          langLabel.textContent = this.currentLanguage === "en" ? "हिन्दी" : "English";
        }
        this.applyTranslations();
        this.showToast(this.currentLanguage === "hi" ? "भाषा बदलकर हिन्दी कर दी गई है।" : "Language switched to English.");
      });
    }
  }

  applyTranslations() {
    const dict = I18N[this.currentLanguage] || I18N.en;
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const key = el.getAttribute("data-i18n");
      if (dict[key]) {
        el.textContent = dict[key];
      }
    });
  }

  /* ------------------------------------------------------------------------
     Navigation Tabs
     ------------------------------------------------------------------------ */
  setupNavTabs() {
    const navItems = document.querySelectorAll(".nav-item");
    const quickReportBtn = document.getElementById("btnQuickReport");
    const brandNav = document.getElementById("brandNav");

    navItems.forEach(btn => {
      btn.addEventListener("click", () => {
        const target = btn.dataset.tab;
        this.switchTab(target);
      });
    });

    if (quickReportBtn) {
      quickReportBtn.addEventListener("click", () => {
        this.switchTab("citizen");
        const titleInput = document.getElementById("complaintTitle");
        if (titleInput) titleInput.focus();
      });
    }

    if (brandNav) {
      brandNav.addEventListener("click", () => this.switchTab("citizen"));
    }
  }

  switchTab(tabName) {
    document.querySelectorAll(".nav-item").forEach(item => {
      item.classList.toggle("active", item.dataset.tab === tabName);
    });

    document.querySelectorAll(".tab-pane").forEach(pane => {
      pane.classList.remove("active");
    });

    const activePane = document.getElementById(`tab${tabName.charAt(0).toUpperCase() + tabName.slice(1)}`);
    if (activePane) {
      activePane.classList.add("active");
    }

    if (tabName === "citizen" && this.citizenPickerMap) {
      setTimeout(() => this.citizenPickerMap.invalidateSize(), 200);
    } else if (tabName === "admin") {
      this.fetchComplaints();
    } else if (tabName === "heatmap") {
      setTimeout(() => {
        if (this.leafletMap) {
          this.leafletMap.invalidateSize();
          this.renderMapMarkers();
        }
      }, 200);
    }
  }

  /* ------------------------------------------------------------------------
     Live SMS & WhatsApp Notification Drawer
     ------------------------------------------------------------------------ */
  setupNotifications() {
    const btnTray = document.getElementById("btnNotificationTray");
    const dropdown = document.getElementById("notifDropdown");
    const clearBtn = document.getElementById("btnClearNotifs");

    btnTray.addEventListener("click", (e) => {
      e.stopPropagation();
      dropdown.classList.toggle("open");
    });

    document.addEventListener("click", (e) => {
      if (!dropdown.contains(e.target) && !btnTray.contains(e.target)) {
        dropdown.classList.remove("open");
      }
    });

    clearBtn.addEventListener("click", async () => {
      try {
        await fetch(`${API_BASE}/notifications/clear`, { method: "POST" });
        this.notifications = [];
        this.renderNotificationList();
        this.updateNotifBadge();
      } catch (e) {}
    });
  }

  renderNotificationList() {
    const list = document.getElementById("notifList");
    if (!list) return;

    if (this.notifications.length === 0) {
      list.innerHTML = `
        <div style="padding: 2rem 1rem; text-align: center; color: var(--text-muted); font-size: 0.82rem;">
          <i class="fa-solid fa-bell-slash" style="font-size: 1.5rem; margin-bottom: 0.5rem;"></i>
          <p>No new SMS or dispatch alerts</p>
        </div>
      `;
      return;
    }

    list.innerHTML = this.notifications.map(n => {
      let channelTagClass = "channel-sms";
      let channelLabel = "SMS";
      if (n.channel === "whatsapp") { channelTagClass = "channel-whatsapp"; channelLabel = "WhatsApp"; }
      else if (n.channel === "alert") { channelTagClass = "channel-alert"; channelLabel = "Escalation"; }

      const timeText = n.sent_at ? new Date(n.sent_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'Recent';

      return `
        <div class="notif-item">
          <div class="notif-item-top">
            <span class="notif-channel ${channelTagClass}">${channelLabel}</span>
            <span class="notif-time">${timeText}</span>
          </div>
          <strong style="color: var(--text-main);">${n.title}</strong>
          <div class="notif-body">${n.body}</div>
        </div>
      `;
    }).join("");
  }

  updateNotifBadge() {
    const badge = document.getElementById("notifBadge");
    if (badge) {
      badge.textContent = this.notifications.length;
      badge.style.display = this.notifications.length > 0 ? "flex" : "none";
    }
  }

  /* ------------------------------------------------------------------------
     Emergency Civic SOS Contacts Modal
     ------------------------------------------------------------------------ */
  setupSosModal() {
    const sosBtn = document.getElementById("btnSosModal");
    const modal = document.getElementById("sosModal");
    const closeBtn = document.getElementById("btnCloseSosModal");
    const dismissBtn = document.getElementById("btnDismissSos");

    const open = () => modal.classList.add("open");
    const close = () => modal.classList.remove("open");

    if (sosBtn) sosBtn.addEventListener("click", open);
    if (closeBtn) closeBtn.addEventListener("click", close);
    if (dismissBtn) dismissBtn.addEventListener("click", close);
    
    modal.addEventListener("click", (e) => {
      if (e.target === modal) close();
    });
  }

  /* ------------------------------------------------------------------------
     Interactive High-Precision Citizen Location Picker & GPS Engine
     ------------------------------------------------------------------------ */
  setupCitizenLocationPicker() {
    const mapEl = document.getElementById("citizenPickerMap");
    if (!mapEl) return;

    // Custom High-Precision SVG Target Pin
    const customPinIcon = L.divIcon({
      className: "custom-gps-pin",
      html: `
        <div style="position: relative; width: 34px; height: 34px; transform: translate(-50%, -100%);">
          <svg width="34" height="34" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 3px 6px rgba(0,0,0,0.35));">
            <path d="M18 2C11.3726 2 6 7.37258 6 14C6 22.5 18 34 18 34C18 34 30 22.5 30 14C30 7.37258 24.6274 2 18 2Z" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
            <circle cx="18" cy="14" r="5" fill="#FFFFFF"/>
            <circle cx="18" cy="14" r="2.5" fill="#2563EB"/>
          </svg>
        </div>
      `,
      iconSize: [34, 34],
      iconAnchor: [17, 34],
      popupAnchor: [0, -32]
    });

    this.citizenPickerMap = L.map("citizenPickerMap", {
      zoomControl: true,
      attributionControl: false
    }).setView([28.632845, 77.219712], 15);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19
    }).addTo(this.citizenPickerMap);

    this.pickerMarker = L.marker([28.632845, 77.219712], {
      draggable: true,
      icon: customPinIcon
    }).addTo(this.citizenPickerMap);

    this.pickerAccuracyCircle = null;

    // Initial display
    this.updatePickerCoords(28.632845, 77.219712, null, "manual");

    // Draggable pin precision event
    this.pickerMarker.on("dragend", async (e) => {
      const position = e.target.getLatLng();
      this.updatePickerCoords(position.lat, position.lng, null, "manual");
      if (this.pickerAccuracyCircle) {
        this.pickerAccuracyCircle.setLatLng(position);
      }
      this.autoSelectNearestWard(position.lat, position.lng);
      await this.reverseGeocode(position.lat, position.lng);
    });

    // Map click direct pinning
    this.citizenPickerMap.on("click", async (e) => {
      this.pickerMarker.setLatLng(e.latlng);
      this.updatePickerCoords(e.latlng.lat, e.latlng.lng, null, "manual");
      if (this.pickerAccuracyCircle) {
        this.pickerAccuracyCircle.setLatLng(e.latlng);
      }
      this.autoSelectNearestWard(e.latlng.lat, e.latlng.lng);
      await this.reverseGeocode(e.latlng.lat, e.latlng.lng);
    });

    // Ward select listener
    const wardSelect = document.getElementById("complaintWard");
    wardSelect.addEventListener("change", () => {
      const wardName = wardSelect.value;
      const coords = WARD_COORDINATES[wardName] || { lat: 28.632845, lng: 77.219712 };
      this.pickerMarker.setLatLng([coords.lat, coords.lng]);
      this.citizenPickerMap.setView([coords.lat, coords.lng], 15);
      this.updatePickerCoords(coords.lat, coords.lng, null, "ward");
      if (this.pickerAccuracyCircle) {
        this.pickerAccuracyCircle.setLatLng([coords.lat, coords.lng]);
      }
      this.reverseGeocode(coords.lat, coords.lng);
    });

    // GPS Auto-detect button
    const btnDetect = document.getElementById("btnAutoDetectGps");
    if (btnDetect) {
      btnDetect.addEventListener("click", () => this.acquireHighPrecisionGps(false));
    }

    // Recalibrate button
    const btnRecalibrate = document.getElementById("btnRecalibrateGps");
    if (btnRecalibrate) {
      btnRecalibrate.addEventListener("click", () => this.acquireHighPrecisionGps(true));
    }

    // Apply reverse-geocoded address to Landmark input
    const btnApplyAddr = document.getElementById("btnApplyAddressToLandmark");
    if (btnApplyAddr) {
      btnApplyAddr.addEventListener("click", () => {
        const textEl = document.getElementById("geoDetectedAddressText");
        const landmarkInput = document.getElementById("complaintLandmark");
        if (textEl && landmarkInput) {
          landmarkInput.value = textEl.textContent;
          this.showToast("📍 Exact physical address copied to Landmark field!");
        }
      });
    }

    // Integrated Address & Place Search
    this.setupAddressSearch();
  }

  /* ------------------------------------------------------------------------
     Hardware High-Precision Geolocation (Satellite / GPS / WiFi)
     ------------------------------------------------------------------------ */
  acquireHighPrecisionGps(isRecalibrate = false) {
    const btnDetect = document.getElementById("btnAutoDetectGps");
    const btnRecalibrate = document.getElementById("btnRecalibrateGps");
    const accuracyText = document.getElementById("accuracyText");

    if (!navigator.geolocation) {
      this.showToast("⚠️ Geolocation API not supported by browser. Using network location.");
      this.fallbackIpLocation();
      return;
    }

    btnDetect.disabled = true;
    btnDetect.innerHTML = `<i class="fa-solid fa-satellite-dish fa-spin"></i> Locking GPS...`;

    if (accuracyText) {
      accuracyText.textContent = "Acquiring high-precision satellite signals...";
    }

    const geoOptions = {
      enableHighAccuracy: true, // Force GPS hardware / precise trilateration
      timeout: 15000,           // 15 seconds
      maximumAge: 0             // Strictly fresh reading, no cached coords
    };

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        btnDetect.disabled = false;
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        const accuracy = position.coords.accuracy || 6; // Accuracy in meters

        // Center map directly on user's exact pinpoint
        this.citizenPickerMap.setView([lat, lng], 17);
        this.pickerMarker.setLatLng([lat, lng]);

        // Draw / update accuracy circle
        if (this.pickerAccuracyCircle) {
          this.pickerAccuracyCircle.setLatLng([lat, lng]);
          this.pickerAccuracyCircle.setRadius(accuracy);
        } else {
          this.pickerAccuracyCircle = L.circle([lat, lng], {
            radius: accuracy,
            color: "#2563eb",
            fillColor: "#3b82f6",
            fillOpacity: 0.15,
            weight: 1.5
          }).addTo(this.citizenPickerMap);
        }

        this.updatePickerCoords(lat, lng, accuracy, "gps");
        this.autoSelectNearestWard(lat, lng);
        await this.reverseGeocode(lat, lng);

        btnDetect.innerHTML = `<i class="fa-solid fa-circle-check"></i> GPS Locked!`;
        if (btnRecalibrate) btnRecalibrate.style.display = "inline-flex";

        const roundedMeters = Math.round(accuracy);
        this.showToast(`🛰️ High-Precision GPS Lock: ±${roundedMeters}m accuracy (${lat.toFixed(5)}°, ${lng.toFixed(5)}°)`);

        setTimeout(() => {
          btnDetect.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> ${I18N[this.currentLanguage].btnDetectGps}`;
        }, 3000);
      },
      (error) => {
        btnDetect.disabled = false;
        btnDetect.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> ${I18N[this.currentLanguage].btnDetectGps}`;

        let warnMsg = "Could not acquire satellite GPS.";
        if (error.code === 1) {
          warnMsg = "GPS permission was denied in your browser. Using network approximate location.";
        } else if (error.code === 2) {
          warnMsg = "GPS position unavailable indoors. Using network location.";
        } else if (error.code === 3) {
          warnMsg = "GPS satellite request timed out.";
        }

        this.showToast(`⚠️ ${warnMsg}`);
        this.fallbackIpLocation();
      },
      geoOptions
    );
  }

  /* ------------------------------------------------------------------------
     Graceful Network IP Geolocation Fallback
     ------------------------------------------------------------------------ */
  async fallbackIpLocation() {
    try {
      const res = await fetch("https://ipapi.co/json/");
      if (res.ok) {
        const data = await res.json();
        if (data.latitude && data.longitude) {
          const lat = data.latitude;
          const lng = data.longitude;
          this.citizenPickerMap.setView([lat, lng], 15);
          this.pickerMarker.setLatLng([lat, lng]);
          this.updatePickerCoords(lat, lng, 300, "ip");
          this.autoSelectNearestWard(lat, lng);
          await this.reverseGeocode(lat, lng);
          this.showToast(`🌐 Approximate Network Location (${data.city || 'Delhi'}): Drag pin on map for exact spot.`);
        }
      }
    } catch (e) {
      console.warn("IP geolocation fallback failed:", e);
    }
  }

  /* ------------------------------------------------------------------------
     Update Coordinates Readout with 6-Decimal Precision & Accuracy Badge
     ------------------------------------------------------------------------ */
  updatePickerCoords(lat, lng, accuracy = null, source = "manual") {
    this.pickedCoordinates = { lat, lng };

    const coordsText = document.getElementById("pickedCoordsText");
    const accuracyBadge = document.getElementById("coordsAccuracyBadge");
    const accuracyText = document.getElementById("accuracyText");

    if (coordsText) {
      const latDir = lat >= 0 ? "N" : "S";
      const lngDir = lng >= 0 ? "E" : "W";
      coordsText.textContent = `${Math.abs(lat).toFixed(6)}° ${latDir}, ${Math.abs(lng).toFixed(6)}° ${lngDir}`;
    }

    if (accuracyBadge && accuracyText) {
      accuracyBadge.className = "coords-accuracy";
      if (accuracy !== null && accuracy <= 15) {
        accuracyBadge.classList.add("accuracy-high");
        accuracyText.innerHTML = `<strong>🟢 Sub-meter GPS Lock (±${Math.round(accuracy)}m)</strong>`;
      } else if (accuracy !== null && accuracy <= 50) {
        accuracyBadge.classList.add("accuracy-high");
        accuracyText.innerHTML = `<span>🟢 Good GPS Fix (±${Math.round(accuracy)}m)</span>`;
      } else if (source === "gps") {
        accuracyBadge.classList.add("accuracy-approx");
        accuracyText.innerHTML = `<span>🟡 GPS Fix (±${Math.round(accuracy || 25)}m) - Fine-tune pin</span>`;
      } else if (source === "ip") {
        accuracyBadge.classList.add("accuracy-approx");
        accuracyText.innerHTML = `<span>🌐 Network Approx - Drag pin to exact pothole</span>`;
      } else {
        accuracyText.innerHTML = `<span><i class="fa-solid fa-location-pin"></i> Pin Confirmed (Exact coordinates)</span>`;
      }
    }
  }

  /* ------------------------------------------------------------------------
     Reverse Geocoding: Coordinate -> Physical Street & Landmark Address
     ------------------------------------------------------------------------ */
  async reverseGeocode(lat, lng) {
    try {
      const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}&zoom=18&addressdetails=1`, {
        headers: { 'Accept': 'application/json' }
      });
      if (res.ok) {
        const data = await res.json();
        if (data && data.address) {
          const a = data.address;
          const road = a.road || a.street || a.pedestrian || a.suburb || "";
          const locality = a.neighbourhood || a.suburb || a.residential || a.commercial || a.city_district || "";
          const city = a.city || a.town || a.state_district || "New Delhi";
          const postcode = a.postcode ? ` - ${a.postcode}` : "";

          const formattedParts = [road, locality, city + postcode].filter(p => p && p.trim().length > 0);
          const fullAddress = formattedParts.length > 0 ? formattedParts.join(", ") : (data.display_name.split(",").slice(0, 3).join(","));

          const card = document.getElementById("geoDetectedAddressCard");
          const textEl = document.getElementById("geoDetectedAddressText");
          const landmarkInput = document.getElementById("complaintLandmark");

          if (card && textEl) {
            textEl.textContent = fullAddress;
            card.style.display = "flex";
          }

          // Automatically suggest into landmark field if user hasn't typed anything yet
          if (landmarkInput && !landmarkInput.value.trim()) {
            landmarkInput.value = fullAddress;
          }

          return fullAddress;
        }
      }
    } catch (e) {
      console.warn("Reverse geocode failed:", e);
    }
    return null;
  }

  /* ------------------------------------------------------------------------
     Auto-Select Nearest Municipal Ward from Exact Coordinates
     ------------------------------------------------------------------------ */
  autoSelectNearestWard(lat, lng) {
    const wardSelect = document.getElementById("complaintWard");
    if (!wardSelect) return;

    let nearestWard = null;
    let minDistance = Infinity;

    for (const [wardName, coords] of Object.entries(WARD_COORDINATES)) {
      const dLat = (lat - coords.lat) * 111;
      const dLng = (lng - coords.lng) * 111 * Math.cos(lat * Math.PI / 180);
      const dist = Math.sqrt(dLat * dLat + dLng * dLng);
      if (dist < minDistance) {
        minDistance = dist;
        nearestWard = wardName;
      }
    }

    if (nearestWard && wardSelect.value !== nearestWard) {
      wardSelect.value = nearestWard;
    }
  }

  /* ------------------------------------------------------------------------
     Place & Address Live Search (Nominatim Forward Geocoding)
     ------------------------------------------------------------------------ */
  setupAddressSearch() {
    const input = document.getElementById("geoSearchInput");
    const clearBtn = document.getElementById("btnGeoSearchClear");
    const submitBtn = document.getElementById("btnGeoSearchSubmit");
    const dropdown = document.getElementById("geoSearchResults");

    if (!input || !dropdown) return;

    let debounceTimer = null;

    const performSearch = async (query) => {
      if (!query || query.length < 3) {
        dropdown.style.display = "none";
        return;
      }

      try {
        if (submitBtn) submitBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i>`;
        const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&countrycodes=in&limit=5`);
        if (submitBtn) submitBtn.textContent = "Find";

        if (res.ok) {
          const results = await res.json();
          if (results && results.length > 0) {
            dropdown.innerHTML = results.map(item => `
              <div class="geo-search-item" data-lat="${item.lat}" data-lng="${item.lon}" data-name="${item.display_name.replace(/"/g, '&quot;')}">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                  <strong>${item.display_name.split(",")[0]}</strong>
                  <div style="font-size: 0.72rem; color: var(--text-muted);">${item.display_name.split(",").slice(1, 4).join(", ")}</div>
                </div>
              </div>
            `).join("");
            dropdown.style.display = "block";

            dropdown.querySelectorAll(".geo-search-item").forEach(el => {
              el.addEventListener("click", async () => {
                const lat = parseFloat(el.dataset.lat);
                const lng = parseFloat(el.dataset.lng);
                const name = el.dataset.name;

                this.citizenPickerMap.setView([lat, lng], 17);
                this.pickerMarker.setLatLng([lat, lng]);
                this.updatePickerCoords(lat, lng, 10, "search");
                this.autoSelectNearestWard(lat, lng);
                await this.reverseGeocode(lat, lng);

                input.value = name.split(",")[0];
                if (clearBtn) clearBtn.style.display = "inline-block";
                dropdown.style.display = "none";
              });
            });
          } else {
            dropdown.innerHTML = `<div style="padding: 0.75rem; text-align: center; color: var(--text-muted); font-size: 0.8rem;">No locations found for "${query}". Try adding city name.</div>`;
            dropdown.style.display = "block";
          }
        }
      } catch (e) {
        if (submitBtn) submitBtn.textContent = "Find";
      }
    };

    input.addEventListener("input", (e) => {
      const val = e.target.value.trim();
      if (clearBtn) clearBtn.style.display = val ? "inline-block" : "none";
      clearTimeout(debounceTimer);
      if (val.length >= 3) {
        debounceTimer = setTimeout(() => performSearch(val), 400);
      } else {
        dropdown.style.display = "none";
      }
    });

    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        clearTimeout(debounceTimer);
        performSearch(input.value.trim());
      }
    });

    if (submitBtn) {
      submitBtn.addEventListener("click", () => performSearch(input.value.trim()));
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        input.value = "";
        clearBtn.style.display = "none";
        dropdown.style.display = "none";
      });
    }

    document.addEventListener("click", (e) => {
      if (!dropdown.contains(e.target) && e.target !== input && e.target !== submitBtn) {
        dropdown.style.display = "none";
      }
    });
  }

  /* ------------------------------------------------------------------------
     Smart Routing Engine & Auto-Classification
     ------------------------------------------------------------------------ */
  setupSmartRoutingListener() {
    const titleInput = document.getElementById("complaintTitle");
    const descInput = document.getElementById("complaintDescription");
    const categorySelect = document.getElementById("complaintCategory");
    const urgencySelect = document.getElementById("urgencyLevel");

    const updateRouting = () => {
      const text = `${titleInput.value} ${descInput.value}`.toLowerCase();
      
      let detectedCategory = categorySelect.value;
      if (text.includes("pothole") || text.includes("gaddha") || text.includes("road") || text.includes("sadak") || text.includes("asphalt")) {
        detectedCategory = "roads";
      } else if (text.includes("kachra") || text.includes("garbage") || text.includes("trash") || text.includes("dump") || text.includes("waste")) {
        detectedCategory = "sanitation";
      } else if (text.includes("wire") || text.includes("taar") || text.includes("light") || text.includes("bijli") || text.includes("spark") || text.includes("shock")) {
        detectedCategory = "electricity";
      } else if (text.includes("paani") || text.includes("water") || text.includes("leak") || text.includes("pipeline") || text.includes("jal")) {
        detectedCategory = "water";
      } else if (text.includes("sewer") || text.includes("gutter") || text.includes("drain") || text.includes("naali") || text.includes("overflow")) {
        detectedCategory = "sewer";
      } else if (text.includes("tree") || text.includes("ped") || text.includes("park") || text.includes("garden")) {
        detectedCategory = "parks";
      }

      if (detectedCategory && categorySelect.value !== detectedCategory) {
        categorySelect.value = detectedCategory;
      }

      const activeCat = categorySelect.value || "roads";
      const config = DEPT_ROUTING_CONFIG[activeCat] || DEPT_ROUTING_CONFIG.roads;

      let slaHours = config.defaultSla;
      if (urgencySelect.value === "Critical") {
        slaHours = Math.min(12, Math.round(slaHours / 2));
      } else if (urgencySelect.value === "High") {
        slaHours = Math.round(slaHours * 0.75);
      }

      document.getElementById("previewDept").textContent = config.name;
      document.getElementById("previewOfficer").textContent = config.officer;
      document.getElementById("previewSla").textContent = `${slaHours} Hours Guaranteed`;
      document.getElementById("previewEscalation").textContent = config.escalateTo;
    };

    titleInput.addEventListener("input", updateRouting);
    descInput.addEventListener("input", updateRouting);
    categorySelect.addEventListener("change", updateRouting);
    urgencySelect.addEventListener("change", updateRouting);

    updateRouting();
  }

  /* ------------------------------------------------------------------------
     Photo Upload / Preset Selection
     ------------------------------------------------------------------------ */
  setupPhotoUpload() {
    const dropzone = document.getElementById("uploadDropzone");
    const fileInput = document.getElementById("photoFileInput");
    const previewContainer = document.getElementById("photoPreviewContainer");
    const previewImg = document.getElementById("photoPreviewImg");
    const removeBtn = document.getElementById("btnRemovePhoto");
    const sampleButtons = document.querySelectorAll(".btn-sample");

    dropzone.addEventListener("click", () => fileInput.click());

    dropzone.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropzone.style.borderColor = "var(--primary)";
    });
    dropzone.addEventListener("dragleave", () => {
      dropzone.style.borderColor = "";
    });
    dropzone.addEventListener("drop", (e) => {
      e.preventDefault();
      dropzone.style.borderColor = "";
      if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) {
        const file = e.dataTransfer.files[0];
        this.uploadedFileObj = file;
        const reader = new FileReader();
        reader.onload = (event) => {
          previewImg.src = event.target.result;
          previewContainer.style.display = "block";
          dropzone.style.display = "none";
        };
        reader.readAsDataURL(file);
      }
    });

    fileInput.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (file) {
        this.uploadedFileObj = file;
        const reader = new FileReader();
        reader.onload = (event) => {
          previewImg.src = event.target.result;
          previewContainer.style.display = "block";
          dropzone.style.display = "none";
        };
        reader.readAsDataURL(file);
      }
    });

    sampleButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const imgUrl = btn.dataset.img;
        this.currentSelectedPhoto = imgUrl;
        this.uploadedFileObj = null;
        previewImg.src = imgUrl;
        previewContainer.style.display = "block";
        dropzone.style.display = "none";
      });
    });

    removeBtn.addEventListener("click", () => {
      this.currentSelectedPhoto = null;
      this.uploadedFileObj = null;
      previewContainer.style.display = "none";
      dropzone.style.display = "block";
      fileInput.value = "";
    });
  }

  /* ------------------------------------------------------------------------
     Complaint Form Submission (Real FormData POST to Backend API)
     ------------------------------------------------------------------------ */
  setupComplaintForm() {
    const form = document.getElementById("grievanceForm");
    
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const citizenName = document.getElementById("citizenName").value.trim();
      const citizenPhone = document.getElementById("citizenPhone").value.trim();
      const title = document.getElementById("complaintTitle").value.trim();
      const category = document.getElementById("complaintCategory").value;
      const urgency = document.getElementById("urgencyLevel").value;
      const ward = document.getElementById("complaintWard").value;
      const landmark = document.getElementById("complaintLandmark").value.trim();
      const description = document.getElementById("complaintDescription").value.trim();

      const submitBtn = document.getElementById("btnSubmitComplaint");
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Processing & Syncing with Govt Gateway...`;

      try {
        const formData = new FormData();
        formData.append("citizenName", citizenName);
        formData.append("citizenPhone", citizenPhone);
        formData.append("title", title);
        formData.append("category", category);
        formData.append("urgency", urgency);
        formData.append("ward", ward);
        formData.append("landmark", landmark);
        formData.append("description", description);
        formData.append("lat", this.pickedCoordinates.lat);
        formData.append("lng", this.pickedCoordinates.lng);

        if (this.uploadedFileObj) {
          formData.append("photo", this.uploadedFileObj);
        } else if (this.currentSelectedPhoto) {
          formData.append("photoUrl", this.currentSelectedPhoto);
        }

        const res = await fetch(`${API_BASE}/complaints`, {
          method: "POST",
          body: formData
        });

        const json = await res.json();
        if (res.ok && json.success) {
          const newComplaint = json.data;

          // Re-fetch all data to synchronize
          await this.fetchComplaints();
          await this.fetchStats();
          await this.fetchNotifications();

          // Reset form
          form.reset();
          document.getElementById("btnRemovePhoto").click();

          this.showToast(`✅ Complaint ${newComplaint.id} logged! Synced with ${newComplaint.govPortalName}.`);

          // Switch to Tracker tab to display result
          this.switchTab("tracker");
          const trackInput = document.getElementById("trackInput");
          trackInput.value = newComplaint.id;
          this.renderTrackerResult(newComplaint.id);
        } else {
          alert(`Error filing complaint: ${json.message || "Server error"}`);
        }
      } catch (err) {
        console.error("Submission failed:", err);
        alert("Failed to reach server. Please check backend connection.");
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = `<i class="fa-solid fa-paper-plane"></i> ${I18N[this.currentLanguage].btnSubmit}`;
      }
    });
  }

  /* ------------------------------------------------------------------------
     Live Complaint Tracker with Printable Receipt & Govt Gateway Badge
     ------------------------------------------------------------------------ */
  setupTracker() {
    const trackInput = document.getElementById("trackInput");
    const trackBtn = document.getElementById("btnTrackComplaint");
    const demoChips = document.querySelectorAll(".demo-chip");

    trackBtn.addEventListener("click", () => {
      const query = trackInput.value.trim();
      if (query) this.renderTrackerResult(query);
    });

    trackInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        const query = trackInput.value.trim();
        if (query) this.renderTrackerResult(query);
      }
    });

    demoChips.forEach(chip => {
      chip.addEventListener("click", () => {
        const id = chip.dataset.id;
        trackInput.value = id;
        this.renderTrackerResult(id);
      });
    });
  }

  renderTrackerEmptyState() {
    const container = document.getElementById("trackerResultArea");
    if (!container) return;
    container.innerHTML = `
      <div class="glass-panel" style="padding: 3.5rem 2rem; text-align: center;">
        <i class="fa-solid fa-compass" style="font-size: 2.8rem; color: var(--primary); margin-bottom: 1rem;"></i>
        <h3 style="font-size: 1.35rem; font-weight: 800;">Real-Time Civic Grievance Tracker</h3>
        <p style="color: var(--text-muted); max-width: 500px; margin: 0.6rem auto 1.5rem; font-size: 0.95rem;">
          Enter your unique Tracking ID above to view live 4-stage ground progress, field officer remarks, and official Government Portal sync details.
        </p>
        <button class="btn-primary" onclick="app.switchTab('citizen')">
          <i class="fa-solid fa-plus"></i> File a New Grievance
        </button>
      </div>
    `;
  }

  renderRecentChips() {
    const container = document.getElementById("citizenDemoChips");
    if (!container) return;

    if (!this.complaints || this.complaints.length === 0) {
      container.innerHTML = `
        <div style="font-size: 0.82rem; color: var(--text-muted); padding: 0.5rem 0;">
          <i class="fa-solid fa-info-circle"></i> No complaints registered yet. File a complaint using the form to track it live here.
        </div>
      `;
      return;
    }

    container.innerHTML = this.complaints.slice(0, 5).map(c => {
      let statusClass = "status-amber";
      if (c.status === "Resolved") statusClass = "status-success";
      else if (c.isBreached || (c.escalationLevel && c.escalationLevel.includes("Escalated"))) statusClass = "status-danger";

      return `
        <button class="demo-chip" data-id="${c.id}" onclick="app.quickTrackFromAdmin('${c.id}')">
          <span>${c.id} (${c.title.length > 25 ? c.title.slice(0, 25) + '...' : c.title})</span>
          <span class="chip-status ${statusClass}">${c.status}</span>
        </button>
      `;
    }).join("");
  }

  renderTrackerResult(ticketId) {
    const container = document.getElementById("trackerResultArea");
    const ticket = this.complaints.find(c => c.id.toLowerCase() === ticketId.trim().toLowerCase());

    if (!ticket) {
      container.innerHTML = `
        <div class="glass-panel" style="padding: 3rem; text-align: center;">
          <i class="fa-solid fa-triangle-exclamation" style="font-size: 2.5rem; color: var(--amber); margin-bottom: 1rem;"></i>
          <h3>Complaint ID "${ticketId}" Not Found in Central Database</h3>
          <p style="color: var(--text-muted); margin-top: 0.5rem;">Please verify your Complaint Reference Number from your SMS confirmation or submitted slip.</p>
        </div>
      `;
      return;
    }

    const createdTime = new Date(ticket.createdAt).getTime();
    const elapsedHours = (Date.now() - createdTime) / (3600 * 1000);
    const isBreached = ticket.status !== "Resolved" && elapsedHours > ticket.slaHours;

    const stages = ["Pending", "Assigned", "In Progress", "Resolved"];
    const currentStageIndex = stages.indexOf(ticket.status);

    container.innerHTML = `
      <div class="tracker-result-card glass-panel" id="printableGrievanceCard">
        
        <!-- Left: Ticket Details -->
        <div class="tracker-details-panel">
          <div class="ticket-header-top">
            <div>
              <span class="ticket-id-tag"><i class="fa-solid fa-receipt"></i> ${ticket.id}</span>
              <h3 class="ticket-title">${ticket.title}</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">${ticket.description}</p>
            </div>
            <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.5rem;">
              <span class="badge-sla" style="${isBreached ? 'background: var(--danger-light); color: var(--danger);' : ''}">
                ${isBreached ? '⚠️ SLA BREACHED' : `${ticket.slaHours}h SLA ACTIVE`}
              </span>
              <button class="btn-print-slip" onclick="window.print()">
                <i class="fa-solid fa-print"></i> Print Slip
              </button>
            </div>
          </div>

          <!-- Official Government Gateway Sync Banner -->
          <div class="gov-gateway-box">
            <div class="gov-gateway-info">
              <span class="gov-gateway-title"><i class="fa-solid fa-landmark-flag"></i> ${ticket.govPortalName || 'Official Govt Grievance Portal'}</span>
              <span class="gov-gateway-ref">Ref No: ${ticket.govReferenceNo || 'GOI-SYNC-VERIFIED'}</span>
            </div>
            <a href="${ticket.govPortalUrl || 'https://pgportal.gov.in'}" target="_blank" rel="noopener" class="btn-gov-portal-link">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Verify on Official Govt Portal
            </a>
          </div>

          <div class="ticket-meta-grid">
            <div class="meta-field">
              <span class="meta-field-label">Department</span>
              <span class="meta-field-val">${ticket.assignedDept}</span>
            </div>
            <div class="meta-field">
              <span class="meta-field-label">Assigned Field Officer</span>
              <span class="meta-field-val">${ticket.assignedOfficer}</span>
            </div>
            <div class="meta-field">
              <span class="meta-field-label">Ward & Location</span>
              <span class="meta-field-val">${ticket.ward} (${ticket.landmark})</span>
            </div>
            <div class="meta-field">
              <span class="meta-field-label">Officer Helpline</span>
              <span class="meta-field-val" style="color: var(--primary);"><i class="fa-solid fa-phone"></i> ${ticket.officerPhone}</span>
            </div>
          </div>

          <!-- Proof Comparison -->
          <div class="proof-compare-row">
            <h4><i class="fa-solid fa-camera"></i> Ground Verification Proof</h4>
            <div class="proof-images">
              <div class="proof-img-box">
                ${ticket.photoBefore 
                  ? `<img src="${ticket.photoBefore}" alt="Reported Condition"><div class="proof-caption">Before: Issue Reported</div>`
                  : `<div style="height: 140px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--bg-card-subtle); color: var(--text-muted); font-size: 0.82rem; text-align: center; padding: 1rem;"><i class="fa-solid fa-camera" style="font-size: 1.5rem; margin-bottom: 0.4rem; opacity: 0.6;"></i> No Citizen Photo Attached</div>`
                }
              </div>
              <div class="proof-img-box">
                ${ticket.photoAfter 
                  ? `<img src="${ticket.photoAfter}" alt="Resolved Condition"><div class="proof-caption" style="color: var(--success); font-weight: 800;">After: Resolved by Field Officer</div>`
                  : `<div style="height: 140px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--bg-card-subtle); color: var(--text-muted); font-size: 0.8rem; text-align: center; padding: 1rem;"><i class="fa-solid fa-clock" style="font-size: 1.5rem; margin-bottom: 0.4rem;"></i> Awaiting Field Officer After-Photo</div>`
                }
              </div>
            </div>
          </div>

          <!-- Citizen Satisfaction Feedback & Re-open -->
          ${ticket.status === 'Resolved' ? `
            <div style="margin-top: 1.5rem; padding: 1.25rem; background: var(--success-light); border: 1px solid rgba(16,185,129,0.3); border-radius: var(--radius-md); text-align: center;">
              <strong style="color: #065f46;"><i class="fa-solid fa-circle-check"></i> Redressal Completed Successfully</strong>
              <p style="font-size: 0.82rem; color: #065f46; margin-top: 0.25rem;">Rate field execution or re-open if the problem was not adequately solved on-ground:</p>
              
              <div class="citizen-rating-stars">
                ${[1, 2, 3, 4, 5].map(star => `
                  <button class="star-btn" onclick="app.submitRating('${ticket.id}', ${star})" title="${star} Stars">
                    <i class="${ticket.rating && ticket.rating >= star ? 'fa-solid' : 'fa-regular'} fa-star"></i>
                  </button>
                `).join("")}
              </div>

              ${ticket.rating ? `<div style="font-size: 0.82rem; color: var(--success); font-weight: 700;">★ ${ticket.rating}/5 Rating Submitted by Citizen</div>` : ''}

              <button class="btn-reopen-complaint" onclick="app.reopenComplaint('${ticket.id}')">
                <i class="fa-solid fa-rotate-left"></i> Re-Open Grievance (Work Incomplete)
              </button>
            </div>
          ` : ''}

        </div>

        <!-- Right: 4-Stage Transparent Timeline -->
        <div class="timeline-panel">
          <h3><i class="fa-solid fa-timeline"></i> 4-Stage Redressal Lifecycle</h3>
          <div class="vertical-stepper">
            
            ${stages.map((stageName, index) => {
              const isPast = index <= currentStageIndex;
              const isCurrent = index === currentStageIndex;
              let nodeClass = "";
              if (isPast && !isCurrent) nodeClass = "completed";
              if (isCurrent) nodeClass = "active";
              if (isCurrent && isBreached) nodeClass = "escalated";

              const historyItem = ticket.timeline ? ticket.timeline.find(t => t.status === stageName) : null;

              return `
                <div class="step-node ${nodeClass}">
                  <div class="step-dot">
                    ${isPast && !isCurrent ? '<i class="fa-solid fa-check"></i>' : (index + 1)}
                  </div>
                  <div class="step-content">
                    <div class="step-header">
                      <span class="step-title">${stageName}</span>
                      <span class="step-time">${historyItem ? historyItem.time : (isPast ? 'Completed' : 'Upcoming')}</span>
                    </div>
                    <p class="step-desc">
                      ${historyItem ? historyItem.note : (isPast ? 'Completed at designated stage.' : `Pending transition to ${stageName}.`)}
                    </p>
                  </div>
                </div>
              `;
            }).join("")}

            ${ticket.escalationLevel && ticket.escalationLevel.includes("Escalated") ? `
              <div class="step-node escalated">
                <div class="step-dot"><i class="fa-solid fa-triangle-exclamation"></i></div>
                <div class="step-content" style="border-left: 3px solid var(--danger);">
                  <div class="step-header">
                    <span class="step-title" style="color: var(--danger);"><i class="fa-solid fa-bolt"></i> Auto-Escalation Activated</span>
                    <span class="step-time">Red-Alert</span>
                  </div>
                  <p class="step-desc" style="color: var(--danger);">
                    ${ticket.escalationLevel}. Immediate priority action requested by municipal commissionerate.
                  </p>
                </div>
              </div>
            ` : ''}

          </div>
        </div>

      </div>
    `;
  }

  async submitRating(ticketId, rating) {
    try {
      const res = await fetch(`${API_BASE}/complaints/${ticketId}/rate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ rating, feedback: "Verified via Citizen Portal" })
      });
      if (res.ok) {
        await this.fetchComplaints();
        this.renderTrackerResult(ticketId);
        this.showToast(`⭐ Thank you! ${rating}-Star feedback saved in database.`);
      }
    } catch (e) {}
  }

  async reopenComplaint(ticketId) {
    const reason = prompt("Please provide reason for re-opening (e.g. 'Pothole patch broke again after rain'):");
    if (!reason || reason.trim() === "") return;

    try {
      const res = await fetch(`${API_BASE}/complaints/${ticketId}/reopen`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ reason })
      });
      if (res.ok) {
        await this.fetchComplaints();
        await this.fetchStats();
        await this.fetchNotifications();
        this.renderTrackerResult(ticketId);
        this.showToast(`⚠️ Complaint ${ticketId} re-opened and flagged to Zonal Supervisor.`);
      }
    } catch (e) {}
  }

  /* ------------------------------------------------------------------------
     Admin & Field Officer SLA Desk & CSV Export
     ------------------------------------------------------------------------ */
  setupAdminDesk() {
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        filterButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.activeFilter = btn.dataset.filter;
        this.renderAdminTable();
      });
    });

    const exportBtn = document.getElementById("btnExportCsv");
    if (exportBtn) {
      exportBtn.addEventListener("click", () => {
        window.location.href = `${API_BASE}/export/csv`;
        this.showToast("📊 Generating CSV export from SQLite database...");
      });
    }

    this.renderAdminTable();
  }

  renderAdminTable() {
    const container = document.getElementById("adminComplaintsList");
    let filtered = [...this.complaints];

    if (this.activeFilter === "Escalated") {
      filtered = filtered.filter(c => {
        const created = new Date(c.createdAt).getTime();
        const elapsed = (Date.now() - created) / (3600 * 1000);
        return c.status !== "Resolved" && (elapsed > c.slaHours || (c.escalationLevel && c.escalationLevel.includes("Escalated")));
      });
    } else if (this.activeFilter !== "all") {
      filtered = filtered.filter(c => c.status === this.activeFilter);
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="glass-panel" style="padding: 2.5rem; text-align: center; color: var(--text-muted);">
          <i class="fa-solid fa-inbox" style="font-size: 2.5rem; margin-bottom: 0.75rem;"></i>
          <p>No complaints match the filter: <strong>${this.activeFilter}</strong></p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(c => {
      const created = new Date(c.createdAt).getTime();
      const elapsedHours = (Date.now() - created) / (3600 * 1000);
      const remainingHours = Math.round(c.slaHours - elapsedHours);
      const isBreached = c.status !== "Resolved" && remainingHours <= 0;

      let countdownBadge = "";
      if (c.status === "Resolved") {
        countdownBadge = `<span class="sla-countdown sla-ok"><i class="fa-solid fa-circle-check"></i> Resolved</span>`;
      } else if (isBreached) {
        countdownBadge = `<span class="sla-countdown sla-breached"><i class="fa-solid fa-bell"></i> Overdue by ${Math.abs(remainingHours)}h</span>`;
      } else if (remainingHours < 6) {
        countdownBadge = `<span class="sla-countdown sla-warning"><i class="fa-solid fa-clock"></i> ${remainingHours}h remaining</span>`;
      } else {
        countdownBadge = `<span class="sla-countdown sla-ok"><i class="fa-solid fa-clock"></i> ${remainingHours}h left</span>`;
      }

      const isEscalatedCard = isBreached || (c.escalationLevel && c.escalationLevel.includes("Escalated"));

      return `
        <div class="admin-ticket-card ${isEscalatedCard ? 'card-escalated' : ''}">
          
          <div class="ticket-col-id">
            <span class="col-id-text">${c.id}</span>
            <span class="col-date-text">${new Date(c.createdAt).toLocaleDateString("en-IN", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" })}</span>
            <span class="badge-sla" style="font-size: 0.7rem; padding: 0.1rem 0.4rem; margin-top: 0.2rem;">${c.urgency}</span>
          </div>

          <div class="ticket-col-main">
            <span class="col-title">${c.title}</span>
            <span class="col-location"><i class="fa-solid fa-location-dot"></i> ${c.ward}</span>
            <span style="font-size: 0.72rem; color: var(--saffron); font-weight: 700; margin-top: 0.2rem;">
              <i class="fa-solid fa-landmark"></i> ${c.govPortalName || 'CPGRAMS'} (${c.govReferenceNo || 'Synced'})
            </span>
          </div>

          <div class="ticket-col-dept">
            <span class="col-dept-name">${c.assignedDept}</span>
            <span class="col-officer-name"><i class="fa-solid fa-user-tie"></i> ${c.assignedOfficer}</span>
          </div>

          <div class="ticket-col-sla">
            ${countdownBadge}
            ${isBreached ? `<span class="escalation-tag tag-esc-2">Level 2 Escalated</span>` : ''}
            ${!isBreached && remainingHours < 6 && c.status !== 'Resolved' ? `<span class="escalation-tag tag-esc-1">Level 1 Alert</span>` : ''}
          </div>

          <div class="ticket-col-actions">
            <button class="btn-action-update" onclick="app.openOfficerModal('${c.id}')">
              <i class="fa-solid fa-sliders"></i> Update Status
            </button>
            <button class="btn-action-view" onclick="app.quickTrackFromAdmin('${c.id}')">
              View Tracking
            </button>
          </div>

        </div>
      `;
    }).join("");
  }

  quickTrackFromAdmin(id) {
    this.switchTab("tracker");
    document.getElementById("trackInput").value = id;
    this.renderTrackerResult(id);
  }

  /* ------------------------------------------------------------------------
     Officer Modal Dialog (Update Status / Upload Proof to Backend)
     ------------------------------------------------------------------------ */
  setupModals() {
    const modal = document.getElementById("officerModal");
    const closeBtn = document.getElementById("btnCloseModal");
    const cancelBtn = document.getElementById("btnCancelModal");
    const form = document.getElementById("officerActionForm");
    const sampleProofBtns = document.querySelectorAll(".btn-sample-proof");

    const closeModal = () => modal.classList.remove("open");
    closeBtn.addEventListener("click", closeModal);
    cancelBtn.addEventListener("click", closeModal);

    sampleProofBtns.forEach(b => {
      b.addEventListener("click", () => {
        document.getElementById("modalProofImgUrl").value = b.dataset.url;
      });
    });

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const id = document.getElementById("modalComplaintId").value;
      const newStatus = document.getElementById("newStatusSelect").value;
      const remarks = document.getElementById("officerRemarks").value.trim();
      const proofUrl = document.getElementById("modalProofImgUrl").value.trim();

      try {
        const formData = new FormData();
        formData.append("status", newStatus);
        formData.append("remarks", remarks);
        formData.append("proofPhotoUrl", proofUrl);

        const res = await fetch(`${API_BASE}/complaints/${id}/status`, {
          method: "PATCH",
          body: formData
        });

        if (res.ok) {
          await this.fetchComplaints();
          await this.fetchStats();
          await this.fetchNotifications();
          this.showToast(`✅ Complaint ${id} updated to "${newStatus}"!`);
          closeModal();
        }
      } catch (err) {
        console.error("Status update error:", err);
      }
    });
  }

  openOfficerModal(id) {
    const complaint = this.complaints.find(c => c.id === id);
    if (!complaint) return;

    document.getElementById("modalComplaintId").value = complaint.id;
    document.getElementById("modalTitle").innerHTML = `<i class="fa-solid fa-wrench"></i> Update Complaint: ${complaint.id}`;
    document.getElementById("modalComplaintSummary").innerHTML = `
      <strong>${complaint.title}</strong><br>
      <span style="color: var(--text-muted); font-size: 0.8rem;">Assigned Officer: ${complaint.assignedOfficer} | Current Status: <strong>${complaint.status}</strong></span>
    `;

    document.getElementById("newStatusSelect").value = complaint.status === "Pending" ? "Assigned" : (complaint.status === "Assigned" ? "In Progress" : "Resolved");
    document.getElementById("officerRemarks").value = "";

    const modal = document.getElementById("officerModal");
    modal.classList.add("open");
  }

  /* ------------------------------------------------------------------------
     Public Heatmap & Transparency Map (Leaflet.js)
     ------------------------------------------------------------------------ */
  setupHeatmap() {
    const mapElement = document.getElementById("civicMap");
    if (!mapElement) return;

    this.leafletMap = L.map("civicMap").setView([28.6139, 77.2290], 12);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 18,
      attribution: "© OpenStreetMap contributors | ONCOP Civic Transparency"
    }).addTo(this.leafletMap);

    this.renderMapMarkers();

    const catFilter = document.getElementById("mapFilterCategory");
    const statusFilter = document.getElementById("mapFilterStatus");

    catFilter.addEventListener("change", () => this.renderMapMarkers());
    statusFilter.addEventListener("change", () => this.renderMapMarkers());
  }

  renderMapMarkers() {
    if (!this.leafletMap) return;

    this.mapMarkers.forEach(m => this.leafletMap.removeLayer(m));
    this.mapMarkers = [];

    const catFilter = document.getElementById("mapFilterCategory").value;
    const statusFilter = document.getElementById("mapFilterStatus").value;

    let items = this.complaints.filter(c => {
      if (catFilter !== "all" && c.category !== catFilter) return false;
      if (statusFilter === "Resolved" && c.status !== "Resolved") return false;
      if (statusFilter === "active" && c.status === "Resolved") return false;
      if (statusFilter === "escalated") {
        const created = new Date(c.createdAt).getTime();
        const elapsed = (Date.now() - created) / (3600 * 1000);
        return c.status !== "Resolved" && elapsed > c.slaHours;
      }
      return true;
    });

    items.forEach(c => {
      const created = new Date(c.createdAt).getTime();
      const elapsed = (Date.now() - created) / (3600 * 1000);
      const isBreached = c.status !== "Resolved" && elapsed > c.slaHours;

      let color = "#1d4ed8";
      if (c.status === "Resolved") color = "#10b981";
      else if (isBreached || c.urgency === "Critical") color = "#ef4444";
      else if (c.status === "In Progress" || c.status === "Assigned") color = "#f59e0b";

      const circle = L.circleMarker([c.lat, c.lng], {
        radius: isBreached ? 14 : 10,
        fillColor: color,
        color: "#ffffff",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.85
      }).addTo(this.leafletMap);

      const popupHtml = `
        <div style="font-family: inherit; font-size: 0.85rem; max-width: 240px;">
          <div style="font-weight: 800; color: ${color}; margin-bottom: 0.2rem;">${c.id} • ${c.status}</div>
          <strong style="display: block; font-size: 0.9rem; line-height: 1.2; margin-bottom: 0.4rem;">${c.title}</strong>
          <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 0.5rem;"><i class="fa-solid fa-location-dot"></i> ${c.ward}</div>
          ${c.photoBefore ? `<img src="${c.photoBefore}" style="width: 100%; height: 90px; object-fit: cover; border-radius: 6px; margin-bottom: 0.5rem;">` : ''}
          <div style="font-size: 0.7rem; color: var(--saffron); font-weight: 700; margin-bottom: 0.4rem;">
            ${c.govPortalName || 'Govt Portal'} (${c.govReferenceNo || 'Synced'})
          </div>
          <button style="width: 100%; background: #1d4ed8; color: white; border: none; padding: 0.35rem 0.65rem; border-radius: 4px; font-weight: 700; cursor: pointer;" onclick="app.quickTrackFromAdmin('${c.id}')">
            Track Grievance
          </button>
        </div>
      `;

      circle.bindPopup(popupHtml);
      this.mapMarkers.push(circle);
    });
  }

  /* ------------------------------------------------------------------------
     KPI & Badge Counters
     ------------------------------------------------------------------------ */
  updateKpiCounters() {
    const total = this.complaints.length;
    const resolved = this.complaints.filter(c => c.status === "Resolved").length;
    const pending = this.complaints.filter(c => c.status === "Pending").length;
    const assigned = this.complaints.filter(c => c.status === "Assigned").length;
    const inProgress = this.complaints.filter(c => c.status === "In Progress").length;

    let escalated = 0;
    this.complaints.forEach(c => {
      const created = new Date(c.createdAt).getTime();
      const elapsed = (Date.now() - created) / (3600 * 1000);
      if (c.status !== "Resolved" && (elapsed > c.slaHours || (c.escalationLevel && c.escalationLevel.includes("Escalated")))) {
        escalated++;
      }
    });

    const setSafeText = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.textContent = val;
    };

    setSafeText("kpiTotal", total);
    setSafeText("kpiResolved", resolved);
    setSafeText("kpiEscalated", escalated);
    setSafeText("adminAlertBadge", escalated);

    setSafeText("countAll", total);
    setSafeText("countPending", pending);
    setSafeText("countAssigned", assigned);
    setSafeText("countInProgress", inProgress);
    setSafeText("countResolved", resolved);
    setSafeText("countEscalated", escalated);
  }

  /* ------------------------------------------------------------------------
     Toast Notification Helper
     ------------------------------------------------------------------------ */
  showToast(message) {
    const toast = document.getElementById("toastNotification");
    if (!toast) return;

    toast.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${message}</span>`;
    toast.classList.add("show");

    setTimeout(() => {
      toast.classList.remove("show");
    }, 4500);
  }
}

// Global App Instance Initialization
let app;
window.addEventListener("DOMContentLoaded", () => {
  app = new OncopApp();
  window.app = app;
});
