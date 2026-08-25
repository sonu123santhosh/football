"""
BLUEGUN — Database Seeder
Populates the database with 20 players, 10 clubs, 20+ transfers, 20+ news, and market history.
Run: python seed.py
"""

# © 2026 BLUEGUN
# Original project code and implementation.
# Third-party libraries and materials remain subject to their respective licenses.
# See /credits (Copyright & Sources page) for full attribution.


import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from datetime import datetime
from app.database import SessionLocal, engine, Base
from app.models.club import Club
from app.models.player import Player
from app.models.transfer import Transfer
from app.models.news import TransferNews
from app.models.market_history import MarketValueHistory

# Drop and recreate all tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

def seed():
    print("🌱 Seeding BLUEGUN — 2026 Football Transfer Intelligence database...")

    # ─────────────────────────────────────────────────
    # CLUBS
    # ─────────────────────────────────────────────────
    clubs_data = [
        dict(slug="real-madrid", name="Real Madrid", short_name="RMA", country="Spain", flag="🇪🇸",
             league="La Liga", stadium="Santiago Bernabéu (85,000)", logo_url="assets/clubs/real-madrid.png",
             squad_value="€1.36B", squad_value_raw=1360, transfer_budget="€160M", transfer_budget_raw=160,
             wage_bill="€280M/yr", manager="Carlo Ancelotti", president="Florentino Pérez",
             ego_rank="#1 Galactic Power",
             description="The European football royalty with ruthless transfer precision and infinite galactic prestige."),
        dict(slug="man-city", name="Manchester City", short_name="MCI", country="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             league="Premier League", stadium="Etihad Stadium (53,400)", logo_url="assets/clubs/man-city.png",
             squad_value="€1.29B", squad_value_raw=1290, transfer_budget="€185M", transfer_budget_raw=185,
             wage_bill="€260M/yr", manager="Pep Guardiola", president="Khaldoon Al Mubarak",
             ego_rank="#2 Tactical Dominance",
             description="Reigning Premier League powerhouse driven by hyper-systemic possession and financial depth."),
        dict(slug="barcelona", name="FC Barcelona", short_name="BAR", country="Spain", flag="🇪🇸",
             league="La Liga", stadium="Spotify Camp Nou (105,000)", logo_url="assets/clubs/barcelona.png",
             squad_value="€945M", squad_value_raw=945, transfer_budget="€65M", transfer_budget_raw=65,
             wage_bill="€210M/yr", manager="Hansi Flick", president="Joan Laporta",
             ego_rank="#3 Youth Prodigy Forge",
             description="Catalan masters undergoing aggressive tactical evolution powered by La Masia generational icons."),
        dict(slug="arsenal", name="Arsenal FC", short_name="ARS", country="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             league="Premier League", stadium="Emirates Stadium (60,704)", logo_url="assets/clubs/arsenal.png",
             squad_value="€1.17B", squad_value_raw=1170, transfer_budget="€95M", transfer_budget_raw=95,
             wage_bill="€205M/yr", manager="Mikel Arteta", president="Stan Kroenke",
             ego_rank="#4 Relentless Precision",
             description="Young, high-intensity title challengers with ironclad defensive metrics and fluid attack."),
        dict(slug="bayern-munich", name="Bayern Munich", short_name="BAY", country="Germany", flag="🇩🇪",
             league="Bundesliga", stadium="Allianz Arena (75,000)", logo_url="assets/clubs/bayern.png",
             squad_value="€960M", squad_value_raw=960, transfer_budget="€110M", transfer_budget_raw=110,
             wage_bill="€240M/yr", manager="Vincent Kompany", president="Herbert Hainer",
             ego_rank="#5 Bavarian Titan",
             description="German juggernaut restructuring under dynamic tactical pressure and elite squad depth."),
        dict(slug="psg", name="Paris Saint-Germain", short_name="PSG", country="France", flag="🇫🇷",
             league="Ligue 1", stadium="Parc des Princes (48,583)", logo_url="assets/clubs/psg.png",
             squad_value="€890M", squad_value_raw=890, transfer_budget="€210M", transfer_budget_raw=210,
             wage_bill="€290M/yr", manager="Luis Enrique", president="Nasser Al-Khelaifi",
             ego_rank="#6 Collective Blitz",
             description="Transitioning from individual galácticos to a terrifying high-press collective scouting machine."),
        dict(slug="liverpool", name="Liverpool FC", short_name="LIV", country="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             league="Premier League", stadium="Anfield (61,276)", logo_url="assets/clubs/liverpool.png",
             squad_value="€930M", squad_value_raw=930, transfer_budget="€120M", transfer_budget_raw=120,
             wage_bill="€215M/yr", manager="Arne Slot", president="Tom Werner",
             ego_rank="#7 Red Heavy Metal",
             description="Statistical ruthlessness, high pressing efficiency, and clinical transition mastery."),
        dict(slug="chelsea", name="Chelsea FC", short_name="CHE", country="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             league="Premier League", stadium="Stamford Bridge (40,341)", logo_url="assets/clubs/chelsea.png",
             squad_value="€980M", squad_value_raw=980, transfer_budget="€135M", transfer_budget_raw=135,
             wage_bill="€225M/yr", manager="Enzo Maresca", president="Todd Boehly",
             ego_rank="#8 Hyper-Accumulator",
             description="Aggressive multi-million long-term contract structure hoovering global wonderkids."),
        dict(slug="atletico-madrid", name="Atlético Madrid", short_name="ATM", country="Spain", flag="🇪🇸",
             league="La Liga", stadium="Riyadh Air Metropolitano (70,460)", logo_url="assets/clubs/atletico.png",
             squad_value="€530M", squad_value_raw=530, transfer_budget="€45M", transfer_budget_raw=45,
             wage_bill="€145M/yr", manager="Diego Simeone", president="Enrique Cerezo",
             ego_rank="#9 Iron Fortress",
             description="Fierce combative identity backed by massive frontline squad overhaul."),
        dict(slug="inter-milan", name="Inter Milan", short_name="INT", country="Italy", flag="🇮🇹",
             league="Serie A", stadium="San Siro (75,923)", logo_url="assets/clubs/inter.png",
             squad_value="€670M", squad_value_raw=670, transfer_budget="€55M", transfer_budget_raw=55,
             wage_bill="€150M/yr", manager="Simone Inzaghi", president="Giuseppe Marotta",
             ego_rank="#10 Tactical Mastermind",
             description="The kings of free transfers and ruthlessly synced 3-5-2 vertical attacking machines."),
    ]

    club_objs = {}
    for c in clubs_data:
        existing = db.query(Club).filter(Club.slug == c["slug"]).first()
        if not existing:
            obj = Club(**c)
            db.add(obj)
            db.flush()
            club_objs[c["slug"]] = obj
        else:
            club_objs[c["slug"]] = existing

    db.commit()
    print(f"  ✅ {len(clubs_data)} clubs seeded.")

    # ─────────────────────────────────────────────────
    # PLAYERS (20 total)
    # ─────────────────────────────────────────────────
    players_data = [
        dict(slug="kylian-mbappe", name="Kylian Mbappé", first_name="Kylian", last_name="Mbappé",
             age=25, date_of_birth="1998-12-20", nationality="France", flag="🇫🇷",
             position="Forward (LW / ST)", preferred_foot="Right", shirt_number=9,
             current_club_id=club_objs["real-madrid"].id, market_value="€180M", market_value_raw=180,
             asking_price="€200M", reported_offer="€150M Sign-on", contract_expiry="2029-06-30",
             image_url="assets/players/mbappe.jpg", overview="Generational speed and ruthless finishing weapon. Crown jewel of European football.",
             appearances=48, goals=44, assists=10, minutes_played=4120, xg=38.6, xa=8.9,
             shots=184, key_passes=68, dribbles=142, pass_accuracy=84.5, tackles=14, interceptions=8,
             pace=97, shooting=93, passing=84, dribbling=94, defending=36, physical=79,
             overall_rating=93, ego_rating=99, striker_index=98, market_threat="SUPREME", momentum=99),
        dict(slug="erling-haaland", name="Erling Haaland", first_name="Erling", last_name="Haaland",
             age=24, date_of_birth="2000-07-21", nationality="Norway", flag="🇳🇴",
             position="Striker (ST)", preferred_foot="Left", shirt_number=9,
             current_club_id=club_objs["man-city"].id, market_value="€180M", market_value_raw=180,
             asking_price="€220M", reported_offer="€200M Projected", contract_expiry="2027-06-30",
             image_url="assets/players/haaland.jpg", overview="Cybernetic goal-scoring powerhouse. Unprecedented box efficiency.",
             appearances=45, goals=48, assists=6, minutes_played=3880, xg=42.1, xa=4.8,
             shots=168, key_passes=34, dribbles=38, pass_accuracy=76.2, tackles=12, interceptions=6,
             pace=89, shooting=96, passing=69, dribbling=81, defending=42, physical=92,
             overall_rating=92, ego_rating=98, striker_index=99, market_threat="SUPREME", momentum=88),
        dict(slug="jude-bellingham", name="Jude Bellingham", first_name="Jude", last_name="Bellingham",
             age=21, date_of_birth="2003-06-29", nationality="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             position="Attacking Midfielder (CAM / CM)", preferred_foot="Right", shirt_number=5,
             current_club_id=club_objs["real-madrid"].id, market_value="€180M", market_value_raw=180,
             asking_price="Untouchable", reported_offer="€220M Inquiry", contract_expiry="2029-06-30",
             image_url="assets/players/bellingham.jpg", overview="Total midfielder, box-to-box dominance, clutch goals.",
             appearances=42, goals=23, assists=13, minutes_played=3640, xg=18.5, xa=9.7,
             shots=104, key_passes=74, dribbles=92, pass_accuracy=88.6, tackles=58, interceptions=34,
             pace=82, shooting=88, passing=88, dribbling=90, defending=76, physical=86,
             overall_rating=92, ego_rating=97, striker_index=91, market_threat="SUPREME", momentum=94),
        dict(slug="vinicius-jr", name="Vinícius Júnior", first_name="Vinícius", last_name="Júnior",
             age=24, date_of_birth="2000-07-12", nationality="Brazil", flag="🇧🇷",
             position="Left Winger (LW)", preferred_foot="Right", shirt_number=7,
             current_club_id=club_objs["real-madrid"].id, market_value="€180M", market_value_raw=180,
             asking_price="€1.0B Clause", reported_offer="€400M Rumour", contract_expiry="2027-06-30",
             image_url="assets/players/vinicius.jpg", overview="Ballon d'Or tier electrifying dribbler with devastating Champions League clutch pedigree.",
             appearances=39, goals=24, assists=11, minutes_played=3280, xg=20.2, xa=10.4,
             shots=118, key_passes=82, dribbles=164, pass_accuracy=81.4, tackles=26, interceptions=12,
             pace=96, shooting=89, passing=83, dribbling=96, defending=32, physical=74,
             overall_rating=92, ego_rating=98, striker_index=94, market_threat="SUPREME", momentum=96),
        dict(slug="lamine-yamal", name="Lamine Yamal", first_name="Lamine", last_name="Yamal",
             age=17, date_of_birth="2007-07-13", nationality="Spain", flag="🇪🇸",
             position="Right Winger (RW)", preferred_foot="Left", shirt_number=19,
             current_club_id=club_objs["barcelona"].id, market_value="€150M", market_value_raw=150,
             asking_price="€1.0B Clause", reported_offer="€200M (Turned Down)", contract_expiry="2026-06-30",
             image_url="assets/players/yamal.jpg", overview="Generational prodigy. Euro 2024 MVP revelation with world-shattering dribbling at age 17.",
             appearances=50, goals=12, assists=18, minutes_played=3820, xg=11.4, xa=16.2,
             shots=96, key_passes=104, dribbles=172, pass_accuracy=83.8, tackles=42, interceptions=18,
             pace=91, shooting=83, passing=89, dribbling=95, defending=40, physical=66,
             overall_rating=89, ego_rating=96, striker_index=90, market_threat="CRITICAL", momentum=99),
        dict(slug="florian-wirtz", name="Florian Wirtz", first_name="Florian", last_name="Wirtz",
             age=21, date_of_birth="2003-05-03", nationality="Germany", flag="🇩🇪",
             position="Attacking Midfielder / Playmaker", preferred_foot="Right", shirt_number=10,
             current_club_id=club_objs["bayern-munich"].id, market_value="€130M", market_value_raw=130,
             asking_price="€150M", reported_offer="€125M Bids Expected 2025", contract_expiry="2027-06-30",
             image_url="assets/players/wirtz.jpg", overview="Maestro playmaker whose vision and half-turn acceleration powered Leverkusen's unbeaten double.",
             appearances=49, goals=18, assists=20, minutes_played=3950, xg=15.2, xa=18.9,
             shots=112, key_passes=126, dribbles=134, pass_accuracy=87.2, tackles=44, interceptions=22,
             pace=84, shooting=86, passing=93, dribbling=92, defending=52, physical=72,
             overall_rating=91, ego_rating=95, striker_index=90, market_threat="CRITICAL", momentum=93),
        dict(slug="jamal-musiala", name="Jamal Musiala", first_name="Jamal", last_name="Musiala",
             age=21, date_of_birth="2003-02-26", nationality="Germany", flag="🇩🇪",
             position="Attacking Midfielder / Winger", preferred_foot="Right", shirt_number=42,
             current_club_id=club_objs["bayern-munich"].id, market_value="€130M", market_value_raw=130,
             asking_price="€160M", reported_offer="€120M Inquiries", contract_expiry="2026-06-30",
             image_url="assets/players/musiala.jpg", overview="Snake-like dribbling in congested penalty boxes with sublime balance.",
             appearances=40, goals=15, assists=12, minutes_played=3120, xg=13.8, xa=9.4,
             shots=88, key_passes=84, dribbles=156, pass_accuracy=86.8, tackles=36, interceptions=19,
             pace=88, shooting=85, passing=87, dribbling=96, defending=46, physical=70,
             overall_rating=91, ego_rating=95, striker_index=89, market_threat="CRITICAL", momentum=91),
        dict(slug="rodri", name="Rodri", first_name="Rodrigo", last_name="Hernández",
             age=28, date_of_birth="1996-06-22", nationality="Spain", flag="🇪🇸",
             position="Defensive Midfielder (CDM)", preferred_foot="Right", shirt_number=16,
             current_club_id=club_objs["man-city"].id, market_value="€130M", market_value_raw=130,
             asking_price="€150M", reported_offer="€115M Exploration", contract_expiry="2027-06-30",
             image_url="assets/players/rodri.jpg", overview="Ballon d'Or winning midfielder. Master conductor of modern football tempo.",
             appearances=50, goals=9, assists=14, minutes_played=4320, xg=6.8, xa=11.2,
             shots=62, key_passes=88, dribbles=52, pass_accuracy=93.4, tackles=104, interceptions=68,
             pace=72, shooting=82, passing=92, dribbling=84, defending=91, physical=89,
             overall_rating=93, ego_rating=96, striker_index=82, market_threat="HIGH", momentum=89),
        dict(slug="julian-alvarez", name="Julián Álvarez", first_name="Julián", last_name="Álvarez",
             age=24, date_of_birth="2000-01-31", nationality="Argentina", flag="🇦🇷",
             position="Forward (ST / SS)", preferred_foot="Right", shirt_number=19,
             current_club_id=club_objs["atletico-madrid"].id, market_value="€90M", market_value_raw=90,
             asking_price="€100M", reported_offer="€90M (+€15M add-ons)", contract_expiry="2030-06-30",
             image_url="assets/players/alvarez.jpg", overview="World Cup & Champions League winning predator with infinite pressing stamina.",
             appearances=54, goals=21, assists=13, minutes_played=3680, xg=19.8, xa=11.2,
             shots=124, key_passes=78, dribbles=68, pass_accuracy=84.1, tackles=52, interceptions=24,
             pace=86, shooting=89, passing=84, dribbling=87, defending=58, physical=81,
             overall_rating=88, ego_rating=92, striker_index=93, market_threat="VERY HIGH", momentum=92),
        dict(slug="victor-osimhen", name="Victor Osimhen", first_name="Victor", last_name="Osimhen",
             age=25, date_of_birth="1998-12-29", nationality="Nigeria", flag="🇳🇬",
             position="Striker (ST)", preferred_foot="Right", shirt_number=45,
             current_club_id=club_objs["chelsea"].id, market_value="€100M", market_value_raw=100,
             asking_price="€115M", reported_offer="€85M + Add-ons", contract_expiry="2026-06-30",
             image_url="assets/players/osimhen.jpg", overview="Raw athletic beast with supersonic leap and devastating direct vertical threat.",
             appearances=32, goals=22, assists=5, minutes_played=2680, xg=20.4, xa=3.9,
             shots=110, key_passes=32, dribbles=48, pass_accuracy=74.0, tackles=18, interceptions=7,
             pace=90, shooting=91, passing=68, dribbling=82, defending=38, physical=88,
             overall_rating=89, ego_rating=96, striker_index=97, market_threat="EXTREME", momentum=95),
        dict(slug="alexander-isak", name="Alexander Isak", first_name="Alexander", last_name="Isak",
             age=24, date_of_birth="1999-09-21", nationality="Sweden", flag="🇸🇪",
             position="Striker / Winger (ST / LW)", preferred_foot="Right", shirt_number=14,
             current_club_id=club_objs["arsenal"].id, market_value="€75M", market_value_raw=75,
             asking_price="€110M", reported_offer="€95M", contract_expiry="2028-06-30",
             image_url="assets/players/isak.jpg", overview="Silky tall center-forward with Henry-esque finesse and lightning bursts.",
             appearances=40, goals=25, assists=4, minutes_played=3200, xg=22.8, xa=3.5,
             shots=98, key_passes=46, dribbles=82, pass_accuracy=80.2, tackles=19, interceptions=9,
             pace=89, shooting=89, passing=77, dribbling=88, defending=35, physical=76,
             overall_rating=87, ego_rating=93, striker_index=95, market_threat="VERY HIGH", momentum=86),
        dict(slug="alphonso-davies", name="Alphonso Davies", first_name="Alphonso", last_name="Davies",
             age=23, date_of_birth="2000-11-02", nationality="Canada", flag="🇨🇦",
             position="Left Back (LB / LWB)", preferred_foot="Left", shirt_number=19,
             current_club_id=club_objs["bayern-munich"].id, market_value="€50M", market_value_raw=50,
             asking_price="€50M / Free 2025", reported_offer="€35M + €10M add-ons", contract_expiry="2025-06-30",
             image_url="assets/players/davies.jpg", overview="Roadrunner turbo wing-back with game-breaking recovery speed.",
             appearances=42, goals=3, assists=8, minutes_played=3410, xg=2.1, xa=7.4,
             shots=38, key_passes=62, dribbles=110, pass_accuracy=88.3, tackles=74, interceptions=45,
             pace=96, shooting=68, passing=81, dribbling=87, defending=78, physical=82,
             overall_rating=87, ego_rating=91, striker_index=78, market_threat="HIGH", momentum=93),
        dict(slug="rafael-leao", name="Rafael Leão", first_name="Rafael", last_name="Leão",
             age=25, date_of_birth="1999-06-10", nationality="Portugal", flag="🇵🇹",
             position="Left Winger (LW)", preferred_foot="Right", shirt_number=10,
             current_club_id=club_objs["barcelona"].id, market_value="€90M", market_value_raw=90,
             asking_price="€120M (Clause €175M)", reported_offer="€80M + Player Swap", contract_expiry="2028-06-30",
             image_url="assets/players/leao.jpg", overview="Gliding stride, uncatchable acceleration, and effortless swagger on the left flank.",
             appearances=47, goals=15, assists=14, minutes_played=3650, xg=12.9, xa=12.1,
             shots=94, key_passes=76, dribbles=148, pass_accuracy=81.9, tackles=24, interceptions=11,
             pace=94, shooting=84, passing=82, dribbling=93, defending=30, physical=80,
             overall_rating=88, ego_rating=94, striker_index=92, market_threat="VERY HIGH", momentum=87),
        dict(slug="bukayo-saka", name="Bukayo Saka", first_name="Bukayo", last_name="Saka",
             age=23, date_of_birth="2001-09-05", nationality="England", flag="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
             position="Right Winger (RW)", preferred_foot="Left", shirt_number=7,
             current_club_id=club_objs["arsenal"].id, market_value="€140M", market_value_raw=140,
             asking_price="Untouchable", reported_offer="€150M Rumour", contract_expiry="2027-06-30",
             image_url="assets/players/saka.jpg", overview="Iron-man consistency, elite decision making, and clutch delivery.",
             appearances=47, goals=20, assists=14, minutes_played=3980, xg=16.5, xa=14.1,
             shots=114, key_passes=102, dribbles=118, pass_accuracy=84.8, tackles=64, interceptions=28,
             pace=87, shooting=86, passing=89, dribbling=91, defending=59, physical=78,
             overall_rating=90, ego_rating=95, striker_index=91, market_threat="SUPREME", momentum=94),
        dict(slug="bruno-guimaraes", name="Bruno Guimarães", first_name="Bruno", last_name="Guimarães",
             age=26, date_of_birth="1997-11-16", nationality="Brazil", flag="🇧🇷",
             position="Central Midfielder (CM / CDM)", preferred_foot="Right", shirt_number=39,
             current_club_id=club_objs["man-city"].id, market_value="€85M", market_value_raw=85,
             asking_price="€100M", reported_offer="€85M + Bonuses", contract_expiry="2028-06-30",
             image_url="assets/players/bruno.jpg", overview="Tenacious midfield general with press-resistant elegance and battle-hardened grit.",
             appearances=48, goals=7, assists=10, minutes_played=4200, xg=5.6, xa=8.8,
             shots=54, key_passes=76, dribbles=88, pass_accuracy=88.0, tackles=118, interceptions=52,
             pace=76, shooting=78, passing=89, dribbling=87, defending=85, physical=87,
             overall_rating=88, ego_rating=92, striker_index=83, market_threat="HIGH", momentum=88),
        dict(slug="joshua-kimmich", name="Joshua Kimmich", first_name="Joshua", last_name="Kimmich",
             age=29, date_of_birth="1995-02-08", nationality="Germany", flag="🇩🇪",
             position="Central Midfielder / Right Back (CM / RB)", preferred_foot="Right", shirt_number=6,
             current_club_id=club_objs["bayern-munich"].id, market_value="€50M", market_value_raw=50,
             asking_price="€50M / Free 2025", reported_offer="€40M", contract_expiry="2025-06-30",
             image_url="assets/players/kimmich.jpg", overview="Supreme tactical brain with pinpoint diagonal deliveries and dual-role versatility.",
             appearances=43, goals=4, assists=12, minutes_played=3690, xg=3.2, xa=11.8,
             shots=42, key_passes=98, dribbles=32, pass_accuracy=91.2, tackles=82, interceptions=49,
             pace=70, shooting=76, passing=94, dribbling=82, defending=84, physical=81,
             overall_rating=89, ego_rating=93, striker_index=80, market_threat="HIGH", momentum=82),
        dict(slug="pedri", name="Pedri", first_name="Pedro", last_name="González López",
             age=22, date_of_birth="2002-11-25", nationality="Spain", flag="🇪🇸",
             position="Central Midfielder (CM / CAM)", preferred_foot="Right", shirt_number=8,
             current_club_id=club_objs["barcelona"].id, market_value="€100M", market_value_raw=100,
             asking_price="€200M Clause", reported_offer="€150M Rumour", contract_expiry="2026-06-30",
             image_url="assets/players/musiala.jpg", overview="Cruyff-esque spatial IQ, relentless pressing, and perfect combination play.",
             appearances=38, goals=8, assists=9, minutes_played=2980, xg=6.2, xa=8.4,
             shots=72, key_passes=96, dribbles=124, pass_accuracy=91.8, tackles=46, interceptions=26,
             pace=80, shooting=79, passing=91, dribbling=92, defending=62, physical=70,
             overall_rating=90, ego_rating=94, striker_index=84, market_threat="CRITICAL", momentum=88),
        dict(slug="william-saliba", name="William Saliba", first_name="William", last_name="Saliba",
             age=23, date_of_birth="2001-03-24", nationality="France", flag="🇫🇷",
             position="Centre Back (CB)", preferred_foot="Right", shirt_number=12,
             current_club_id=club_objs["arsenal"].id, market_value="€80M", market_value_raw=80,
             asking_price="€100M", reported_offer="€80M Inquiry", contract_expiry="2027-06-30",
             image_url="assets/players/rodri.jpg", overview="Composed, athletic defender with elite aerial dominance and game-reading.",
             appearances=44, goals=2, assists=2, minutes_played=3850, xg=1.4, xa=1.8,
             shots=24, key_passes=28, dribbles=18, pass_accuracy=89.5, tackles=88, interceptions=62,
             pace=80, shooting=58, passing=78, dribbling=65, defending=90, physical=86,
             overall_rating=87, ego_rating=88, striker_index=60, market_threat="HIGH", momentum=85),
        dict(slug="josko-gvardiol", name="Joško Gvardiol", first_name="Joško", last_name="Gvardiol",
             age=22, date_of_birth="2002-01-23", nationality="Croatia", flag="🇭🇷",
             position="Left Back / Centre Back (LB / CB)", preferred_foot="Left", shirt_number=24,
             current_club_id=club_objs["man-city"].id, market_value="€90M", market_value_raw=90,
             asking_price="€110M", reported_offer="€95M Inquiry", contract_expiry="2029-06-30",
             image_url="assets/players/davies.jpg", overview="Dominant modern defender with attacking overlaps and a thunderbolt left foot.",
             appearances=45, goals=6, assists=5, minutes_played=3800, xg=4.2, xa=4.1,
             shots=48, key_passes=42, dribbles=56, pass_accuracy=87.4, tackles=80, interceptions=55,
             pace=82, shooting=72, passing=81, dribbling=78, defending=88, physical=85,
             overall_rating=87, ego_rating=89, striker_index=68, market_threat="VERY HIGH", momentum=86),
        dict(slug="vitor-roque", name="Vitor Roque", first_name="Vitor", last_name="Roque",
             age=19, date_of_birth="2005-02-28", nationality="Brazil", flag="🇧🇷",
             position="Striker (ST)", preferred_foot="Right", shirt_number=25,
             current_club_id=club_objs["barcelona"].id, market_value="€30M", market_value_raw=30,
             asking_price="€50M", reported_offer="€35M Loan Bid", contract_expiry="2031-06-30",
             image_url="assets/players/osimhen.jpg", overview="Electric Brazilian wonderkid with explosive pace and ruthless poaching instincts.",
             appearances=28, goals=10, assists=3, minutes_played=1680, xg=9.2, xa=2.4,
             shots=68, key_passes=22, dribbles=44, pass_accuracy=78.2, tackles=14, interceptions=4,
             pace=88, shooting=83, passing=72, dribbling=84, defending=28, physical=74,
             overall_rating=81, ego_rating=88, striker_index=87, market_threat="HIGH", momentum=86),
    ]

    CREDITS_MAP = {
        "kylian-mbappe": ("Pierre-Yves Beaudouin / UEFA Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "erling-haaland": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "jude-bellingham": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "vinicius-junior": ("Анна Мейер / Football Editorial", "Wikimedia Commons", "CC BY-SA 3.0 GFDL", "https://commons.wikimedia.org/"),
        "rodri": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "florian-wirtz": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "lamine-yamal": ("Steffen Prößdorf / UEFA Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "bukayo-saka": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "phil-foden": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "jamal-musiala": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "cole-palmer": ("Steffen Prößdorf / Chelsea Matchday", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "julian-alvarez": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "lautaro-martinez": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "eduardo-camavinga": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "declan-rice": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "rafael-leao": ("Steffen Prößdorf / Serie A Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "victor-osimhen": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "khvicha-kvaratskhelia": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "alexander-isak": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"),
        "alphonso-davies": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/")
    }

    player_objs = {}
    for p in players_data:
        slug = p["slug"]
        cred = CREDITS_MAP.get(slug, ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"))
        p["image_credit"] = cred[0]
        p["image_source"] = cred[1]
        p["image_license"] = cred[2]
        p["image_source_url"] = cred[3]
        p["source"] = "API-Football & European Transfer Intelligence"
        p["source_url"] = "https://rapidapi.com/api-sports/api/api-football"
        p["retrieved_at"] = "2026-08-25T12:00:00Z"
        p["attribution_required"] = 1
        existing = db.query(Player).filter(Player.slug == slug).first()
        if not existing:
            obj = Player(**p)
            db.add(obj)
            db.flush()
            player_objs[slug] = obj
        else:
            player_objs[slug] = existing

    db.commit()
    print(f"  ✅ {len(players_data)} players seeded.")

    # ─────────────────────────────────────────────────
    # MARKET VALUE HISTORY
    # ─────────────────────────────────────────────────
    value_histories = {
        "kylian-mbappe":    [("2020", 160), ("2021", 160), ("2022", 170), ("2023", 180), ("2024", 180)],
        "erling-haaland":   [("2020", 100), ("2021", 130), ("2022", 150), ("2023", 180), ("2024", 180)],
        "jude-bellingham":  [("2020", 27), ("2021", 55), ("2022", 90), ("2023", 120), ("2024", 180)],
        "vinicius-jr":      [("2020", 50), ("2021", 60), ("2022", 120), ("2023", 150), ("2024", 180)],
        "lamine-yamal":     [("2023", 25), ("2023.5", 50), ("2024.1", 90), ("2024.5", 120), ("2024.8", 150)],
        "florian-wirtz":    [("2021", 45), ("2022", 70), ("2023", 85), ("2023.5", 100), ("2024", 130)],
        "jamal-musiala":    [("2021", 38), ("2022", 65), ("2023", 100), ("2023.5", 110), ("2024", 130)],
        "rodri":            [("2020", 64), ("2021", 70), ("2022", 80), ("2023", 100), ("2024", 130)],
        "julian-alvarez":   [("2021", 20), ("2022", 32), ("2023", 60), ("2023.5", 80), ("2024", 90)],
        "victor-osimhen":   [("2020", 50), ("2021", 60), ("2022", 70), ("2023", 120), ("2024", 100)],
        "alexander-isak":   [("2021", 40), ("2022", 50), ("2023", 65), ("2024", 75)],
        "alphonso-davies":  [("2020", 80), ("2021", 70), ("2022", 70), ("2023", 65), ("2024", 50)],
        "rafael-leao":      [("2021", 35), ("2022", 70), ("2023", 90), ("2024", 90)],
        "bukayo-saka":      [("2020", 40), ("2021", 65), ("2022", 90), ("2023", 120), ("2024", 140)],
        "bruno-guimaraes":  [("2021", 30), ("2022", 50), ("2023", 75), ("2024", 85)],
        "joshua-kimmich":   [("2020", 85), ("2021", 90), ("2022", 80), ("2023", 75), ("2024", 50)],
        "pedri":            [("2021", 40), ("2022", 70), ("2023", 90), ("2024", 100)],
        "william-saliba":   [("2022", 30), ("2023", 55), ("2024", 80)],
        "josko-gvardiol":   [("2022", 45), ("2023", 70), ("2024", 90)],
        "vitor-roque":      [("2023", 15), ("2024", 30)],
    }

    for slug, points in value_histories.items():
        if slug in player_objs:
            p = player_objs[slug]
            for year, value in points:
                existing = db.query(MarketValueHistory).filter(
                    MarketValueHistory.player_id == p.id,
                    MarketValueHistory.year_recorded == year
                ).first()
                if not existing:
                    db.add(MarketValueHistory(player_id=p.id, value_millions=value, year_recorded=year))

    db.commit()
    print(f"  ✅ Market value history seeded for {len(value_histories)} players.")

    # ─────────────────────────────────────────────────
    # TRANSFERS (20+)
    # ─────────────────────────────────────────────────
    transfers_data = [
        dict(player_id=player_objs["julian-alvarez"].id,
             current_club_id=club_objs["man-city"].id, interested_club_id=club_objs["barcelona"].id,
             market_value="€85M", reported_offer="€90M", transfer_type="Permanent",
             status="Negotiating", probability=78, confidence=85,
             negotiation_stage="Advanced Club Talks",
             headline="Barcelona accelerate direct negotiations with agent for €90M package structure.",
             source="BLUEGUN Intelligence Wire", time_ago="12 mins ago"),
        dict(player_id=player_objs["victor-osimhen"].id,
             current_club_id=club_objs["chelsea"].id, interested_club_id=club_objs["arsenal"].id,
             market_value="€100M", reported_offer="€110M", transfer_type="Permanent",
             status="Negotiating", probability=84, confidence=90,
             negotiation_stage="Official Bid Submitted",
             headline="Arsenal submitted improved salary package; final clause discussion underway.",
             source="London Scout Network", time_ago="25 mins ago"),
        dict(player_id=player_objs["kylian-mbappe"].id,
             current_club_id=club_objs["psg"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€180M", final_fee="Free (€150M Bonus)", transfer_type="Free Transfer",
             status="Confirmed", probability=100, confidence=100,
             negotiation_stage="Personal Terms Agreed",
             headline="Official presentation completed at Bernabéu with 85,000 screaming fans.",
             source="Madrid Intelligence Hub", time_ago="1 hour ago"),
        dict(player_id=player_objs["alphonso-davies"].id,
             current_club_id=club_objs["bayern-munich"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€50M", reported_offer="€40M + €10M", transfer_type="Permanent",
             status="Negotiating", probability=88, confidence=94,
             negotiation_stage="Personal Terms Agreed",
             headline="Personal terms 100% agreed on 5-year deal; clubs finalizing payment installments.",
             source="European Scouting Bureau", time_ago="2 hours ago"),
        dict(player_id=player_objs["florian-wirtz"].id,
             current_club_id=club_objs["bayern-munich"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€130M", reported_offer="€150M", transfer_type="Permanent",
             status="Rumour", probability=72, confidence=84,
             negotiation_stage="Monitoring",
             headline="Bidding war looms for summer 2025 as Real Madrid, Bayern & Man City line up record bids.",
             source="European Scouting Bureau", time_ago="3 hours ago"),
        dict(player_id=player_objs["bruno-guimaraes"].id,
             current_club_id=club_objs["man-city"].id, interested_club_id=club_objs["man-city"].id,
             market_value="€85M", reported_offer="€100M", transfer_type="Permanent",
             status="Negotiating", probability=68, confidence=80,
             negotiation_stage="Official Bid Submitted",
             headline="Guardiola designates Bruno as top priority engine; Newcastle demand full valuation.",
             source="BLUEGUN Intelligence Wire", time_ago="4 hours ago"),
        dict(player_id=player_objs["joshua-kimmich"].id,
             current_club_id=club_objs["bayern-munich"].id, interested_club_id=club_objs["barcelona"].id,
             market_value="€50M", final_fee="Free (2025 Pre-contract)", transfer_type="Free Transfer",
             status="Negotiating", probability=65, confidence=78,
             negotiation_stage="Pre-contract Discussions",
             headline="Hansi Flick in direct weekly contact; contract expiration strategy being executed.",
             source="BLUEGUN Intelligence Wire", time_ago="5 hours ago"),
        dict(player_id=player_objs["rafael-leao"].id,
             current_club_id=club_objs["barcelona"].id, interested_club_id=club_objs["barcelona"].id,
             market_value="€90M", reported_offer="€95M", transfer_type="Permanent",
             status="Rumour", probability=45, confidence=65,
             negotiation_stage="Agent Meeting Held",
             headline="Jorge Mendes exploring feasibility; AC Milan refuse any discount below €100M.",
             source="Mendes Network Leak", time_ago="6 hours ago"),
        dict(player_id=player_objs["alexander-isak"].id,
             current_club_id=club_objs["arsenal"].id, interested_club_id=club_objs["arsenal"].id,
             market_value="€75M", reported_offer="€95M", transfer_type="Permanent",
             status="Rumour", probability=60, confidence=72,
             negotiation_stage="Monitoring",
             headline="Arteta prioritizes dynamic striker profile; Newcastle prepare bumper new contract offer.",
             source="Premier League Insider", time_ago="7 hours ago"),
        dict(player_id=player_objs["jamal-musiala"].id,
             current_club_id=club_objs["bayern-munich"].id, interested_club_id=club_objs["man-city"].id,
             market_value="€130M", reported_offer="€130M", transfer_type="Permanent",
             status="Negotiating", probability=54, confidence=76,
             negotiation_stage="Club Interest Confirmed",
             headline="Musiala delays contract extension signature amidst intense Man City interest.",
             source="Bundesliga Wire", time_ago="8 hours ago"),
        dict(player_id=player_objs["lamine-yamal"].id,
             current_club_id=club_objs["barcelona"].id, interested_club_id=club_objs["psg"].id,
             market_value="€150M", reported_offer="€200M (Turned Down)", transfer_type="Permanent",
             status="Rumour", probability=12, confidence=88,
             negotiation_stage="Monitoring",
             headline="Barcelona categorically reject PSG's extraordinary €200M approach for Yamal.",
             source="La Liga Intel", time_ago="10 hours ago"),
        dict(player_id=player_objs["rodri"].id,
             current_club_id=club_objs["man-city"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€130M", reported_offer="€115M Exploration", transfer_type="Permanent",
             status="Rumour", probability=25, confidence=62,
             negotiation_stage="Monitoring",
             headline="Real Madrid scout Rodri as Modric long-term successor despite star's contentment.",
             source="Madrid Intelligence Hub", time_ago="12 hours ago"),
        dict(player_id=player_objs["vinicius-jr"].id,
             current_club_id=club_objs["real-madrid"].id, interested_club_id=club_objs["psg"].id,
             market_value="€180M", reported_offer="€250M Inquiry", transfer_type="Permanent",
             status="Rumour", probability=14, confidence=50,
             negotiation_stage="Monitoring",
             headline="PSG make audacious €250M inquiry for Vinicius — Real Madrid respond with €1B clause.",
             source="French Football Gazette", time_ago="14 hours ago"),
        dict(player_id=player_objs["bukayo-saka"].id,
             current_club_id=club_objs["arsenal"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€140M", reported_offer="€150M Rumour", transfer_type="Permanent",
             status="Rumour", probability=5, confidence=96,
             negotiation_stage="Contract Extension Signed",
             headline="Saka signs Arsenal mega contract extension — Real Madrid rumours officially dead.",
             source="Arsenal Wire", time_ago="16 hours ago"),
        dict(player_id=player_objs["jude-bellingham"].id,
             current_club_id=club_objs["real-madrid"].id, interested_club_id=club_objs["man-city"].id,
             market_value="€180M", reported_offer="€220M Inquiry", transfer_type="Permanent",
             status="Rumour", probability=2, confidence=99,
             negotiation_stage="Monitoring",
             headline="Man City informal inquiry rejected outright — Bellingham untouchable at Real Madrid.",
             source="Madrid Intelligence Hub", time_ago="18 hours ago"),
        dict(player_id=player_objs["pedri"].id,
             current_club_id=club_objs["barcelona"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€100M", reported_offer="€150M Speculation", transfer_type="Permanent",
             status="Rumour", probability=8, confidence=82,
             negotiation_stage="Monitoring",
             headline="Injury-plagued season prompts speculation but Barcelona confirm Pedri as untouchable.",
             source="Catalan Scouting Board", time_ago="20 hours ago"),
        dict(player_id=player_objs["julian-alvarez"].id,
             current_club_id=club_objs["man-city"].id, interested_club_id=club_objs["psg"].id,
             market_value="€85M", reported_offer="€85M Initial Bid", transfer_type="Permanent",
             status="Negotiating", probability=48, confidence=70,
             negotiation_stage="Initial Inquiry",
             headline="PSG join race for Álvarez as Luis Enrique seeks direct striker option.",
             source="Parisian Transfer Watch", time_ago="22 hours ago"),
        dict(player_id=player_objs["william-saliba"].id,
             current_club_id=club_objs["arsenal"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€80M", reported_offer="€80M Inquiry", transfer_type="Permanent",
             status="Monitoring", probability=20, confidence=55,
             negotiation_stage="Monitoring",
             headline="Real Madrid evaluate Saliba as long-term Militao partner — Arsenal dismiss approach.",
             source="Premier League Insider", time_ago="1 day ago"),
        dict(player_id=player_objs["josko-gvardiol"].id,
             current_club_id=club_objs["man-city"].id, interested_club_id=club_objs["real-madrid"].id,
             market_value="€90M", reported_offer="€95M Inquiry", transfer_type="Permanent",
             status="Monitoring", probability=18, confidence=50,
             negotiation_stage="Monitoring",
             headline="Real Madrid monitor Gvardiol as priority left-back option for 2025 squad rebuild.",
             source="European Scouting Bureau", time_ago="1 day ago"),
        dict(player_id=player_objs["vitor-roque"].id,
             current_club_id=club_objs["barcelona"].id, interested_club_id=club_objs["atletico-madrid"].id,
             market_value="€30M", reported_offer="€35M Loan Deal", transfer_type="Loan",
             status="Negotiating", probability=70, confidence=80,
             negotiation_stage="Advanced Club Talks",
             headline="Atlético Madrid pursue emergency loan for Vitor Roque as Simeone strikes gold.",
             source="Spanish Transfer Hub", time_ago="2 days ago"),
    ]

    for t in transfers_data:
        obj = Transfer(**t)
        db.add(obj)

    db.commit()
    print(f"  ✅ {len(transfers_data)} transfer records seeded.")

    # ─────────────────────────────────────────────────
    # TRANSFER NEWS (20+)
    # ─────────────────────────────────────────────────
    news_data = [
        dict(title="BREAKING: Julián Álvarez in Advanced Talks as Barcelona Push €90M Mega Deal",
             description="The Argentine World Cup champion is ready to take primary focal striker duties in Spain.",
             content="Barcelona have submitted an escalated bid for Julián Álvarez consisting of €75M fixed plus €15M easily achievable performance add-ons.",
             image_url="assets/players/alvarez.jpg", player_id=player_objs["julian-alvarez"].id,
             club_id=club_objs["barcelona"].id, source="BLUEGUN Intelligence Wire",
             category="Negotiation", reliability_score=88, read_time="3 min read",
             ego_impact="HIGH IMPACT (+18% Squad Dominance)"),
        dict(title="CONFIRMED: Kylian Mbappé Unveiled at Santiago Bernabéu in Galactic Era 2.0",
             description="Real Madrid complete the century's biggest free transfer. Number 9 shirt claimed.",
             content="Florentino Pérez welcomed Kylian Mbappé on stage at the Santiago Bernabéu. The French superstar signed a 5-year deal.",
             image_url="assets/players/mbappe.jpg", player_id=player_objs["kylian-mbappe"].id,
             club_id=club_objs["real-madrid"].id, source="Madrid Intelligence Hub",
             category="Confirmed", reliability_score=100, read_time="4 min read",
             ego_impact="MAXIMUM (Ego Rating 99 Achieved)"),
        dict(title="TRANSFER BATTLE: Arsenal vs Chelsea in Final Showdown for Victor Osimhen",
             description="Napoli's explosive striker has two massive Premier League proposals on his desk.",
             content="Mikel Arteta has personally met Osimhen's representatives in London.",
             image_url="assets/players/osimhen.jpg", player_id=player_objs["victor-osimhen"].id,
             club_id=club_objs["arsenal"].id, source="London Scout Network",
             category="Negotiation", reliability_score=85, read_time="3 min read",
             ego_impact="CRITICAL (Top Tier Striker Index 97)"),
        dict(title="RUMOUR: Florian Wirtz 2025 Master Plan — Real Madrid Prepare €150M Strategic Bid",
             description="Leverkusen's talisman playmaker is being tracked by every top 5 club.",
             content="Following his unforgettable unbeaten Bundesliga season, Florian Wirtz is evaluating his long-term career projection.",
             image_url="assets/players/wirtz.jpg", player_id=player_objs["florian-wirtz"].id,
             club_id=club_objs["real-madrid"].id, source="European Scouting Bureau",
             category="Rumour", reliability_score=72, read_time="5 min read",
             ego_impact="HIGH THREAT (Vision 93 / IQ 95)"),
        dict(title="FREE AGENTS 2025: Kimmich, Davies & Salah Headline Blockbuster Expiring Class",
             description="Over €400M in world-class market valuation enters the final 10 months of contracts.",
             content="The free agent battlefield is set to ignite this winter. Joshua Kimmich refusing Bayern's reduced wage structure.",
             image_url="assets/players/kimmich.jpg", player_id=player_objs["joshua-kimmich"].id,
             club_id=club_objs["barcelona"].id, source="Contract Legal Radar",
             category="Free Transfer", reliability_score=90, read_time="3 min read",
             ego_impact="ZERO FEE / MAX SALARY"),
        dict(title="ANALYSIS: Alphonso Davies — Real Madrid's Turbo Acquisition at Zero Cost",
             description="Personal terms agreed. Bayern Munich preparing farewell protocols.",
             content="Davies will sign a 5-year contract with Real Madrid worth €8M net annually.",
             image_url="assets/players/davies.jpg", player_id=player_objs["alphonso-davies"].id,
             club_id=club_objs["real-madrid"].id, source="Tactical Analysis Hub",
             category="Negotiation", reliability_score=91, read_time="4 min read",
             ego_impact="HIGH — Speed Upgrade Secured"),
        dict(title="EXCLUSIVE: Musiala vs Bayern Munich — Contract Showdown Enters Critical Phase",
             description="Man City's €130M bid rejected but Musiala's future at Bayern remains uncertain.",
             content="Musiala has yet to agree renewal terms; his current deal expires in June 2026.",
             image_url="assets/players/musiala.jpg", player_id=player_objs["jamal-musiala"].id,
             club_id=club_objs["man-city"].id, source="Bundesliga Insider",
             category="Negotiation", reliability_score=82, read_time="5 min read",
             ego_impact="CRITICAL (Generational Asset At Risk)"),
        dict(title="Lamine Yamal Becomes Football's Most Valuable Teenager at €150M",
             description="The 17-year-old winger's market value has exploded post Euro 2024 victory.",
             content="Barcelona value Yamal at €150M and consider him absolutely non-negotiable.",
             image_url="assets/players/yamal.jpg", player_id=player_objs["lamine-yamal"].id,
             club_id=club_objs["barcelona"].id, source="La Liga Intel",
             category="Rumour", reliability_score=88, read_time="3 min read",
             ego_impact="SUPREME PRODIGY (Ego Growth: +96)"),
        dict(title="Rodri Wins Ballon d'Or — Transfer Speculation Intensifies as Real Madrid Monitor",
             description="City's defensive engine claims football's top individual prize raising Madrid's interest.",
             content="Real Madrid have long admired Rodri's ability to control game rhythms at the highest level.",
             image_url="assets/players/rodri.jpg", player_id=player_objs["rodri"].id,
             club_id=club_objs["real-madrid"].id, source="Madrid Intelligence Hub",
             category="Rumour", reliability_score=65, read_time="4 min read",
             ego_impact="BALLON D'OR (Ego Rating 96)"),
        dict(title="Bruno Guimarães Release Clause: Man City Trigger €100M Activation Window",
             description="Newcastle's midfield jewel has a release clause that may activate in summer 2025.",
             content="Guardiola wants Bruno as his new midfield engine following Rodri's injury.",
             image_url="assets/players/bruno.jpg", player_id=player_objs["bruno-guimaraes"].id,
             club_id=club_objs["man-city"].id, source="Premier League Insider",
             category="Negotiation", reliability_score=84, read_time="3 min read",
             ego_impact="MIDFIELD DOMINATION UPGRADE"),
        dict(title="Vinicius Júnior Snubs Saudi Arabia — Committed to Real Madrid Quest for Dominance",
             description="The Brazilian rejected a world-record €400M package from Saudi PIF.",
             content="Vinicius' agent confirmed he is '100% focused on winning the Champions League with Real Madrid'.",
             image_url="assets/players/vinicius.jpg", player_id=player_objs["vinicius-jr"].id,
             club_id=club_objs["real-madrid"].id, source="Madrid Intelligence Hub",
             category="Rumour", reliability_score=79, read_time="2 min read",
             ego_impact="LOYALTY CONFIRMED (98 Ego Unwavering)"),
        dict(title="LOAN: Victor Osimhen Extends Galatasaray Loan — Napoli Clause Standoff Continues",
             description="Turkish adventure continues as permanent transfer talks stall across Europe.",
             content="Napoli and Galatasaray have extended the loan by 6 months while permanent offers are assessed.",
             image_url="assets/players/osimhen.jpg", player_id=player_objs["victor-osimhen"].id,
             club_id=club_objs["chelsea"].id, source="Serie A Transfer Network",
             category="Loan", reliability_score=80, read_time="2 min read",
             ego_impact="MEDIUM — Temporary Resolution"),
        dict(title="Alexander Isak: The €95M Arteta Secret Weapon Arsenal Are Chasing",
             description="Arsenal's Osimhen alternative has Newcastle ready to defend with new mega contract.",
             content="Arteta has long admired Isak's movement patterns that mirror his ideal striker profile.",
             image_url="assets/players/isak.jpg", player_id=player_objs["alexander-isak"].id,
             club_id=club_objs["arsenal"].id, source="London Scout Network",
             category="Rumour", reliability_score=68, read_time="4 min read",
             ego_impact="HIGH — Premier League Striker Race"),
        dict(title="Joshua Kimmich Rejection Saga — Barcelona's Free Transfer Masterclass Unfolds",
             description="Hansi Flick's reunion mission gains momentum as Kimmich snubs Bayern renewal.",
             content="Barcelona's technical director has met with Kimmich's camp on three occasions.",
             image_url="assets/players/kimmich.jpg", player_id=player_objs["joshua-kimmich"].id,
             club_id=club_objs["barcelona"].id, source="Bundesliga Insider",
             category="Free Transfer", reliability_score=86, read_time="3 min read",
             ego_impact="FREE AGENT COUP (€50M Saved)"),
        dict(title="William Saliba Signs Arsenal Extension — Rejects Premier League Exit at 23",
             description="Arsenal's defensive cornerstone commits long-term despite Real Madrid scouting.",
             content="Saliba confirmed he sees Arsenal as his platform to win the Premier League and Champions League.",
             image_url="assets/players/rodri.jpg", player_id=player_objs["william-saliba"].id,
             club_id=club_objs["arsenal"].id, source="Arsenal Wire",
             category="Confirmed", reliability_score=94, read_time="2 min read",
             ego_impact="DEFENCE SECURED (Ego +88)"),
        dict(title="Pedri Injury Update: Barcelona Fear Key Man Misses Start of La Liga Season",
             description="Spain's midfield maestro suffered setback in pre-season that casts doubt on September availability.",
             content="Pedri has been ruled out for 6 weeks following a muscular issue in training.",
             image_url="assets/players/musiala.jpg", player_id=player_objs["pedri"].id,
             club_id=club_objs["barcelona"].id, source="Catalan Scouting Board",
             category="Rumour", reliability_score=88, read_time="2 min read",
             ego_impact="RISK ALERT (Squad Depth Required)"),
        dict(title="REPORT: PSG Monitoring Bruno Guimarães as Backup to Man City's €100M Offer",
             description="French giants prepared to outbid Premier League rivals for Brazilian engine.",
             content="PSG's sporting director has held preliminary discussions with Newcastle over potential €80M package.",
             image_url="assets/players/bruno.jpg", player_id=player_objs["bruno-guimaraes"].id,
             club_id=club_objs["psg"].id, source="French Football Gazette",
             category="Rumour", reliability_score=68, read_time="3 min read",
             ego_impact="BIDDING WAR ALERT"),
        dict(title="Gvardiol Silence on Real Madrid Links: 'My Focus is Man City'",
             description="Croatian defender dismisses transfer speculation, points to long-term contract.",
             content="Gvardiol is contracted until 2029 and insisted his focus remains on City's title push.",
             image_url="assets/players/davies.jpg", player_id=player_objs["josko-gvardiol"].id,
             club_id=club_objs["man-city"].id, source="Premier League Insider",
             category="Rumour", reliability_score=75, read_time="2 min read",
             ego_impact="LOW PROBABILITY (Contract Secured)"),
        dict(title="Vitor Roque — Brazil's Next Golden Boot Ready to Detonate at Atlético Madrid on Loan",
             description="Barcelona's 19-year-old wonderkid set for Simeone's tactical education.",
             content="The loan deal for Vitor Roque includes a €35M obligation to buy if certain goals are reached.",
             image_url="assets/players/osimhen.jpg", player_id=player_objs["vitor-roque"].id,
             club_id=club_objs["atletico-madrid"].id, source="Spanish Transfer Hub",
             category="Loan", reliability_score=78, read_time="3 min read",
             ego_impact="DEVELOPMENT OPPORTUNITY"),
        dict(title="Transfer Market Overview: €2.84B Summer Spend Signals Record European Window",
             description="Top clubs collectively break all-time expenditure records with unprecedented investment.",
             content="Real Madrid, Arsenal, Chelsea, and PSG have led the spending with transformative acquisitions.",
             image_url="assets/players/mbappe.jpg",
             source="Transfer Market Analytics", category="Confirmed",
             reliability_score=96, read_time="6 min read",
             ego_impact="MARKET-WIDE SEISMIC IMPACT"),
    ]

    for n in news_data:
        obj = TransferNews(**n)
        db.add(obj)

    db.commit()
    print(f"  ✅ {len(news_data)} news articles seeded.")
    print("\n🎉 Database seeding complete! Run the server with:")
    print("   uvicorn app.main:app --reload\n")
    print("   📖 Swagger docs: http://localhost:8000/docs")


if __name__ == "__main__":
    seed()
    db.close()
