/**
 * BLUEGUN — 2026 Football Transfer & Club Intelligence Platform
 * Component Library & UI View Engine
 * Tagline: "ENTER THE TRANSFER BATTLEFIELD."
 */

import { renderRadarChart, renderMarketValueChart } from './chart.js';
import { DATA_SOURCES, THIRD_PARTY_ASSETS, COMPLIANCE_DISCLAIMERS, PLAYERS, CLUBS, DASHBOARD_STATS } from './data.js';
import { SOURCES_REGISTRY, AUDIT_METADATA, getSourceById, getOriginalWorkSources, getThirdPartySources, getUnverifiedSources, getSourcesCount } from './sources.js';

// Global SVG Fallback for Player Images
export const PLAYER_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23050a18'/><circle cx='50' cy='38' r='20' fill='%2300f0ff' opacity='0.35'/><path d='M15 92 Q50 58 85 92' fill='%2300f0ff' opacity='0.35'/><text x='50' y='96' font-family='sans-serif' font-weight='bold' font-size='7' fill='%2300f0ff' text-anchor='middle'>BLUEGUN INTEL</text></svg>`;

// Global SVG Fallback for Club Badges
export const CLUB_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><polygon points='50,5 95,25 95,75 50,95 5,75 5,25' fill='%230b1325' stroke='%2300f0ff' stroke-width='3'/><circle cx='50' cy='50' r='20' fill='%230077ff' opacity='0.5'/></svg>`;

/**
 * Micro Source Trigger Button Helper
 */
export function renderSourceBtn(sourceId, label = "ⓘ Source") {
  return `<button class="bl-source-btn" data-source-id="${sourceId}" title="Inspect source provenance & licensing">${label}</button>`;
}

/**
 * Source Verification Status Badge Helper
 */
export function getSourceStatusBadge(status) {
  if (status === 'VERIFIED') {
    return `<span class="source-status-pill verified">🟢 VERIFIED</span>`;
  } else if (status === 'REVIEW REQUIRED') {
    return `<span class="source-status-pill review">🟡 REVIEW REQUIRED</span>`;
  } else {
    return `<span class="source-status-pill unknown">🔴 LICENSE UNKNOWN</span>`;
  }
}

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
          ${renderSourceBtn('NEWS-001')}
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
  const sourceId = p.sourceId || 'IMG-001';

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
        <div class="player-photo-attribution">
          <span>📷 ${photoCreditShort}</span>
          ${renderSourceBtn(sourceId)}
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
  const logoSourceId = club.logoSourceId || 'LOGO-001';

  return `
    <article class="bl-club-card" data-club-id="${club.id}">
      <div class="card-glow-edge"></div>
      <div class="club-card-header">
        <div class="club-badge-wrap">
          <img src="${club.badge}" alt="${club.name}" class="club-badge-img" loading="lazy" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
        </div>
        <div class="club-header-info">
          <div class="club-header-top-row">
            <span class="club-ego-rank">${club.egoRank}</span>
            ${renderSourceBtn(logoSourceId)}
          </div>
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
        <span>* Football club names, logos, badges and trademarks belong to their respective owners.</span>
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
          ${renderSourceBtn('NEWS-001')}
        </div>

        <h3 class="news-headline">${item.title}</h3>
        <p class="news-summary">${item.summary}</p>
        <span class="news-summary-tag">BLUEGUN SUMMARY</span>

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
  const primaryTarget = p.interestedClubs && p.interestedClubs.length > 0 ? p.interestedClubs[0] : { name: "Evaluating Offers", probability: 50 };
  const photoSourceId = p.sourceId || 'IMG-001';

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
              <div class="photo-credit-row">
                <span class="photo-icon">📷</span>
                <span class="photo-credit-text">Credit: <strong>${photoCredit}</strong> (${photoLicense})</span>
              </div>
              <div class="photo-actions-row">
                <a href="${photoSourceUrl}" target="_blank" rel="noopener noreferrer" class="license-source-link">Source ↗</a>
                ${renderSourceBtn(photoSourceId)}
              </div>
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
                <div class="card-micro-source">${renderSourceBtn('DATA-002')}</div>
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
            <span><strong>Match Statistics:</strong> FBref & Opta Sports Match Analytics</span>
            ${renderSourceBtn('DATA-003')}
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
              ${renderSourceBtn('DATA-002')}
            </div>
            <div id="playerValuationChart" class="valuation-chart-wrap"></div>
            <div class="valuation-meta-footnote">
              * Market valuation trajectory benchmarked against Transfermarkt public indices.
            </div>
          </div>
        </div>

        <!-- Right: Season Stats, Interested Clubs, Rumours -->
        <div class="profile-right-col">
          <div class="bl-card bl-hud-panel season-stats-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title"><span class="title-bracket">[</span> 2025/2026 PERFORMANCE METRICS <span class="title-bracket">]</span></h2>
              ${renderSourceBtn('DATA-003')}
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
              ${renderSourceBtn('NEWS-003')}
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
 * CLUB INTELLIGENCE DASHBOARD
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

      <!-- CLUB OVERVIEW PANEL -->
      <section class="club-header-panel bl-hud-panel" style="border-top: 3px solid ${club.color};">
        <div class="hud-corner top-left"></div>
        <div class="hud-corner top-right"></div>
        <div class="hud-corner bottom-left"></div>
        <div class="hud-corner bottom-right"></div>

        <div class="club-header-flex">
          <div class="club-crest-col">
            <img src="${club.badge}" alt="${club.name}" class="club-big-crest" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            ${renderSourceBtn('LOGO-001')}
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
              <span>Source: <strong>API-Football</strong></span>
              ${renderSourceBtn('DATA-001')}
            </div>
          </div>
        </div>

        <div class="club-trademark-footer">
          <span>* Football club names, logos, badges and trademarks belong to their respective owners.</span>
        </div>
      </section>

      <!-- PLAYER AVAILABILITY SUMMARY -->
      <section class="club-availability-summary-strip bl-hud-panel">
        <div class="avail-summary-header">
          <div class="avail-title-group">
            <span class="section-kicker">SQUAD READINESS</span>
            <h2 class="avail-main-title">PLAYER AVAILABILITY STATUS</h2>
          </div>
          <div class="avail-total-group">
            <span class="avail-total-tag">SQUAD: <strong>${availSummary.squad}</strong> PLAYERS</span>
            ${renderSourceBtn('DATA-001')}
          </div>
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

      <!-- CLUB INTELLIGENCE NAVIGATION TABS -->
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
              <div class="header-right-tools">
                <span class="panel-tag red">${injuriesList.length} CURRENTLY UNAVAILABLE</span>
                ${renderSourceBtn('DATA-001')}
              </div>
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
                    ${renderSourceBtn('DATA-001')}
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
              <div class="header-right-tools">
                <span class="panel-tag gold">${suspensionsList.length} BANS ACTIVE</span>
                ${renderSourceBtn('DATA-001')}
              </div>
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
              ${renderSourceBtn('DATA-001')}
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
              ${renderSourceBtn('DATA-003')}
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
        ${renderSourceBtn('DATA-002')}
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
            <div class="photo-attr-micro">📷 ${playerA.imageCredit || 'Wikimedia'} ${renderSourceBtn(playerA.sourceId || 'IMG-001')}</div>
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
            <div class="photo-attr-micro">📷 ${playerB.imageCredit || 'Wikimedia'} ${renderSourceBtn(playerB.sourceId || 'IMG-002')}</div>
          </div>
        </div>
      </div>

      <!-- Stat Comparison Matrix Table -->
      <div class="bl-card bl-hud-panel comparison-stats-table-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title">
            <span class="title-bracket">[</span>
            HEAD-TO-HEAD SCOUTING BREAKDOWN
            <span class="title-bracket">]</span>
          </h2>
          ${renderSourceBtn('DATA-003')}
        </div>

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

export function renderCreditsView(categoryFilter = 'ALL', searchQuery = '') {
  const counts = getSourcesCount();
  const originals  = getOriginalWorkSources();
  const unverified = getUnverifiedSources();

  let list = [...SOURCES_REGISTRY];

  // Category filtering
  if (categoryFilter !== 'ALL') {
    const f = categoryFilter.toUpperCase();
    list = list.filter(s => {
      const t = s.type.toUpperCase();
      const c = s.category.toUpperCase();
      if (f === 'ORIGINAL')    return t === 'BLUEGUN_ORIGINAL';
      if (f === 'IMAGES')      return t === 'IMAGE';
      if (f === 'DATA')        return t === 'DATA';
      if (f === 'NEWS')        return t === 'NEWS';
      if (f === 'LOGOS')       return t === 'LOGO';
      if (f === 'FONTS')       return t === 'FONT';
      if (f === 'LIBRARIES')   return t === 'LIBRARY';
      if (f === 'APIS')        return t === 'API';
      if (f === 'AI')          return t === 'AI';
      if (f === 'TOOLS')       return t === 'TOOL' || t === 'INFRASTRUCTURE';
      if (f === 'UNVERIFIED')  return s.status === 'REVIEW REQUIRED' || s.status === 'UNVERIFIED';
      return c.includes(f) || t === f;
    });
  }

  // Search filtering
  if (searchQuery) {
    const q = searchQuery.toLowerCase().trim();
    list = list.filter(s =>
      s.id.toLowerCase().includes(q) ||
      s.name.toLowerCase().includes(q) ||
      (s.creator    && s.creator.toLowerCase().includes(q)) ||
      (s.license    && s.license.toLowerCase().includes(q)) ||
      (s.category   && s.category.toLowerCase().includes(q)) ||
      (s.used_in    && s.used_in.some(u => u.toLowerCase().includes(q))) ||
      (s.status     && s.status.toLowerCase().includes(q))
    );
  }

  // Split list for display
  const origList      = list.filter(s => s.type === 'bluegun_original');
  const thirdList     = list.filter(s => s.type !== 'bluegun_original');
  const imgList       = list.filter(s => s.type === 'image');
  const logoList      = list.filter(s => s.type === 'logo');
  const dataList      = list.filter(s => s.type === 'data');
  const newsList      = list.filter(s => s.type === 'news');
  const apiList       = list.filter(s => s.type === 'api');
  const fontList      = list.filter(s => s.type === 'font');
  const iconList      = list.filter(s => s.type === 'icon');
  const libList       = list.filter(s => s.type === 'library');
  const aiList        = list.filter(s => s.type === 'ai');
  const toolList      = list.filter(s => s.type === 'tool' || s.type === 'infrastructure');
  const unverList     = list.filter(s => s.status === 'REVIEW REQUIRED');

  function sourceCard(s) {
    const isOriginal = s.type === 'bluegun_original';
    return `
      <article class="source-registry-card bl-hud-panel ${isOriginal ? 'source-card--original' : ''}" id="src-${s.id}">
        <div class="source-card-header">
          <div class="source-id-block">
            <span class="source-id-tag">${s.id}</span>
            <span class="source-category-tag">${s.category}</span>
          </div>
          <div class="source-status-block">
            ${isOriginal
              ? `<span class="source-status-pill original">🔵 BLUEGUN ORIGINAL</span>`
              : getSourceStatusBadge(s.status)}
          </div>
        </div>

        <h3 class="source-title-name">${s.name}</h3>

        <div class="source-specs-grid">
          <div class="source-cell">
            <span class="lbl">CREATOR / AUTHOR</span>
            <strong class="val">${s.creator || 'BLUEGUN Project'}</strong>
          </div>
          <div class="source-cell">
            <span class="lbl">COPYRIGHT / TRADEMARK HOLDER</span>
            <strong class="val">${s.copyright_holder || (isOriginal ? 'BLUEGUN' : 'N/A')}</strong>
          </div>
          <div class="source-cell">
            <span class="lbl">LICENSE TYPE</span>
            <strong class="val ${isOriginal ? 'neon' : 'cyan'}">${s.license || 'SOURCE / LICENSE VERIFICATION REQUIRED'}</strong>
          </div>
          <div class="source-cell">
            <span class="lbl">DATE DOCUMENTED</span>
            <strong class="val">${s.date_accessed || '2026-08-25'}</strong>
          </div>
        </div>

        ${s.attribution_text ? `
          <div class="source-attr-box ${isOriginal ? 'attr-note' : ''}">
            <span class="lbl">${isOriginal ? 'NOTE:' : 'MANDATORY ATTRIBUTION:'}</span>
            <p class="attr-text">${s.attribution_text}</p>
          </div>
        ` : ''}

        <div class="source-used-in-row">
          <span class="lbl">USED IN:</span>
          <div class="used-in-tags">
            ${(s.used_in || ['General Application']).map(u => `<span class="used-tag">${u}</span>`).join('')}
          </div>
        </div>

        <div class="source-card-footer">
          <div class="links-group">
            ${s.source_url ? `<a href="${s.source_url}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-xs bl-btn-cyber">Original Source ↗</a>` : ''}
            ${s.license_url ? `<a href="${s.license_url}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-xs bl-btn-outline">License Terms ↗</a>` : ''}
          </div>
          <span class="source-audit-tag">${isOriginal ? '© 2026 BLUEGUN' : 'Audited & documented in data/sources.json'}</span>
        </div>
      </article>
    `;
  }

  function sectionBlock(title, tag, tagClass, items, emptyMsg = '') {
    return items.length === 0 ? '' : `
      <section class="credits-section-block">
        <div class="credits-section-header">
          <h2 class="credits-section-title">${title}</h2>
          <span class="panel-tag ${tagClass}">${tag}</span>
        </div>
        <div class="credits-sources-stream">${items.map(sourceCard).join('')}</div>
      </section>
    `;
  }

  // ─── ORIGINAL SECTION GROUPS ────────────────────────────────────────────────
  const coreOriginals      = origList.filter(s => s.category === 'BLUEGUN ORIGINAL WORK');
  const clubIntOrig        = origList.filter(s => s.category === 'NEW FEATURES — CLUB INTELLIGENCE');
  const availOrig          = origList.filter(s => s.category === 'NEW FEATURES — AVAILABILITY SYSTEM');
  const crOrig             = origList.filter(s => s.category === 'NEW FEATURES — COPYRIGHT SYSTEM');
  const metricsOrig        = origList.filter(s => s.category === 'BLUEGUN SCOUTING METRICS');

  // ─── THIRD-PARTY SECTION GROUPS ────────────────────────────────────────────
  const injSuspData        = thirdList.filter(s => s.category.includes('INJURY') || s.category.includes('SUSPENSION'));
  const transferData       = thirdList.filter(s => s.category === 'TRANSFER DATA');
  const playerData         = thirdList.filter(s => s.category === 'PLAYER DATA' || s.category === 'FOOTBALL DATA');
  const clubData           = thirdList.filter(s => s.category === 'CLUB DATA');
  const playerImgs         = thirdList.filter(s => s.type === 'image');
  const clubLogos          = thirdList.filter(s => s.type === 'logo');
  const newsData           = thirdList.filter(s => s.type === 'news');
  const apis               = thirdList.filter(s => s.type === 'api');
  const fonts              = thirdList.filter(s => s.type === 'font');
  const icons              = thirdList.filter(s => s.type === 'icon');
  const libs               = thirdList.filter(s => s.type === 'library');
  const aiAssets           = thirdList.filter(s => s.type === 'ai');
  const devTools           = thirdList.filter(s => s.type === 'tool' || s.type === 'infrastructure');
  const reviewRequired     = list.filter(s => s.status === 'REVIEW REQUIRED');

  const today = new Date().toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric' });

  return `
    <div class="bl-credits-view">

      <!-- ═══════════════════════════════════════════════════════════════
           PAGE HEADER
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-header bl-hud-panel">
        <div class="hud-corner top-left"></div>
        <div class="hud-corner top-right"></div>
        <div class="hud-corner bottom-left"></div>
        <div class="hud-corner bottom-right"></div>

        <div class="compliance-header-content">
          <span class="compliance-kicker">BLUEGUN MASTER PROVENANCE REGISTER // AUDIT ID: 2026-BG-SRC-v${AUDIT_METADATA.version}</span>
          <h1 class="compliance-title">BLUEGUN — COPYRIGHT, CREDITS &amp; SOURCES</h1>
          <p class="compliance-subtitle">
            "Transparency for every asset, dataset, library and external resource used by BLUEGUN.<br>
            Protecting BLUEGUN's genuinely original work while accurately respecting everyone else's intellectual property."
          </p>
          <div class="credits-meta-row">
            <span class="audit-chip">🔵 BLUEGUN Original Items: <strong>${counts.original}</strong></span>
            <span class="audit-chip">📁 Third-Party Items: <strong>${counts.thirdParty}</strong></span>
            <span class="audit-chip">🟢 Verified: <strong>${counts.verified}</strong></span>
            <span class="audit-chip">🟡 Review Required: <strong>${counts.reviewRequired}</strong></span>
            <span class="audit-chip">📅 Last Audit: <strong>${AUDIT_METADATA.last_audit_date}</strong></span>
          </div>
        </div>
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SEARCH & FILTER BAR
      ═══════════════════════════════════════════════════════════════ -->
      <div class="credits-filter-bar bl-hud-panel">
        <div class="search-input-wrap">
          <input type="text" id="creditsSearchInput" class="bl-input"
            placeholder="Search sources by ID, name, creator, license, feature, or component..."
            value="${searchQuery}" aria-label="Search source registry" />
        </div>
        <div class="filter-chips-group credits-category-filters">
          ${['ALL','ORIGINAL','IMAGES','LOGOS','DATA','NEWS','FONTS','LIBRARIES','APIS','AI','TOOLS','UNVERIFIED'].map(cat => `
            <button class="filter-chip ${categoryFilter === cat ? 'active' : ''}" data-credits-filter="${cat}">
              ${cat}
            </button>
          `).join('')}
        </div>
      </div>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 1 — BLUEGUN ORIGINAL WORK
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel original-content-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 1. BLUEGUN ORIGINAL WORK — 2026 <span class="title-bracket">]</span></h2>
          <span class="panel-tag cyan">PROPRIETARY IP</span>
        </div>

        <div class="legal-notice-box">
          <h3 class="legal-box-title">
            © 2026 BLUEGUN — Original software, interface design and project-specific content. All rights reserved, subject to applicable law and third-party rights.
          </h3>
          <p>
            The following software, interface designs, algorithmic systems, branding elements, and analytical features are <strong>original intellectual creations developed specifically for the BLUEGUN project</strong>. They are not derived from, copied from, or owned by any third party.
          </p>
          <p>
            <strong>Important:</strong> BLUEGUN does not claim copyright over any third-party content, data, photographs, trademarks, statistics, or other materials used within the platform. All such third-party materials are separately documented below.
          </p>
          <div class="original-assets-grid">
            <div class="asset-bullet">🔵 <strong>BLUEGUN Name &amp; Tagline:</strong> "ENTER THE TRANSFER BATTLEFIELD." — Original brand identity</div>
            <div class="asset-bullet">🔵 <strong>BLUEGUN Vector Logo:</strong> Custom SVG hexagonal cyber geometry — original artwork</div>
            <div class="asset-bullet">🔵 <strong>UI/UX Design System:</strong> Cyber HUD panels, glow cards, layouts, and visual design language</div>
            <div class="asset-bullet">🔵 <strong>CSS Design Tokens:</strong> main.css, components.css, sections.css, responsive.css</div>
            <div class="asset-bullet">🔵 <strong>JavaScript SPA Router:</strong> Custom ES6 single-page application architecture (js/app.js)</div>
            <div class="asset-bullet">🔵 <strong>UI Component Library:</strong> Player cards, club cards, transfer cards, news cards (js/components.js)</div>
            <div class="asset-bullet">🔵 <strong>FastAPI Backend:</strong> All Python backend routes, models, schemas, and database architecture</div>
            <div class="asset-bullet">🔵 <strong>Database Architecture:</strong> Original SQLite/PostgreSQL relational schema design</div>
            <div class="asset-bullet">🔵 <strong>Global Search System:</strong> Accent-insensitive Unicode search (frontend + backend)</div>
            <div class="asset-bullet">🔵 <strong>Player Comparison Interface:</strong> Ego Clash radar and head-to-head system</div>
            <div class="asset-bullet">🔵 <strong>SVG Radar Chart Engine:</strong> Zero-dependency pure-math polygon visualizer (js/chart.js)</div>
            <div class="asset-bullet">🔵 <strong>Market Value Chart Engine:</strong> Original SVG line chart renderer</div>
            <div class="asset-bullet">🔵 <strong>CSS Animations:</strong> Pulse, scanline, grid overlay, and glow keyframe effects</div>
            <div class="asset-bullet">🔵 <strong>Responsive Mobile Design:</strong> Mobile drawer, touch optimization, responsive breakpoints</div>
            <div class="asset-bullet">🔵 <strong>Transfer War Room Interface:</strong> Original dashboard layout and information architecture</div>
            <div class="asset-bullet">🔵 <strong>Player Scouting File Interface:</strong> Original player profile design and layout</div>
            <div class="asset-bullet highlight">🔵 <strong>EGO RATING:</strong> Proprietary player impact mathematical engine</div>
            <div class="asset-bullet highlight">🔵 <strong>TRANSFER MOMENTUM:</strong> Algorithmic negotiation velocity tracking</div>
            <div class="asset-bullet highlight">🔵 <strong>MARKET PRESSURE:</strong> Mathematical spread valuation index</div>
            <div class="asset-bullet highlight">🔵 <strong>TRANSFER PROBABILITY:</strong> Multi-parameter predictive analytical model</div>
            <div class="asset-bullet highlight">🔵 <strong>SCOUTING SCORE:</strong> Composite player assessment formula</div>
            <div class="asset-bullet highlight">🔵 <strong>MARKET THREAT:</strong> Competitive acquisition risk indicator</div>
          </div>
          <div class="legal-disclaimer-box" style="margin-top:20px;">
            ⚠️ <strong>Analytical Metrics Disclaimer:</strong> BLUEGUN analytical metrics (EGO RATING, TRANSFER MOMENTUM, MARKET PRESSURE, TRANSFER PROBABILITY, SCOUTING SCORE, MARKET THREAT) are proprietary project features and calculations and <strong>should not be interpreted as official football statistics or predictions</strong>.
          </div>
        </div>

        ${coreOriginals.length > 0 ? `
          <div class="credits-sources-stream" style="margin-top:24px;">
            ${coreOriginals.map(sourceCard).join('')}
          </div>
        ` : ''}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 2 — NEW FEATURES & UPDATES
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel original-content-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 2. NEW FEATURES &amp; UPDATES — BLUEGUN ORIGINAL <span class="title-bracket">]</span></h2>
          <span class="panel-tag cyan">ORIGINAL SOFTWARE</span>
        </div>
        <div class="legal-notice-box">
          <p>The following newly developed features are original BLUEGUN software interfaces. While the interface designs are original BLUEGUN work, <strong>the underlying football data displayed within these features (squad information, injuries, suspensions, contracts, transfer history) is third-party data subject to its respective source terms</strong>.</p>
        </div>
        ${[...clubIntOrig, ...availOrig, ...crOrig].length > 0 ? `
          <div class="credits-sources-stream">
            ${[...clubIntOrig, ...availOrig, ...crOrig].map(sourceCard).join('')}
          </div>
        ` : '<p class="empty-state">No new feature entries in current filter.</p>'}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 3 — BLUEGUN SCOUTING METRICS
      ═══════════════════════════════════════════════════════════════ -->
      ${metricsOrig.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 3. BLUEGUN SCOUTING METRICS — PROPRIETARY CALCULATIONS <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">PROPRIETARY ALGORITHM</span>
        </div>
        <div class="legal-notice-box">
          <p><strong>BLUEGUN analytical metrics are proprietary project features/calculations and should not be interpreted as official football statistics or predictions.</strong> These metrics are original algorithmic implementations developed specifically for this project and do not represent FIFA, UEFA, or any club's official assessments.</p>
        </div>
        <div class="credits-sources-stream">${metricsOrig.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 4 — PLAYER DATA SOURCES (THIRD-PARTY)
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 4. PLAYER DATA SOURCES — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">THIRD-PARTY DATA</span>
        </div>
        <div class="legal-notice-box">
          <div class="ownership-split-grid">
            <div class="ownership-col ownership-col--original">
              <h4>🔵 BLUEGUN ORIGINAL (Interface &amp; Calculations)</h4>
              <ul>
                <li>Player card design &amp; layout</li>
                <li>Player scouting file interface</li>
                <li>Player comparison interface (Ego Clash)</li>
                <li>Radar chart visualization engine</li>
                <li>Market value chart engine</li>
                <li>Scouting analytical metrics</li>
                <li>Search &amp; filtering system</li>
              </ul>
            </div>
            <div class="ownership-col ownership-col--third">
              <h4>⚠️ THIRD-PARTY (Data — Not Owned by BLUEGUN)</h4>
              <ul>
                <li>Player statistics (goals, assists, etc.)</li>
                <li>Market valuations (Transfermarkt benchmark)</li>
                <li>Transfer history facts</li>
                <li>Injury &amp; suspension records</li>
                <li>Player photographs (see Image Credits)</li>
                <li>Club membership &amp; squad data</li>
                <li>Contract details</li>
              </ul>
            </div>
          </div>
          <p class="legal-note">⚠️ BLUEGUN does not claim ownership of player statistics, market valuations, transfer facts, injury records, or photographs. All player data is illustrative/demo data. See individual source registry entries for attribution details.</p>
        </div>
        ${playerData.length > 0 ? `<div class="credits-sources-stream">${playerData.map(sourceCard).join('')}</div>` : ''}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 5 — TRANSFER DATA SOURCES
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 5. TRANSFER DATA SOURCES — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">THIRD-PARTY DATA</span>
        </div>
        <div class="legal-notice-box">
          <p><strong>Transfer information is provided by third-party data sources and remains subject to their respective terms, licences and attribution requirements.</strong></p>
          <p>All 2026 transfer records displayed by BLUEGUN are <strong>illustrative/demo data</strong>. They should not be relied upon as factual. Every transfer record retains: source, source URL, provider, retrieval date, last updated date, and licence information where available.</p>
        </div>
        ${transferData.length > 0 ? `<div class="credits-sources-stream">${transferData.map(sourceCard).join('')}</div>`
          : `<div class="legal-notice-box"><p class="legal-note">🟡 All transfer data currently displayed is illustrative demo data — SOURCE VERIFICATION REQUIRED for each individual transfer before publication. Refer to Sky Sports, Fabrizio Romano, official club announcements, and Transfermarkt for verified records.</p></div>`}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 6 — INJURY & SUSPENSION DATA
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 6. INJURY &amp; SUSPENSION DATA — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">THIRD-PARTY DATA</span>
        </div>
        <div class="legal-notice-box">
          <p>The <strong>Injury Center</strong> and <strong>Suspension Center</strong> interfaces are original BLUEGUN software designs. However, the underlying injury and suspension records are <strong>third-party data</strong> and remain the property of their respective sports data providers.</p>
          <p>All injury/suspension data currently displayed is <strong>illustrative/demo data</strong> — SOURCE VERIFICATION REQUIRED before publication. Reference Physioroom.com, BBC Sport, and official club medical announcements for verified records.</p>
        </div>
        ${injSuspData.length > 0 ? `<div class="credits-sources-stream">${injSuspData.map(sourceCard).join('')}</div>` : ''}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 7 — CLUB DATA SOURCES
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 7. CLUB DATA SOURCES — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">THIRD-PARTY DATA</span>
        </div>
        <div class="legal-notice-box">
          <p>Squad information, contract figures, club statistics, and transfer history displayed within the <strong>Club Intelligence</strong> feature are <strong>third-party data</strong> and remain the property of the respective football clubs, official leagues, and data providers.</p>
          <p>If a source cannot be verified, it is displayed as: <strong>SOURCE VERIFICATION REQUIRED</strong>. We do not invent attribution.</p>
        </div>
        ${clubData.length > 0 ? `<div class="credits-sources-stream">${clubData.map(sourceCard).join('')}</div>` : ''}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 8 — PLAYER IMAGE CREDITS
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 8. PLAYER IMAGE CREDITS — THIRD-PARTY PHOTOGRAPHS <span class="title-bracket">]</span></h2>
          <span class="panel-tag">THIRD-PARTY IMAGES</span>
        </div>
        <div class="legal-notice-box">
          <p>Player portrait photographs are <strong>not owned by BLUEGUN</strong>. All photographs are sourced under documented Creative Commons licences with individual creator credits. BLUEGUN does not claim copyright over any player photograph.</p>
          <p>Every image entry stores: image URL, creator/photographer, copyright holder, source, licence, licence URL, attribution text, and date accessed.</p>
        </div>
        ${playerImgs.length > 0
          ? `<div class="credits-sources-stream">${playerImgs.map(sourceCard).join('')}</div>`
          : '<p class="empty-state">No image entries match current filter.</p>'}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 9 — CLUB & LEAGUE TRADEMARK NOTICE
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 9. CLUB &amp; LEAGUE TRADEMARK NOTICE <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">TRADEMARKS</span>
        </div>
        <div class="legal-notice-box">
          <p><strong>Football club names, badges, crests, logos, and trademarks are the property of their respective clubs and are not owned by BLUEGUN.</strong> Club logos and badges displayed on this platform are used for informational/editorial purposes only and are not endorsed by the clubs.</p>
          <p>League names (Premier League, La Liga, Bundesliga, Serie A, Ligue 1, etc.) are trademarks of their respective governing bodies. BLUEGUN is not affiliated with any football club, league, or governing body.</p>
        </div>
        ${logoList.length > 0
          ? `<div class="credits-sources-stream">${logoList.map(sourceCard).join('')}</div>`
          : ''}
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 10 — NEWS SOURCES
      ═══════════════════════════════════════════════════════════════ -->
      ${newsList.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 10. NEWS SOURCES — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">THIRD-PARTY NEWS</span>
        </div>
        <div class="legal-notice-box">
          <p>Transfer news headlines and summaries displayed by BLUEGUN are sourced from third-party sports media outlets. BLUEGUN does not own this news content. Full source attribution is included for every news item.</p>
        </div>
        <div class="credits-sources-stream">${newsList.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 11 — APIs & DATA SERVICES
      ═══════════════════════════════════════════════════════════════ -->
      ${apis.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 11. APIS &amp; DATA SERVICES <span class="title-bracket">]</span></h2>
          <span class="panel-tag">THIRD-PARTY</span>
        </div>
        <div class="credits-sources-stream">${apis.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 12 — FONTS
      ═══════════════════════════════════════════════════════════════ -->
      ${fonts.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 12. FONTS — THIRD-PARTY <span class="title-bracket">]</span></h2>
          <span class="panel-tag">TYPOGRAPHY</span>
        </div>
        <div class="credits-sources-stream">${fonts.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 13 — ICONS
      ═══════════════════════════════════════════════════════════════ -->
      ${icons.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 13. ICONS <span class="title-bracket">]</span></h2>
          <span class="panel-tag">ICONS</span>
        </div>
        <div class="credits-sources-stream">${icons.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 14 — OPEN-SOURCE LIBRARIES
      ═══════════════════════════════════════════════════════════════ -->
      ${libs.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 14. OPEN-SOURCE LIBRARIES &amp; PACKAGES <span class="title-bracket">]</span></h2>
          <span class="panel-tag">OPEN SOURCE</span>
        </div>
        <div class="credits-sources-stream">${libs.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 15 — AI-GENERATED ASSETS
      ═══════════════════════════════════════════════════════════════ -->
      ${aiAssets.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 15. AI-GENERATED ASSETS <span class="title-bracket">]</span></h2>
          <span class="panel-tag">AI-GENERATED</span>
        </div>
        <div class="credits-sources-stream">${aiAssets.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 16 — DEVELOPMENT TOOLS & INFRASTRUCTURE
      ═══════════════════════════════════════════════════════════════ -->
      ${devTools.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 16. DEVELOPMENT TOOLS &amp; INFRASTRUCTURE <span class="title-bracket">]</span></h2>
          <span class="panel-tag">TOOLS</span>
        </div>
        <div class="credits-sources-stream">${devTools.map(sourceCard).join('')}</div>
      </section>
      ` : ''}

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 17 — BLUE LOCK DISCLAIMER
      ═══════════════════════════════════════════════════════════════ -->
      <section class="compliance-section bl-card bl-hud-panel" style="margin-top: 32px;">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 17. BLUE LOCK INDEPENDENCE DISCLAIMER <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">INDEPENDENT PROJECT</span>
        </div>
        <div class="legal-notice-box">
          <div class="quote-notice">
            "BLUEGUN is an independent football transfer and scouting project and is not affiliated with, endorsed by, sponsored by, or officially connected to Blue Lock or its creators/rightsholders."
          </div>
          <p>
            BLUEGUN does not use, reproduce, or distribute: official Blue Lock character artwork, manga panels, anime screenshots, soundtracks, promotional materials, or any other Blue Lock intellectual property. All BLUEGUN software, UI design, color schemes, vector elements, animations, and written content are <strong>original creations</strong> developed independently for the BLUEGUN project.
          </p>
          <p>
            Blue Lock (ブルーロック) is a manga series by Muneyuki Kaneshiro and Yusuke Nomura, published by Kodansha. All rights belong to the respective rightsholders. BLUEGUN makes no claim to any Blue Lock intellectual property.
          </p>
        </div>
      </section>

      <!-- ═══════════════════════════════════════════════════════════════
           SECTION 18 — UNVERIFIED SOURCES REQUIRING REVIEW
      ═══════════════════════════════════════════════════════════════ -->
      ${reviewRequired.length > 0 ? `
      <section class="compliance-section bl-card bl-hud-panel" style="border-color: var(--neon-gold, #ffd700);">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 18. UNVERIFIED SOURCES — REVIEW REQUIRED <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">🟡 ACTION REQUIRED</span>
        </div>
        <div class="legal-notice-box">
          <p>⚠️ The following <strong>${reviewRequired.length} source(s)</strong> require manual licence/attribution verification before the platform can be considered fully compliant. We do not claim ownership or verified attribution for these items until review is complete.</p>
        </div>
        <div class="credits-sources-stream">${reviewRequired.map(sourceCard).join('')}</div>
      </section>
      ` : `
      <section class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 18. UNVERIFIED SOURCES <span class="title-bracket">]</span></h2>
          <span class="panel-tag">STATUS</span>
        </div>
        <div class="legal-notice-box">
          <p>🟢 No unverified sources detected in current filter. All registered resources are either documented as BLUEGUN ORIGINAL or carry verified licence attribution.</p>
        </div>
      </section>
      `}

      <!-- ═══════════════════════════════════════════════════════════════
           FINAL COPYRIGHT NOTICE
      ═══════════════════════════════════════════════════════════════ -->
      <section class="final-copyright-section bl-hud-panel">
        <div class="final-copyright-box">
          <h3 class="final-cr-title">© 2026 BLUEGUN</h3>
          <p class="final-cr-text">
            © 2026 BLUEGUN. Original project software, interface and project-specific content are protected to the extent permitted by applicable law. Third-party data, images, trademarks, logos, software and other materials belong to their respective owners and are used according to applicable permissions, licences and terms.
          </p>
          <p class="final-cr-text" style="margin-top:12px; opacity: 0.7; font-size: 13px;">
            BLUEGUN is an independent project. It is not affiliated with any football club, player, league, governing body, or the Blue Lock franchise. All analytical metrics are project features only and not official football assessments.
          </p>
          <div class="final-audit-badge">

/**
 * Backward compatibility alias for renderCopyrightAndAttributionView
 */
export function renderCopyrightAndAttributionView() {
  return renderCreditsView('ALL', '');
}

/**
 * Source Inspector Modal Content Generator
 */
export function renderSourceModalContent(sourceId) {
  const source = getSourceById(sourceId) || {
    id: sourceId,
    name: "Third-Party Football Intelligence Asset",
    category: "FOOTBALL DATA",
    creator: "API-Football / Transfermarkt Public Benchmark",
    copyright_holder: "Respective Data Provider",
    license: "Editorial Reference & Public Valuation Benchmark",
    source_url: "https://www.transfermarkt.com",
    license_url: "https://www.transfermarkt.com/intern/impressum",
    status: "VERIFIED",
    attribution_text: "Benchmarked against public sports data registries.",
    date_accessed: "2026-08-25",
    used_in: ["Player Profile", "Transfer Cards"]
  };

  return `
    <div class="source-modal-details">
      <div class="source-modal-head">
        <div>
          <span class="source-id-tag">${source.id}</span>
          <h2 class="source-modal-title">${source.name}</h2>
          <span class="source-modal-cat">${source.category}</span>
        </div>
        <div>${getSourceStatusBadge(source.status)}</div>
      </div>

      <div class="source-modal-grid">
        <div class="s-m-cell">
          <span class="lbl">CREATOR / PROVIDER:</span>
          <strong>${source.creator || 'N/A'}</strong>
        </div>
        <div class="s-m-cell">
          <span class="lbl">COPYRIGHT HOLDER:</span>
          <strong>${source.copyright_holder || 'N/A'}</strong>
        </div>
        <div class="s-m-cell">
          <span class="lbl">LICENSE:</span>
          <strong class="cyan">${source.license || 'SOURCE / LICENSE VERIFICATION REQUIRED'}</strong>
        </div>
        <div class="s-m-cell">
          <span class="lbl">LAST VERIFIED:</span>
          <strong>${source.date_accessed || '2026-08-25'}</strong>
        </div>
      </div>

      ${source.attribution_text ? `
        <div class="source-modal-attr">
          <span class="lbl">ATTRIBUTION TEXT:</span>
          <p>${source.attribution_text}</p>
        </div>
      ` : ''}

      <div class="source-modal-used">
        <span class="lbl">USED IN:</span>
        <div class="used-in-tags">
          ${(source.used_in || []).map(u => `<span class="used-tag">${u}</span>`).join('')}
        </div>
      </div>

      <div class="source-modal-actions">
        ${source.source_url ? `<a href="${source.source_url}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-sm bl-btn-cyber">Original Source ↗</a>` : ''}
        ${source.license_url ? `<a href="${source.license_url}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-sm bl-btn-outline">License Terms ↗</a>` : ''}
        <button class="bl-btn bl-btn-sm bl-btn-outline" onclick="window.bluegunApp.navigateTo('credits'); window.bluegunApp.closeSourceModal();">
          <span>View in Credits Registry →</span>
        </button>
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
            <strong>© 2026 BLUEGUN. Original project software, interface and project-specific content are protected to the extent permitted by applicable law. Third-party data, images, trademarks, logos, software and other materials belong to their respective owners and are used according to applicable permissions, licences and terms.</strong>
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
            <li><a href="#credits" class="footer-nav-link highlight" data-view="credits">⚖️ Copyright & Sources</a></li>
            <li><a href="#privacy" class="footer-legal-modal-trigger" data-modal="privacy">🔒 Privacy Policy</a></li>
            <li><a href="#terms" class="footer-legal-modal-trigger" data-modal="terms">📜 Terms of Use</a></li>
            <li><a href="#credits" class="footer-nav-link" data-view="credits">📊 Data Providers & APIs</a></li>
            <li><a href="mailto:intel@bluegun.football" class="footer-ext-link">📬 Contact Compliance</a></li>
          </ul>
        </div>

        <!-- Disclaimers & Attribution Note -->
        <div class="footer-col disclaimer-col">
          <h4 class="footer-heading">INTELLECTUAL PROPERTY</h4>
          <div class="footer-disclaimer-box">
            <p class="disclaimer-p">
              <strong>Trademarks:</strong> Football club names, logos, badges and trademarks belong to their respective owners.
            </p>
            <p class="disclaimer-p">
              <strong>Blue Lock Notice:</strong> BLUEGUN is an independent football transfer and scouting project. BLUEGUN is not affiliated with, endorsed by, sponsored by, or officially connected to Blue Lock or its creators/rightsholders.
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
          <span class="status-indicator">🟢 2026 INTELLIGENCE ONLINE // AUDIT VERIFIED</span>
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
        Football club names, logos, badges, competition trademarks, and player photography remain the property of their respective creators and owners.
      </p>

      <h3>4. No Warranty</h3>
      <p>
        The software is provided "as is", without warranty of any kind, express or implied.
      </p>
    </div>
  `;
}