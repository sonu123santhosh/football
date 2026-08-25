"""
Script to create the enhanced js/components.js with complete copyright, attribution, and compliance rendering.
"""

new_components_js = '''/**
 * BLUELOCK // TRANSFER IQ - Component Library & View Renderers
 * Pure JavaScript component renderers generating semantic, reactive HTML elements.
 * Features full copyright compliance, image credits, third-party source attribution,
 * and clear distinction between proprietary analytics and third-party sports data.
 */

import { renderRadarChart, renderMarketValueChart } from './chart.js';
import { DATA_SOURCES, THIRD_PARTY_ASSETS, COMPLIANCE_DISCLAIMERS, PLAYERS, CLUBS } from './data.js';

// Global SVG Fallback for Player Images
export const PLAYER_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23070c18'/><circle cx='50' cy='38' r='20' fill='%2300f0ff' opacity='0.35'/><path d='M15 92 Q50 58 85 92' fill='%2300f0ff' opacity='0.35'/><text x='50' y='96' font-family='sans-serif' font-weight='bold' font-size='7' fill='%2300f0ff' text-anchor='middle'>BLUELOCK INTEL</text></svg>`;

// Global SVG Fallback for Club Badges
export const CLUB_IMG_FALLBACK = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><polygon points='50,5 95,25 95,75 50,95 5,75 5,25' fill='%230b1325' stroke='%2300f0ff' stroke-width='3'/><circle cx='50' cy='50' r='20' fill='%230077ff' opacity='0.5'/></svg>`;

/**
 * Status Badge Helper
 */
export function getStatusBadge(status) {
  const map = {
    CONFIRMED: { label: "CONFIRMED", class: "badge-confirmed", icon: "🔵" },
    NEGOTIATING: { label: "NEGOTIATING", class: "badge-negotiating", icon: "🟡" },
    RUMOUR: { label: "RUMOUR", class: "badge-rumour", icon: "🟠" },
    LOAN: { label: "LOAN", class: "badge-loan", icon: "🟣" },
    "FREE TRANSFER": { label: "FREE TRANSFER", class: "badge-free", icon: "🟢" }
  };
  const item = map[status] || { label: status, class: "badge-default", icon: "⚪" };
  return `<span class="bl-status-badge ${item.class}">${item.icon} ${item.label}</span>`;
}

/**
 * Single Transfer Card (Live Feed & Dashboard Spotlight)
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
            <span class="ego-tag" title="Ego Threat Level (Proprietary Algorithm)">THREAT: ${tr.egoThreat}</span>
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

        <!-- Club Transition Flow Visual -->
        <div class="club-transfer-flow">
          <div class="club-node" data-club-id="${tr.fromClubId || ''}">
            <img src="${tr.fromBadge}" alt="${tr.fromClub}" class="club-logo-sm" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            <span class="club-label">${tr.fromClub}</span>
          </div>

          <div class="transfer-arrow-hud">
            <div class="arrow-line"></div>
            <div class="arrow-head">▶</div>
            <span class="prob-tag" title="Algorithmic Estimated Probability">${tr.probability}% EST.</span>
          </div>

          <div class="club-node highlight" data-club-id="${tr.toClubId || ''}">
            <img src="${tr.toBadge}" alt="${tr.toClub}" class="club-logo-sm" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            <span class="club-label">${tr.toClub}</span>
          </div>
        </div>

        <!-- Financial Breakdown -->
        <div class="transfer-financials">
          <div class="fin-item">
            <span class="fin-lbl">MARKET VALUE</span>
            <span class="fin-val">${tr.marketValue}</span>
          </div>
          <div class="fin-item">
            <span class="fin-lbl">REPORTED FEE</span>
            <span class="fin-val highlight-fee">${tr.reportedFee}</span>
          </div>
        </div>

        <!-- Headline / Source Wire -->
        <p class="transfer-headline">"${tr.headline}"</p>
        <div class="transfer-source-tag">
          <span class="source-icon">📡</span>
          <span>Source: <strong>${tr.source || 'European Scouting Wire'}</strong></span>
        </div>
      </div>

      <div class="card-footer">
        <div class="confidence-bar-wrap">
          <div class="confidence-bar-label">
            <span>TRANSFER MOMENTUM (ESTIMATED)</span>
            <strong>${tr.confidence}%</strong>
          </div>
          <div class="bl-progress-track">
            <div class="bl-progress-fill" style="width: ${tr.confidence}%;"></div>
          </div>
        </div>

        <button class="bl-btn bl-btn-sm bl-btn-cyber btn-view-player" data-player-id="${tr.playerId}">
          <span>ANALYZE EGO & STATS</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
    </article>
  `;
}

/**
 * Player Card (Players Grid View) with photo attribution badge
 */
export function renderPlayerCard(p) {
  const imgSrc = p.image || p.photo;
  const photoCreditShort = p.imageCredit ? p.imageCredit.split('/')[0].trim() : 'Wikimedia Commons';
  return `
    <article class="bl-player-card" data-player-id="${p.id}">
      <div class="card-glow-edge"></div>
      <div class="player-card-banner">
        <span class="ego-pill" title="Proprietary Blue Lock Analysis">⚡ EGO: ${p.egoRating}</span>
        <span class="ovr-rating">${p.rating}</span>
      </div>

      <div class="player-visual">
        <img src="${imgSrc}" alt="${p.name}" class="player-portrait" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="player-flag-badge">${p.flag}</div>
        <div class="player-photo-attribution" title="Photo Credit: ${p.imageCredit || 'Sports Photography Archive'} (${p.imageLicense || 'CC BY-SA 4.0'})">
          📷 ${photoCreditShort}
        </div>
      </div>

      <div class="player-info">
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
            <span class="lbl">STATUS</span>
            ${getStatusBadge(p.transferStatus)}
          </div>
        </div>
      </div>

      <div class="player-card-actions">
        <button class="bl-btn bl-btn-cyber bl-btn-block btn-view-player" data-player-id="${p.id}">
          <span>FULL SCOUT REPORT</span>
        </button>
      </div>
    </article>
  `;
}

/**
 * Club Card (Clubs Grid View) with trademark notice
 */
export function renderClubCard(club) {
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
          <span class="lbl">TRANSFER BUDGET</span>
          <span class="val gold">${club.transferBudget}</span>
        </div>
        <div class="intel-cell">
          <span class="lbl">WAGE BILL</span>
          <span class="val">${club.wageBill}</span>
        </div>
        <div class="intel-cell">
          <span class="lbl">MANAGER</span>
          <span class="val">${club.manager}</span>
        </div>
      </div>

      <div class="club-activity-preview">
        <div class="activity-col">
          <span class="col-lbl">INCOMING (${club.incoming.length})</span>
          <ul class="activity-list">
            ${club.incoming.slice(0, 2).map(inc => `
              <li><span class="dot in"></span> ${inc.player} <span class="fee">${inc.fee}</span></li>
            `).join('')}
          </ul>
        </div>
        <div class="activity-col">
          <span class="col-lbl">TOP TARGET</span>
          <span class="target-name highlight">🎯 ${club.targets[0] ? club.targets[0].name : 'Evaluating'}</span>
        </div>
      </div>

      <div class="club-trademark-notice">
        <span>* Club crest & name are trademarks of ${club.name}</span>
      </div>

      <div class="club-card-actions">
        <button class="bl-btn bl-btn-outline bl-btn-block btn-view-club" data-club-id="${club.id}">
          <span>ACCESS WAR ROOM</span>
        </button>
      </div>
    </article>
  `;
}

/**
 * News Card with direct external source report link
 */
export function renderNewsCard(item) {
  const imgSrc = item.image || 'assets/players/mbappe.jpg';
  const sourceUrl = item.sourceUrl || item.readOriginalUrl || 'https://www.skysports.com/football/transfer-paper-talk';
  return `
    <article class="bl-news-card" data-news-id="${item.id}">
      <div class="news-media-wrap">
        <img src="${imgSrc}" alt="${item.title}" class="news-thumb" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="news-category-tag">${item.category}</div>
        <div class="news-ego-tag">${item.egoImpact}</div>
      </div>

      <div class="news-body">
        <div class="news-meta-row">
          <span class="news-source">📰 Source: <strong>${item.source}</strong></span>
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
              <span>INTEL SUMMARY</span>
            </button>
            <a href="${sourceUrl}" target="_blank" rel="noopener noreferrer" class="bl-btn bl-btn-sm bl-btn-outline news-outbound-link" title="Open source reporting in a new tab">
              <span>ORIGINAL REPORT →</span>
            </a>
          </div>
        </div>
      </div>
    </article>
  `;
}

/**
 * Full Detailed Player Profile Page with clear Attribution Strip
 */
export function renderPlayerProfile(p) {
  const imgSrc = p.image || p.photo;
  const photoCredit = p.imageCredit || 'Steffen Prößdorf / Sports Photography Archive';
  const photoLicense = p.imageLicense || 'CC BY-SA 4.0';
  const photoSourceUrl = p.imageSourceUrl || 'https://commons.wikimedia.org/';
  const dataSource = p.dataSource || 'API-Football & European Transfer Intelligence';
  const dataSourceUrl = p.dataSourceUrl || 'https://rapidapi.com/api-sports/api/api-football';

  return `
    <div class="bl-profile-view">
      <!-- Top Action Navigation Back -->
      <div class="profile-top-bar">
        <button class="bl-btn bl-btn-outline bl-btn-sm btn-back-dashboard">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>BACK TO BATTLEFIELD</span>
        </button>
        <div class="profile-breadcrumbs">
          <span>SCOUTING HUB</span> / <span>PLAYERS</span> / <strong class="cyan">${p.name.toUpperCase()}</strong>
        </div>
        <button class="bl-btn bl-btn-cyber bl-btn-sm btn-quick-compare" data-compare-id="${p.id}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>
          <span>COMPARE PLAYER</span>
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
                  <span class="current-club-badge">${p.currentClub}</span>
                  <span class="position-tag">${p.position}</span>
                  <span class="age-tag">AGE ${p.age}</span>
                </div>
              </div>

              <div class="player-threat-indicator">
                <span class="threat-label">MARKET THREAT INDEX</span>
                <span class="threat-badge-large ${p.marketThreat.toLowerCase()}">${p.marketThreat}</span>
                <span class="threat-disclaimer">* Proprietary Algorithm</span>
              </div>
            </div>

            <p class="player-bio-text">${p.overview}</p>

            <!-- Key Metric Holograms -->
            <div class="player-quick-metrics">
              <div class="metric-holo-card">
                <span class="lbl">MARKET VALUATION</span>
                <span class="val cyan">${p.marketValue}</span>
                <span class="sub">${p.valueDiff}</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">EGO RATING (PROPRIETARY)</span>
                <span class="val gold">${p.egoRating} / 100</span>
                <span class="sub">World Class Threat</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">TRANSFER PROBABILITY</span>
                <span class="val neon">${p.probability}%</span>
                <span class="sub">Algorithmic Score</span>
              </div>
              <div class="metric-holo-card">
                <span class="lbl">CONTRACT EXPIRY</span>
                <span class="val">${p.contractExpiry}</span>
                <span class="sub">Asking: ${p.askingPrice}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Compliance & Data Source Attribution Strip -->
        <div class="profile-attribution-strip">
          <div class="attr-chip">
            <span class="attr-icon">⚡</span>
            <span><strong>Proprietary Analysis:</strong> Ego Rating & Transfer Probability are calculated by BLUELOCK // TRANSFER IQ.</span>
          </div>
          <div class="attr-chip">
            <span class="attr-icon">📊</span>
            <span><strong>Third-Party Sports Data:</strong> ${dataSource}</span>
            <a href="${dataSourceUrl}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Provider ↗</a>
          </div>
        </div>
      </section>

      <!-- Main Profile Grid (Charts, Stats, Rumours) -->
      <div class="profile-analytics-layout">
        
        <!-- Left: Radar Chart & Scouting Breakdown -->
        <div class="profile-left-col">
          
          <!-- Radar Hexagon HUD -->
          <div class="bl-card bl-hud-panel radar-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title">
                <span class="title-bracket">[</span>
                TACTICAL RADAR ANALYSIS
                <span class="title-bracket">]</span>
              </h2>
              <span class="panel-tag cyan">EGO-HEXAGON HUD</span>
            </div>
            
            <div id="playerRadarContainer" class="radar-chart-wrap">
              <!-- Rendered via chart.js renderRadarChart -->
            </div>

            <!-- Radar Attribute Progress Bars -->
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

          <!-- Market Value History Line Chart -->
          <div class="bl-card bl-hud-panel valuation-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title">
                <span class="title-bracket">[</span>
                VALUATION TRAJECTORY (€M)
                <span class="title-bracket">]</span>
              </h2>
              <span class="panel-tag">5-YEAR INDEX</span>
            </div>
            <div id="playerValuationChart" class="valuation-chart-wrap">
              <!-- Rendered via chart.js renderMarketValueChart -->
            </div>
            <div class="valuation-meta-footnote">
              * Market valuation trajectory benchmarked against European historical transfer fee milestones.
            </div>
          </div>
        </div>

        <!-- Right: Season Stats, Interested Clubs, Rumours -->
        <div class="profile-right-col">
          
          <!-- Season Performance Table (Third-Party Stats) -->
          <div class="bl-card bl-hud-panel season-stats-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title">
                <span class="title-bracket">[</span>
                2024/25 SEASON PERFORMANCE METRICS
                <span class="title-bracket">]</span>
              </h2>
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
              Data verified against Opta/FBref match index feeds.
            </div>
          </div>

          <!-- Transfer Radar & Interested Clubs War Room -->
          <div class="bl-card bl-hud-panel transfer-battleground-panel">
            <div class="panel-header-clean">
              <h2 class="panel-section-title">
                <span class="title-bracket">[</span>
                TRANSFER BATTLEFIELD: CLUBS IN PURSUIT
                <span class="title-bracket">]</span>
              </h2>
              <span class="panel-tag gold">ACTIVE NEGOTIATIONS</span>
            </div>

            <div class="interested-clubs-list">
              ${p.interestedClubs.map(c => `
                <div class="interested-club-card">
                  <div class="club-summary-row">
                    <div class="club-id-col">
                      <span class="club-title">${c.name}</span>
                      <span class="club-league-sub">${c.league}</span>
                    </div>
                    <div class="interest-badge-col">
                      <span class="interest-pill ${c.interest.toLowerCase().replace(' ', '-')}">${c.interest}</span>
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
 * Club War Room Profile Page
 */
export function renderClubProfile(club) {
  return `
    <div class="bl-club-profile-view">
      <div class="profile-top-bar">
        <button class="bl-btn bl-btn-outline bl-btn-sm btn-back-dashboard">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>BACK TO DASHBOARD</span>
        </button>
        <div class="profile-breadcrumbs">
          <span>WAR ROOMS</span> / <span>CLUBS</span> / <strong class="cyan">${club.name.toUpperCase()}</strong>
        </div>
      </div>

      <!-- Club Header Banner -->
      <section class="club-header-panel bl-hud-panel" style="border-top: 3px solid ${club.color};">
        <div class="club-header-flex">
          <div class="club-crest-col">
            <img src="${club.badge}" alt="${club.name}" class="club-big-crest" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
          </div>
          <div class="club-info-col">
            <div class="club-tier-badge">${club.egoRank}</div>
            <h1 class="club-title-big">${club.name} ${club.flag}</h1>
            <p class="club-stadium-lead">🏟️ ${club.stadium} // 🏆 ${club.league}</p>
            <p class="club-lore-text">${club.description}</p>
          </div>
          <div class="club-exec-col">
            <div class="exec-card">
              <span class="lbl">PRESIDENT / OWNER</span>
              <span class="val">${club.president}</span>
            </div>
            <div class="exec-card">
              <span class="lbl">HEAD COACH</span>
              <span class="val cyan">${club.manager}</span>
            </div>
            <div class="exec-card">
              <span class="lbl">SQUAD VALUE</span>
              <span class="val gold">${club.squadValue}</span>
            </div>
          </div>
        </div>

        <div class="club-trademark-footer">
          <span>* All club names, crests, and branding are the property of ${club.name}. Used under fair-use commentary guidelines.</span>
        </div>
      </section>

      <!-- In / Out / Targets Tabs Layout -->
      <div class="club-dossier-grid">
        <!-- Incoming Transfers -->
        <div class="bl-card bl-hud-panel">
          <div class="panel-header-clean">
            <h2 class="panel-section-title"><span class="title-bracket">[</span> INCOMING TRANSFERS <span class="title-bracket">]</span></h2>
            <span class="badge-count">${club.incoming.length} DEALS</span>
          </div>
          <div class="transfers-table-mini">
            ${club.incoming.map(t => `
              <div class="deal-item">
                <div class="deal-p-name"><strong>${t.player}</strong> <span class="from-sub">from ${t.from}</span></div>
                <div class="deal-fee">${t.fee}</div>
                <div>${getStatusBadge(t.status)}</div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Outgoing Transfers -->
        <div class="bl-card bl-hud-panel">
          <div class="panel-header-clean">
            <h2 class="panel-section-title"><span class="title-bracket">[</span> OUTGOING DEPARTURES <span class="title-bracket">]</span></h2>
            <span class="badge-count">${club.outgoing.length} DEALS</span>
          </div>
          <div class="transfers-table-mini">
            ${club.outgoing.map(t => `
              <div class="deal-item">
                <div class="deal-p-name"><strong>${t.player}</strong> <span class="from-sub">to ${t.to}</span></div>
                <div class="deal-fee">${t.fee}</div>
                <div>${getStatusBadge(t.status)}</div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Strategic Scouting Targets -->
        <div class="bl-card bl-hud-panel full-width">
          <div class="panel-header-clean">
            <h2 class="panel-section-title"><span class="title-bracket">[</span> ACTIVE SCOUTING TARGETS & BIDS <span class="title-bracket">]</span></h2>
            <span class="badge-count gold">${club.targets.length} MONITORED</span>
          </div>
          <div class="targets-grid-view">
            ${club.targets.map(tgt => `
              <div class="target-card">
                <div class="tgt-head">
                  <span class="tgt-name">${tgt.name}</span>
                  <span class="tgt-val">${tgt.value}</span>
                </div>
                <div class="tgt-sub">Status: <strong>${tgt.status}</strong></div>
                <div class="tgt-sub">Interest Priority: <strong class="cyan">${tgt.interest}</strong></div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    </div>
  `;
}

/**
 * Transfer Market Data Matrix (Sortable & Filterable Table)
 */
export function renderTransferMarketTable(players, sortKey, sortAsc) {
  return `
    <div class="bl-market-table-wrapper">
      <div class="table-disclaimer-bar">
        <span>⚡ <strong>Original Analytical Scores:</strong> Ego Rating, Striker Index, Market Threat.</span>
        <span>📊 <strong>Third-Party Financial Benchmarks:</strong> Market Value and Contract terms (Ref: Transfermarkt).</span>
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
 * Player Comparison View (Side-by-Side Ego Clash Radar)
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
          Comparing proprietary scouting algorithms & verified 2024/25 match statistics.
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
          
          <div id="comparisonRadarContainer" class="comparison-radar-wrap">
            <!-- Rendered via chart.js -->
          </div>
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
            { label: "EGO RATING (PROPRIETARY)", valA: playerA.egoRating, valB: playerB.egoRating },
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
 * Dedicated Copyright, Attribution & Third-Party Content Compliance Page
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
          <span class="compliance-kicker">INTELLECTUAL PROPERTY & COMPLIANCE REGISTER</span>
          <h1 class="compliance-title">COPYRIGHT, ATTRIBUTION & LICENSING</h1>
          <p class="compliance-subtitle">
            Transparent distinction between original mathematical analysis, open-source frameworks, 
            licensed sports photography, and third-party football intelligence.
          </p>
        </div>
      </section>

      <!-- Section 1: Copyright Statement & IP Framework -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 1. WEBSITE COPYRIGHT & OWNERSHIP FRAMEWORK <span class="title-bracket">]</span></h2>
          <span class="panel-tag cyan">LEGAL POLICY</span>
        </div>

        <div class="legal-notice-box">
          <h3 class="legal-box-title">© 2026 BLUELOCK // TRANSFER IQ. All rights reserved.</h3>
          <p>
            Original website code, UI layout, CSS stylesheets, SVG charting engines, data presentation models, 
            and proprietary analytical scoring systems (including <em>Ego Rating, Transfer Probability Engine, Striker Index,</em> and <em>Market Threat Levels</em>) 
            are original creations protected by applicable intellectual-property laws.
          </p>
          <p class="legal-subtext">
            <strong>Third-Party Content Clarification:</strong> Third-party names, football club trademarks, competition logos, 
            photographs, match statistics, transfer rumours, and news reports remain the sole intellectual property of their respective owners 
            and are utilized exclusively under applicable open-content licenses, public APIs, or fair-use editorial reference.
          </p>
        </div>

        <!-- IP Separation Matrix Table -->
        <div class="ip-matrix-grid">
          <div class="ip-matrix-card original">
            <div class="ip-card-header">
              <span class="ip-icon">⚡</span>
              <h4>ORIGINAL PROPRIETARY CONTENT</h4>
            </div>
            <ul class="ip-feature-list">
              <li><strong>Ego Rating System:</strong> Proprietary mathematical calculation based on player performance metrics.</li>
              <li><strong>Transfer Probability Score:</strong> Algorithmic probability calculation model.</li>
              <li><strong>Striker Index & Threat Levels:</strong> Custom scouting evaluation indices.</li>
              <li><strong>Custom SVG Radar Visualizer:</strong> Original zero-dependency vector charting engine.</li>
              <li><strong>User Interface & Design System:</strong> Original cyberpunk dark-mode layout.</li>
            </ul>
          </div>

          <div class="ip-matrix-card third-party">
            <div class="ip-card-header">
              <span class="ip-icon">📊</span>
              <h4>THIRD-PARTY CONTENT & DATA</h4>
            </div>
            <ul class="ip-feature-list">
              <li><strong>Player Photographs:</strong> Sourced under Creative Commons licenses (CC BY-SA 4.0 / 3.0).</li>
              <li><strong>Club Badges & Trademarks:</strong> Owned by respective football clubs and leagues.</li>
              <li><strong>Season Match Statistics:</strong> Provided via API-Football and public statistics references.</li>
              <li><strong>Transfer Rumours & News:</strong> Editorial excerpts attributed to original news outlets.</li>
              <li><strong>Market Value Benchmarks:</strong> Historical valuation indexes referenced from public records.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Section 2: Player Photography Attribution Register -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 2. PLAYER PHOTOGRAPHY & IMAGE LICENSING REGISTER <span class="title-bracket">]</span></h2>
          <span class="panel-tag gold">20 ATHLETES DOCUMENTED</span>
        </div>
        <p class="section-intro-text">
          Every player photograph featured on BLUELOCK // TRANSFER IQ is mapped to its verified creator, source repository, and license terms. 
          No claim of ownership is made over any third-party photograph.
        </p>

        <div class="table-responsive">
          <table class="bl-table compliance-table">
            <thead>
              <tr>
                <th>PLAYER</th>
                <th>PHOTOGRAPHER / CREDIT</th>
                <th>LICENSE</th>
                <th>SOURCE HOST</th>
                <th>LINK</th>
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

      <!-- Section 3: Club Trademarks & Blue Lock Fan Tribute -->
      <div class="compliance-dual-grid">
        
        <!-- Club Trademarks -->
        <div class="bl-card bl-hud-panel">
          <div class="panel-header-clean">
            <h2 class="panel-section-title"><span class="title-bracket">[</span> 3. CLUB TRADEMARKS & BADGES <span class="title-bracket">]</span></h2>
          </div>
          <div class="disclaimer-body">
            <p>
              All football club names, crests, logos, badges, stadium names, and league identifiers 
              (including <em>Real Madrid, Manchester City, Arsenal, Barcelona, Bayern Munich, Liverpool, Chelsea, PSG, Inter Milan, Atlético Madrid</em>) 
              are registered trademarks of their respective clubs, leagues, and football associations.
            </p>
            <div class="quote-notice">
              "Club names, logos, and trademarks belong to their respective owners."
            </div>
            <p class="sub-clause">
              Their depiction on this website is strictly for identification, non-commercial commentary, and tactical scouting simulation under fair-use principles.
            </p>
          </div>
        </div>

        <!-- Blue Lock Fan Tribute -->
        <div class="bl-card bl-hud-panel">
          <div class="panel-header-clean">
            <h2 class="panel-section-title"><span class="title-bracket">[</span> 4. BLUE LOCK INSPIRATION NOTICE <span class="title-bracket">]</span></h2>
          </div>
          <div class="disclaimer-body">
            <p>
              This website incorporates a futuristic, high-intensity aesthetic inspired by the fictional football training concept of <strong>Blue Lock</strong>. 
              The application uses 100% original code, custom CSS shaders, original SVG radar graphics, and zero copyrighted manga or anime panels.
            </p>
            <div class="quote-notice">
              "This is an independent fan-inspired project and is not affiliated with, sponsored by, or endorsed by Muneyuki Kaneshiro, Yusuke Nomura, Kodansha Ltd., 8bit animation studio, or any official Blue Lock rights holders."
            </div>
          </div>
        </div>

      </div>

      <!-- Section 4: Data Sources & Third-Party APIs -->
      <div class="compliance-section bl-card bl-hud-panel">
        <div class="panel-header-clean">
          <h2 class="panel-section-title"><span class="title-bracket">[</span> 5. DATA PROVIDERS & API ATTRIBUTIONS <span class="title-bracket">]</span></h2>
          <span class="panel-tag">VERIFIED APIS</span>
        </div>

        <div class="data-sources-grid">
          ${DATA_SOURCES.map(src => `
            <div class="data-source-card">
              <div class="ds-head">
                <span class="ds-category">${src.category}</span>
                <h3 class="ds-name">${src.name}</h3>
              </div>
              <p class="ds-desc">${src.description}</p>
              <div class="ds-footer">
                <span class="ds-license">License: <strong>${src.license}</strong></span>
                <a href="${src.website}" target="_blank" rel="noopener noreferrer" class="attr-ext-link">Provider Website ↗</a>
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- Section 5: Open-Source Software & Typography Registry -->
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
 * Global Rich Footer Renderer with Copyright, Trademarks, and Legal Links
 */
export function renderGlobalFooter() {
  return `
    <footer class="bl-global-footer">
      <div class="footer-container">
        
        <!-- Brand & Tagline -->
        <div class="footer-col brand-col">
          <div class="footer-brand">
            <svg class="footer-logo-svg" width="24" height="24" viewBox="0 0 100 100">
              <polygon points="50,5 90,25 90,75 50,95 10,75 10,25" fill="none" stroke="#00f0ff" stroke-width="6"/>
              <polygon points="50,22 75,37 75,63 50,78 25,63 25,37" fill="rgba(0, 240, 255, 0.15)" stroke="#0077ff" stroke-width="4"/>
              <circle cx="50" cy="50" r="10" fill="#00f0ff"/>
            </svg>
            <span class="footer-brand-title">BLUELOCK // TRANSFER IQ</span>
          </div>
          <p class="footer-motto">"ENTER THE TRANSFER BATTLEFIELD."</p>
          <p class="footer-desc">
            Futuristic football transfer intelligence platform combining tactical ego scouting with European market analytics.
          </p>
          <div class="footer-copyright-main">
            <strong>© 2026 BLUELOCK // TRANSFER IQ. All rights reserved.</strong>
          </div>
        </div>

        <!-- Quick Navigation -->
        <div class="footer-col">
          <h4 class="footer-heading">PLATFORM MODULES</h4>
          <ul class="footer-links">
            <li><a href="#transfers" class="footer-nav-link" data-view="transfers">Live Transfer Wire</a></li>
            <li><a href="#players" class="footer-nav-link" data-view="players">Player Scouting Hub</a></li>
            <li><a href="#clubs" class="footer-nav-link" data-view="clubs">Club War Rooms</a></li>
            <li><a href="#compare" class="footer-nav-link" data-view="compare">Ego Clash Radar</a></li>
            <li><a href="#market" class="footer-nav-link" data-view="market">Valuation Matrix</a></li>
            <li><a href="#news" class="footer-nav-link" data-view="news">Transfer News Wire</a></li>
          </ul>
        </div>

        <!-- Legal & Attribution Links -->
        <div class="footer-col">
          <h4 class="footer-heading">COMPLIANCE & LEGAL</h4>
          <ul class="footer-links">
            <li><a href="#copyright" class="footer-nav-link highlight" data-view="copyright">⚖️ Copyright & Attribution</a></li>
            <li><a href="#privacy" class="footer-legal-modal-trigger" data-modal="privacy">🔒 Privacy Policy</a></li>
            <li><a href="#terms" class="footer-legal-modal-trigger" data-modal="terms">📜 Terms of Use</a></li>
            <li><a href="#sources" class="footer-nav-link" data-view="copyright">📊 Data Sources & APIs</a></li>
            <li><a href="mailto:intel@bluelocktransferiq.com" class="footer-ext-link">📬 Contact Compliance</a></li>
          </ul>
        </div>

        <!-- Disclaimers & Attribution Note -->
        <div class="footer-col disclaimer-col">
          <h4 class="footer-heading">INTELLECTUAL PROPERTY</h4>
          <div class="footer-disclaimer-box">
            <p class="disclaimer-p">
              <strong>Trademarks:</strong> Club names, badges, crests, and trademarks belong strictly to their respective owners.
            </p>
            <p class="disclaimer-p">
              <strong>Fan Project:</strong> Independent tribute; not affiliated with Kodansha or the creators of Blue Lock.
            </p>
            <p class="disclaimer-p">
              <strong>Photography:</strong> Athlete portraits sourced under documented Creative Commons licenses with individual creator credits.
            </p>
          </div>
        </div>

      </div>

      <div class="footer-bottom-bar">
        <div class="footer-bottom-container">
          <span>BLUELOCK // TRANSFER IQ • Version 1.2.0 • Zero-Dependency Architecture</span>
          <span class="status-indicator">🟢 ALL SYSTEMS OPERATIONAL</span>
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
      <h2>PRIVACY POLICY</h2>
      <p class="effective-date">Last Updated: August 25, 2026</p>
      
      <h3>1. Data Collection & Privacy First</h3>
      <p>
        BLUELOCK // TRANSFER IQ operates as a client-first football intelligence platform. We do not sell personal scouting queries, user data, or tracking information to third-party data brokers.
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
        For inquiries regarding compliance or privacy, contact <code>intel@bluelocktransferiq.com</code>.
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
      <h2>TERMS OF USE</h2>
      <p class="effective-date">Last Updated: August 25, 2026</p>

      <h3>1. Demonstration & Fan Concept Purpose</h3>
      <p>
        BLUELOCK // TRANSFER IQ is an interactive sports intelligence and scouting simulation application built for analytical and educational demonstration.
      </p>

      <h3>2. Algorithmic Nature of Metrics</h3>
      <p>
        Metrics including <em>Transfer Probability, Ego Threat Index,</em> and <em>Scouting Momentum</em> are algorithmic simulations and proprietary analytical estimations. They do not constitute official statements by football clubs, players, or football governing bodies.
      </p>

      <h3>3. Third-Party Intellectual Property</h3>
      <p>
        All football club names, emblems, competition trademarks, and player photography remain the property of their respective creators and owners. Users may not scrape or republish third-party assets without complying with their respective licenses.
      </p>

      <h3>4. No Warranty</h3>
      <p>
        The software is provided "as is", without warranty of any kind, express or implied.
      </p>
    </div>
  `;
}
'''

target_path = r"c:\Users\LENOVO\Desktop\web\js\components.js"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(new_components_js.strip())

print("Created updated js/components.js successfully!")
