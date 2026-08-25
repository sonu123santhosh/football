"""
Append CSS for Credits Page, Source Registry Cards, Source Inspector Modal & Verification Badges.
"""

credits_css = '''
/* ==========================================================================
   BLUEGUN — COPYRIGHT, CREDITS & SOURCE MANAGEMENT SYSTEM STYLES
   ========================================================================== */

/* Micro Source Trigger Button */
.bl-source-btn {
  background: rgba(0, 240, 255, 0.08);
  border: 1px solid rgba(0, 240, 255, 0.25);
  color: var(--neon-cyan);
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 2px 7px;
  border-radius: 4px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: all 0.2s ease;
  vertical-align: middle;
}

.bl-source-btn:hover {
  background: var(--neon-cyan);
  color: #030712;
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
}

/* Source Status Badges */
.source-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  letter-spacing: 0.6px;
  text-transform: uppercase;
}

.source-status-pill.verified {
  background: rgba(0, 255, 136, 0.15);
  color: #00ff88;
  border: 1px solid rgba(0, 255, 136, 0.4);
}

.source-status-pill.review {
  background: rgba(254, 190, 16, 0.15);
  color: #febe10;
  border: 1px solid rgba(254, 190, 16, 0.4);
}

.source-status-pill.unknown {
  background: rgba(255, 51, 102, 0.15);
  color: #ff3366;
  border: 1px solid rgba(255, 51, 102, 0.4);
}

/* Source ID Tag */
.source-id-tag {
  display: inline-block;
  background: rgba(0, 240, 255, 0.15);
  border: 1px solid var(--neon-cyan);
  color: var(--neon-cyan);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
}

.source-category-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-left: 8px;
}

/* Credits Header Meta */
.credits-meta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 16px;
}

.audit-chip {
  background: rgba(11, 19, 37, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 6px 14px;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-secondary);
}

.audit-chip strong {
  color: #fff;
}

/* Original Content Panel */
.original-content-panel {
  margin-top: 24px;
}

.original-assets-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 12px;
  margin-top: 16px;
}

.asset-bullet {
  background: rgba(11, 19, 37, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 10px 14px;
  border-radius: 6px;
  font-size: 12px;
  color: var(--text-secondary);
}

.asset-bullet strong {
  color: #fff;
}

.asset-bullet.highlight {
  border-color: rgba(0, 240, 255, 0.3);
  background: rgba(0, 240, 255, 0.06);
}

.asset-bullet.highlight strong {
  color: var(--neon-cyan);
}

/* Credits Filter Bar */
.credits-filter-bar {
  background: rgba(6, 12, 28, 0.85);
  border: 1px solid rgba(0, 240, 255, 0.25);
  padding: 16px 20px;
  border-radius: 8px;
  margin: 28px 0 20px 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.credits-sources-stream {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.source-registry-card {
  background: rgba(11, 19, 37, 0.95);
  border: 1px solid rgba(0, 240, 255, 0.2);
  border-radius: 8px;
  padding: 20px;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.source-registry-card:hover {
  border-color: var(--neon-cyan);
  box-shadow: 0 4px 20px rgba(0, 240, 255, 0.15);
}

.source-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.source-title-name {
  font-family: var(--font-hud);
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 14px;
}

.source-specs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-bottom: 14px;
  background: rgba(6, 12, 28, 0.6);
  padding: 12px 16px;
  border-radius: 6px;
}

.source-cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.source-cell .lbl, .source-attr-box .lbl, .source-used-in-row .lbl {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  letter-spacing: 0.8px;
}

.source-cell .val {
  font-size: 13px;
  color: #fff;
}

.source-attr-box {
  background: rgba(0, 240, 255, 0.05);
  border-left: 3px solid var(--neon-cyan);
  padding: 10px 14px;
  border-radius: 0 4px 4px 0;
  margin-bottom: 12px;
}

.attr-text {
  font-size: 12px;
  color: var(--text-primary);
  margin-top: 4px;
}

.source-used-in-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.used-in-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.used-tag {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-secondary);
}

.source-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  flex-wrap: wrap;
  gap: 10px;
}

.source-audit-tag {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}

/* Final Notice Section */
.final-copyright-section {
  background: rgba(6, 12, 28, 0.9);
  border: 1px solid rgba(0, 240, 255, 0.3);
  padding: 24px;
  border-radius: 8px;
  margin-top: 32px;
}

.final-cr-title {
  font-family: var(--font-hud);
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 10px;
}

.final-cr-text {
  font-size: 13px;
  line-height: 1.6;
  color: var(--text-secondary);
}

.final-audit-badge {
  margin-top: 14px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--neon-cyan);
}

/* Source Inspector Modal */
.source-modal-details {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.source-modal-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(0, 240, 255, 0.2);
}

.source-modal-title {
  font-family: var(--font-hud);
  font-size: 20px;
  font-weight: 800;
  color: #fff;
  margin: 6px 0 2px 0;
}

.source-modal-cat {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}

.source-modal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  background: rgba(6, 12, 28, 0.7);
  padding: 14px;
  border-radius: 6px;
}

.s-m-cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.s-m-cell .lbl, .source-modal-attr .lbl, .source-modal-used .lbl {
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
}

.source-modal-attr {
  background: rgba(0, 240, 255, 0.05);
  border-left: 3px solid var(--neon-cyan);
  padding: 12px;
  border-radius: 0 4px 4px 0;
}

.source-modal-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  padding-top: 10px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
'''

with open(r"c:\Users\LENOVO\Desktop\web\css\sections.css", "a", encoding="utf-8") as f:
    f.write(credits_css)

print("Appended Credits Page, Source Registry Cards, and Source Inspector CSS styles!")
