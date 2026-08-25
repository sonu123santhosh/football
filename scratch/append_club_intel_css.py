"""
Append CSS for Club Intelligence, Injury Center, Suspension Center & Availability Badges.
"""

club_intel_css = '''
/* ==========================================================================
   BLUEGUN — CLUB INTELLIGENCE & SQUAD READINESS STYLES
   ========================================================================== */

/* Availability Status Badges */
.bl-avail-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.8px;
  padding: 3px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

.bl-avail-badge.avail-available {
  background: rgba(0, 255, 136, 0.12);
  color: #00ff88;
  border: 1px solid rgba(0, 255, 136, 0.35);
}

.bl-avail-badge.avail-minor {
  background: rgba(254, 190, 16, 0.12);
  color: #febe10;
  border: 1px solid rgba(254, 190, 16, 0.35);
}

.bl-avail-badge.avail-injured {
  background: rgba(255, 51, 102, 0.15);
  color: #ff3366;
  border: 1px solid rgba(255, 51, 102, 0.4);
}

.bl-avail-badge.avail-suspended {
  background: rgba(255, 140, 0, 0.15);
  color: #ff8c00;
  border: 1px solid rgba(255, 140, 0, 0.4);
}

.bl-avail-badge.avail-intl {
  background: rgba(0, 119, 255, 0.15);
  color: #0077ff;
  border: 1px solid rgba(0, 119, 255, 0.4);
}

.bl-avail-badge.avail-unavail {
  background: rgba(120, 120, 120, 0.15);
  color: #a0a0a0;
  border: 1px solid rgba(120, 120, 120, 0.4);
}

.bl-avail-badge.avail-unknown {
  background: rgba(255, 255, 255, 0.1);
  color: #e0e0e0;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Club Header & Update Badge */
.data-update-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 240, 255, 0.1);
  border: 1px solid rgba(0, 240, 255, 0.3);
  padding: 6px 12px;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--neon-cyan);
  margin-bottom: 8px;
}

.source-credit-box {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}

.club-switch-picker select {
  max-width: 220px;
}

/* Availability Summary Strip */
.club-availability-summary-strip {
  background: rgba(6, 12, 28, 0.85);
  border: 1px solid rgba(0, 240, 255, 0.25);
  border-radius: 8px;
  padding: 20px 24px;
  margin-bottom: 24px;
}

.avail-summary-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.avail-main-title {
  font-family: var(--font-hud);
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #fff;
}

.avail-total-tag {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-secondary);
}

.avail-metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
  margin-bottom: 16px;
}

.avail-metric-card {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(11, 19, 37, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  padding: 12px 16px;
}

.avail-metric-card.green { border-color: rgba(0, 255, 136, 0.3); }
.avail-metric-card.red { border-color: rgba(255, 51, 102, 0.3); }
.avail-metric-card.gold { border-color: rgba(255, 140, 0, 0.3); }
.avail-metric-card.grey { border-color: rgba(120, 120, 120, 0.3); }

.avail-count {
  display: block;
  font-family: var(--font-hud);
  font-size: 20px;
  font-weight: 800;
  color: #fff;
}

.avail-label {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  letter-spacing: 0.8px;
}

.avail-bar-track {
  display: flex;
  height: 8px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid rgba(0, 240, 255, 0.2);
}

.bar-seg { height: 100%; transition: width 0.6s ease; }
.bar-seg.green { background: #00ff88; box-shadow: 0 0 6px #00ff88; }
.bar-seg.red { background: #ff3366; box-shadow: 0 0 6px #ff3366; }
.bar-seg.gold { background: #ff8c00; box-shadow: 0 0 6px #ff8c00; }
.bar-seg.grey { background: #787878; }

/* Club Intelligence Tabs Bar */
.club-intel-tabs-bar {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 12px;
  margin-bottom: 24px;
  border-bottom: 1px solid rgba(0, 240, 255, 0.15);
}

.club-tab-btn {
  background: rgba(6, 12, 28, 0.8);
  border: 1px solid rgba(0, 240, 255, 0.25);
  color: var(--text-secondary);
  font-family: var(--font-hud);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1px;
  padding: 10px 18px;
  border-radius: 6px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}

.club-tab-btn:hover {
  background: rgba(0, 240, 255, 0.1);
  color: #fff;
  border-color: var(--neon-cyan);
}

.club-tab-btn.active {
  background: var(--neon-cyan);
  color: #030712;
  border-color: var(--neon-cyan);
  box-shadow: 0 0 16px rgba(0, 240, 255, 0.5);
}

/* Squad Grid & Cards */
.squad-filters-bar {
  display: flex;
  gap: 20px;
  align-items: center;
  margin-bottom: 20px;
  padding: 12px 18px;
  background: rgba(6, 12, 28, 0.8);
}

.squad-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.squad-player-card {
  background: rgba(6, 12, 28, 0.9);
  border: 1px solid rgba(0, 240, 255, 0.25);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.squad-player-card:hover {
  transform: translateY(-3px);
  border-color: var(--neon-cyan);
  box-shadow: 0 8px 24px rgba(0, 240, 255, 0.2);
}

.squad-p-img-wrap {
  height: 140px;
  position: relative;
  background: #050a18;
  overflow: hidden;
}

.squad-p-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
}

.squad-p-shirt {
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.75);
  border: 1px solid var(--neon-cyan);
  color: var(--neon-cyan);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}

.squad-p-body {
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex-grow: 1;
}

.squad-p-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.squad-p-name {
  font-family: var(--font-hud);
  font-size: 15px;
  font-weight: 800;
  color: #fff;
}

.squad-p-ovr {
  font-family: var(--font-hud);
  font-size: 13px;
  font-weight: 800;
  background: rgba(0, 240, 255, 0.15);
  color: var(--neon-cyan);
  padding: 2px 6px;
  border-radius: 4px;
}

.squad-p-role {
  font-size: 11px;
  color: var(--text-secondary);
}

.squad-p-meta {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  margin-top: 4px;
}

.squad-p-contract {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}

.squad-scout-btn {
  border-radius: 0 0 7px 7px;
  width: 100%;
}

/* Injury & Suspension Dossier Cards */
.injury-dossier-card, .suspension-dossier-card {
  background: rgba(11, 19, 37, 0.95);
  border: 1px solid rgba(255, 51, 102, 0.35);
  border-radius: 8px;
  padding: 18px;
  margin-bottom: 16px;
}

.suspension-dossier-card {
  border-color: rgba(255, 140, 0, 0.35);
}

.inj-card-header, .susp-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.inj-p-name, .susp-p-name {
  font-family: var(--font-hud);
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  margin-top: 4px;
}

.inj-days-badge, .susp-remaining-badge {
  text-align: right;
}

.days-num, .match-num {
  font-family: var(--font-hud);
  font-size: 22px;
  font-weight: 800;
  color: #ff3366;
  display: block;
}

.match-num { color: #ff8c00; }

.days-lbl, .match-lbl {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
}

.inj-details-grid, .susp-details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px;
}

.inj-cell, .susp-cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.inj-cell .lbl, .susp-cell .lbl {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  letter-spacing: 0.8px;
}

.inj-cell .val, .susp-cell .val {
  font-size: 13px;
  color: #fff;
}

.source-link-span a {
  color: var(--neon-cyan);
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 11px;
}
'''

with open(r"c:\Users\LENOVO\Desktop\web\css\sections.css", "a", encoding="utf-8") as f:
    f.write(club_intel_css)

print("Appended Club Intelligence, Squad, Injury & Suspension styles!")
