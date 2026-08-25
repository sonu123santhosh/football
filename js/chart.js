/**
 * BLUELOCK // TRANSFER IQ - Custom SVG Visuals & Chart Engine
 * Lightweight, zero-dependency SVG Radar and Line Chart generators.
 */

/**
 * Generates an interactive SVG Radar Chart comparing 1 or 2 players.
 * Attributes: Pace, Shooting, Passing, Dribbling, Defending, Physical, Ego
 */
export function renderRadarChart(containerId, playerA, playerB = null) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const size = 340;
  const center = size / 2;
  const radius = 120;
  const attributes = [
    { key: "pace", label: "PACE" },
    { key: "shooting", label: "SHOOTING" },
    { key: "passing", label: "PASSING" },
    { key: "dribbling", label: "DRIBBLING" },
    { key: "defending", label: "DEFENDING" },
    { key: "physical", label: "PHYSICAL" }
  ];

  const totalAxes = attributes.length;
  const angleSlice = (Math.PI * 2) / totalAxes;

  // Grid levels (20%, 40%, 60%, 80%, 100%)
  const levels = [0.2, 0.4, 0.6, 0.8, 1.0];
  let gridPolygons = "";

  levels.forEach((level) => {
    let levelPoints = [];
    for (let i = 0; i < totalAxes; i++) {
      const angle = angleSlice * i - Math.PI / 2;
      const x = center + Math.cos(angle) * (radius * level);
      const y = center + Math.sin(angle) * (radius * level);
      levelPoints.push(`${x.toFixed(1)},${y.toFixed(1)}`);
    }
    gridPolygons += `
      <polygon points="${levelPoints.join(" ")}" fill="none" stroke="rgba(0, 240, 255, ${level === 1.0 ? 0.4 : 0.12})" stroke-width="${level === 1.0 ? 1.5 : 1}" stroke-dasharray="${level === 1.0 ? 'none' : '2,3'}" />
    `;
  });

  // Radial Axis lines & Labels
  let axisLines = "";
  let axisLabels = "";

  attributes.forEach((attr, i) => {
    const angle = angleSlice * i - Math.PI / 2;
    const x = center + Math.cos(angle) * radius;
    const y = center + Math.sin(angle) * radius;

    // Label coordinates (pushed outward)
    const labelX = center + Math.cos(angle) * (radius + 28);
    const labelY = center + Math.sin(angle) * (radius + 22);

    axisLines += `
      <line x1="${center}" y1="${center}" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" stroke="rgba(0, 240, 255, 0.2)" stroke-width="1" />
    `;

    const textAnchor = Math.abs(Math.cos(angle)) < 0.1 ? "middle" : (Math.cos(angle) > 0 ? "start" : "end");

    axisLabels += `
      <text x="${labelX.toFixed(1)}" y="${labelY.toFixed(1)}" fill="#8ca0c9" font-family="'Rajdhani', sans-serif" font-size="11" font-weight="700" letter-spacing="1px" text-anchor="${textAnchor}" dominant-baseline="central">
        ${attr.label}
      </text>
    `;
  });

  // Calculate points for Player A
  function getPolygonPoints(playerRadar) {
    return attributes.map((attr, i) => {
      const val = (playerRadar[attr.key] || 50) / 100;
      const angle = angleSlice * i - Math.PI / 2;
      const x = center + Math.cos(angle) * (radius * val);
      const y = center + Math.sin(angle) * (radius * val);
      return { x, y, val: playerRadar[attr.key] };
    });
  }

  const pointsA = getPolygonPoints(playerA.radar);
  const polygonAStr = pointsA.map(p => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");

  let dotsA = pointsA.map(p => `
    <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4" fill="#00f0ff" stroke="#040914" stroke-width="1.5" filter="drop-shadow(0 0 4px #00f0ff)">
      <title>${p.val}</title>
    </circle>
  `).join("");

  let playerBElement = "";
  if (playerB) {
    const pointsB = getPolygonPoints(playerB.radar);
    const polygonBStr = pointsB.map(p => `${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
    let dotsB = pointsB.map(p => `
      <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4" fill="#ff3b57" stroke="#040914" stroke-width="1.5" filter="drop-shadow(0 0 4px #ff3b57)">
        <title>${p.val}</title>
      </circle>
    `).join("");

    playerBElement = `
      <polygon points="${polygonBStr}" fill="rgba(255, 59, 87, 0.25)" stroke="#ff3b57" stroke-width="2" stroke-linejoin="round" />
      ${dotsB}
    `;
  }

  container.innerHTML = `
    <svg viewBox="0 0 ${size} ${size}" class="bl-radar-svg" preserveAspectRatio="xMidYMid meet">
      <defs>
        <radialGradient id="radarGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="rgba(0, 240, 255, 0.15)" />
          <stop offset="100%" stop-color="rgba(0, 240, 255, 0)" />
        </radialGradient>
        <linearGradient id="polyGradA" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="rgba(0, 240, 255, 0.45)" />
          <stop offset="100%" stop-color="rgba(0, 119, 255, 0.25)" />
        </linearGradient>
      </defs>
      
      <!-- Background circular ambient aura -->
      <circle cx="${center}" cy="${center}" r="${radius}" fill="url(#radarGlow)" />
      
      <!-- Grid -->
      ${gridPolygons}
      ${axisLines}
      
      <!-- Polygons -->
      <polygon points="${polygonAStr}" fill="url(#polyGradA)" stroke="#00f0ff" stroke-width="2" stroke-linejoin="round" filter="drop-shadow(0 0 8px rgba(0, 240, 255, 0.5))" />
      ${dotsA}
      ${playerBElement}
      
      <!-- Labels -->
      ${axisLabels}
      
      <!-- Center Ego Core -->
      <circle cx="${center}" cy="${center}" r="3" fill="#00f0ff" />
    </svg>
  `;
}

/**
 * Generates an SVG Market Value Trend Chart
 */
export function renderMarketValueChart(containerId, valueHistory, currentValStr) {
  const container = document.getElementById(containerId);
  if (!container || !valueHistory || valueHistory.length === 0) return;

  const width = 460;
  const height = 180;
  const padding = { top: 24, right: 30, bottom: 30, left: 45 };

  const values = valueHistory.map(v => v.value);
  const minVal = Math.max(0, Math.min(...values) - 20);
  const maxVal = Math.max(...values) + 20;

  const getX = (index) => padding.left + (index / (valueHistory.length - 1)) * (width - padding.left - padding.right);
  const getY = (val) => height - padding.bottom - ((val - minVal) / (maxVal - minVal)) * (height - padding.top - padding.bottom);

  const points = valueHistory.map((item, idx) => ({
    x: getX(idx),
    y: getY(item.value),
    year: item.year,
    val: item.value
  }));

  const linePath = points.reduce((acc, p, idx) => `${acc} ${idx === 0 ? 'M' : 'L'} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`, '');
  const areaPath = `${linePath} L ${points[points.length - 1].x.toFixed(1)} ${height - padding.bottom} L ${points[0].x.toFixed(1)} ${height - padding.bottom} Z`;

  // Grid lines
  const gridSteps = 3;
  let gridSvg = "";
  for (let i = 0; i <= gridSteps; i++) {
    const v = minVal + (i / gridSteps) * (maxVal - minVal);
    const y = getY(v);
    gridSvg += `
      <line x1="${padding.left}" y1="${y.toFixed(1)}" x2="${width - padding.right}" y2="${y.toFixed(1)}" stroke="rgba(255, 255, 255, 0.07)" stroke-dasharray="3,3" />
      <text x="${padding.left - 8}" y="${(y + 3).toFixed(1)}" fill="#607297" font-size="10" font-family="'Orbitron', sans-serif" text-anchor="end">€${Math.round(v)}M</text>
    `;
  }

  // Points & Labels
  let pointsSvg = "";
  points.forEach((p, i) => {
    pointsSvg += `
      <g class="chart-point-group" data-val="${p.val}" data-year="${p.year}">
        <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4.5" fill="#00f0ff" stroke="#060c18" stroke-width="2" class="chart-dot" />
        <text x="${p.x.toFixed(1)}" y="${height - 10}" fill="#8ca0c9" font-size="10" font-family="'Rajdhani', sans-serif" font-weight="700" text-anchor="middle">${p.year}</text>
        <title>${p.year}: €${p.val}M</title>
      </g>
    `;
  });

  container.innerHTML = `
    <svg viewBox="0 0 ${width} ${height}" class="bl-linechart-svg" preserveAspectRatio="xMidYMid meet">
      <defs>
        <linearGradient id="chartAreaGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="rgba(0, 240, 255, 0.35)" />
          <stop offset="100%" stop-color="rgba(0, 240, 255, 0.0)" />
        </linearGradient>
        <filter id="neonLineGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="glow" />
          <feMerge>
            <feMergeNode in="glow" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      
      <!-- Grid -->
      ${gridSvg}
      
      <!-- Area Under Curve -->
      <path d="${areaPath}" fill="url(#chartAreaGrad)" />
      
      <!-- Neon Trend Line -->
      <path d="${linePath}" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" filter="url(#neonLineGlow)" />
      
      <!-- Data Points -->
      ${pointsSvg}
    </svg>
  `;
}
