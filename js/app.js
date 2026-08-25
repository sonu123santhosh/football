/**
 * BLUELOCK // TRANSFER IQ - Core Application Controller
 * Single-page router, reactive state manager, global search, and interactive controllers.
 */

import { CLUBS, PLAYERS, LIVE_TRANSFERS, TRANSFER_NEWS, DASHBOARD_STATS } from './data.js';
import {
  renderTransferCard,
  renderPlayerCard,
  renderClubCard,
  renderNewsCard,
  renderPlayerProfile,
  renderClubProfile,
  renderTransferMarketTable,
  renderComparisonView,
  getStatusBadge,
  PLAYER_IMG_FALLBACK,
  CLUB_IMG_FALLBACK
} from './components.js';
import { renderRadarChart, renderMarketValueChart } from './chart.js';

// Application State
const state = {
  currentView: 'home', // 'home' | 'transfers' | 'players' | 'clubs' | 'news' | 'market' | 'compare' | 'player-profile' | 'club-profile'
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
}

/**
 * Global Event Listeners
 */
function initEventListeners() {
  // Navigation Bar Links (Desktop & Mobile)
  document.querySelectorAll('[data-view]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const view = btn.getAttribute('data-view');
      navigateTo(view);
      closeMobileDrawer();
    });
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

  // Click Outside Modals
  window.addEventListener('click', (e) => {
    if (e.target === globalSearchModal) closeSearchModal();
    if (e.target === notifModal) closeNotifModal();
  });

  // Delegated Click Handlers for dynamic cards, buttons & tables
  document.addEventListener('click', handleGlobalClicks);
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
    if (e.key === '/' && document.activeElement !== globalSearchInput && !globalSearchModal.classList.contains('active')) {
      e.preventDefault();
      openSearchModal();
    }
    if (e.key === 'Escape') {
      closeSearchModal();
      closeNotifModal();
      closeNewsModal();
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
    default:
      renderHomeView();
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
    <!-- Top Breaking Live Marquee -->
    <div class="bl-ticker-wrapper">
      <div class="ticker-badge">⚡ LIVE RADAR</div>
      <div class="ticker-content-track">
        <div class="ticker-item">BREAKING: Julián Álvarez €90M Formula Talks Accelerate With Barcelona</div>
        <div class="ticker-item">CONFIRMED: Kylian Mbappé Presented at Bernabéu with Number 9</div>
        <div class="ticker-item">BATTLE: Arsenal & Chelsea Submit Bids for Victor Osimhen</div>
        <div class="ticker-item">SCOUTING: Florian Wirtz €150M 2025 War Chest Prepared</div>
      </div>
    </div>

    <!-- Hero Section -->
    <section class="bl-hero-section">
      <div class="hero-bg-grid"></div>
      <div class="hero-glow-orb"></div>
      
      <div class="hero-content">
        <div class="hero-badge-tag">
          <span class="pulse-icon"></span>
          <span>INTELLIGENCE & SCOUTING SYSTEM 2.0</span>
        </div>
        
        <h1 class="hero-main-title">
          THE TRANSFER MARKET<br>
          <span class="hero-gradient-text">IS MOVING.</span>
        </h1>
        
        <p class="hero-subtitle">
          "ENTER THE TRANSFER BATTLEFIELD." Harness ruthless tactical analytics, valuation radars, and Blue Lock scouting algorithms across global football.
        </p>

        <div class="hero-actions-row">
          <button class="bl-btn bl-btn-lg bl-btn-cyber" data-view="transfers">
            <span>EXPLORE LIVE BATTLEFIELD</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
          <button class="bl-btn bl-btn-lg bl-btn-outline" data-view="compare">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>
            <span>EGO CLASH // COMPARE</span>
          </button>
        </div>
      </div>

      <!-- Hero Analytics HUD Cards -->
      <div class="hero-stats-hud">
        <div class="hud-stat-box">
          <span class="hud-stat-lbl">ACTIVE RUMOURS</span>
          <span class="hud-stat-val cyan count-up" data-target="${DASHBOARD_STATS.activeRumours}">${DASHBOARD_STATS.activeRumours}</span>
          <span class="hud-stat-sub">Across Top 5 Leagues</span>
        </div>

        <div class="hud-stat-box">
          <span class="hud-stat-lbl">CONFIRMED DEALS</span>
          <span class="hud-stat-val gold count-up" data-target="${DASHBOARD_STATS.confirmedTransfers}">${DASHBOARD_STATS.confirmedTransfers}</span>
          <span class="hud-stat-sub">Official Signings</span>
        </div>

        <div class="hud-stat-box">
          <span class="hud-stat-lbl">BIGGEST DEAL</span>
          <span class="hud-stat-val white font-sm">${DASHBOARD_STATS.biggestTransfer.player}</span>
          <span class="hud-stat-sub cyan">${DASHBOARD_STATS.biggestTransfer.fee} → ${DASHBOARD_STATS.biggestTransfer.club}</span>
        </div>

        <div class="hud-stat-box">
          <span class="hud-stat-lbl">MOST ACTIVE CLUB</span>
          <span class="hud-stat-val gold font-sm">${DASHBOARD_STATS.mostActiveClub.name}</span>
          <span class="hud-stat-sub">${DASHBOARD_STATS.mostActiveClub.deals} deals // ${DASHBOARD_STATS.mostActiveClub.spend}</span>
        </div>
      </div>
    </section>

    <!-- Section: Live Transfer Feed Spotlight -->
    <section class="bl-dashboard-section">
      <div class="section-header-row">
        <div>
          <h2 class="bl-section-title">
            <span class="title-bracket">[</span>
            LIVE TRANSFER FEED // BREAKING RADAR
            <span class="title-bracket">]</span>
          </h2>
          <p class="section-subtitle">Real-time negotiations, probability meters, and reported valuations.</p>
        </div>
        <button class="bl-btn bl-btn-outline bl-btn-sm" data-view="transfers">
          <span>VIEW ALL TRANSFERS (${LIVE_TRANSFERS.length})</span>
        </button>
      </div>

      <div class="transfer-cards-grid">
        ${topTransfers.map(tr => renderTransferCard(tr)).join('')}
      </div>
    </section>

    <!-- Section: Featured Elite Talents -->
    <section class="bl-dashboard-section">
      <div class="section-header-row">
        <div>
          <h2 class="bl-section-title">
            <span class="title-bracket">[</span>
            SCOUTING HIGHLIGHTS // TOP VALUATIONS
            <span class="title-bracket">]</span>
          </h2>
          <p class="section-subtitle">Tactical profiles, ego ratings, and statistical supremacy.</p>
        </div>
        <button class="bl-btn bl-btn-outline bl-btn-sm" data-view="players">
          <span>ALL PLAYERS (${PLAYERS.length})</span>
        </button>
      </div>

      <div class="player-cards-grid">
        ${topTalents.map(p => renderPlayerCard(p)).join('')}
      </div>
    </section>

    <!-- Section: Transfer Wire News Highlights -->
    <section class="bl-dashboard-section">
      <div class="section-header-row">
        <div>
          <h2 class="bl-section-title">
            <span class="title-bracket">[</span>
            TRANSFER INTELLIGENCE WIRE
            <span class="title-bracket">]</span>
          </h2>
          <p class="section-subtitle">Verified journalism and battlefield briefings.</p>
        </div>
        <button class="bl-btn bl-btn-outline bl-btn-sm" data-view="news">
          <span>VIEW ALL NEWS</span>
        </button>
      </div>

      <div class="news-cards-grid">
        ${hotNews.map(n => renderNewsCard(n)).join('')}
      </div>
    </section>
  `;
}

/**
 * VIEW: LIVE TRANSFER FEED
 */
function renderTransfersFeedView() {
  const filtered = state.transferFilter === 'ALL'
    ? LIVE_TRANSFERS
    : LIVE_TRANSFERS.filter(t => t.status === state.transferFilter);

  const filters = ['ALL', 'CONFIRMED', 'NEGOTIATING', 'RUMOUR', 'LOAN', 'FREE TRANSFER'];

  mainContentEl.innerHTML = `
    <div class="feed-view-header">
      <h1 class="bl-section-title">
        <span class="title-bracket">[</span>
        LIVE TRANSFER FEED
        <span class="title-bracket">]</span>
      </h1>
      <p class="section-subtitle">Real-time scouting telemetry and negotiation confidence meters.</p>
      
      <!-- Filter Chips -->
      <div class="filter-chips-row">
        ${filters.map(f => `
          <button class="bl-chip ${state.transferFilter === f ? 'active' : ''}" data-feed-filter="${f}">
            ${f}
          </button>
        `).join('')}
      </div>
    </div>

    <div class="transfer-cards-grid">
      ${filtered.length > 0 
        ? filtered.map(tr => renderTransferCard(tr)).join('')
        : `<div class="bl-empty-state"><p>No transfers matching filter '${state.transferFilter}'</p></div>`
      }
    </div>
  `;
}

/**
 * VIEW: PLAYERS LIST
 */
function renderPlayersListView() {
  mainContentEl.innerHTML = `
    <div class="feed-view-header">
      <h1 class="bl-section-title">
        <span class="title-bracket">[</span>
        GLOBAL SCOUTING DATABASE // PLAYERS
        <span class="title-bracket">]</span>
      </h1>
      <p class="section-subtitle">Inspect comprehensive ego ratings, season performance, and transfer valuations.</p>
    </div>

    <div class="player-cards-grid">
      ${PLAYERS.map(p => renderPlayerCard(p)).join('')}
    </div>
  `;
}

/**
 * VIEW: CLUBS LIST
 */
function renderClubsListView() {
  mainContentEl.innerHTML = `
    <div class="feed-view-header">
      <h1 class="bl-section-title">
        <span class="title-bracket">[</span>
        WAR ROOM // EUROPEAN POWERHOUSES
        <span class="title-bracket">]</span>
      </h1>
      <p class="section-subtitle">Club transfer budgets, squad valuations, incoming and outgoing dossiers.</p>
    </div>

    <div class="club-cards-grid">
      ${CLUBS.map(c => renderClubCard(c)).join('')}
    </div>
  `;
}

/**
 * VIEW: TRANSFER NEWS
 */
function renderNewsView() {
  const filtered = state.newsFilter === 'ALL'
    ? TRANSFER_NEWS
    : TRANSFER_NEWS.filter(n => n.category === state.newsFilter);

  const categories = ['ALL', 'CONFIRMED', 'RUMOURS', 'NEGOTIATIONS', 'LOANS', 'FREE TRANSFERS'];

  mainContentEl.innerHTML = `
    <div class="feed-view-header">
      <h1 class="bl-section-title">
        <span class="title-bracket">[</span>
        TRANSFER INTELLIGENCE WIRE // NEWS
        <span class="title-bracket">]</span>
      </h1>
      <p class="section-subtitle">Confidential leaks, agent discussions, and official signing alerts.</p>
      
      <div class="filter-chips-row">
        ${categories.map(c => `
          <button class="bl-chip ${state.newsFilter === c ? 'active' : ''}" data-news-filter="${c}">
            ${c}
          </button>
        `).join('')}
      </div>
    </div>

    <div class="news-cards-grid">
      ${filtered.length > 0
        ? filtered.map(n => renderNewsCard(n)).join('')
        : `<div class="bl-empty-state"><p>No news found in category '${state.newsFilter}'</p></div>`
      }
    </div>
  `;
}

/**
 * VIEW: TRANSFER MARKET DATA TABLE
 */
function renderMarketTableView() {
  let list = [...PLAYERS];

  // Filtering
  if (state.marketPositionFilter !== 'ALL') {
    list = list.filter(p => p.position.toLowerCase().includes(state.marketPositionFilter.toLowerCase()));
  }
  if (state.marketStatusFilter !== 'ALL') {
    list = list.filter(p => p.transferStatus === state.marketStatusFilter);
  }
  if (state.marketSearchQuery.trim()) {
    const q = state.marketSearchQuery.toLowerCase();
    list = list.filter(p => p.name.toLowerCase().includes(q) || p.currentClub.toLowerCase().includes(q));
  }

  // Sorting
  list.sort((a, b) => {
    let valA = a[state.marketSortKey];
    let valB = b[state.marketSortKey];

    if (typeof valA === 'string') {
      return state.marketSortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
    }
    return state.marketSortAsc ? valA - valB : valB - valA;
  });

  mainContentEl.innerHTML = `
    <div class="market-view-header">
      <div>
        <h1 class="bl-section-title">
          <span class="title-bracket">[</span>
          TRANSFER MARKET INTELLIGENCE MATRIX
          <span class="title-bracket">]</span>
        </h1>
        <p class="section-subtitle">Interactive sortable and filterable transfer valuation database.</p>
      </div>

      <!-- Controls Row -->
      <div class="market-filters-bar">
        <div class="search-box">
          <input type="text" id="marketTableSearch" class="bl-input" placeholder="Filter player or club..." value="${state.marketSearchQuery}" />
        </div>

        <div class="filter-select-wrap">
          <select id="marketPosSelect" class="bl-select">
            <option value="ALL" ${state.marketPositionFilter === 'ALL' ? 'selected' : ''}>All Positions</option>
            <option value="Forward" ${state.marketPositionFilter === 'Forward' ? 'selected' : ''}>Forwards / Wingers</option>
            <option value="Midfielder" ${state.marketPositionFilter === 'Midfielder' ? 'selected' : ''}>Midfielders</option>
            <option value="Back" ${state.marketPositionFilter === 'Back' ? 'selected' : ''}>Defenders</option>
          </select>
        </div>

        <div class="filter-select-wrap">
          <select id="marketStatusSelect" class="bl-select">
            <option value="ALL" ${state.marketStatusFilter === 'ALL' ? 'selected' : ''}>All Statuses</option>
            <option value="CONFIRMED" ${state.marketStatusFilter === 'CONFIRMED' ? 'selected' : ''}>Confirmed</option>
            <option value="NEGOTIATING" ${state.marketStatusFilter === 'NEGOTIATING' ? 'selected' : ''}>Negotiating</option>
            <option value="RUMOUR" ${state.marketStatusFilter === 'RUMOUR' ? 'selected' : ''}>Rumour</option>
          </select>
        </div>
      </div>
    </div>

    ${renderTransferMarketTable(list, state.marketSortKey, state.marketSortAsc)}
  `;

  // Attach Table Specific Listeners
  const searchInput = document.getElementById('marketTableSearch');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.marketSearchQuery = e.target.value;
      renderMarketTableView();
    });
  }

  const posSelect = document.getElementById('marketPosSelect');
  if (posSelect) {
    posSelect.addEventListener('change', (e) => {
      state.marketPositionFilter = e.target.value;
      renderMarketTableView();
    });
  }

  const statusSelect = document.getElementById('marketStatusSelect');
  if (statusSelect) {
    statusSelect.addEventListener('change', (e) => {
      state.marketStatusFilter = e.target.value;
      renderMarketTableView();
    });
  }

  // Table Headers Sorting
  document.querySelectorAll('.bl-market-datatable th[data-sort]').forEach(th => {
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
 * VIEW: PLAYER COMPARISON
 */
function renderCompareView() {
  const playerA = PLAYERS.find(p => p.id === state.comparePlayerAId) || PLAYERS[0];
  const playerB = PLAYERS.find(p => p.id === state.comparePlayerBId) || PLAYERS[1];

  mainContentEl.innerHTML = renderComparisonView(PLAYERS, playerA, playerB);

  // Render SVG Radar Overlay
  renderRadarChart('comparisonRadarMount', playerA, playerB);

  // Attach Select Changes
  const selectA = document.getElementById('selectPlayerA');
  const selectB = document.getElementById('selectPlayerB');

  if (selectA) {
    selectA.addEventListener('change', (e) => {
      state.comparePlayerAId = e.target.value;
      renderCompareView();
    });
  }

  if (selectB) {
    selectB.addEventListener('change', (e) => {
      state.comparePlayerBId = e.target.value;
      renderCompareView();
    });
  }
}

/**
 * VIEW: DETAILED PLAYER PROFILE
 */
function renderPlayerProfileView() {
  const player = PLAYERS.find(p => p.id === state.selectedPlayerId) || PLAYERS[0];
  mainContentEl.innerHTML = renderPlayerProfile(player);

  // Render Visual Charts
  setTimeout(() => {
    renderRadarChart('playerProfileRadar', player);
    renderMarketValueChart('playerValuationChart', player.valueHistory, player.marketValue);
  }, 50);
}

/**
 * VIEW: DETAILED CLUB PROFILE
 */
function renderClubProfileView() {
  const club = CLUBS.find(c => c.id === state.selectedClubId) || CLUBS[0];
  mainContentEl.innerHTML = renderClubProfile(club);
}

/**
 * Global Delegated Clicks Handler
 */
function handleGlobalClicks(e) {
  // 1. View Player Detail
  const viewPlayerBtn = e.target.closest('.btn-view-player, [data-player-id]');
  if (viewPlayerBtn && !e.target.closest('button:not(.btn-view-player)')) {
    const playerId = viewPlayerBtn.getAttribute('data-player-id');
    if (playerId) {
      navigateTo('player-profile', { playerId });
      return;
    }
  }

  // 2. View Club Detail
  const viewClubBtn = e.target.closest('.btn-view-club, [data-club-id]');
  if (viewClubBtn && !e.target.closest('button:not(.btn-view-club)')) {
    const clubId = viewClubBtn.getAttribute('data-club-id');
    if (clubId) {
      navigateTo('club-profile', { clubId });
      return;
    }
  }

  // 3. Read News Modal
  const readNewsBtn = e.target.closest('.btn-read-news, [data-news-id]');
  if (readNewsBtn) {
    const newsId = readNewsBtn.getAttribute('data-news-id');
    openNewsModal(newsId);
    return;
  }

  // 4. Quick Compare from Profile
  const compareBtn = e.target.closest('.btn-quick-compare');
  if (compareBtn) {
    const pId = compareBtn.getAttribute('data-compare-id');
    const otherPlayer = PLAYERS.find(p => p.id !== pId) || PLAYERS[0];
    navigateTo('compare', { compareA: pId, compareB: otherPlayer.id });
    return;
  }

  // 5. Back Navigation Buttons
  if (e.target.closest('.btn-back-dashboard')) {
    navigateTo('home');
    return;
  }
  if (e.target.closest('.btn-back-clubs')) {
    navigateTo('clubs');
    return;
  }

  // 6. Feed Filters
  const feedFilterBtn = e.target.closest('[data-feed-filter]');
  if (feedFilterBtn) {
    state.transferFilter = feedFilterBtn.getAttribute('data-feed-filter');
    renderTransfersFeedView();
    return;
  }

  // 7. News Filters
  const newsFilterBtn = e.target.closest('[data-news-filter]');
  if (newsFilterBtn) {
    state.newsFilter = newsFilterBtn.getAttribute('data-news-filter');
    renderNewsView();
    return;
  }
}

/**
 * GLOBAL SEARCH SYSTEM
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
  if (globalSearchModal) {
    globalSearchModal.classList.remove('active');
  }
}

function handleGlobalSearchInput() {
  const query = (globalSearchInput ? globalSearchInput.value : '').trim().toLowerCase();
  
  if (!query) {
    globalSearchResults.innerHTML = `
      <div class="search-suggest-box">
        <span class="suggest-title">POPULAR SCOUTING SEARCHES:</span>
        <div class="suggest-tags">
          <button class="suggest-tag-btn" onclick="document.getElementById('globalSearchInput').value='Mbappé'; document.getElementById('globalSearchInput').dispatchEvent(new Event('input'));">Kylian Mbappé</button>
          <button class="suggest-tag-btn" onclick="document.getElementById('globalSearchInput').value='Barcelona'; document.getElementById('globalSearchInput').dispatchEvent(new Event('input'));">FC Barcelona</button>
          <button class="suggest-tag-btn" onclick="document.getElementById('globalSearchInput').value='Alvarez'; document.getElementById('globalSearchInput').dispatchEvent(new Event('input'));">Julián Álvarez</button>
          <button class="suggest-tag-btn" onclick="document.getElementById('globalSearchInput').value='Osimhen'; document.getElementById('globalSearchInput').dispatchEvent(new Event('input'));">Victor Osimhen</button>
        </div>
      </div>
    `;
    return;
  }

  const matchingPlayers = PLAYERS.filter(p => p.name.toLowerCase().includes(query) || p.currentClub.toLowerCase().includes(query) || p.nationality.toLowerCase().includes(query));
  const matchingClubs = CLUBS.filter(c => c.name.toLowerCase().includes(query) || c.league.toLowerCase().includes(query) || c.country.toLowerCase().includes(query));
  const matchingNews = TRANSFER_NEWS.filter(n => n.title.toLowerCase().includes(query) || n.player.toLowerCase().includes(query));

  let resultsHtml = '';

  // Players
  if (matchingPlayers.length > 0) {
    resultsHtml += `
      <div class="search-category-group">
        <h4 class="category-header">PLAYERS (${matchingPlayers.length})</h4>
        <div class="search-items-list">
          ${matchingPlayers.map(p => `
            <div class="search-result-item" data-player-id="${p.id}" onclick="window.bluelockApp.selectSearchResult('player', '${p.id}')">
              <img src="${p.image || p.photo}" alt="${p.name}" class="result-thumb" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
              <div class="result-info">
                <strong class="result-name">${p.name}</strong>
                <span class="result-sub">${p.currentClub} // ${p.position} // Valuation: <strong class="cyan">${p.marketValue}</strong></span>
              </div>
              <span class="result-ego-badge">EGO ${p.egoRating}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Clubs
  if (matchingClubs.length > 0) {
    resultsHtml += `
      <div class="search-category-group">
        <h4 class="category-header">CLUBS (${matchingClubs.length})</h4>
        <div class="search-items-list">
          ${matchingClubs.map(c => `
            <div class="search-result-item" data-club-id="${c.id}" onclick="window.bluelockApp.selectSearchResult('club', '${c.id}')">
              <img src="${c.badge}" alt="${c.name}" class="result-thumb" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
              <div class="result-info">
                <strong class="result-name">${c.name} ${c.flag}</strong>
                <span class="result-sub">${c.league} // Budget: <strong class="gold">${c.transferBudget}</strong></span>
              </div>
              <span class="result-ego-badge">${c.egoRank}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // News
  if (matchingNews.length > 0) {
    resultsHtml += `
      <div class="search-category-group">
        <h4 class="category-header">INTELLIGENCE WIRE (${matchingNews.length})</h4>
        <div class="search-items-list">
          ${matchingNews.map(n => `
            <div class="search-result-item" onclick="window.bluelockApp.openNewsModal('${n.id}')">
              <div class="result-info">
                <strong class="result-name">${n.title}</strong>
                <span class="result-sub">${n.published} // Focus: <strong class="cyan">${n.player}</strong></span>
              </div>
              ${getStatusBadge(n.status)}
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  if (!matchingPlayers.length && !matchingClubs.length && !matchingNews.length) {
    resultsHtml = `
      <div class="bl-empty-state">
        <p>No scouting intel matches found for "<strong>${query}</strong>"</p>
      </div>
    `;
  }

  globalSearchResults.innerHTML = resultsHtml;
}

/**
 * Mobile Drawer
 */
function toggleMobileDrawer() {
  if (mobileNavDrawer) mobileNavDrawer.classList.toggle('active');
}
function closeMobileDrawer() {
  if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
}

/**
 * Notifications Modal
 */
function toggleNotifModal() {
  if (notifModal) notifModal.classList.toggle('active');
}
function closeNotifModal() {
  if (notifModal) notifModal.classList.remove('active');
}

/**
 * News Article Reader Modal
 */
function openNewsModal(newsId) {
  const article = TRANSFER_NEWS.find(n => n.id === newsId) || TRANSFER_NEWS[0];
  const modalEl = document.getElementById('newsModal');
  const modalBody = document.getElementById('newsModalBody');

  if (modalEl && modalBody) {
    modalBody.innerHTML = `
      <div class="news-modal-content">
        <div class="news-modal-img-wrap">
          <img src="${article.image}" alt="${article.title}" class="news-modal-banner" />
          <div class="news-modal-badge">${article.category}</div>
        </div>

        <div class="news-modal-header">
          <div class="news-meta-line">
            <span class="source-tag">${article.source}</span>
            <span class="time-tag">${article.published}</span>
            <span class="impact-tag cyan">${article.egoImpact}</span>
          </div>
          <h2 class="modal-news-title">${article.title}</h2>
        </div>

        <div class="modal-news-body">
          <p class="lead-paragraph">${article.summary}</p>
          <div class="full-content-text">${article.content}</div>
        </div>

        <div class="modal-news-footer">
          <div class="related-tags">
            <span class="tag-label">INVOLVED CLUBS:</span>
            ${article.clubs.map(c => `<span class="club-chip">${c}</span>`).join('')}
          </div>
          <button class="bl-btn bl-btn-cyber bl-btn-sm" onclick="window.bluelockApp.navigateTo('player-profile', { playerId: '${article.playerId}' }); window.bluelockApp.closeNewsModal();">
            <span>INSPECT ${article.player.toUpperCase()}</span>
          </button>
        </div>
      </div>
    `;
    modalEl.classList.add('active');
  }
}

function closeNewsModal() {
  const modalEl = document.getElementById('newsModal');
  if (modalEl) modalEl.classList.remove('active');
}

/**
 * Hero Ticker Auto-scroll
 */
function startHeroTicker() {
  // Visual subtle ticker animations are controlled via CSS keyframes
}

// Expose app handlers to window for inline HTML onclick helpers
window.bluelockApp = {
  navigateTo,
  selectSearchResult: (type, id) => {
    closeSearchModal();
    if (type === 'player') navigateTo('player-profile', { playerId: id });
    if (type === 'club') navigateTo('club-profile', { clubId: id });
  },
  openNewsModal: (id) => {
    closeSearchModal();
    openNewsModal(id);
  },
  closeNewsModal
};
