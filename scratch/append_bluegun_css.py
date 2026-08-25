"""
Append BLUEGUN 2026 War Room and Transfer Battle styles.
"""

bluegun_css = '''
/* ==========================================================================
   BLUEGUN — 2026 War Room Spotlight Grid & Transfer Battle HUD
   ========================================================================== */

.war-room-spotlight-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
  margin: 32px 0 28px 0;
  width: 100%;
}

.spotlight-card {
  background: rgba(6, 12, 28, 0.85);
  border: 1px solid rgba(0, 240, 255, 0.25);
  border-radius: 8px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.spotlight-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--neon-cyan);
  box-shadow: 0 0 10px var(--neon-cyan);
  transition: width 0.2s ease;
}

.spotlight-card:hover {
  transform: translateY(-3px);
  border-color: var(--neon-cyan);
  box-shadow: 0 8px 24px rgba(0, 240, 255, 0.2);
}

.spotlight-card:hover::before {
  width: 6px;
}

.sp-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.sp-icon {
  font-size: 16px;
}

.sp-title {
  font-family: var(--font-hud);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.2px;
  color: var(--text-muted);
}

.sp-main {
  font-family: var(--font-hud);
  font-size: 16px;
  font-weight: 800;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sp-sub {
  font-size: 12px;
  color: var(--text-secondary);
  margin-bottom: 10px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sp-badge {
  display: inline-block;
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.8px;
  padding: 3px 8px;
  border-radius: 4px;
  background: rgba(0, 240, 255, 0.12);
  color: var(--neon-cyan);
  border: 1px solid rgba(0, 240, 255, 0.3);
}

.sp-badge.gold-badge {
  background: rgba(254, 190, 16, 0.12);
  color: #febe10;
  border-color: rgba(254, 190, 16, 0.3);
}

.sp-badge.red-badge {
  background: rgba(255, 51, 102, 0.12);
  color: #ff3366;
  border-color: rgba(255, 51, 102, 0.3);
}

.sp-badge.neon-badge {
  background: rgba(0, 255, 136, 0.12);
  color: #00ff88;
  border-color: rgba(0, 255, 136, 0.3);
}

/* ==========================================================================
   2026 TRANSFER BATTLE HUD SECTION
   ========================================================================== */

.transfer-battle-section {
  margin: 24px 0 16px 0;
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.05), rgba(5, 10, 24, 0.8));
  border: 1px solid rgba(0, 240, 255, 0.35);
  border-radius: 8px;
  padding: 16px 20px;
  position: relative;
}

.battle-title-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
  padding-bottom: 8px;
  border-bottom: 1px dashed rgba(0, 240, 255, 0.2);
}

.battle-badge {
  font-family: var(--font-hud);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: var(--neon-cyan);
  text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
}

.battle-sub {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
  letter-spacing: 1px;
}

.battle-flow-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 16px;
  align-items: center;
}

@media (max-width: 768px) {
  .battle-flow-container {
    grid-template-columns: 1fr;
    gap: 12px;
  }
}

.battle-club-node {
  background: rgba(11, 19, 37, 0.9);
  border: 1px solid rgba(0, 240, 255, 0.2);
  border-radius: 6px;
  padding: 12px 14px;
  text-align: center;
}

.battle-club-node.to {
  border-color: rgba(0, 240, 255, 0.6);
  background: rgba(0, 240, 255, 0.08);
}

.node-status {
  display: block;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  letter-spacing: 1px;
  margin-bottom: 4px;
}

.node-name {
  font-family: var(--font-hud);
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 0.5px;
  color: #fff;
}

.node-name.highlight-cyan {
  color: var(--neon-cyan);
  text-shadow: 0 0 8px rgba(0, 240, 255, 0.5);
}

.battle-meter-hud {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.battle-meter-header {
  display: flex;
  justify-content: space-between;
  font-family: var(--font-hud);
  font-size: 12px;
  color: var(--text-secondary);
}

.battle-track {
  height: 8px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid rgba(0, 240, 255, 0.3);
}

.battle-fill {
  height: 100%;
  background: linear-gradient(90deg, #0077ff, #00f0ff);
  box-shadow: 0 0 12px #00f0ff;
  transition: width 1s ease-in-out;
}

.battle-stage-pill {
  display: flex;
  justify-content: center;
  margin-top: 4px;
}

.hero-sub-glitch {
  display: block;
  font-size: 16px;
  font-family: var(--font-hud);
  font-weight: 700;
  letter-spacing: 3px;
  color: var(--neon-cyan);
  margin-top: 8px;
  text-shadow: 0 0 12px rgba(0, 240, 255, 0.7);
}
'''

with open(r"c:\Users\LENOVO\Desktop\web\css\sections.css", "a", encoding="utf-8") as f:
    f.write(bluegun_css)

print("Appended BLUEGUN War Room and Battle styles to sections.css!")
