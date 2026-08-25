compliance_css = """
/* ==========================================================================
   Compliance, Copyright & Attribution Styles
   ========================================================================== */

/* Photo Attribution Tag on Player Card */
.player-photo-attribution {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(4, 7, 14, 0.85);
  border: 1px solid rgba(0, 240, 255, 0.25);
  color: var(--text-secondary);
  font-size: 10px;
  font-family: var(--font-hud);
  font-weight: 600;
  letter-spacing: 0.5px;
  padding: 2px 6px;
  border-radius: 3px;
  backdrop-filter: blur(4px);
  z-index: 3;
  pointer-events: auto;
  transition: var(--transition-fast);
}
.player-photo-attribution:hover {
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
  box-shadow: 0 0 8px rgba(0, 240, 255, 0.4);
}

/* Photo License Box on Profile Header */
.photo-license-box {
  margin-top: 10px;
  background: rgba(11, 19, 37, 0.8);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
  padding: 6px 12px;
  font-size: 11px;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.photo-license-box .photo-icon {
  font-size: 12px;
}
.photo-license-box .license-source-link {
  color: var(--neon-cyan);
  text-decoration: none;
  font-weight: 600;
  margin-left: auto;
}
.photo-license-box .license-source-link:hover {
  text-decoration: underline;
}

/* Micro photo attribution on comparison cards */
.photo-attr-micro {
  font-size: 10px;
  color: var(--text-muted);
  font-family: var(--font-hud);
  margin-top: 8px;
}

/* Profile Attribution & Data Source Strip */
.profile-attribution-strip {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px dashed var(--border-subtle);
}
.attr-chip {
  background: rgba(7, 12, 24, 0.8);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
  padding: 6px 12px;
  font-size: 11px;
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.attr-chip strong {
  color: var(--text-primary);
}
.attr-ext-link {
  color: var(--neon-cyan);
  text-decoration: none;
  font-weight: 700;
  margin-left: 4px;
  font-size: 11px;
}
.attr-ext-link:hover {
  text-decoration: underline;
}

/* Club Trademark Notices */
.club-trademark-notice {
  font-size: 10px;
  color: var(--text-muted);
  font-family: var(--font-hud);
  margin: 10px 0;
  text-align: center;
}
.club-trademark-footer {
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px dashed var(--border-subtle);
  font-size: 11px;
  color: var(--text-muted);
}

/* News Outbound Actions */
.news-actions-group {
  display: flex;
  gap: 8px;
  align-items: center;
}
.news-outbound-link {
  border-color: rgba(0, 240, 255, 0.3);
  color: var(--text-secondary);
}
.news-outbound-link:hover {
  color: var(--neon-cyan);
  border-color: var(--neon-cyan);
}
.news-modal-compliance-notice {
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  font-size: 12px;
  color: var(--text-muted);
}

/* Table Disclaimer Bar */
.table-disclaimer-bar {
  background: rgba(11, 19, 37, 0.6);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
  padding: 8px 16px;
  margin-bottom: 16px;
  font-size: 11px;
  color: var(--text-secondary);
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

/* ==========================================================================
   Dedicated Copyright & Compliance Page View
   ========================================================================== */
.bl-compliance-view {
  display: flex;
  flex-direction: column;
  gap: 32px;
  padding-bottom: 60px;
}

.compliance-header {
  padding: 40px;
  background: linear-gradient(180deg, rgba(11, 19, 37, 0.9) 0%, rgba(4, 7, 14, 0.95) 100%);
  border: 1px solid var(--border-bright);
  box-shadow: 0 0 30px rgba(0, 240, 255, 0.15);
}
.compliance-kicker {
  font-family: var(--font-hud);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 2px;
  color: var(--neon-cyan);
  display: block;
  margin-bottom: 8px;
}
.compliance-title {
  font-family: var(--font-display);
  font-size: 28px;
  font-weight: 900;
  color: #fff;
  letter-spacing: 1px;
  margin-bottom: 12px;
}
.compliance-subtitle {
  font-size: 14px;
  color: var(--text-secondary);
  max-width: 800px;
  line-height: 1.6;
}

.compliance-section {
  padding: 32px;
}
.section-intro-text {
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 20px;
  line-height: 1.6;
}

.legal-notice-box {
  background: rgba(7, 12, 24, 0.8);
  border: 1px solid var(--border-subtle);
  border-left: 4px solid var(--neon-cyan);
  padding: 20px 24px;
  border-radius: 4px;
  margin-bottom: 24px;
}
.legal-box-title {
  font-family: var(--font-hud);
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 10px;
}
.legal-notice-box p {
  font-size: 13px;
  color: var(--text-primary);
  line-height: 1.6;
  margin-bottom: 10px;
}
.legal-subtext {
  color: var(--text-secondary) !important;
  font-size: 12px !important;
}

/* IP Separation Matrix */
.ip-matrix-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.ip-matrix-card {
  background: rgba(11, 19, 37, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 20px;
}
.ip-matrix-card.original {
  border-top: 3px solid var(--neon-cyan);
}
.ip-matrix-card.third-party {
  border-top: 3px solid var(--gold-accent);
}
.ip-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-card);
}
.ip-card-header h4 {
  font-family: var(--font-hud);
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #fff;
}
.ip-feature-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 12px;
  color: var(--text-secondary);
}
.ip-feature-list li strong {
  color: var(--text-primary);
}

/* Compliance Tables */
.compliance-table th {
  font-size: 11px;
  letter-spacing: 1px;
}
.compliance-table td {
  font-size: 12px;
}
.license-tag {
  background: rgba(0, 240, 255, 0.12);
  color: var(--neon-cyan);
  border: 1px solid rgba(0, 240, 255, 0.3);
  font-family: var(--font-hud);
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 3px;
}

/* Dual Grid for Disclaimers */
.compliance-dual-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
}
.disclaimer-body p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 16px;
}
.quote-notice {
  background: rgba(4, 7, 14, 0.85);
  border-left: 3px solid var(--gold-accent);
  padding: 12px 16px;
  font-family: var(--font-hud);
  font-size: 13px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 16px;
  border-radius: 0 4px 4px 0;
}
.sub-clause {
  font-size: 11px !important;
  color: var(--text-muted) !important;
}

/* Data Sources Grid */
.data-sources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
.data-source-card {
  background: rgba(11, 19, 37, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 20px;
  display: flex;
  flex-direction: column;
}
.ds-head {
  margin-bottom: 10px;
}
.ds-category {
  font-family: var(--font-hud);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1px;
  color: var(--neon-cyan);
  text-transform: uppercase;
}
.ds-name {
  font-family: var(--font-hud);
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  margin-top: 4px;
}
.ds-desc {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 16px;
  flex-grow: 1;
}
.ds-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid var(--border-card);
  font-size: 11px;
  color: var(--text-muted);
}

/* ==========================================================================
   Global Rich Footer System
   ========================================================================== */
.bl-global-footer {
  background: #020409;
  border-top: 1px solid var(--border-subtle);
  margin-top: 60px;
  position: relative;
  overflow: hidden;
}
.bl-global-footer::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
}
.footer-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 48px 24px 36px 24px;
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.4fr;
  gap: 36px;
}
@media (max-width: 992px) {
  .footer-container {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 640px) {
  .footer-container {
    grid-template-columns: 1fr;
  }
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}
.footer-brand-title {
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 900;
  letter-spacing: 1.5px;
  color: #fff;
}
.footer-motto {
  font-family: var(--font-hud);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: var(--neon-cyan);
  margin-bottom: 12px;
}
.footer-desc {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 16px;
}
.footer-copyright-main {
  font-size: 12px;
  color: var(--text-primary);
}

.footer-heading {
  font-family: var(--font-hud);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: var(--neon-cyan);
  margin-bottom: 16px;
  text-transform: uppercase;
}
.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.footer-nav-link,
.footer-legal-modal-trigger,
.footer-ext-link {
  font-size: 12px;
  color: var(--text-secondary);
  text-decoration: none;
  cursor: pointer;
  background: none;
  border: none;
  padding: 0;
  text-align: left;
  font-family: var(--font-body);
  transition: var(--transition-fast);
}
.footer-nav-link:hover,
.footer-legal-modal-trigger:hover,
.footer-ext-link:hover {
  color: var(--neon-cyan);
  transform: translateX(3px);
}
.footer-nav-link.highlight {
  color: var(--neon-cyan);
  font-weight: 600;
}

.footer-disclaimer-box {
  background: rgba(11, 19, 37, 0.5);
  border: 1px solid var(--border-card);
  border-radius: 4px;
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.disclaimer-p {
  font-size: 11px;
  color: var(--text-secondary);
  line-height: 1.5;
}
.disclaimer-p strong {
  color: var(--text-primary);
}

.footer-bottom-bar {
  background: #010205;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding: 14px 24px;
}
.footer-bottom-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: var(--text-muted);
  font-family: var(--font-hud);
  letter-spacing: 0.5px;
  flex-wrap: wrap;
  gap: 10px;
}
.status-indicator {
  color: #00ff88;
  font-weight: 700;
}

/* ==========================================================================
   Legal Policy Modals (Privacy & Terms)
   ========================================================================== */
.legal-modal-content {
  padding: 10px 4px;
  color: var(--text-primary);
  line-height: 1.6;
}
.legal-modal-content h2 {
  font-family: var(--font-display);
  font-size: 20px;
  color: var(--neon-cyan);
  margin-bottom: 4px;
}
.legal-modal-content .effective-date {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 20px;
  font-family: var(--font-hud);
}
.legal-modal-content h3 {
  font-family: var(--font-hud);
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  margin-top: 18px;
  margin-bottom: 6px;
  letter-spacing: 0.8px;
}
.legal-modal-content p {
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 12px;
}
.legal-modal-content code {
  background: rgba(0, 240, 255, 0.1);
  color: var(--neon-cyan);
  padding: 2px 6px;
  border-radius: 3px;
  font-family: monospace;
}
"""

with open(r"c:\Users\LENOVO\Desktop\web\css\sections.css", "a", encoding="utf-8") as f:
    f.write(compliance_css)

print("Appended compliance styles to sections.css successfully!")
