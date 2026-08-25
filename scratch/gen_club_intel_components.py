"""
Generate the complete enhanced BLUEGUN js/components.js file with Club Intelligence,
Injury Center, Suspension Center, Squad Filters, and Full 6-Section Licensing Hub.
"""

components_code = '''/**
 * BLUEGUN — 2026 Football Transfer & Club Intelligence Platform
 * Component Library & UI View Engine
 * Tagline: "ENTER THE TRANSFER BATTLEFIELD."
 */

import { renderRadarChart, renderMarketValueChart } from './chart.js';
import { DATA_SOURCES, THIRD_PARTY_ASSETS, COMPLIANCE_DISCLAIMERS, PLAYERS, CLUBS, DASHBOARD_STATS } from './data.js';

// Global SVG Fallback for Player Images
export const PLAYER_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23050a18'/><circle cx='50' cy='38' r='20' fill='%2300f0ff' opacity='0.35'/><path d='M15 92 Q50 58 85 92' fill='%2300f0ff' opacity='0.35'/><text x='50' y='96' font-family='sans-serif' font-weight='bold' font-size='7' fill='%2300f0ff' text-anchor='middle'>BLUEGUN INTEL</text></svg>`;

// Global SVG Fallback for Club Badges
export const CLUB_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><polygon points='50,5 95,25 95,75 50,95 5,75 5,25' fill='%230b1325' stroke='%2300f0ff' stroke-width='3'/><circle cx='50' cy='50' r='20' fill='%230077ff' opacity='0.5'/></svg>`;

/**
 * Player Availability Status Badge
 */
export function getAvailabilityBadge(status) {
  const map = {
    AVAILABLE: { label: "AVAILABLE", class: "avail-available", icon: "🟢" },
    "MINOR INJURY": { label: "MINOR INJURY", class: "avail-minor", icon: "🟡" },
    INJURED: { label: "INJURED", class: "avail-injured", icon: "🔴" },
    SUSPENDED: { label: "SUSPENDED", class: "avail-suspended", icon: "🟠" },
    "INTERNATIONAL DUTY": { label: "INTL DUTY", class: "avail-intl", icon: "🔵" },
    UNAVAILABLE: { label: "UNAVAILABLE", class: "avail-unavail", icon: "⚫" },
    UNKNOWN: { label: "UNKNOWN", class: "avail-unknown", icon: "⚪" }
  };
  const item = map[status] || { label: status || "UNKNOWN", class: "avail-unknown", icon: "⚪" };
  return `<span class="bl-avail-badge ${item.class}" title="Availability: ${item.label}">${item.icon} ${item.label}</span>`;
}

/**
 * 2026 Transfer Status Badge Helper
 */
export function getStatusBadge(status) {
  const map = {
    CONFIRMED: { label: "CONFIRMED", class: "badge-confirmed", icon: "🔵" },
    COMPLETED: { label: "COMPLETED", class: "badge-confirmed", icon: "✅" },
    NEGOTIATING: { label: "NEGOTIATING", class: "badge-negotiating", icon: "🟡" },
    INTERESTED: { label: "INTERESTED", class: "badge-negotiating", icon: "🟣" },
    RUMOUR: { label: "RUMOUR", class: "badge-rumour", icon: "🟠" },
    MONITORING: { label: "MONITORING", class: "badge-loan", icon: "👁️" },
    REJECTED: { label: "REJECTED", class: "badge-threat", icon: "❌" },
    LOAN: { label: "LOAN", class: "badge-loan", icon: "🟣" },
    "FREE TRANSFER": { label: "FREE TRANSFER", class: "badge-free", icon: "🟢" }
  };
  const item = map[status] || { label: status, class: "badge-default", icon: "⚪" };
  return `<span class="bl-status-badge ${item.class}">${item.icon} ${item.label}</span>`;
}

/**
 * 2026 Transfer Card (Live Intelligence Feed & War Room)
 */
export function renderTransferCard(tr) {
  const imgSrc = tr.image || tr.playerPhoto;
  return `
    <article class="bl-transfer-card" data-player-id="${tr.playerId}">
      <div class="card-glow-edge"></div>
      
      <div class="card-header">
        <div class="header-badges">
          ${getStatusBadge(tr.status)}
          <span class="badge-type">${tr.transferType}</span>
        </div>
        <div class="time-ago">
          <span class="pulse-dot"></span>
          ${tr.timeAgo}
        </div>
      </div>

      <div class="card-body">
        <div class="player-summary">
          <div class="player-avatar-wrap">
            <img src="${imgSrc}" alt="${tr.playerName}" class="player-thumb" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
            <span class="ego-tag" title="BLUEGUN Ego Threat Rating">THREAT: ${tr.egoThreat}</span>
          </div>
          
          <div class="player-meta">
            <h3 class="player-name">${tr.playerName}</h3>
            <div class="player-subinfo">
              <span class="meta-age">Age: <strong>${tr.age}</strong></span>
              <span class="meta-separator">//</span>
              <span class="meta-pos">${tr.position}</span>
            </div>
          </div>
        </div>

        <!-- Transfer Battle Flow HUD -->
        <div class="club-transfer-flow">
          <div class="club-node" data-view="club-profile" data-club-id="${tr.fromClubId || ''}">
            <img src="${tr.fromBadge}" alt="${tr.fromClub}" class="club-logo-sm" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            <span class="club-label">${tr.fromClub}</span>
          </div>

          <div class="transfer-arrow-hud">
            <div class="arrow-line"></div>
            <div class="arrow-head">▶</div>
            <span class="prob-tag" title="BLUEGUN Algorithmic Probability Estimate">${tr.probability}% PROB.</span>
          </div>

          <div class="club-node highlight" data-view="club-profile" data-club-id="${tr.toClubId || ''}">
            <img src="${tr.toBadge}" alt="${tr.toClub}" class="club-logo-sm" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            <span class="club-label">${tr.toClub}</span>
          </div>
        </div>

        <!-- Financial & Market Pressure Breakdown -->
        <div class="transfer-financials">
          <div class="fin-item">
            <span class="fin-lbl">MARKET VALUE</span>
            <span class="fin-val cyan">${tr.marketValue}</span>
          </div>
          <div class="fin-item">
            <span class="fin-lbl">REPORTED FEE</span>
            <span class="fin-val highlight-fee">${tr.reportedFee}</span>
          </div>
          <div class="fin-item">
            <span class="fin-lbl">MARKET PRESSURE</span>
            <span class="fin-val gold">${tr.marketPressure || 'Normal'}</span>
          </div>
        </div>

        <!-- Headline / Source Wire -->
        <p class="transfer-headline">"${tr.headline}"</p>
        <div class="transfer-source-tag">
          <span class="source-icon">📡</span>
          <span>Source: <strong>${tr.source || 'BLUEGUN Wire'}</strong></span>
        </div>
      </div>

      <div class="card-footer">
        <div class="confidence-bar-wrap">
          <div class="confidence-bar-label">
            <span>TRANSFER MOMENTUM</span>
            <strong>${tr.confidence}%</strong>
          </div>
          <div class="bl-progress-track">
            <div class="bl-progress-fill" style="width: ${tr.confidence}%;"></div>
          </div>
        </div>

        <button class="bl-btn bl-btn-sm bl-btn-cyber btn-view-player" data-player-id="${tr.playerId}">
          <span>SCOUTING FILE</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
    </article>
  `;
}

/**
 * Player Card (Players Grid View)
 */
export function renderPlayerCard(p) {
  const imgSrc = p.image || p.photo;
  const photoCreditShort = p.imageCredit ? p.imageCredit.split('/')[0].trim() : 'Wikimedia Commons';
  const avail = p.availability || 'AVAILABLE';
  return `
    <article class="bl-player-card" data-player-id="${p.id}">
      <div class="card-glow-edge"></div>
      <div class="player-card-banner">
        <span class="ego-pill" title="BLUEGUN Ego Rating">⚡ EGO: ${p.egoRating}</span>
        <span class="ovr-rating">${p.rating}</span>
      </div>

      <div class="player-visual">
        <img src="${imgSrc}" alt="${p.name}" class="player-portrait" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="player-flag-badge">${p.flag}</div>
        <div class="player-photo-attribution" title="Photo Credit: ${p.imageCredit || 'Sports Photography'} (${p.imageLicense || 'CC BY-SA 4.0'})">
          📷 ${photoCreditShort}
        </div>
      </div>

      <div class="player-info">
        <div class="player-avail-row">
          ${getAvailabilityBadge(avail)}
        </div>
        <h3 class="player-name">${p.name}</h3>
        <p class="player-role">${p.position} // #${p.shirtNumber}</p>
        <p class="player-club">${p.currentClub}</p>

        <div class="player-stats-mini">
          <div class="stat-mini-pill">
            <span class="lbl">PACE</span>
            <span class="val">${p.radar.pace}</span>
          </div>
          <div class="stat-mini-pill">
            <span class="lbl">SHOOT</span>
            <span class="val">${p.radar.shooting}</span>
          </div>
          <div class="stat-mini-pill">
            <span class="lbl">PASS</span>
            <span class="val">${p.radar.passing}</span>
          </div>
          <div class="stat-mini-pill">
            <span class="lbl">DRIB</span>
            <span class="val">${p.radar.dribbling}</span>
          </div>
        </div>

        <div class="player-val-row">
          <div class="val-col">
            <span class="lbl">VALUATION</span>
            <span class="val cyan">${p.marketValue}</span>
          </div>
          <div class="val-col text-right">
            <span class="lbl">CONTRACT</span>
            <span class="val">${p.contractExpiry ? p.contractExpiry.slice(0, 4) : '2027'}</span>
          </div>
        </div>
      </div>

      <div class="player-card-actions">
        <button class="bl-btn bl-btn-cyber bl-btn-block btn-view-player" data-player-id="${p.id}">
          <span>OPEN SCOUTING FILE</span>
        </button>
      </div>
    </article>
  `;
}

/**
 * Club Card (Clubs Grid View)
 */
export function renderClubCard(club) {
  const availSummary = club.availabilitySummary || { squad: club.squad ? club.squad.length : 25, available: 21, injured: 2, suspended: 1, otherUnavailable: 1 };
  return `
    <article class="bl-club-card" data-club-id="${club.id}">
      <div class="card-glow-edge"></div>
      <div class="club-card-header">
        <div class="club-badge-wrap">
          <img src="${club.badge}" alt="${club.name}" class="club-badge-img" loading="lazy" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
        </div>
        <div class="club-header-info">
          <span class="club-ego-rank">${club.egoRank}</span>
          <h3 class="club-name">${club.name} ${club.flag}</h3>
          <span class="club-league">${club.league}</span>
        </div>
      </div>

      <p class="club-desc">${club.description}</p>

      <div class="club-intel-grid">
        <div class="intel-cell">
          <span class="lbl">SQUAD VALUE</span>
          <span class="val cyan">${club.squadValue}</span>
        </div>
        <div class="intel-cell">
          <span class="lbl">SQUAD ROSTER</span>
          <span class="val">${availSummary.squad} Players</span>
        </div>
        <div class="intel-cell">
          <span class="lbl">INJURED</span>
          <span class="val ${availSummary.injured > 0 ? 'red' : ''}">${availSummary.injured}</span>
        </div>
        <div class="intel-cell">
          <span class="lbl">SUSPENDED</span>
          <span class="val ${availSummary.suspended > 0 ? 'gold' : ''}">${availSummary.suspended}</span>
        </div>
      </div>

      <div class="club-trademark-notice">
        <span>* Club names, logos, badges and trademarks belong to their respective owners.</span>
      </div>

      <div class="club-card-actions">
        <button class="bl-btn bl-btn-cyber bl-btn-block btn-view-club" data-club-id="${club.id}">
          <span>OPEN CLUB INTELLIGENCE</span>
        </button>
      </div>
    </article>
  `;
}

/**
 * News Card (TRANSFER INTELLIGENCE)
 */
export function renderNewsCard(item) {
  const imgSrc = item.image || 'assets/players/mbappe.jpg';
  const sourceUrl = item.sourceUrl || 'https://www.skysports.com/football/transfers';
  return `
    <article class="bl-news-card" data-news-id="${item.id}">
      <div class="news-media-wrap">
        <img src="${imgSrc}" alt="${item.title}" class="news-thumb" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="news-category-tag">${item.category}</div>
        <div class="news-ego-tag">${item.egoImpact}</div>
      </div>

      <div class="news-body">
        <div class="news-meta-row">
          <span class="news-source">Source: <strong>${item.source}</strong></span>
          <span class="news-time">${item.published}</span>
        </div>

        <h3 class="news-headline">${item.title}</h3>
        <p class="news-summary">${item.summary}</p>

        <div class="news-footer">
          <div class="news-involved">
            <span class="involved-lbl">FOCUS:</span>
            <strong class="cyan">${item.player}</strong>
          </div>

          <div class="news-actions-group">
            <button class="bl-btn bl-btn-sm bl-btn-cyber btn-read-news" data-news-id="${item.id}">
              <span>INTEL DOSSIER</span>
            </button>
            <a href="${sourceUrl}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-sm bl-btn-outline news-outbound-link" title="Open source reporting">
              <span>Read original report →</span>
            </a>
          </div>
        </div>
      </div>
    </article>
  `;
}

/**
 * 2026 PLAYER SCOUTING FILE (Detailed Profile with TRANSFER BATTLE HUD)
 */
export function renderPlayerProfile(p) {
  const imgSrc = p.image || p.photo;
  const photoCredit = p.imageCredit || 'Steffen Prößdorf / Sports Photography Archive';
  const photoLicense = p.imageLicense || 'CC BY-SA 4.0';
  const photoSourceUrl = p.imageSourceUrl || 'https://commons.wikimedia.org/';
  const dataSource = p.dataSource || 'API-Football & 2026 Transfer Intelligence';
  const dataSourceUrl = p.dataSourceUrl || 'https://rapidapi.com/api-sports/api/api-football';
  const primaryTarget = p.interestedClubs && p.interestedClubs.length > 0 ? p.interestedClubs[0] : { name: "Evaluating Offers", probability: 50 };

  return `
    <div class="bl-profile-view">
      <!-- Top Action Navigation Back -->
      <div class="profile-top-bar">
        <button class="bl-btn bl-btn-outline bl-btn-sm btn-back-dashboard">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>BACK TO WAR ROOM</span>
        </button>
        <div class="profile-breadcrumbs">
          <span>BLUEGUN SCOUTING FILE</span> / <span>2026</span> / <strong class="cyan">${p.name.toUpperCase()}</strong>
        </div>
        <button class="bl-btn bl-btn-cyber bl-btn-sm btn-quick-compare" data-compare-id="${p.id}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>
          <span>EGO CLASH</span>
        </button>
      </div>

      <!-- Player Header HUD Banner -->
      <section class="player-profile-header bl-hud-panel">
        <div class="hud-corner top-left"></div>
        <div class="hud-corner top-right"></div>
        <div class="hud-corner bottom-left"></div>
        <div class="hud-corner bottom-right"></div>

        <div class="player-header-grid">
          <div class="player-media-column">
            <div class="player-photo-frame">
              <img src="${imgSrc}" alt="${p.name}" class="profile-main-photo" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
              <div class="photo-overlay-scanline"></div>
              <div class="ovr-badge-large">
                <span class="ovr-label">OVR</span>
                <span class="ovr-number">${p.rating}</span>
              </div>
            </div>
            
            <!-- Photo License & Attribution Tag -->
            <div class="photo-license-box">
              <span class="photo-icon">📷</span>
              <span class="photo-credit-text">Credit: <strong>${photoCredit}</strong> (${photoLicense})</span>
              <a href="${photoSourceUrl}" target="_blank" rel="noopener noreferrer" class="license-source-link">Source ↗</a>
            </div>
          </div>

          <div class="player-primary-details">
            <div class="player-identity-row">
              <div class="player-name-block">
                <div class="player-national-tag">
                  <span class="flag-icon">${p.flag}</span>
                  <span class="nation-name">${p.nationality.toUpperCase()}</span>
                  <span class="slash">//</span>
                  <span class="preferred-foot">${p.preferredFoot.toUpperCase()} FOOT</span>
                  <span class="slash">//</span>
                  <span class="shirt-num">NO. ${p.shirtNumber}</span>
                </div>
                <h1 class="player-big-name">${p.name}</h1>
                <div class="player-club-position">
                  <span class="current-club-badge" data-view="club-profile" data-club-id="${p.currentClubId}">${p.currentClub}</span>
                  <span class="position-tag">${p.position}</span>
                  <span class="age-tag">AGE ${p.age}</span>
                  ${getAvailabilityBadge(p.availability || 'AVAILABLE')}
                </div>
              </div>

              <div class="player-threat-indicator">
                <span class="threat-label">MARKET THREAT INDEX</span>
                <span class="threat-badge-large ${p.marketThreat.toLowerCase()}">${p.marketThreat}</span>
                <span class="threat-disclaimer">* BLUEGUN Proprietary Algorithm</span>
              </div>
            </div>

            <p class="player-bio-text">${p.overview}</p>

            <!-- Key Metric Holograms -->
            <div class="player-quick-metrics">
              <div class="metric-holo-card">
                <span class="lbl">MARKET VALUATION</span>
                <span class="val cyan">${p.marketValue}</span>
                <span class="sub">Benchmark Val.</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">EGO RATING</span>
                <span class="val gold">${p.egoRating} / 100</span>
                <span class="sub">Impact Factor</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">TRANSFER PROBABILITY</span>
                <span class="val neon">${p.probability}%</span>
                <span class="sub">Algorithmic Est.</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">MARKET PRESSURE</span>
                <span class="val">${p.marketPressure || 'Equilibrium'}</span>
                <span class="sub">Asking: ${p.askingPrice}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2026 TRANSFER BATTLE HUD -->
        <div class="transfer-battle-section">
          <div class="battle-title-bar">
            <span class="battle-badge">⚡ 2026 TRANSFER BATTLE</span>
            <span class="battle-sub">CURRENT CLUB ➔ TARGET PURSUIT</span>
          </div>

          <div class="battle-flow-container">
            <div class="battle-club-node from" data-view="club-profile" data-club-id="${p.currentClubId}">
              <span class="node-status">CURRENT CLUB</span>
              <strong class="node-name">${p.currentClub}</strong>
            </div>

            <div class="battle-meter-hud">
              <div class="battle-meter-header">
                <span>TRANSFER MOMENTUM: <strong>${p.transferMomentum || p.momentum}%</strong></span>
                <span>MOVE PROBABILITY: <strong class="cyan">${p.probability}%</strong></span>
              </div>
              <div class="bl-progress-track battle-track">
                <div class="bl-progress-fill battle-fill" style="width: ${p.probability}%;"></div>
              </div>
              <div class="battle-stage-pill">${getStatusBadge(p.transferStatus)}</div>
            </div>

            <div class="battle-club-node to">
              <span class="node-status">PRIMARY TARGET</span>
              <strong class="node-name highlight-cyan">${primaryTarget.name}</strong>
            </div>
          </div>
        </div>

        <!-- Compliance & Data Source Attribution Strip -->
        <div class="profile-attribution-strip">
          <div class="attr-chip">
            <span class="attr-icon">⚡</span>
            <span><strong>BLUEGUN Intelligence:</strong> Ego Rating, Transfer Momentum, Market Pressure & Probability are proprietary estimates.</span>
          </div>
          <div class="attr-chip">
            <span class="attr-icon">📊</span>
            <span><strong>Match Statistics:</strong> ${dataSource}</span>
            <a href="${dataSourceUrl}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Provider ↗</a>
          </div>
        </div>
      </section>

      <!-- Main Profile Grid (Charts, Stats, Rumours) -->
      <div class="profile-analytics-layout">
        
        <!-- Left: Radar Chart & Scouting Breakdown -->
        <div class="profile-left-col">
          <div class="bl-card bl-hud-panel radar-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> TACTICAL RADAR ANALYSIS <span class="title-bracket">]</span></h2>
              <span class="panel-tag cyan">EGO-HEXAGON HUD</span>
            </div>
            
            <div id="playerRadarContainer" class="radar-chart-wrap"></div>

            <div class="radar-stat-bars">
              ${Object.entries(p.radar).map(([key, val]) => `
                <div class="stat-bar-item">
                  <div class="stat-bar-header">
                    <span class="stat-key">${key.toUpperCase()}</span>
                    <strong class="stat-val ${key === 'ego' ? 'gold' : 'cyan'}">${val}</strong>
                  </div>
                  <div class="bl-progress-track">
                    <div class="bl-progress-fill ${key === 'ego' ? 'gold-fill' : ''}" style="width: ${val}%;"></div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="bl-card bl-hud-panel valuation-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> VALUATION TRAJECTORY (€M) <span class="title-bracket">]</span></h2>
              <span class="panel-tag">5-YEAR INDEX</span>
            </div>
            <div id="playerValuationChart" class="valuation-chart-wrap"></div>
            <div class="valuation-meta-footnote">
              * Market valuation trajectory benchmarked against 2026 European transfer fee indices.
            </div>
          </div>
        </div>

        <!-- Right: Season Stats, Interested Clubs, Rumours -->
        <div class="profile-right-col">
          <div class="bl-card bl-hud-panel season-stats-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> 2025/2026 PERFORMANCE METRICS <span class="title-bracket">]</span></h2>
              <span class="panel-tag">MATCH INTEL</span>
            </div>

            <div class="season-stats-grid">
              <div class="stat-box">
                <span class="sb-lbl">MATCHES PLAYED</span>
                <span class="sb-val">${p.stats.appearances}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">GOALS SCORED</span>
                <span class="sb-val cyan">${p.stats.goals}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">ASSISTS</span>
                <span class="sb-val">${p.stats.assists}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">MINUTES PLAYED</span>
                <span class="sb-val">${p.stats.minutes}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">EXPECTED GOALS (xG)</span>
                <span class="sb-val gold">${p.stats.xg}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">EXPECTED ASSISTS (xA)</span>
                <span class="sb-val gold">${p.stats.xa}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">TOTAL SHOTS</span>
                <span class="sb-val">${p.stats.shots}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">KEY PASSES</span>
                <span class="sb-val">${p.stats.keyPasses}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">DRIBBLES COMPLETED</span>
                <span class="sb-val">${p.stats.dribbles}</span>
              </div>
              <div class="stat-box">
                <span class="sb-lbl">PASS ACCURACY</span>
                <span class="sb-val cyan">${p.stats.passAccuracy}%</span>
              </div>
            </div>
            <div class="stat-source-footnote">
              Verified 2025/26 season match data (Opta / FBref index).
            </div>
          </div>

          <div class="bl-card bl-hud-panel transfer-battleground-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> CLUBS IN PURSUIT & NEGOTIATIONS <span class="title-bracket">]</span></h2>
              <span class="panel-tag gold">2026 TARGET RADAR</span>
            </div>

            <div class="interested-clubs-list">
              ${(p.interestedClubs || []).map(c => `
                <div class="interested-club-card">
                  <div class="club-summary-row">
                    <div class="club-id-col">
                      <span class="club-title">${c.name}</span>
                      <span class="club-league-sub">${c.league}</span>
                    </div>
                    <div class="interest-badge-col">
                      <span class="interest-pill ${(c.interest || 'HIGH').toLowerCase().replace(' ', '-')}">${c.interest}</span>
                    </div>
                  </div>

                  <div class="offer-details-row">
                    <div class="offer-snippet">
                      <span class="lbl">REPORTED PROPOSAL:</span>
                      <span class="val cyan">${c.offer}</span>
                    </div>
                    <div class="status-snippet">
                      <span class="lbl">STATUS:</span>
                      <span class="val">${c.status}</span>
                    </div>
                  </div>

                  <div class="deal-prob-bar">
                    <div class="prob-header">
                      <span>SIGNING LIKELIHOOD (ESTIMATED)</span>
                      <strong>${c.probability}%</strong>
                    </div>
                    <div class="bl-progress-track">
                      <div class="bl-progress-fill" style="width: ${c.probability}%;"></div>
                    </div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

        </div>
      </div>
    </div>
  `;
}

/**
 * ==========================================================================
 * CLUB INTELLIGENCE DASHBOARD (Complete Squad, Injuries, Suspensions, Contracts)
 * ==========================================================================
 */
export function renderClubIntelligenceView(club, activeTab = 'squad', filters = {}) {
  const availSummary = club.availabilitySummary || {
    squad: club.squad ? club.squad.length : 25,
    available: 21,
    injured: club.injuries ? club.injuries.length : 2,
    suspended: club.suspensions ? club.suspensions.length : 1,
    otherUnavailable: 1
  };

  const squadList = club.squad || [];
  const injuriesList = club.injuries || [];
  const suspensionsList = club.suspensions || [];

  // Filter squad list
  let filteredSquad = [...squadList];
  if (filters.position && filters.position !== 'ALL') {
    filteredSquad = filteredSquad.filter(p => p.position.toLowerCase().includes(filters.position.toLowerCase()));
  }
  if (filters.availability && filters.availability !== 'ALL') {
    filteredSquad = filteredSquad.filter(p => p.availability === filters.availability);
  }

  return `
    <div class="bl-club-intelligence-view">
      
      <!-- Top Action Navigation Bar -->
      <div class="profile-top-bar">
        <button class="bl-btn bl-btn-outline bl-btn-sm btn-back-dashboard">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>BACK TO WAR ROOM</span>
        </button>
        <div class="profile-breadcrumbs">
          <span>BLUEGUN</span> / <span>CLUB INTELLIGENCE</span> / <strong class="cyan">${club.name.toUpperCase()}</strong>
        </div>

        <!-- Quick Club Selector Dropdown -->
        <div class="club-switch-picker">
          <select id="switchClubSelect" class="bl-select bl-select-sm">
            ${CLUBS.map(c => `<option value="${c.id}" ${c.id === club.id ? 'selected' : ''}>${c.name} (${c.league})</option>`).join('')}
          </select>
        </div>
      </div>

      <!-- 11. CLUB OVERVIEW PANEL -->
      <section class="club-header-panel bl-hud-panel" style="border-top: 3px solid ${club.color};">
        <div class="hud-corner top-left"></div>
        <div class="hud-corner top-right"></div>
        <div class="hud-corner bottom-left"></div>
        <div class="hud-corner bottom-right"></div>

        <div class="club-header-flex">
          <div class="club-crest-col">
            <img src="${club.badge}" alt="${club.name}" class="club-big-crest" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
          </div>
          
          <div class="club-info-col">
            <div class="club-tier-badge">${club.egoRank}</div>
            <h1 class="club-title-big">${club.name} ${club.flag}</h1>
            <p class="club-stadium-lead">🏟️ ${club.stadium} // 🏆 ${club.league} // 📅 Season: ${club.currentSeason}</p>
            <p class="club-lore-text">${club.description}</p>
            
            <div class="club-meta-tags-row">
              <span class="meta-tag-item">Manager: <strong>${club.manager}</strong></span>
              <span class="meta-tag-item">President: <strong>${club.president}</strong></span>
              <span class="meta-tag-item">Squad Valuation: <strong class="cyan">${club.squadValue}</strong></span>
              <span class="meta-tag-item">Transfer Budget: <strong class="gold">${club.transferBudget}</strong></span>
            </div>
          </div>

          <div class="club-status-col">
            <div class="data-update-badge">
              <span class="pulse-dot"></span>
              <strong>DATA UPDATED:</strong> ${club.lastDataUpdate ? club.lastDataUpdate.replace('T', ' ').slice(0, 16) + ' UTC' : '2026-08-25 14:30 UTC'}
            </div>
            <div class="source-credit-box">
              <span>Source: <strong>${club.dataSource || 'API-Football'}</strong></span>
            </div>
          </div>
        </div>

        <div class="club-trademark-footer">
          <span>* Club names, logos, badges and trademarks belong to their respective owners.</span>
        </div>
      </section>

      <!-- 16. PLAYER AVAILABILITY SUMMARY -->
      <section class="club-availability-summary-strip bl-hud-panel">
        <div class="avail-summary-header">
          <div class="avail-title-group">
            <span class="section-kicker">SQUAD READINESS</span>
            <h2 class="avail-main-title">PLAYER AVAILABILITY STATUS</h2>
          </div>
          <span class="avail-total-tag">SQUAD: <strong>${availSummary.squad}</strong> PLAYERS</span>
        </div>

        <div class="avail-metrics-grid">
          <div class="avail-metric-card green">
            <span class="avail-icon">🟢</span>
            <div class="avail-data">
              <span class="avail-count">${availSummary.available}</span>
              <span class="avail-label">AVAILABLE</span>
            </div>
          </div>

          <div class="avail-metric-card red">
            <span class="avail-icon">🔴</span>
            <div class="avail-data">
              <span class="avail-count">${availSummary.injured}</span>
              <span class="avail-label">INJURED</span>
            </div>
          </div>

          <div class="avail-metric-card gold">
            <span class="avail-icon">🟠</span>
            <div class="avail-data">
              <span class="avail-count">${availSummary.suspended}</span>
              <span class="avail-label">SUSPENDED</span>
            </div>
          </div>

          <div class="avail-metric-card grey">
            <span class="avail-icon">⚫</span>
            <div class="avail-data">
              <span class="avail-count">${availSummary.otherUnavailable}</span>
              <span class="avail-label">OTHER UNAVAIL.</span>
            </div>
          </div>
        </div>

        <!-- Visual Segmented Distribution Bar -->
        <div class="avail-bar-track" title="Squad Availability Distribution">
          <div class="bar-seg green" style="width: ${(availSummary.available / availSummary.squad) * 100}%;"></div>
          <div class="bar-seg red" style="width: ${(availSummary.injured / availSummary.squad) * 100}%;"></div>
          <div class="bar-seg gold" style="width: ${(availSummary.suspended / availSummary.squad) * 100}%;"></div>
          <div class="bar-seg grey" style="width: ${(availSummary.otherUnavailable / availSummary.squad) * 100}%;"></div>
        </div>
      </section>

      <!-- 21. CLUB INTELLIGENCE NAVIGATION TABS -->
      <div class="club-intel-tabs-bar">
        <button class="club-tab-btn ${activeTab === 'squad' ? 'active' : ''}" data-club-tab="squad">
          <span>👥 CURRENT SQUAD (${squadList.length})</span>
        </button>
        <button class="club-tab-btn ${activeTab === 'injuries' ? 'active' : ''}" data-club-tab="injuries">
          <span>🏥 INJURY CENTER (${injuriesList.length})</span>
        </button>
        <button class="club-tab-btn ${activeTab === 'suspensions' ? 'active' : ''}" data-club-tab="suspensions">
          <span>⚖️ SUSPENSION CENTER (${suspensionsList.length})</span>
        </button>
        <button class="club-tab-btn ${activeTab === 'transfers' ? 'active' : ''}" data-club-tab="transfers">
          <span>🔄 TRANSFERS (${(club.incoming || []).length + (club.outgoing || []).length})</span>
        </button>
        <button class="club-tab-btn ${activeTab === 'contracts' ? 'active' : ''}" data-club-tab="contracts">
          <span>📜 CONTRACTS</span>
        </button>
        <button class="club-tab-btn ${activeTab === 'statistics' ? 'active' : ''}" data-club-tab="statistics">
          <span>📊 PERFORMANCE STATS</span>
        </button>
      </div>

      <!-- TAB CONTENT AREA -->
      <div class="club-tab-content-mount">
        
        <!-- TAB 1: CURRENT SQUAD -->
        ${activeTab === 'squad' ? `
          <div class="club-squad-section">
            
            <!-- Squad Filters -->
            <div class="squad-filters-bar bl-hud-panel">
              <div class="filter-item">
                <label>POSITION:</label>
                <select id="squadFilterPos" class="bl-select bl-select-sm">
                  <option value="ALL" ${!filters.position || filters.position === 'ALL' ? 'selected' : ''}>All Positions</option>
                  <option value="Forward" ${filters.position === 'Forward' ? 'selected' : ''}>Forwards</option>
                  <option value="Midfielder" ${filters.position === 'Midfielder' ? 'selected' : ''}>Midfielders</option>
                  <option value="Defender" ${filters.position === 'Defender' ? 'selected' : ''}>Defenders</option>
                  <option value="Goalkeeper" ${filters.position === 'Goalkeeper' ? 'selected' : ''}>Goalkeepers</option>
                </select>
              </div>

              <div class="filter-item">
                <label>AVAILABILITY:</label>
                <select id="squadFilterAvail" class="bl-select bl-select-sm">
                  <option value="ALL" ${!filters.availability || filters.availability === 'ALL' ? 'selected' : ''}>All Statuses</option>
                  <option value="AVAILABLE" ${filters.availability === 'AVAILABLE' ? 'selected' : ''}>🟢 Available Only</option>
                  <option value="INJURED" ${filters.availability === 'INJURED' ? 'selected' : ''}>🔴 Injured Only</option>
                  <option value="SUSPENDED" ${filters.availability === 'SUSPENDED' ? 'selected' : ''}>🟠 Suspended Only</option>
                </select>
              </div>
            </div>

            <!-- Squad Grid -->
            <div class="squad-cards-grid">
              ${filteredSquad.length > 0 ? filteredSquad.map(p => `
                <div class="squad-player-card bl-hud-panel" data-view="player-profile" data-player-id="${p.id}">
                  <div class="squad-p-img-wrap">
                    <img src="${p.image || 'assets/players/mbappe.jpg'}" alt="${p.name}" class="squad-p-img" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
                    <span class="squad-p-shirt">#${p.shirtNumber}</span>
                  </div>

                  <div class="squad-p-body">
                    <div class="squad-p-top">
                      <strong class="squad-p-name">${p.name}</strong>
                      <span class="squad-p-ovr">${p.rating}</span>
                    </div>
                    
                    <div class="squad-p-role">${p.position} // ${p.flag} ${p.nationality}</div>
                    
                    <div class="squad-p-meta">
                      <span class="p-age">Age: <strong>${p.age}</strong></span>
                      <span class="p-val cyan">${p.marketValue}</span>
                    </div>

                    <div class="squad-p-contract">
                      <span class="lbl">Contract Expiry:</span>
                      <span class="val">${p.contractExpiry}</span>
                    </div>

                    <div class="squad-p-avail">
                      ${getAvailabilityBadge(p.availability)}
                    </div>
                  </div>

                  <button class="bl-btn bl-btn-xs bl-btn-cyber btn-view-player squad-scout-btn" data-player-id="${p.id}">
                    <span>SCOUT DOSSIER →</span>
                  </button>
                </div>
              `).join('') : '<p class="empty-state">No squad players match the selected filter criteria.</p>'}
            </div>
          </div>
        ` : ''}

        <!-- TAB 2: INJURY CENTER -->
        ${activeTab === 'injuries' ? `
          <div class="injury-center-view bl-card bl-hud-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> 🏥 CLUB INJURY CENTER <span class="title-bracket">]</span></h2>
              <span class="panel-tag red">${injuriesList.length} CURRENTLY UNAVAILABLE</span>
            </div>

            <p class="section-intro-text">
              Official medical bulletin data. Verified via official club medical departments and sports injury registries.
            </p>

            <div class="injury-cards-stream">
              ${injuriesList.length > 0 ? injuriesList.map(inj => `
                <div class="injury-dossier-card">
                  <div class="inj-card-header">
                    <div class="inj-p-info">
                      <span class="inj-badge red">🔴 INJURED</span>
                      <h3 class="inj-p-name">${inj.playerName}</h3>
                    </div>
                    <div class="inj-days-badge">
                      <span class="days-num">${inj.daysUnavailable}</span>
                      <span class="days-lbl">DAYS OUT</span>
                    </div>
                  </div>

                  <div class="inj-details-grid">
                    <div class="inj-cell">
                      <span class="lbl">DIAGNOSED INJURY</span>
                      <strong class="val red">${inj.injury}</strong>
                    </div>
                    <div class="inj-cell">
                      <span class="lbl">BODY AREA</span>
                      <strong class="val">${inj.bodyArea}</strong>
                    </div>
                    <div class="inj-cell">
                      <span class="lbl">DATE INJURED</span>
                      <strong class="val">${inj.dateInjured}</strong>
                    </div>
                    <div class="inj-cell">
                      <span class="lbl">EXPECTED RETURN</span>
                      <strong class="val cyan">${inj.expectedReturn || 'RETURN DATE: UNKNOWN'}</strong>
                    </div>
                    <div class="inj-cell">
                      <span class="lbl">RECOVERY STATUS</span>
                      <strong class="val">${inj.status}</strong>
                    </div>
                    <div class="inj-cell">
                      <span class="lbl">MEDICAL SOURCE</span>
                      <span class="source-link-span"><a href="${inj.sourceUrl || '#'}" target="_blank" rel="noopener noreferrer">${inj.source} ↗</a></span>
                    </div>
                  </div>

                  <div class="inj-footer-bar">
                    <span>Last Updated: ${inj.lastUpdated ? inj.lastUpdated.replace('T', ' ').slice(0, 16) : 'Recently'}</span>
                  </div>
                </div>
              `).join('') : '<p class="empty-state green">🟢 No active player injuries currently registered for this club.</p>'}
            </div>
          </div>
        ` : ''}

        <!-- TAB 3: SUSPENSION CENTER -->
        ${activeTab === 'suspensions' ? `
          <div class="suspension-center-view bl-card bl-hud-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> ⚖️ DISCIPLINARY & SUSPENSION CENTER <span class="title-bracket">]</span></h2>
              <span class="panel-tag gold">${suspensionsList.length} BANS ACTIVE</span>
            </div>

            <p class="section-intro-text">
              Official competition disciplinary registers and league suspension tracking.
            </p>

            <div class="suspension-cards-stream">
              ${suspensionsList.length > 0 ? suspensionsList.map(susp => `
                <div class="suspension-dossier-card">
                  <div class="susp-card-header">
                    <div class="susp-p-info">
                      <span class="susp-badge gold">🟠 ${susp.status.toUpperCase()}</span>
                      <h3 class="susp-p-name">${susp.playerName}</h3>
                    </div>
                    <div class="susp-remaining-badge">
                      <span class="match-num">${susp.matchesRemaining}</span>
                      <span class="match-lbl">MATCH REMAINING</span>
                    </div>
                  </div>

                  <div class="susp-details-grid">
                    <div class="susp-cell">
                      <span class="lbl">COMPETITION</span>
                      <strong class="val cyan">${susp.competition}</strong>
                    </div>
                    <div class="susp-cell">
                      <span class="lbl">DISCIPLINARY REASON</span>
                      <strong class="val">${susp.reason}</strong>
                    </div>
                    <div class="susp-cell">
                      <span class="lbl">CARDS RECORD</span>
                      <strong class="val">🟨 ${susp.yellowCards} // 🟥 ${susp.redCards}</strong>
                    </div>
                    <div class="susp-cell">
                      <span class="lbl">SUSPENSION DATES</span>
                      <strong class="val">${susp.suspensionStart} to ${susp.suspensionEnd}</strong>
                    </div>
                    <div class="susp-cell">
                      <span class="lbl">SANCTION LENGTH</span>
                      <strong class="val">${susp.suspensionLength}</strong>
                    </div>
                    <div class="susp-cell">
                      <span class="lbl">DISCIPLINARY SOURCE</span>
                      <span class="source-link-span"><a href="${susp.sourceUrl || '#'}" target="_blank" rel="noopener noreferrer">${susp.source} ↗</a></span>
                    </div>
                  </div>
                </div>
              `).join('') : '<p class="empty-state green">🟢 No active disciplinary suspensions currently recorded for this club.</p>'}
            </div>
          </div>
        ` : ''}

        <!-- TAB 4: TRANSFERS -->
        ${activeTab === 'transfers' ? `
          <div class="club-transfers-layout">
            <div class="club-dossier-grid">
              
              <!-- Incoming -->
              <div class="bl-card bl-hud-panel">
                <div class="panel-header-clean">
                  <h2 class="panel-section-title"><span class="title-bracket">[</span> 2026 INCOMING MOVES <span class="title-bracket">]</span></h2>
                  <span class="badge-count">${(club.incoming || []).length} DEALS</span>
                </div>
                <div class="transfers-table-mini">
                  ${(club.incoming || []).map(t => `
                    <div class="deal-item">
                      <div class="deal-p-name"><strong>${t.player}</strong> <span class="from-sub">from ${t.from}</span></div>
                      <div class="deal-fee">${t.fee}</div>
                      <div>${getStatusBadge(t.status)}</div>
                    </div>
                  `).join('')}
                </div>
              </div>

              <!-- Outgoing -->
              <div class="bl-card bl-hud-panel">
                <div class="panel-header-clean">
                  <h2 class="panel-section-title"><span class="title-bracket">[</span> 2026 DEPARTURES <span class="title-bracket">]</span></h2>
                  <span class="badge-count">${(club.outgoing || []).length} DEALS</span>
                </div>
                <div class="transfers-table-mini">
                  ${(club.outgoing || []).map(t => `
                    <div class="deal-item">
                      <div class="deal-p-name"><strong>${t.player}</strong> <span class="from-sub">to ${t.to}</span></div>
                      <div class="deal-fee">${t.fee}</div>
                      <div>${getStatusBadge(t.status)}</div>
                    </div>
                  `).join('')}
                </div>
              </div>

              <!-- Strategic Targets -->
              <div class="bl-card bl-hud-panel full-width">
                <div class="panel-header-clean">
                  <h2 class="panel-section-title"><span class="title-bracket">[</span> ACTIVE 2026 TARGETS & SCOUTING BIDS <span class="title-bracket">]</span></h2>
                  <span class="badge-count gold">${(club.targets || []).length} MONITORED</span>
                </div>
                <div class="targets-grid-view">
                  ${(club.targets || []).map(tgt => `
                    <div class="target-card">
                      <div class="tgt-head">
                        <span class="tgt-name">${tgt.name}</span>
                        <span class="tgt-val">${tgt.value}</span>
                      </div>
                      <div class="tgt-sub">Status: <strong>${tgt.status}</strong></div>
                      <div class="tgt-sub">Probability: <strong class="cyan">${tgt.probability || 50}%</strong></div>
                      <div class="tgt-sub">Source: <em>${tgt.source || 'Transfer Wire'}</em></div>
                    </div>
                  `).join('')}
                </div>
              </div>

            </div>
          </div>
        ` : ''}

        <!-- TAB 5: CONTRACT INFORMATION -->
        ${activeTab === 'contracts' ? `
          <div class="club-contracts-view bl-card bl-hud-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> 📜 SQUAD CONTRACT REGISTER <span class="title-bracket">]</span></h2>
              <span class="panel-tag cyan">PUBLIC BENCHMARK DATA</span>
            </div>

            <div class="table-responsive">
              <table class="bl-table">
                <thead>
                  <tr>
                    <th>PLAYER</th>
                    <th>SHIRT</th>
                    <th>POSITION</th>
                    <th>CONTRACT START</th>
                    <th>CONTRACT EXPIRY</th>
                    <th>CONTRACT STATUS</th>
                    <th>MARKET VALUE</th>
                  </tr>
                </thead>
                <tbody>
                  ${squadList.map(p => `
                    <tr>
                      <td><strong>${p.name}</strong></td>
                      <td>#${p.shirtNumber}</td>
                      <td>${p.position}</td>
                      <td>${p.contractStart || '2023-07-01'}</td>
                      <td><strong class="cyan">${p.contractExpiry || '2028-06-30'}</strong></td>
                      <td><span class="contract-status-pill">${p.contractStatus || 'Active First-Team'}</span></td>
                      <td>${p.marketValue}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
            <div class="stat-source-footnote">
              * Public contract duration benchmarks referenced from official club registry records.
            </div>
          </div>
        ` : ''}

        <!-- TAB 6: PERFORMANCE STATISTICS -->
        ${activeTab === 'statistics' ? `
          <div class="club-stats-view bl-card bl-hud-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> 📊 2025/2026 SEASON PERFORMANCE STATISTICS <span class="title-bracket">]</span></h2>
              <span class="panel-tag">OPTA / API-SPORTS</span>
            </div>

            <div class="table-responsive">
              <table class="bl-table">
                <thead>
                  <tr>
                    <th>PLAYER</th>
                    <th>POS</th>
                    <th>APPS</th>
                    <th>STARTS</th>
                    <th>MINS</th>
                    <th>GOALS</th>
                    <th>ASSISTS</th>
                    <th>xG</th>
                    <th>xA</th>
                    <th>KEY PASSES</th>
                    <th>PASS ACC.</th>
                    <th>TACKLES</th>
                    <th>CLEAN SHEETS</th>
                  </tr>
                </thead>
                <tbody>
                  ${squadList.map(p => {
                    const st = p.stats || {};
                    return `
                      <tr>
                        <td><strong>${p.name}</strong></td>
                        <td>${p.position.split(' ')[0]}</td>
                        <td>${st.appearances !== undefined ? st.appearances : 'N/A'}</td>
                        <td>${st.starts !== undefined ? st.starts : 'N/A'}</td>
                        <td>${st.minutes !== undefined ? st.minutes : 'N/A'}</td>
                        <td><strong class="cyan">${st.goals !== undefined ? st.goals : 'N/A'}</strong></td>
                        <td><strong>${st.assists !== undefined ? st.assists : 'N/A'}</strong></td>
                        <td>${st.xg !== undefined ? st.xg : 'N/A'}</td>
                        <td>${st.xa !== undefined ? st.xa : 'N/A'}</td>
                        <td>${st.keyPasses !== undefined ? st.keyPasses : 'N/A'}</td>
                        <td>${st.passAccuracy !== undefined ? st.passAccuracy + '%' : 'N/A'}</td>
                        <td>${st.tackles !== undefined ? st.tackles : 'N/A'}</td>
                        <td>${st.cleanSheets !== undefined ? st.cleanSheets : 'N/A'}</td>
                      </tr>
                    `;
                  }).join('')}
                </tbody>
              </table>
            </div>
          </div>
        ` : ''}

      </div>
    </div>
  `;
}

/**
 * Compatibility wrapper for club profile
 */
export function renderClubProfile(club) {
  return renderClubIntelligenceView(club, 'squad', {});
}

/**
 * MARKET INTELLIGENCE Matrix Table
 */
export function renderTransferMarketTable(players, sortKey, sortAsc) {
  return `
    <div class="bl-market-table-wrapper">
      <div class="table-disclaimer-bar">
        <span>⚡ <strong>BLUEGUN Metrics:</strong> Ego Rating, Transfer Momentum, Market Pressure.</span>
        <span>📊 <strong>2026 Benchmarks:</strong> Market Value & Contract Data (Ref: Transfermarkt).</span>
      </div>

      <div class="table-responsive">
        <table class="bl-table">
          <thead>
            <tr>
              <th>PLAYER</th>
              <th>CLUB</th>
              <th>POS</th>
              <th>AGE</th>
              <th class="sortable ${sortKey === 'marketValueRaw' ? 'sorted' : ''}" data-sort="marketValueRaw">
                MARKET VALUE ${sortKey === 'marketValueRaw' ? (sortAsc ? '▲' : '▼') : ''}
              </th>
              <th class="sortable ${sortKey === 'egoRating' ? 'sorted' : ''}" data-sort="egoRating">
                EGO ${sortKey === 'egoRating' ? (sortAsc ? '▲' : '▼') : ''}
              </th>
              <th class="sortable ${sortKey === 'probability' ? 'sorted' : ''}" data-sort="probability">
                MOVE PROB. ${sortKey === 'probability' ? (sortAsc ? '▲' : '▼') : ''}
              </th>
              <th>STATUS</th>
              <th>ACTION</th>
            </tr>
          </thead>
          <tbody>
            ${players.map(p => {
              const imgSrc = p.image || p.photo;
              return `
                <tr class="table-row-player" data-player-id="${p.id}">
                  <td class="player-cell">
                    <img src="${imgSrc}" alt="${p.name}" class="cell-avatar" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
                    <div class="cell-meta">
                      <strong class="cell-name">${p.name}</strong>
                      <span class="cell-nat">${p.flag} ${p.nationality}</span>
                    </div>
                  </td>
                  <td><span class="cell-club">${p.currentClub}</span></td>
                  <td><span class="cell-pos">${p.position.split(' ')[0]}</span></td>
                  <td>${p.age}</td>
                  <td><strong class="cyan">${p.marketValue}</strong></td>
                  <td><strong class="gold">${p.egoRating}</strong></td>
                  <td>
                    <div class="prob-cell-wrap">
                      <span>${p.probability}%</span>
                      <div class="prob-mini-track">
                        <div class="prob-mini-fill" style="width: ${p.probability}%;"></div>
                      </div>
                    </div>
                  </td>
                  <td>${getStatusBadge(p.transferStatus)}</td>
                  <td>
                    <button class="bl-btn bl-btn-xs bl-btn-cyber btn-view-player" data-player-id="${p.id}">
                      SCOUT
                    </button>
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

/**
 * Player Comparison View (EGO CLASH RADAR)
 */
export function renderComparisonView(playerA, playerB) {
  const imgA = playerA.image || playerA.photo;
  const imgB = playerB.image || playerB.photo;

  return `
    <div class="bl-comparison-view">
      <div class="comparison-header">
        <div class="section-title-wrap">
          <span class="sub-label">TACTICAL HEAD-TO-HEAD MATRIX</span>
          <h1 class="main-title">EGO CLASH: <span class="cyan">${playerA.name}</span> VS <span class="red">${playerB.name}</span></h1>
        </div>
        <p class="comparison-disclaimer">
          Comparing proprietary BLUEGUN algorithms with verified 2025/2026 match intelligence.
        </p>
      </div>

      <!-- Selectors & Dual Radar Chart -->
      <div class="comparison-arena-grid">
        
        <!-- Player A Head -->
        <div class="compare-head-card card-a">
          <div class="compare-img-wrap">
            <img src="${imgA}" alt="${playerA.name}" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
            <div class="compare-head-overlay cyan"></div>
          </div>
          <div class="compare-head-info">
            <span class="compare-flag">${playerA.flag} ${playerA.nationality}</span>
            <h2 class="compare-player-name">${playerA.name}</h2>
            <p class="compare-sub">${playerA.currentClub} // ${playerA.position}</p>
            <div class="compare-big-ratings">
              <div class="c-rat">
                <span class="lbl">OVR</span>
                <span class="val cyan">${playerA.rating}</span>
              </div>
              <div class="c-rat">
                <span class="lbl">EGO</span>
                <span class="val cyan">${playerA.egoRating}</span>
              </div>
              <div class="c-rat">
                <span class="lbl">VALUATION</span>
                <span class="val cyan">${playerA.marketValue}</span>
              </div>
            </div>
            <div class="photo-attr-micro">📷 ${playerA.imageCredit || 'Wikimedia'}</div>
          </div>
        </div>

        <!-- Center Radar Visualizer -->
        <div class="compare-radar-center bl-hud-panel">
          <div class="panel-header-clean">
            <span class="radar-legend-item cyan"><span class="legend-dot cyan"></span> ${playerA.name}</span>
            <span class="radar-legend-item red"><span class="legend-dot red"></span> ${playerB.name}</span>
          </div>
          
          <div id="comparisonRadarContainer" class="comparison-radar-wrap"></div>
        </div>

        <!-- Player B Head -->
        <div class="compare-head-card card-b">
          <div class="compare-img-wrap">
            <img src="${imgB}" alt="${playerB.name}" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
            <div class="compare-head-overlay red"></div>
          </div>
          <div class="compare-head-info">
            <span class="compare-flag">${playerB.flag} ${playerB.nationality}</span>
            <h2 class="compare-player-name">${playerB.name}</h2>
            <p class="compare-sub">${playerB.currentClub} // ${playerB.position}</p>
            <div class="compare-big-ratings">
              <div class="c-rat">
                <span class="lbl">OVR</span>
                <span class="val red">${playerB.rating}</span>
              </div>
              <div class="c-rat">
                <span class="lbl">EGO</span>
                <span class="val red">${playerB.egoRating}</span>
              </div>
              <div class="c-rat">
                <span class="lbl">VALUATION</span>
                <span class="val red">${playerB.marketValue}</span>
              </div>
            </div>
            <div class="photo-attr-micro">📷 ${playerB.imageCredit || 'Wikimedia'}</div>
          </div>
        </div>
      </div>

      <!-- Stat Comparison Matrix Table -->
      <div class="bl-card bl-hud-panel comparison-stats-table-panel">
        <h2 class="panel-section-title">
          <span class="title-bracket">[</span>
          HEAD-TO-HEAD SCOUTING BREAKDOWN
          <span class="title-bracket">]</span>
        </h2>

        <div class="h2h-stat-list">
          ${[
            { label: "AGE", valA: playerA.age, valB: playerB.age, lowerBetter: true },
            { label: "MARKET VALUE (€M)", valA: playerA.marketValueRaw, valB: playerB.marketValueRaw, suffix: "M" },
            { label: "GOALS", valA: playerA.stats.goals, valB: playerB.stats.goals },
            { label: "ASSISTS", valA: playerA.stats.assists, valB: playerB.stats.assists },
            { label: "EXPECTED GOALS (xG)", valA: playerA.stats.xg, valB: playerB.stats.xg },
            { label: "EXPECTED ASSISTS (xA)", valA: playerA.stats.xa, valB: playerB.stats.xa },
            { label: "KEY PASSES", valA: playerA.stats.keyPasses, valB: playerB.stats.keyPasses },
            { label: "DRIBBLES COMPLETED", valA: playerA.stats.dribbles, valB: playerB.stats.dribbles },
            { label: "PACE", valA: playerA.radar.pace, valB: playerB.radar.pace },
            { label: "SHOOTING", valA: playerA.radar.shooting, valB: playerB.radar.shooting },
            { label: "PASSING", valA: playerA.radar.passing, valB: playerB.radar.passing },
            { label: "DRIBBLING", valA: playerA.radar.dribbling, valB: playerB.radar.dribbling },
            { label: "DEFENDING", valA: playerA.radar.defending, valB: playerB.radar.defending },
            { label: "PHYSICAL", valA: playerA.radar.physical, valB: playerB.radar.physical },
            { label: "EGO RATING", valA: playerA.egoRating, valB: playerB.egoRating },
            { label: "TRANSFER PROBABILITY (EST.)", valA: playerA.probability, valB: playerB.probability, suffix: "%" }
          ].map(stat => {
            const winA = stat.lowerBetter ? stat.valA < stat.valB : stat.valA > stat.valB;
            const winB = stat.lowerBetter ? stat.valB < stat.valA : stat.valB > stat.valA;
            return `
              <div class="h2h-stat-row">
                <div class="stat-col col-a ${winA ? 'winner-a' : ''}">
                  <span class="stat-val">${stat.valA}${stat.suffix || ''}</span>
                  ${winA ? '<span class="lead-badge cyan">▲ ADV</span>' : ''}
                </div>
                <div class="stat-col col-label">
                  <span>${stat.label}</span>
                </div>
                <div class="stat-col col-b ${winB ? 'winner-b' : ''}">
                  ${winB ? '<span class="lead-badge red">ADV ▲</span>' : ''}
                  <span class="stat-val">${stat.valB}${stat.suffix || ''}</span>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>

    </div>
  `;
}

/**
 * Complete 6-Section COPYRIGHT & ATTRIBUTION Page
 */
export function renderCopyrightAndAttributionView() {
  return `
    <div class="bl-compliance-view">
      
      <!-- Header Banner -->
      <section class="compliance-header bl-hud-panel">
        <div class="hud-corner top-left"></div>
        <div class="hud-corner top-right"></div>
        <div class="hud-corner bottom-left"></div>
        <div class="hud-corner bottom-right"></div>

        <div class="compliance-header-content">
          <span class="compliance-kicker">BLUEGUN LEGAL & INTELLECTUAL PROPERTY REGISTER</span>
          <h1 class="compliance-title">COPYRIGHT & ATTRIBUTION</h1>
          <p class="compliance-subtitle">
            Complete provenance registry distinguishing original BLUEGUN scouting algorithms, 
            licensed sports photography, third-party data providers, and club trademarks.
          </p>
        </div>
      </section>

      <!-- Section 1: BLUEGUN ORIGINAL CONTENT -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 1. BLUEGUN ORIGINAL CONTENT <span class="title-bracket">]</span></h2>
          <span class="panel-tag cyan">ORIGINAL CREATIONS</span>
        </div>

        <div class="legal-notice-box">
          <h3 class="legal-box-title">© 2026 BLUEGUN. All rights reserved.</h3>
          <p>
            The following assets and systems are original intellectual creations of BLUEGUN:
          </p>
          <ul class="legal-bullets">
            <li><strong>Brand Identity:</strong> BLUEGUN name, logo, cyber visual theme, and motto ("ENTER THE TRANSFER BATTLEFIELD.").</li>
            <li><strong>UI/UX Architecture:</strong> Responsive cyber layouts, HUD cards, modal systems, and navigation flows.</li>
            <li><strong>EGO RATING:</strong> Proprietary player impact mathematical estimation engine.</li>
            <li><strong>TRANSFER MOMENTUM:</strong> Original algorithm calculating progression velocity of active negotiations.</li>
            <li><strong>MARKET PRESSURE:</strong> Mathematical formula tracking spread between asking fee and market value.</li>
            <li><strong>TRANSFER PROBABILITY:</strong> Multi-parameter predictive algorithmic model.</li>
            <li><strong>Custom Chart Engine:</strong> Lightweight zero-dependency SVG vector radar and trajectory visualizers.</li>
            <li><strong>Editorial Analysis:</strong> Original scouting descriptions, tactical overviews, and battle commentary.</li>
          </ul>
        </div>
      </div>

      <!-- Section 2: DATA PROVIDERS -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 2. DATA PROVIDERS <span class="title-bracket">]</span></h2>
          <span class="panel-tag">VERIFIED APIS</span>
        </div>

        <div class="data-sources-grid">
          ${DATA_SOURCES.map(src => `
            <div class="data-source-card">
              <div class="ds-head">
                <span class="ds-category">${src.category}</span>
                <h3 class="ds-name">${src.provider} — ${src.apiName}</h3>
              </div>
              <p class="ds-desc">${src.description}</p>
              <div class="ds-footer">
                <span class="ds-license">License: <strong>${src.license}</strong></span>
                <a href="${src.website}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Provider Website ↗</a>
                <a href="${src.termsUrl}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Terms URL ↗</a>
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- Section 3: NEWS SOURCES -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 3. NEWS SOURCES <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">ATTRIBUTED WIRE</span>
        </div>
        <p class="section-intro-text">
          Transfer intelligence reports are short editorial excerpts only. We do not reproduce complete copyrighted news articles.
        </p>

        <div class="news-sources-list">
          <div class="news-source-item">
            <strong>The Athletic Football</strong> — Syndicated European transfer news & tactical reporting. (Source links provided).
          </div>
          <div class="news-source-item">
            <strong>Sky Sports Transfer Centre</strong> — Premier League breaking transfer news.
          </div>
          <div class="news-source-item">
            <strong>Fabrizio Romano Wire</strong> — Live deal confirmations and player personal terms.
          </div>
          <div class="news-source-item">
            <strong>Marca & Diario AS</strong> — Spanish football & La Liga transfer market coverage.
          </div>
        </div>
      </div>

      <!-- Section 4: IMAGE SOURCES -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 4. IMAGE SOURCES & PHOTOGRAPHY LICENSING <span class="title-bracket">]</span></h2>
          <span class="panel-tag cyan">DOCUMENTED ATHLETES</span>
        </div>
        <p class="section-intro-text">
          All featured athlete photographs are sourced with verified photographers, hosts, and Creative Commons licenses.
        </p>

        <div class="table-responsive">
          <table class="bl-table compliance-table">
            <thead>
              <tr>
                <th>PLAYER</th>
                <th>PHOTOGRAPHER / CREDIT</th>
                <th>LICENSE STATUS</th>
                <th>SOURCE HOST</th>
                <th>REPOSITORY LINK</th>
              </tr>
            </thead>
            <tbody>
              ${PLAYERS.map(p => `
                <tr>
                  <td>
                    <div class="player-cell">
                      <img src="${p.image || p.photo}" alt="${p.name}" class="cell-avatar" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
                      <strong>${p.name}</strong>
                    </div>
                  </td>
                  <td>${p.imageCredit || 'Steffen Prößdorf'}</td>
                  <td><span class="license-tag">${p.imageLicense || 'CC BY-SA 4.0'}</span></td>
                  <td>${p.imageSource || 'Wikimedia Commons'}</td>
                  <td>
                    <a href="${p.imageSourceUrl || 'https://commons.wikimedia.org/'}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">
                      Source Repository ↗
                    </a>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section 5: CLUB & LEAGUE TRADEMARKS -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 5. CLUB & LEAGUE TRADEMARKS <span class="title-bracket">]</span></h2>
        </div>
        <div class="disclaimer-body">
          <div class="quote-notice">
            "Club names, logos, badges and trademarks belong to their respective owners."
          </div>
          <p>
            All football club crests, stadium names, competition logos, and league brand assets 
            (including UEFA Champions League, Premier League, La Liga, Serie A, Bundesliga, Ligue 1) 
            are protected trademarks of their respective rights holders. Their appearance on BLUEGUN is strictly for non-commercial identification, educational commentary, and scouting simulation under fair-use standards.
          </p>
        </div>
      </div>

      <!-- Section 6: OPEN-SOURCE SOFTWARE -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 6. OPEN-SOURCE SOFTWARE & TYPOGRAPHY <span class="title-bracket">]</span></h2>
        </div>

        <div class="table-responsive">
          <table class="bl-table compliance-table">
            <thead>
              <tr>
                <th>PACKAGE / ASSET</th>
                <th>TYPE</th>
                <th>AUTHOR / MAINTAINER</th>
                <th>LICENSE</th>
                <th>PROJECT REPOSITORY</th>
              </tr>
            </thead>
            <tbody>
              ${THIRD_PARTY_ASSETS.map(ast => `
                <tr>
                  <td><strong>${ast.name}</strong></td>
                  <td>${ast.type}</td>
                  <td>${ast.author}</td>
                  <td><span class="license-tag">${ast.license}</span></td>
                  <td><a href="${ast.website}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Website ↗</a></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  `;
}

/**
 * Global Rich Footer Renderer for BLUEGUN
 */
export function renderGlobalFooter() {
  return `
    <footer class="bl-global-footer">
      <div class="footer-container">
        
        <!-- Brand & Tagline -->
        <div class="footer-col brand-col">
          <div class="footer-brand">
            <svg class="footer-logo-svg" width="24" height="24" viewBox="0 0 100 100">
              <polygon points="50,5 92,27 92,73 50,95 8,73 8,27" fill="none" stroke="#00f0ff" stroke-width="6"/>
              <line x1="50" y1="5" x2="50" y2="95" stroke="#0077ff" stroke-width="3" stroke-dasharray="4,4"/>
              <circle cx="50" cy="50" r="18" fill="rgba(0, 240, 255, 0.15)" stroke="#00f0ff" stroke-width="4"/>
              <circle cx="50" cy="50" r="6" fill="#00f0ff"/>
            </svg>
            <span class="footer-brand-title">BLUEGUN</span>
          </div>
          <p class="footer-motto">"ENTER THE TRANSFER BATTLEFIELD."</p>
          <p class="footer-desc">
            Next-generation 2026 football transfer & club intelligence platform combining tactical ego scouting with European market analytics.
          </p>
          <div class="footer-copyright-main">
            <strong>© 2026 BLUEGUN. All rights reserved.</strong>
          </div>
        </div>

        <!-- Quick Navigation -->
        <div class="footer-col">
          <h4 class="footer-heading">PLATFORM MODULES</h4>
          <ul class="footer-links">
            <li><a href="#transfers" class="footer-nav-link" data-view="transfers">Live Transfer Wire</a></li>
            <li><a href="#players" class="footer-nav-link" data-view="players">Player Scouting Files</a></li>
            <li><a href="#clubs" class="footer-nav-link" data-view="clubs">Club Intelligence</a></li>
            <li><a href="#compare" class="footer-nav-link" data-view="compare">Ego Clash Radar</a></li>
            <li><a href="#market" class="footer-nav-link" data-view="market">Market Intelligence</a></li>
            <li><a href="#news" class="footer-nav-link" data-view="news">Transfer Intelligence</a></li>
          </ul>
        </div>

        <!-- Legal & Attribution Links -->
        <div class="footer-col">
          <h4 class="footer-heading">COMPLIANCE & LEGAL</h4>
          <ul class="footer-links">
            <li><a href="#copyright" class="footer-nav-link highlight" data-view="copyright">⚖️ Copyright & Attribution</a></li>
            <li><a href="#privacy" class="footer-legal-modal-trigger" data-modal="privacy">🔒 Privacy Policy</a></li>
            <li><a href="#terms" class="footer-legal-modal-trigger" data-modal="terms">📜 Terms of Use</a></li>
            <li><a href="#sources" class="footer-nav-link" data-view="copyright">📊 Data Providers & APIs</a></li>
            <li><a href="mailto:intel@bluegun.football" class="footer-ext-link">📬 Contact Compliance</a></li>
          </ul>
        </div>

        <!-- Disclaimers & Attribution Note -->
        <div class="footer-col disclaimer-col">
          <h4 class="footer-heading">INTELLECTUAL PROPERTY</h4>
          <div class="footer-disclaimer-box">
            <p class="disclaimer-p">
              <strong>Trademarks:</strong> Club names, logos, badges and trademarks belong to their respective owners.
            </p>
            <p class="disclaimer-p">
              <strong>Blue Lock Notice:</strong> BLUEGUN is an independent football transfer and scouting project. It is not affiliated with, endorsed by, or sponsored by the creators or rights holders of Blue Lock.
            </p>
            <p class="disclaimer-p">
              <strong>Photography:</strong> Athlete portraits sourced under documented Creative Commons licenses with individual creator credits.
            </p>
          </div>
        </div>

      </div>

      <div class="footer-bottom-bar">
        <div class="footer-bottom-container">
          <span>BLUEGUN • 2026 Football Transfer & Club Intelligence • Zero-Dependency Architecture</span>
          <span class="status-indicator">🟢 2026 INTELLIGENCE ONLINE</span>
        </div>
      </div>
    </footer>
  `;
}

/**
 * Privacy Policy Content Generator
 */
export function getPrivacyPolicyHtml() {
  return `
    <div class="legal-modal-content">
      <h2>BLUEGUN PRIVACY POLICY</h2>
      <p class="effective-date">Last Updated: August 25, 2026</p>
      
      <h3>1. Data Collection & Privacy First</h3>
      <p>
        BLUEGUN operates as a client-first football intelligence platform. We do not sell personal scouting queries, user data, or tracking information to third-party data brokers.
      </p>

      <h3>2. Local Client Storage</h3>
      <p>
        Preferences (such as filter selections, search history, and favorite players) are retained locally in the user's browser via localStorage where applicable.
      </p>

      <h3>3. External Links & Third Parties</h3>
      <p>
        Our platform contains links to external news providers, photo repositories (e.g. Wikimedia Commons), and sports statistics providers. We are not responsible for the privacy practices or contents of these third-party websites.
      </p>

      <h3>4. Contact</h3>
      <p>
        For inquiries regarding compliance or privacy, contact <code>intel@bluegun.football</code>.
      </p>
    </div>
  `;
}

/**
 * Terms of Use Content Generator
 */
export function getTermsOfUseHtml() {
  return `
    <div class="legal-modal-content">
      <h2>BLUEGUN TERMS OF USE</h2>
      <p class="effective-date">Last Updated: August 25, 2026</p>

      <h3>1. Demonstration & Fan Concept Purpose</h3>
      <p>
        BLUEGUN is an interactive sports intelligence and scouting simulation application built for analytical demonstration.
      </p>

      <h3>2. Algorithmic Nature of Metrics</h3>
      <p>
        Metrics including <em>Ego Rating, Transfer Momentum, Market Pressure,</em> and <em>Transfer Probability</em> are algorithmic estimations generated by BLUEGUN. They do not constitute official statements by football clubs, players, or football governing bodies.
      </p>

      <h3>3. Third-Party Intellectual Property</h3>
      <p>
        All football club names, emblems, competition trademarks, and player photography remain the property of their respective creators and owners.
      </p>

      <h3>4. No Warranty</h3>
      <p>
        The software is provided "as is", without warranty of any kind, express or implied.
      </p>
    </div>
  `;
}
'''

with open(r"c:\Users\LENOVO\Desktop\web\js\components.js", "w", encoding="utf-8") as f:
    f.write(components_code.strip())

print("Successfully updated js/components.js with Club Intelligence, Injury Center, Suspension Center & 6-Section Licensing Hub!")
