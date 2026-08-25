/**
 * BLUELOCK // TRANSFER IQ - Component Library & View Renderers
 * Pure JavaScript component renderers generating semantic, reactive HTML elements.
 * Updated with real football player images and robust graceful error fallbacks.
 */

import { renderRadarChart, renderMarketValueChart } from './chart.js';

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
            <span class="ego-tag" title="Ego Threat Level">THREAT: ${tr.egoThreat}</span>
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
            <span class="club-title">${tr.fromClub}</span>
          </div>
          
          <div class="transfer-arrow-hud">
            <div class="arrow-line"></div>
            <div class="arrow-head">▶</div>
            <span class="prob-tag">${tr.confidence}% PROB</span>
          </div>

          <div class="club-node" data-club-id="${tr.toClubId || ''}">
            <img src="${tr.toBadge}" alt="${tr.toClub}" class="club-logo-sm" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
            <span class="club-title">${tr.toClub}</span>
          </div>
        </div>

        <!-- Valuation Grid -->
        <div class="transfer-metrics-grid">
          <div class="metric-cell">
            <span class="metric-lbl">MARKET VALUE</span>
            <span class="metric-val cyan">${tr.marketValue}</span>
          </div>
          <div class="metric-cell">
            <span class="metric-lbl">REPORTED FEE</span>
            <span class="metric-val gold">${tr.reportedFee}</span>
          </div>
        </div>

        <p class="transfer-headline">${tr.headline}</p>
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
          <span>ANALYZE EGO & STATS</span>
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
  return `
    <article class="bl-player-card" data-player-id="${p.id}">
      <div class="card-glow-edge"></div>
      <div class="player-card-banner">
        <span class="ego-pill">EGO: ${p.egoRating}</span>
        <span class="ovr-rating">${p.rating}</span>
      </div>

      <div class="player-visual">
        <img src="${imgSrc}" alt="${p.name}" class="player-portrait" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <div class="player-flag-badge">${p.flag}</div>
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
 * Club Card (Clubs Grid View)
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

      <div class="club-metrics-row">
        <div class="c-metric">
          <span class="lbl">SQUAD VALUE</span>
          <span class="val cyan">${club.squadValue}</span>
        </div>
        <div class="c-metric">
          <span class="lbl">BUDGET</span>
          <span class="val gold">${club.transferBudget}</span>
        </div>
      </div>

      <div class="club-targets-peek">
        <span class="peek-title">TOP TARGET:</span>
        <span class="peek-val">${club.targets[0] ? club.targets[0].name : 'Active Scouting'} (${club.targets[0] ? club.targets[0].interest : ''})</span>
      </div>

      <button class="bl-btn bl-btn-outline bl-btn-block btn-view-club" data-club-id="${club.id}">
        <span>INSPECT WAR ROOM</span>
      </button>
    </article>
  `;
}

/**
 * Transfer News Card (News Feed)
 */
export function renderNewsCard(item) {
  return `
    <article class="bl-news-card" data-news-id="${item.id}">
      <div class="news-img-container">
        <img src="${item.image}" alt="${item.title}" class="news-img" loading="lazy" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
        <span class="news-category-badge">${item.category}</span>
        <span class="news-read-time">${item.readTime}</span>
      </div>

      <div class="news-content">
        <div class="news-meta-row">
          <span class="news-source">${item.source}</span>
          <span class="news-time">${item.published}</span>
        </div>

        <h3 class="news-headline">${item.title}</h3>
        <p class="news-summary">${item.summary}</p>

        <div class="news-footer">
          <div class="news-involved">
            <span class="involved-lbl">FOCUS:</span>
            <strong class="cyan">${item.player}</strong>
          </div>

          <button class="bl-btn bl-btn-sm bl-btn-cyber btn-read-news" data-news-id="${item.id}">
            <span>READ FULL WIRE</span>
          </button>
        </div>
      </div>
    </article>
  `;
}

/**
 * Full Detailed Player Profile Page
 */
export function renderPlayerProfile(p) {
  const imgSrc = p.image || p.photo;
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

              <!-- Blue Lock Ego Metrics Box -->
              <div class="ego-metrics-box">
                <div class="ego-metric-item">
                  <span class="ego-lbl">EGO RATING</span>
                  <div class="ego-val-circle">
                    <span class="ego-num">${p.egoRating}</span>
                    <span class="ego-denom">/100</span>
                  </div>
                </div>
                <div class="ego-metric-item">
                  <span class="ego-lbl">STRIKER INDEX</span>
                  <div class="ego-val-circle alt">
                    <span class="ego-num">${p.strikerIndex}</span>
                    <span class="ego-denom">/100</span>
                  </div>
                </div>
                <div class="ego-metric-item">
                  <span class="ego-lbl">MARKET THREAT</span>
                  <div class="ego-threat-pill ${p.marketThreat.toLowerCase()}">${p.marketThreat}</div>
                </div>
              </div>
            </div>

            <p class="player-scout-overview">${p.overview}</p>

            <!-- Momentum Bar -->
            <div class="header-momentum-wrap">
              <div class="momentum-meta">
                <span>TRANSFER MOMENTUM & BATTLE PRESSURE</span>
                <strong class="cyan">${p.momentum}%</strong>
              </div>
              <div class="bl-progress-track large">
                <div class="bl-progress-fill glow" style="width: ${p.momentum}%;"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Main Profile Content Grid -->
      <div class="profile-sections-grid">
        
        <!-- Left Column: Transfer Status & Value Valuation -->
        <div class="profile-left-col">
          
          <!-- Transfer Status Panel -->
          <div class="bl-card bl-hud-panel">
            <h2 class="panel-section-title">
              <span class="title-bracket">[</span>
              TRANSFER STATUS & CONTRACT
              <span class="title-bracket">]</span>
            </h2>

            <div class="status-props-table">
              <div class="prop-row">
                <span class="prop-k">CURRENT CLUB</span>
                <strong class="prop-v">${p.currentClub}</strong>
              </div>
              <div class="prop-row">
                <span class="prop-k">TRANSFER TYPE</span>
                <strong class="prop-v gold">${p.transferType}</strong>
              </div>
              <div class="prop-row">
                <span class="prop-k">NEGOTIATION STATUS</span>
                <div class="prop-v">${getStatusBadge(p.transferStatus)}</div>
              </div>
              <div class="prop-row">
                <span class="prop-k">CONTRACT EXPIRY</span>
                <strong class="prop-v">${p.contractExpiry}</strong>
              </div>
              <div class="prop-row">
                <span class="prop-k">TRANSFER PROBABILITY</span>
                <strong class="prop-v cyan">${p.probability}%</strong>
              </div>
            </div>
          </div>

          <!-- Market Value & Historical Line Chart Panel -->
          <div class="bl-card bl-hud-panel">
            <h2 class="panel-section-title">
              <span class="title-bracket">[</span>
              MARKET VALUE RADAR
              <span class="title-bracket">]</span>
            </h2>

            <div class="valuation-highlight-grid">
              <div class="v-box">
                <span class="v-label">CURRENT MARKET VALUE</span>
                <span class="v-amount cyan">${p.marketValue}</span>
              </div>
              <div class="v-box">
                <span class="v-label">ASKING PRICE</span>
                <span class="v-amount gold">${p.askingPrice}</span>
              </div>
              <div class="v-box">
                <span class="v-label">LATEST REPORTED OFFER</span>
                <span class="v-amount white">${p.reportedOffer}</span>
              </div>
              <div class="v-box">
                <span class="v-label">VALUE DIFFERENCE</span>
                <span class="v-amount green">${p.valueDiff}</span>
              </div>
            </div>

            <!-- SVG Valuation Line Chart Container -->
            <div class="chart-wrapper">
              <h4 class="chart-subtitle">5-YEAR VALUATION MOVEMENT</h4>
              <div id="playerValuationChart" class="svg-chart-mount"></div>
            </div>
          </div>

          <!-- Who Wants Him Section -->
          <div class="bl-card bl-hud-panel">
            <h2 class="panel-section-title">
              <span class="title-bracket">[</span>
              WHO WANTS HIM? // INTERESTED CLUBS
              <span class="title-bracket">]</span>
            </h2>

            <div class="interested-clubs-list">
              ${p.interestedClubs.map(ic => `
                <div class="interested-club-item">
                  <div class="ic-header">
                    <span class="ic-name">${ic.name}</span>
                    <span class="ic-league">${ic.league}</span>
                  </div>
                  <div class="ic-details">
                    <div class="ic-col">
                      <span class="lbl">INTEREST</span>
                      <strong class="val gold">${ic.interest}</strong>
                    </div>
                    <div class="ic-col">
                      <span class="lbl">OFFER</span>
                      <strong class="val cyan">${ic.offer}</strong>
                    </div>
                    <div class="ic-col">
                      <span class="lbl">STATUS</span>
                      <strong class="val">${ic.status}</strong>
                    </div>
                  </div>
                  <div class="ic-probability">
                    <div class="prob-lbl">
                      <span>DEAL PROBABILITY</span>
                      <strong>${ic.probability}%</strong>
                    </div>
                    <div class="bl-progress-track">
                      <div class="bl-progress-fill" style="width: ${ic.probability}%;"></div>
                    </div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- Right Column: Scouting Analytics & Stats Dashboard -->
        <div class="profile-right-col">
          
          <!-- Tactical Attribute Radar -->
          <div class="bl-card bl-hud-panel">
            <h2 class="panel-section-title">
              <span class="title-bracket">[</span>
              EGO RADAR // SCOUTING MATRIX
              <span class="title-bracket">]</span>
            </h2>

            <div class="radar-section-wrap">
              <div id="playerProfileRadar" class="svg-radar-mount"></div>
              
              <!-- Attribute Scorecards -->
              <div class="radar-score-grid">
                <div class="r-score-card">
                  <span class="r-attr">PACE</span>
                  <span class="r-val">${p.radar.pace}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.pace}%;"></div></div>
                </div>
                <div class="r-score-card">
                  <span class="r-attr">SHOOTING</span>
                  <span class="r-val">${p.radar.shooting}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.shooting}%;"></div></div>
                </div>
                <div class="r-score-card">
                  <span class="r-attr">PASSING</span>
                  <span class="r-val">${p.radar.passing}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.passing}%;"></div></div>
                </div>
                <div class="r-score-card">
                  <span class="r-attr">DRIBBLING</span>
                  <span class="r-val">${p.radar.dribbling}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.dribbling}%;"></div></div>
                </div>
                <div class="r-score-card">
                  <span class="r-attr">DEFENDING</span>
                  <span class="r-val">${p.radar.defending}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.defending}%;"></div></div>
                </div>
                <div class="r-score-card">
                  <span class="r-attr">PHYSICAL</span>
                  <span class="r-val">${p.radar.physical}</span>
                  <div class="r-bar"><div class="r-fill" style="width: ${p.radar.physical}%;"></div></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Deep Season Statistics Dashboard -->
          <div class="bl-card bl-hud-panel">
            <h2 class="panel-section-title">
              <span class="title-bracket">[</span>
              ADVANCED SCOUTING METRICS
              <span class="title-bracket">]</span>
            </h2>

            <div class="stats-matrix-grid">
              <div class="stat-tile">
                <span class="stat-lbl">MATCHES</span>
                <span class="stat-num cyan">${p.stats.appearances}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">GOALS</span>
                <span class="stat-num gold">${p.stats.goals}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">ASSISTS</span>
                <span class="stat-num">${p.stats.assists}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">MINUTES</span>
                <span class="stat-num">${p.stats.minutes}'</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">EXP. GOALS (xG)</span>
                <span class="stat-num cyan">${p.stats.xg}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">EXP. ASSISTS (xA)</span>
                <span class="stat-num">${p.stats.xa}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">TOTAL SHOTS</span>
                <span class="stat-num">${p.stats.shots}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">KEY PASSES</span>
                <span class="stat-num gold">${p.stats.keyPasses}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">DRIBBLES WON</span>
                <span class="stat-num cyan">${p.stats.dribbles}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">PASS ACCURACY</span>
                <span class="stat-num">${p.stats.passAccuracy}%</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">TACKLES WON</span>
                <span class="stat-num">${p.stats.tackles}</span>
              </div>
              <div class="stat-tile">
                <span class="stat-lbl">INTERCEPTIONS</span>
                <span class="stat-num">${p.stats.interceptions}</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  `;
}

/**
 * Full Detailed Club Profile Page
 */
export function renderClubProfile(club) {
  return `
    <div class="bl-club-profile-view">
      <div class="profile-top-bar">
        <button class="bl-btn bl-btn-outline bl-btn-sm btn-back-clubs">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>ALL CLUBS</span>
        </button>
        <div class="profile-breadcrumbs">
          <span>SCOUTING HUB</span> / <span>CLUBS</span> / <strong class="cyan">${club.name.toUpperCase()}</strong>
        </div>
      </div>

      <!-- Club Banner -->
      <section class="club-banner bl-hud-panel">
        <div class="club-banner-content">
          <div class="club-banner-badge">
            <img src="${club.badge}" alt="${club.name}" class="big-club-badge" onerror="this.onerror=null; this.src='${CLUB_IMG_FALLBACK}';" />
          </div>
          <div class="club-banner-text">
            <div class="club-pre-title">
              <span class="country-flag">${club.flag}</span>
              <span>${club.country.toUpperCase()}</span>
              <span class="slash">//</span>
              <span>${club.league}</span>
            </div>
            <h1 class="club-hero-name">${club.name}</h1>
            <p class="club-stadium">🏟️ ${club.stadium}</p>
            <p class="club-philosophy">${club.description}</p>
          </div>
          <div class="club-hq-metrics">
            <div class="hq-metric-item">
              <span class="lbl">TOTAL SQUAD VALUE</span>
              <span class="val cyan">${club.squadValue}</span>
            </div>
            <div class="hq-metric-item">
              <span class="lbl">TRANSFER WAR CHEST</span>
              <span class="val gold">${club.transferBudget}</span>
            </div>
            <div class="hq-metric-item">
              <span class="lbl">ANNUAL WAGE BILL</span>
              <span class="val">${club.wageBill}</span>
            </div>
            <div class="hq-metric-item">
              <span class="lbl">MANAGER</span>
              <span class="val white">${club.manager}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Club Transfer War Room Tables -->
      <div class="club-warroom-grid">
        
        <!-- Incoming Transfers -->
        <div class="bl-card bl-hud-panel">
          <h2 class="panel-section-title">
            <span class="title-bracket">[</span>
            INCOMING TRANSFERS & SIGNINGS
            <span class="title-bracket">]</span>
          </h2>
          <div class="warroom-table-wrap">
            <table class="bl-table">
              <thead>
                <tr>
                  <th>PLAYER</th>
                  <th>PREVIOUS CLUB</th>
                  <th>FEE</th>
                  <th>STATUS</th>
                </tr>
              </thead>
              <tbody>
                ${club.incoming.map(inc => `
                  <tr>
                    <td><strong>${inc.player}</strong></td>
                    <td>${inc.from}</td>
                    <td class="cyan">${inc.fee}</td>
                    <td>${getStatusBadge(inc.status)}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Outgoing Transfers -->
        <div class="bl-card bl-hud-panel">
          <h2 class="panel-section-title">
            <span class="title-bracket">[</span>
            OUTGOING TRANSFERS & DEPARTURES
            <span class="title-bracket">]</span>
          </h2>
          <div class="warroom-table-wrap">
            <table class="bl-table">
              <thead>
                <tr>
                  <th>PLAYER</th>
                  <th>NEW CLUB</th>
                  <th>FEE</th>
                  <th>STATUS</th>
                </tr>
              </thead>
              <tbody>
                ${club.outgoing.map(out => `
                  <tr>
                    <td><strong>${out.player}</strong></td>
                    <td>${out.to}</td>
                    <td class="gold">${out.fee}</td>
                    <td>${getStatusBadge(out.status)}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Active Transfer Targets -->
        <div class="bl-card bl-hud-panel full-width">
          <h2 class="panel-section-title">
            <span class="title-bracket">[</span>
            CONFIDENTIAL SCOUTING TARGETS
            <span class="title-bracket">]</span>
          </h2>
          <div class="warroom-table-wrap">
            <table class="bl-table">
              <thead>
                <tr>
                  <th>TARGET PLAYER</th>
                  <th>MARKET VALUE</th>
                  <th>SCOUTING PRIORITY</th>
                  <th>STATUS</th>
                  <th>ACTION</th>
                </tr>
              </thead>
              <tbody>
                ${club.targets.map(tgt => `
                  <tr>
                    <td><strong class="cyan">${tgt.name}</strong></td>
                    <td>${tgt.value}</td>
                    <td><span class="target-prio-pill">${tgt.interest}</span></td>
                    <td>${tgt.status}</td>
                    <td>
                      <button class="bl-btn bl-btn-sm bl-btn-cyber btn-view-player" data-player-id="${tgt.playerId}">
                        <span>SCOUT INTEL</span>
                      </button>
                    </td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>
  `;
}

/**
 * Transfer Market Sortable & Filterable Table
 */
export function renderTransferMarketTable(players, sortKey = 'marketValueRaw', sortAsc = false) {
  return `
    <div class="market-table-container">
      <div class="table-scroll">
        <table class="bl-table bl-market-datatable">
          <thead>
            <tr>
              <th data-sort="name" class="${sortKey === 'name' ? (sortAsc ? 'asc' : 'desc') : ''}">PLAYER <span class="sort-icon">↕</span></th>
              <th data-sort="age" class="${sortKey === 'age' ? (sortAsc ? 'asc' : 'desc') : ''}">AGE <span class="sort-icon">↕</span></th>
              <th data-sort="position" class="${sortKey === 'position' ? (sortAsc ? 'asc' : 'desc') : ''}">POSITION <span class="sort-icon">↕</span></th>
              <th>CURRENT CLUB</th>
              <th>TARGET CLUB</th>
              <th data-sort="marketValueRaw" class="${sortKey === 'marketValueRaw' ? (sortAsc ? 'asc' : 'desc') : ''}">MARKET VALUE <span class="sort-icon">↕</span></th>
              <th>REPORTED FEE</th>
              <th>TRANSFER TYPE</th>
              <th data-sort="transferStatus" class="${sortKey === 'transferStatus' ? (sortAsc ? 'asc' : 'desc') : ''}">STATUS <span class="sort-icon">↕</span></th>
              <th data-sort="probability" class="${sortKey === 'probability' ? (sortAsc ? 'asc' : 'desc') : ''}">PROBABILITY <span class="sort-icon">↕</span></th>
              <th>ACTION</th>
            </tr>
          </thead>
          <tbody>
            ${players.map(p => {
              const imgSrc = p.image || p.photo;
              return `
              <tr class="market-row" data-player-id="${p.id}">
                <td>
                  <div class="table-player-cell">
                    <img src="${imgSrc}" alt="${p.name}" class="table-thumb" onerror="this.onerror=null; this.src='${PLAYER_IMG_FALLBACK}';" />
                    <div>
                      <strong class="player-link">${p.name}</strong>
                      <span class="table-flag">${p.flag}</span>
                    </div>
                  </div>
                </td>
                <td>${p.age}</td>
                <td><span class="table-pos-pill">${p.position}</span></td>
                <td>${p.currentClub}</td>
                <td><span class="cyan">${p.targetClub || 'Evaluating'}</span></td>
                <td class="cyan font-mono font-bold">${p.marketValue}</td>
                <td class="gold font-mono">${p.askingPrice}</td>
                <td><span class="table-type-pill">${p.transferType}</span></td>
                <td>${getStatusBadge(p.transferStatus)}</td>
                <td>
                  <div class="table-prob-cell">
                    <span>${p.probability}%</span>
                    <div class="bl-progress-track mini">
                      <div class="bl-progress-fill" style="width: ${p.probability}%;"></div>
                    </div>
                  </div>
                </td>
                <td>
                  <button class="bl-btn bl-btn-xs bl-btn-cyber btn-view-player" data-player-id="${p.id}">
                    <span>VIEW</span>
                  </button>
                </td>
              </tr>
            `;}).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

/**
 * Player Comparison Matrix View
 */
export function renderComparisonView(allPlayers, playerA, playerB) {
  const isWinner = (valA, valB) => valA > valB;
  const imgA = playerA.image || playerA.photo;
  const imgB = playerB.image || playerB.photo;

  return `
    <div class="bl-comparison-view">
      <div class="comparison-header">
        <h1 class="bl-section-title">
          <span class="title-bracket">[</span>
          EGO CLASH // TACTICAL RADAR COMPARISON
          <span class="title-bracket">]</span>
        </h1>
        <p class="section-subtitle">Side-by-side scouting breakdown and radar overlay analysis.</p>
      </div>

      <!-- Player Selector Controls -->
      <div class="comparison-selectors-row">
        <div class="selector-box player-a-select">
          <label class="select-label cyan">PLAYER A (CYAN)</label>
          <select id="selectPlayerA" class="bl-select">
            ${allPlayers.map(p => `<option value="${p.id}" ${p.id === playerA.id ? 'selected' : ''}>${p.name} (${p.currentClub})</option>`).join('')}
          </select>
        </div>

        <div class="versus-badge">
          <span>VS</span>
        </div>

        <div class="selector-box player-b-select">
          <label class="select-label red">PLAYER B (CRIMSON)</label>
          <select id="selectPlayerB" class="bl-select">
            ${allPlayers.map(p => `<option value="${p.id}" ${p.id === playerB.id ? 'selected' : ''}>${p.name} (${p.currentClub})</option>`).join('')}
          </select>
        </div>
      </div>

      <!-- Dual Player Comparison Heads -->
      <div class="compare-heads-grid">
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
          </div>
        </div>

        <!-- Radar Overlay Center Mount -->
        <div class="compare-radar-center bl-card bl-hud-panel">
          <h3 class="radar-center-title">POLYGON OVERLAY</h3>
          <div class="radar-legend">
            <span class="legend-item cyan"><span class="color-dot cyan"></span> ${playerA.name}</span>
            <span class="legend-item red"><span class="color-dot red"></span> ${playerB.name}</span>
          </div>
          <div id="comparisonRadarMount" class="svg-radar-mount"></div>
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
            { label: "TRANSFER PROBABILITY", valA: playerA.probability, valB: playerB.probability, suffix: "%" }
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
