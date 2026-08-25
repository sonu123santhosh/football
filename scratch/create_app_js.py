"""
Enrich js/app.js to support the copyright view, legal modals, and compliance interactions.
"""

new_app_js = '''/**
 * BLUELOCK // TRANSFER IQ - Core Application Controller
 * Single-page router, reactive state manager, global search, and interactive controllers.
 * Enhanced with full copyright, attribution, and compliance handlers.
 */

import { CLUBS, PLAYERS, LIVE_TRANSFERS, TRANSFER_NEWS, DASHBOARD_STATS, DATA_SOURCES } from './data.js';
import {
  renderTransferCard,
  renderPlayerCard,
  renderClubCard,
  renderNewsCard,
  renderPlayerProfile,
  renderClubProfile,
  renderTransferMarketTable,
  renderComparisonView,
  renderCopyrightAndAttributionView,
  renderGlobalFooter,
  getPrivacyPolicyHtml,
  getTermsOfUseHtml,
  getStatusBadge,
  PLAYER_IMG_FALLBACK,
  CLUB_IMG_FALLBACK
} from './components.js';
import { renderRadarChart, renderMarketValueChart } from './chart.js';

// Application State
const state = {
  currentView: 'home', // 'home' | 'transfers' | 'players' | 'clubs' | 'news' | 'market' | 'compare' | 'player-profile' | 'club-profile' | 'copyright'
  selectedPlayerId: 'julian-alvarez',
  selectedClubId: 'real-madrid',
  comparePlayerAId: 'kylian-mbappe',
  comparePlayerBId: 'erling-haaland',
  transferFilter: 'ALL',
  newsFilter: 'ALL',
  marketSearchQuery: '',
  marketSortKey: 'marketValueRaw',
  marketSortAsc: false,
  marketPositionFilter: 'ALL',
  marketStatusFilter: 'ALL',
  globalSearchQuery: ''
};

// DOM Cache
let mainContentEl;
let navLinks;
let globalSearchModal;
let globalSearchInput;
let globalSearchResults;
let mobileMenuBtn;
let mobileNavDrawer;
let notifBtn;
let notifModal;
let legalModal;
let legalModalTitle;
let legalModalBody;

/**
 * Initialize Application
 */
document.addEventListener('DOMContentLoaded', () => {
  initDomElements();
  initEventListeners();
  initKeyboardShortcuts();
  renderCurrentView();
  startHeroTicker();
});

function initDomElements() {
  mainContentEl = document.getElementById('mainContent');
  navLinks = document.querySelectorAll('.nav-link');
  globalSearchModal = document.getElementById('searchModal');
  globalSearchInput = document.getElementById('globalSearchInput');
  globalSearchResults = document.getElementById('globalSearchResults');
  mobileMenuBtn = document.getElementById('mobileMenuToggle');
  mobileNavDrawer = document.getElementById('mobileNavDrawer');
  notifBtn = document.getElementById('btnNotifications');
  notifModal = document.getElementById('notifModal');
  legalModal = document.getElementById('legalModal');
  legalModalTitle = document.getElementById('legalModalTitle');
  legalModalBody = document.getElementById('legalModalBody');
}

/**
 * Global Event Listeners
 */
function initEventListeners() {
  // Navigation Bar Links (Desktop & Mobile)
  document.addEventListener('click', (e) => {
    const viewBtn = e.target.closest('[data-view]');
    if (viewBtn) {
      e.preventDefault();
      const view = viewBtn.getAttribute('data-view');
      const pId = viewBtn.getAttribute('data-player-id');
      const cId = viewBtn.getAttribute('data-club-id');
      navigateTo(view, { playerId: pId, clubId: cId });
      closeMobileDrawer();
      return;
    }

    // Legal Modal Triggers (Privacy / Terms)
    const legalTrigger = e.target.closest('.footer-legal-modal-trigger');
    if (legalTrigger) {
      e.preventDefault();
      const modalType = legalTrigger.getAttribute('data-modal');
      openLegalModal(modalType);
      return;
    }

    // Back to dashboard buttons
    if (e.target.closest('.btn-back-dashboard')) {
      e.preventDefault();
      navigateTo('home');
      return;
    }

    // View Player Profile Trigger
    const btnPlayer = e.target.closest('.btn-view-player');
    if (btnPlayer) {
      e.preventDefault();
      const pId = btnPlayer.getAttribute('data-player-id');
      navigateTo('player-profile', { playerId: pId });
      return;
    }

    // View Club Profile Trigger
    const btnClub = e.target.closest('.btn-view-club');
    if (btnClub) {
      e.preventDefault();
      const cId = btnClub.getAttribute('data-club-id');
      navigateTo('club-profile', { clubId: cId });
      return;
    }

    // Quick Compare Trigger
    const btnCompare = e.target.closest('.btn-quick-compare');
    if (btnCompare) {
      e.preventDefault();
      const pId = btnCompare.getAttribute('data-compare-id');
      navigateTo('compare', { compareA: pId });
      return;
    }

    // Read News Story Trigger
    const btnNews = e.target.closest('.btn-read-news');
    if (btnNews) {
      e.preventDefault();
      const nId = btnNews.getAttribute('data-news-id');
      openNewsModal(nId);
      return;
    }
  });

  // Mobile Drawer Toggle
  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', toggleMobileDrawer);
  }
  const closeDrawerBtn = document.getElementById('closeDrawerBtn');
  if (closeDrawerBtn) {
    closeDrawerBtn.addEventListener('click', closeMobileDrawer);
  }

  // Global Search Modal Open / Close
  const searchTriggerBtn = document.getElementById('btnOpenSearch');
  const searchInputTrigger = document.getElementById('navSearchTrigger');
  const closeSearchBtn = document.getElementById('closeSearchBtn');

  if (searchTriggerBtn) searchTriggerBtn.addEventListener('click', openSearchModal);
  if (searchInputTrigger) searchInputTrigger.addEventListener('click', openSearchModal);
  if (closeSearchBtn) closeSearchBtn.addEventListener('click', closeSearchModal);

  // Global Search Typing
  if (globalSearchInput) {
    globalSearchInput.addEventListener('input', handleGlobalSearchInput);
  }

  // Notifications Modal
  if (notifBtn) {
    notifBtn.addEventListener('click', toggleNotifModal);
  }
  const closeNotifBtn = document.getElementById('closeNotifBtn');
  if (closeNotifBtn) {
    closeNotifBtn.addEventListener('click', closeNotifModal);
  }

  // Legal Modal Close Button
  const closeLegalBtn = document.getElementById('closeLegalBtn');
  if (closeLegalBtn) {
    closeLegalBtn.addEventListener('click', closeLegalModal);
  }

  // Click Outside Modals
  window.addEventListener('click', (e) => {
    if (e.target === globalSearchModal) closeSearchModal();
    if (e.target === notifModal) closeNotifModal();
    const newsModal = document.getElementById('newsModal');
    if (e.target === newsModal) closeNewsModal();
    if (e.target === legalModal) closeLegalModal();
  });
}

/**
 * Keyboard Shortcuts (e.g. Ctrl+K or / to search, Esc to close)
 */
function initKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearchModal();
    }
    if (e.key === '/' && document.activeElement !== globalSearchInput && !globalSearchModal?.classList.contains('active')) {
      e.preventDefault();
      openSearchModal();
    }
    if (e.key === 'Escape') {
      closeSearchModal();
      closeNotifModal();
      closeNewsModal();
      closeLegalModal();
    }
  });
}

/**
 * Route / View Navigation
 */
export function navigateTo(viewName, params = {}) {
  state.currentView = viewName;
  if (params.playerId) state.selectedPlayerId = params.playerId;
  if (params.clubId) state.selectedClubId = params.clubId;
  if (params.compareA) state.comparePlayerAId = params.compareA;
  if (params.compareB) state.comparePlayerBId = params.compareB;

  // Update active states on nav items
  document.querySelectorAll('.nav-link, .drawer-link').forEach(link => {
    const target = link.getAttribute('data-view');
    if (target === viewName) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderCurrentView();
}

/**
 * View Dispatcher
 */
function renderCurrentView() {
  if (!mainContentEl) return;

  switch (state.currentView) {
    case 'home':
      renderHomeView();
      break;
    case 'transfers':
      renderTransfersFeedView();
      break;
    case 'players':
      renderPlayersListView();
      break;
    case 'clubs':
      renderClubsListView();
      break;
    case 'news':
      renderNewsView();
      break;
    case 'market':
      renderMarketTableView();
      break;
    case 'compare':
      renderCompareView();
      break;
    case 'player-profile':
      renderPlayerProfileView();
      break;
    case 'club-profile':
      renderClubProfileView();
      break;
    case 'copyright':
      renderCopyrightView();
      break;
    default:
      renderHomeView();
  }

  // Update dynamic footer at the bottom of the page
  const footerContainer = document.getElementById('globalFooterMount');
  if (footerContainer) {
    footerContainer.innerHTML = renderGlobalFooter();
  }
}

/**
 * VIEW: HOME / DASHBOARD
 */
function renderHomeView() {
  const topTransfers = LIVE_TRANSFERS.slice(0, 4);
  const hotNews = TRANSFER_NEWS.slice(0, 3);
  const topTalents = PLAYERS.slice(0, 4);

  mainContentEl.innerHTML = `
    <!-- Top Live Transfer Marquee Ticker -->
    <div class="bl-ticker-wrapper">
      <div class="ticker-badge">LIVE RADAR WIRE</div>
      <div class="ticker-content-track" id="heroTickerTrack">
        ${LIVE_TRANSFERS.map(t => `
          <span class="ticker-item">
            <span class="pulse-dot"></span>
            <strong>${t.playerName}</strong> (${t.fromClub} ➔ ${t.toClub}) // 
            <span class="cyan">${t.reportedFee}</span> // 
            <span class="gold">${t.status}</span>
          </span>
        `).join('')}
      </div>
    </div>

    <!-- Hero Intelligence Section -->
    <section class="bl-hero-section">
      <div class="hero-bg-grid"></div>
      <div class="hero-glow-orb cyan"></div>
      <div class="hero-glow-orb blue"></div>

      <div class="hero-content">
        <div class="hero-tag-badge">
          <span class="pulse-dot"></span>
          <span>TRANSFER BATTLEFIELD ACTIVE // 2025/2026</span>
        </div>

        <h1 class="hero-headline">
          THE TRANSFER MARKET IS MOVING.
          <span class="hero-sub-glitch">DOMINATE THE BATTLEFIELD.</span>
        </h1>

        <p class="hero-lead">
          Real-time tactical intelligence, algorithmic transfer probability, and high-ego scouting analytics.
        </p>

        <!-- Hero Stats HUD Grid -->
        <div class="hero-stats-hud">
          <div class="stat-hud-card">
            <span class="hud-lbl">ACTIVE RUMOURS</span>
            <span class="hud-val cyan">${DASHBOARD_STATS.activeRumours}</span>
            <span class="hud-sub">Live Signals</span>
          </div>

          <div class="stat-hud-card">
            <span class="hud-lbl">CONFIRMED DEALS</span>
            <span class="hud-val green">${DASHBOARD_STATS.confirmedTransfers}</span>
            <span class="hud-sub">Signed & Presented</span>
          </div>

          <div class="stat-hud-card">
            <span class="hud-lbl">MARKET POWERHOUSE</span>
            <span class="hud-val gold">${DASHBOARD_STATS.mostActiveClub.name}</span>
            <span class="hud-sub">${DASHBOARD_STATS.mostActiveClub.deals} Completed Deals</span>
          </div>

          <div class="stat-hud-card">
            <span class="hud-lbl">AVG EGO THREAT</span>
            <span class="hud-val">${DASHBOARD_STATS.avgEgoRating}</span>
            <span class="hud-sub">Top Tier Rating</span>
          </div>
        </div>

        <!-- Quick Battlefield Actions -->
        <div class="hero-cta-group">
          <button class="bl-btn bl-btn-lg bl-btn-cyber" data-view="transfers">
            <span>EXPLORE LIVE TRANSFERS</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
          <button class="bl-btn bl-btn-lg bl-btn-outline" data-view="compare">
            <span>EGO CLASH RADAR</span>
          </button>
          <button class="bl-btn bl-btn-lg bl-btn-outline" data-view="copyright">
            <span>⚖️ ATTRIBUTION & LICENSES</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Hot Spotlights Grid -->
    <div class="dashboard-grid-layout">
      
      <!-- Left: Top Transfer Movements -->
      <div class="dash-column left">
        <div class="section-title-wrap">
          <div class="section-title-icon">🔵</div>
          <h2 class="section-heading">HOT TRANSFER SPOTLIGHT</h2>
          <button class="bl-btn bl-btn-xs bl-btn-outline" data-view="transfers">VIEW ALL (${LIVE_TRANSFERS.length})</button>
        </div>

        <div class="transfers-cards-stack">
          ${topTransfers.map(tr => renderTransferCard(tr)).join('')}
        </div>
      </div>

      <!-- Right: Breaking Wire & Scouting Radar -->
      <div class="dash-column right">
        <div class="section-title-wrap">
          <div class="section-title-icon">📰</div>
          <h2 class="section-heading">BREAKING TRANSFER WIRE</h2>
          <button class="bl-btn bl-btn-xs bl-btn-outline" data-view="news">ALL NEWS</button>
        </div>

        <div class="news-cards-stack">
          ${hotNews.map(item => renderNewsCard(item)).join('')}
        </div>

        <!-- Featured Scouting Talents Mini Grid -->
        <div class="section-title-wrap" style="margin-top: 32px;">
          <div class="section-title-icon">⚡</div>
          <h2 class="section-heading">TOP EGO TARGETS</h2>
          <button class="bl-btn bl-btn-xs bl-btn-outline" data-view="players">DATABASE</button>
        </div>

        <div class="top-talents-mini-grid">
          ${topTalents.map(p => `
            <div class="talent-mini-card" data-view="player-profile" data-player-id="${p.id}">
              <img src="${p.image || p.photo}" alt="${p.name}" class="mini-avatar" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
              <div class="mini-info">
                <strong>${p.name}</strong>
                <span>${p.currentClub} // ${p.position.split(' ')[0]}</span>
              </div>
              <div class="mini-ego gold">EGO ${p.egoRating}</div>
            </div>
          `).join('')}
        </div>
      </div>

    </div>
  `;
}

/**
 * VIEW: LIVE TRANSFERS FEED
 */
function renderTransfersFeedView() {
  let list = [...LIVE_TRANSFERS];
  if (state.transferFilter !== 'ALL') {
    list = list.filter(t => t.status === state.transferFilter);
  }

  mainContentEl.innerHTML = `
    <div class="view-header-strip">
      <div>
        <span class="sub-label">RADAR DISPATCH</span>
        <h1 class="main-title">LIVE TRANSFER WIRE & NEGOTIATIONS</h1>
      </div>
      
      <!-- Filter Chips -->
      <div class="filter-chips-group">
        ${['ALL', 'CONFIRMED', 'NEGOTIATING', 'RUMOUR', 'LOAN', 'FREE TRANSFER'].map(status => `
          <button class="filter-chip ${state.transferFilter === status ? 'active' : ''}" data-filter-status="${status}">
            ${status}
          </button>
        `).join('')}
      </div>
    </div>

    <div class="transfers-masonry-grid">
      ${list.length > 0 ? list.map(tr => renderTransferCard(tr)).join('') : '<p class="empty-state">No transfers match the selected filter criteria.</p>'}
    </div>
  `;

  // Attach filter events
  document.querySelectorAll('[data-filter-status]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      state.transferFilter = e.target.getAttribute('data-filter-status');
      renderTransfersFeedView();
    });
  });
}

/**
 * VIEW: PLAYERS LISTING
 */
function renderPlayersListView() {
  mainContentEl.innerHTML = `
    <div class="view-header-strip">
      <div>
        <span class="sub-label">TACTICAL DATABASE</span>
        <h1 class="main-title">SUPERSTAR SCOUTING DOSSIER (${PLAYERS.length} ATHLETES)</h1>
      </div>
      <div class="search-bar-inline">
        <input type="text" id="playerInlineSearch" class="bl-input" placeholder="Search player name, position, or club..." />
      </div>
    </div>

    <div class="players-responsive-grid" id="playersGridMount">
      ${PLAYERS.map(p => renderPlayerCard(p)).join('')}
    </div>
  `;

  const searchInput = document.getElementById('playerInlineSearch');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const filtered = PLAYERS.filter(p => 
        p.name.toLowerCase().includes(q) ||
        p.currentClub.toLowerCase().includes(q) ||
        p.position.toLowerCase().includes(q) ||
        p.nationality.toLowerCase().includes(q)
      );
      const grid = document.getElementById('playersGridMount');
      if (grid) {
        grid.innerHTML = filtered.length > 0 
          ? filtered.map(p => renderPlayerCard(p)).join('') 
          : '<p class="empty-state">No players found matching your query.</p>';
      }
    });
  }
}

/**
 * VIEW: CLUBS LISTING
 */
function renderClubsListView() {
  mainContentEl.innerHTML = `
    <div class="view-header-strip">
      <div>
        <span class="sub-label">EUROPEAN WAR ROOMS</span>
        <h1 class="main-title">TOP 10 EUROPEAN POWERHOUSES</h1>
      </div>
    </div>

    <div class="clubs-grid-layout">
      ${CLUBS.map(club => renderClubCard(club)).join('')}
    </div>
  `;
}

/**
 * VIEW: NEWS WIRE
 */
function renderNewsView() {
  let list = [...TRANSFER_NEWS];
  if (state.newsFilter !== 'ALL') {
    list = list.filter(n => n.category === state.newsFilter);
  }

  mainContentEl.innerHTML = `
    <div class="view-header-strip">
      <div>
        <span class="sub-label">CONFIDENTIAL WIRE</span>
        <h1 class="main-title">TRANSFER MARKET HEADLINES & REPORTS</h1>
      </div>

      <div class="filter-chips-group">
        ${['ALL', 'CONFIRMED', 'NEGOTIATIONS', 'RUMOURS', 'LOANS', 'FREE TRANSFERS'].map(cat => `
          <button class="filter-chip ${state.newsFilter === cat ? 'active' : ''}" data-news-filter="${cat}">
            ${cat}
          </button>
        `).join('')}
      </div>
    </div>

    <div class="news-stream-grid">
      ${list.map(item => renderNewsCard(item)).join('')}
    </div>
  `;

  document.querySelectorAll('[data-news-filter]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      state.newsFilter = e.target.getAttribute('data-news-filter');
      renderNewsView();
    });
  });
}

/**
 * VIEW: TRANSFER MARKET DATA MATRIX
 */
function renderMarketTableView() {
  let list = [...PLAYERS];

  // Sorting
  list.sort((a, b) => {
    let valA = a[state.marketSortKey];
    let valB = b[state.marketSortKey];
    if (state.marketSortAsc) {
      return valA > valB ? 1 : -1;
    } else {
      return valA < valB ? 1 : -1;
    }
  });

  mainContentEl.innerHTML = `
    <div class="view-header-strip">
      <div>
        <span class="sub-label">FINANCIAL INTEL</span>
        <h1 class="main-title">TRANSFER MARKET VALUATION MATRIX</h1>
      </div>
    </div>

    ${renderTransferMarketTable(list, state.marketSortKey, state.marketSortAsc)}
  `;

  // Attach Table Header Sorting
  document.querySelectorAll('.bl-table th.sortable').forEach(th => {
    th.addEventListener('click', () => {
      const key = th.getAttribute('data-sort');
      if (state.marketSortKey === key) {
        state.marketSortAsc = !state.marketSortAsc;
      } else {
        state.marketSortKey = key;
        state.marketSortAsc = false;
      }
      renderMarketTableView();
    });
  });
}

/**
 * VIEW: EGO CLASH / COMPARE
 */
function renderCompareView() {
  const pA = PLAYERS.find(p => p.id === state.comparePlayerAId) || PLAYERS[0];
  const pB = PLAYERS.find(p => p.id === state.comparePlayerBId) || PLAYERS[1];

  mainContentEl.innerHTML = `
    <!-- Top Player Pickers Bar -->
    <div class="compare-selector-bar bl-hud-panel">
      <div class="picker-group">
        <label>PLAYER A (CYAN)</label>
        <select id="selectPlayerA" class="bl-select">
          ${PLAYERS.map(p => `<option value="${p.id}" ${p.id === pA.id ? 'selected' : ''}>${p.name} (${p.currentClub})</option>`).join('')}
        </select>
      </div>

      <div class="vs-symbol-badge">VS</div>

      <div class="picker-group">
        <label>PLAYER B (RED)</label>
        <select id="selectPlayerB" class="bl-select">
          ${PLAYERS.map(p => `<option value="${p.id}" ${p.id === pB.id ? 'selected' : ''}>${p.name} (${p.currentClub})</option>`).join('')}
        </select>
      </div>
    </div>

    ${renderComparisonView(pA, pB)}
  `;

  // Initialize SVG Radar Chart for comparison
  setTimeout(() => {
    renderRadarChart('comparisonRadarContainer', pA, pB);
  }, 50);

  // Selector listeners
  const selA = document.getElementById('selectPlayerA');
  const selB = document.getElementById('selectPlayerB');

  if (selA) {
    selA.addEventListener('change', (e) => {
      state.comparePlayerAId = e.target.value;
      renderCompareView();
    });
  }
  if (selB) {
    selB.addEventListener('change', (e) => {
      state.comparePlayerBId = e.target.value;
      renderCompareView();
    });
  }
}

/**
 * VIEW: PLAYER PROFILE
 */
function renderPlayerProfileView() {
  const player = PLAYERS.find(p => p.id === state.selectedPlayerId) || PLAYERS[0];
  mainContentEl.innerHTML = renderPlayerProfile(player);

  // Render Charts
  setTimeout(() => {
    renderRadarChart('playerRadarContainer', player);
    renderMarketValueChart('playerValuationChart', player.valueHistory);
  }, 50);
}

/**
 * VIEW: CLUB PROFILE
 */
function renderClubProfileView() {
  const club = CLUBS.find(c => c.id === state.selectedClubId) || CLUBS[0];
  mainContentEl.innerHTML = renderClubProfile(club);
}

/**
 * VIEW: COPYRIGHT, ATTRIBUTION & LICENSES
 */
function renderCopyrightView() {
  mainContentEl.innerHTML = renderCopyrightAndAttributionView();
}

/**
 * Helper: Open News Reader Modal
 */
export function openNewsModal(newsId) {
  const item = TRANSFER_NEWS.find(n => n.id === newsId);
  if (!item) return;

  const modal = document.getElementById('newsModal');
  const body = document.getElementById('newsModalBody');
  if (!modal || !body) return;

  const sourceUrl = item.sourceUrl || 'https://www.skysports.com/football/transfers';

  body.innerHTML = `
    <div class="news-modal-body-content">
      <div class="news-modal-hero">
        <img src="${item.image || 'assets/players/mbappe.jpg'}" alt="${item.title}" class="news-modal-img" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="news-category-tag">${item.category}</div>
      </div>
      <div class="news-modal-meta">
        <span>📰 Source: <strong>${item.source}</strong></span>
        <span>⏱️ ${item.published} (${item.readTime})</span>
      </div>
      <h2 class="news-modal-title">${item.title}</h2>
      <p class="news-modal-lead">${item.summary}</p>
      <div class="news-modal-text">
        <p>${item.content}</p>
      </div>

      <div class="news-modal-compliance-notice">
        <p>* Editorial intelligence excerpt. Read the complete verified coverage on the original publication.</p>
        <a href="${sourceUrl}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-sm bl-btn-cyber">
          <span>READ ON ORIGINAL SOURCE →</span>
        </a>
      </div>
    </div>
  `;

  modal.classList.add('active');
}

export function closeNewsModal() {
  const modal = document.getElementById('newsModal');
  if (modal) modal.classList.remove('active');
}

/**
 * Helper: Open Legal Policy Modal (Privacy Policy or Terms of Use)
 */
export function openLegalModal(type) {
  if (!legalModal || !legalModalTitle || !legalModalBody) return;

  if (type === 'privacy') {
    legalModalTitle.textContent = 'LEGAL POLICY: PRIVACY STATEMENT';
    legalModalBody.innerHTML = getPrivacyPolicyHtml();
  } else {
    legalModalTitle.textContent = 'LEGAL POLICY: TERMS OF USE';
    legalModalBody.innerHTML = getTermsOfUseHtml();
  }

  legalModal.classList.add('active');
}

export function closeLegalModal() {
  if (legalModal) legalModal.classList.remove('active');
}

/**
 * Global Search Autocomplete
 */
function openSearchModal() {
  if (globalSearchModal) {
    globalSearchModal.classList.add('active');
    setTimeout(() => {
      if (globalSearchInput) {
        globalSearchInput.focus();
        handleGlobalSearchInput();
      }
    }, 100);
  }
}

function closeSearchModal() {
  if (globalSearchModal) globalSearchModal.classList.remove('active');
}

function handleGlobalSearchInput() {
  const q = globalSearchInput ? globalSearchInput.value.toLowerCase().trim() : '';
  if (!globalSearchResults) return;

  if (!q) {
    globalSearchResults.innerHTML = `
      <div class="search-hint-box">
        <span>⚡ Quick shortcuts: Type player name (e.g. <em>Mbappé, Haaland, Palmer</em>), club (<em>Real Madrid, Man City</em>), or status (<em>Confirmed</em>).</span>
      </div>
    `;
    return;
  }

  const matchedPlayers = PLAYERS.filter(p => p.name.toLowerCase().includes(q) || p.currentClub.toLowerCase().includes(q));
  const matchedClubs = CLUBS.filter(c => c.name.toLowerCase().includes(q) || c.league.toLowerCase().includes(q));
  const matchedNews = TRANSFER_NEWS.filter(n => n.title.toLowerCase().includes(q) || n.player.toLowerCase().includes(q));

  let html = '';

  if (matchedPlayers.length > 0) {
    html += '<div class="search-category-title">ATHLETES & PROFILES</div>';
    html += matchedPlayers.slice(0, 4).map(p => `
      <div class="search-result-item" data-view="player-profile" data-player-id="${p.id}" onclick="window.bluelockApp.navigateTo('player-profile', { playerId: '${p.id}' }); window.bluelockApp.closeSearchModal();">
        <img src="${p.image || p.photo}" class="res-thumb" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="result-info">
          <strong class="result-name">${p.name}</strong>
          <span class="result-sub">${p.currentClub} // ${p.position}</span>
        </div>
        <span class="cyan font-mono">${p.marketValue}</span>
      </div>
    `).join('');
  }

  if (matchedClubs.length > 0) {
    html += '<div class="search-category-title">CLUBS & WAR ROOMS</div>';
    html += matchedClubs.slice(0, 3).map(c => `
      <div class="search-result-item" data-view="club-profile" data-club-id="${c.id}" onclick="window.bluelockApp.navigateTo('club-profile', { clubId: '${c.id}' }); window.bluelockApp.closeSearchModal();">
        <img src="${c.badge}" class="res-thumb" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
        <div class="result-info">
          <strong class="result-name">${c.name}</strong>
          <span class="result-sub">${c.league} // ${c.country}</span>
        </div>
        <span class="gold font-mono">${c.squadValue}</span>
      </div>
    `).join('');
  }

  if (matchedNews.length > 0) {
    html += '<div class="search-category-title">NEWS WIRE</div>';
    html += matchedNews.slice(0, 3).map(n => `
      <div class="search-result-item" onclick="window.bluelockApp.openNewsModal('${n.id}'); window.bluelockApp.closeSearchModal();">
        <span class="res-icon">📰</span>
        <div class="result-info">
          <strong class="result-name">${n.title}</strong>
          <span class="result-sub">${n.published} // Source: ${n.source}</span>
        </div>
      </div>
    `).join('');
  }

  if (!html) {
    html = '<div class="search-hint-box"><span>No matching intel records found. Try another query.</span></div>';
  }

  globalSearchResults.innerHTML = html;
}

/**
 * Mobile Drawer & Notifications
 */
function toggleMobileDrawer() {
  if (mobileNavDrawer) mobileNavDrawer.classList.toggle('active');
}
function closeMobileDrawer() {
  if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
}
function toggleNotifModal() {
  if (notifModal) notifModal.classList.toggle('active');
}
function closeNotifModal() {
  if (notifModal) notifModal.classList.remove('active');
}

/**
 * Marquee Ticker Loop
 */
function startHeroTicker() {
  // Built-in CSS keyframe handles smooth 60fps scrolling
}

// Global namespace exposure for inline onclick handlers
window.bluelockApp = {
  navigateTo,
  openNewsModal,
  closeNewsModal,
  openSearchModal,
  closeSearchModal,
  openLegalModal,
  closeLegalModal
};
'''

with open(r"c:\Users\LENOVO\Desktop\web\js\app.js", "w", encoding="utf-8") as f:
    f.write(new_app_js.strip())

print("Created updated js/app.js successfully!")
