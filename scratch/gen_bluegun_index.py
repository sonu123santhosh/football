"""
Generate the updated index.html for BLUEGUN.
"""

index_html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BLUEGUN // 2026 Football Transfer Intelligence — Enter the Transfer Battlefield</title>
  <meta name="description" content="BLUEGUN — 2026 Football Transfer Intelligence. Real-time tactical scouting, player ego ratings, transfer momentum, and European market analytics.">
  
  <!-- Favicon / Icon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><polygon points='50,5 92,27 92,73 50,95 8,73 8,27' fill='none' stroke='%2300f0ff' stroke-width='8'/><circle cx='50' cy='50' r='20' fill='%2300f0ff'/></svg>">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/sections.css">
  <link rel="stylesheet" href="css/responsive.css">
</head>
<body>

  <!-- Top Sticky Navigation Bar -->
  <header class="bl-navbar">
    <div class="bl-navbar-inner">
      
      <!-- Brand Logo -->
      <a class="bl-logo-brand" data-view="home">
        <div class="logo-symbol">
          <svg width="28" height="28" viewBox="0 0 100 100">
            <polygon points="50,5 92,27 92,73 50,95 8,73 8,27" fill="none" stroke="#00f0ff" stroke-width="8"/>
            <line x1="50" y1="5" x2="50" y2="95" stroke="#0077ff" stroke-width="4" stroke-dasharray="6,6"/>
            <circle cx="50" cy="50" r="22" fill="rgba(0, 240, 255, 0.2)" stroke="#00f0ff" stroke-width="5"/>
            <circle cx="50" cy="50" r="8" fill="#00f0ff"/>
          </svg>
        </div>
        <div class="logo-text-group">
          <span class="logo-main-title">BLUEGUN</span>
          <span class="logo-tagline">"ENTER THE TRANSFER BATTLEFIELD."</span>
        </div>
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="bl-nav-menu">
        <ul class="bl-nav-links">
          <li><a href="#home" class="nav-link active" data-view="home">WAR ROOM</a></li>
          <li><a href="#transfers" class="nav-link" data-view="transfers">LIVE TRANSFERS</a></li>
          <li><a href="#players" class="nav-link" data-view="players">SCOUTING FILES</a></li>
          <li><a href="#clubs" class="nav-link" data-view="clubs">CLUBS</a></li>
          <li><a href="#news" class="nav-link" data-view="news">INTELLIGENCE</a></li>
          <li><a href="#market" class="nav-link" data-view="market">MARKET MATRIX</a></li>
          <li><a href="#compare" class="nav-link" data-view="compare">EGO CLASH</a></li>
          <li><a href="#copyright" class="nav-link" data-view="copyright">COMPLIANCE</a></li>
        </ul>
      </nav>

      <!-- Right Action Bar -->
      <div class="bl-nav-right">
        
        <!-- Search Trigger -->
        <button class="nav-search-trigger" id="navSearchTrigger" title="Quick Search (Ctrl+K)">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
          <span>Search 2026 intel...</span>
          <kbd class="search-hint-kbd">Ctrl+K</kbd>
        </button>

        <!-- Notification Bell -->
        <button class="nav-icon-btn" id="btnNotifications" title="Live 2026 Radar Alerts">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span class="notif-badge-dot"></span>
        </button>

        <!-- Profile Avatar Placeholder -->
        <div class="user-ego-avatar" title="BLUEGUN Commander ID: EGO-01" data-view="home">
          <span>BG</span>
        </div>

        <!-- Mobile Menu Toggle Button -->
        <button class="mobile-menu-btn" id="mobileMenuToggle" aria-label="Toggle Navigation">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>

      </div>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <aside class="bl-mobile-drawer" id="mobileNavDrawer">
    <div class="drawer-header">
      <div class="bl-logo-brand">
        <div class="logo-symbol">
          <svg width="22" height="22" viewBox="0 0 100 100">
            <polygon points="50,5 92,27 92,73 50,95 8,73 8,27" fill="none" stroke="#00f0ff" stroke-width="8"/>
            <circle cx="50" cy="50" r="18" fill="#00f0ff"/>
          </svg>
        </div>
        <div class="logo-text-group">
          <span class="logo-main-title">BLUEGUN</span>
        </div>
      </div>
      <button class="modal-close-btn" id="closeDrawerBtn" aria-label="Close Drawer">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <ul class="drawer-links-list">
      <li><a class="drawer-link active" data-view="home">TRANSFER WAR ROOM</a></li>
      <li><a class="drawer-link" data-view="transfers">LIVE TRANSFERS (2026)</a></li>
      <li><a class="drawer-link" data-view="players">PLAYER SCOUTING FILES</a></li>
      <li><a class="drawer-link" data-view="clubs">EUROPEAN CLUBS</a></li>
      <li><a class="drawer-link" data-view="news">TRANSFER INTELLIGENCE</a></li>
      <li><a class="drawer-link" data-view="market">MARKET INTELLIGENCE</a></li>
      <li><a class="drawer-link" data-view="compare">EGO CLASH / RADAR</a></li>
      <li><a class="drawer-link" data-view="copyright">⚖️ COPYRIGHT & ATTRIBUTION</a></li>
    </ul>
  </aside>

  <!-- Main Application Container -->
  <main class="bl-main-app">
    <div class="bl-container" id="mainContent">
      <!-- Dynamic views rendered via JavaScript router -->
    </div>
  </main>

  <!-- Global Footer Container Mount -->
  <div id="globalFooterMount"></div>

  <!-- Global Search Modal -->
  <div class="bl-modal-backdrop" id="searchModal">
    <div class="bl-modal-window">
      <div class="search-modal-bar">
        <svg class="search-icon-cyan" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="globalSearchInput" class="search-main-input" placeholder="Search 2026 players, clubs, rumours, news..." autocomplete="off" />
        <button class="modal-close-btn" id="closeSearchBtn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="search-results-list" id="globalSearchResults">
        <!-- Live search suggestions rendered here -->
      </div>
    </div>
  </div>

  <!-- Notifications / Breaking Alerts Modal -->
  <div class="bl-modal-backdrop" id="notifModal">
    <div class="bl-modal-window" style="max-width: 480px;">
      <div class="modal-header-bar">
        <span class="modal-title">2026 WAR ROOM BREAKING ALERTS</span>
        <button class="modal-close-btn" id="closeNotifBtn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-scroll-body">
        <div class="search-items-list">
          <div class="search-result-item" onclick="window.bluegunApp.navigateTo('player-profile', { playerId: 'florian-wirtz' }); document.getElementById('notifModal').classList.remove('active');">
            <span class="pulse-dot"></span>
            <div class="result-info">
              <strong class="result-name">Florian Wirtz → Real Madrid</strong>
              <span class="result-sub">Decisive €140M package entering active talks</span>
            </div>
            <span class="cyan font-bold font-mono">82%</span>
          </div>

          <div class="search-result-item" onclick="window.bluegunApp.navigateTo('player-profile', { playerId: 'alexander-isak' }); document.getElementById('notifModal').classList.remove('active');">
            <span class="pulse-dot"></span>
            <div class="result-info">
              <strong class="result-name">Arsenal Submits €100M for Alexander Isak</strong>
              <span class="result-sub">Striker target priority for Arteta</span>
            </div>
            <span class="gold font-bold font-mono">79%</span>
          </div>

          <div class="search-result-item" onclick="window.bluegunApp.navigateTo('player-profile', { playerId: 'victor-osimhen' }); document.getElementById('notifModal').classList.remove('active');">
            <span class="pulse-dot"></span>
            <div class="result-info">
              <strong class="result-name">Chelsea Close on Osimhen €75M Clause</strong>
              <span class="result-sub">Personal terms settled in London</span>
            </div>
            <span class="neon font-bold font-mono">88%</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- News Story Reader Modal -->
  <div class="bl-modal-backdrop" id="newsModal">
    <div class="bl-modal-window" style="max-width: 720px;">
      <div class="modal-header-bar">
        <span class="modal-title">BLUEGUN SCOUTING INTEL DOSSIER</span>
        <button class="modal-close-btn" onclick="window.bluegunApp.closeNewsModal()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-scroll-body" id="newsModalBody">
        <!-- Content injected dynamically -->
      </div>
    </div>
  </div>

  <!-- Legal Policy Modal (Privacy Policy & Terms of Use) -->
  <div class="bl-modal-backdrop" id="legalModal">
    <div class="bl-modal-window" style="max-width: 720px;">
      <div class="modal-header-bar">
        <span class="modal-title" id="legalModalTitle">BLUEGUN LEGAL POLICY</span>
        <button class="modal-close-btn" id="closeLegalBtn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-scroll-body" id="legalModalBody">
        <!-- Policy content injected dynamically -->
      </div>
    </div>
  </div>

  <!-- Application Bootstrap -->
  <script type="module" src="js/app.js"></script>
</body>
</html>
'''

with open(r"c:\Users\LENOVO\Desktop\web\index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content.strip())

print("Successfully updated index.html with BLUEGUN branding!")
