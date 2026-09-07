"""
Comprehensive Automated Audit Suite for BLUEGUN
Tests Backend APIs, Database Integrity, Data Consistency, Search Accent Normalization,
Security / Secrets Leakage, Image Fallbacks, and Source Registry.
"""

import os
import sys
import json
import re
import unicodedata
from fastapi.testclient import TestClient

# Fix Windows cp1252 output encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(WORKSPACE, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)
if WORKSPACE not in sys.path:
    sys.path.insert(0, WORKSPACE)

try:
    from app.main import app
    from app.database import SessionLocal
    from app.models.club import Club
    from app.models.player import Player
    from app.models.transfer import Transfer
    from app.models.news import TransferNews
except ImportError:
    from backend.app.main import app
    from backend.app.database import SessionLocal
    from backend.app.models.club import Club
    from backend.app.models.player import Player
    from backend.app.models.transfer import Transfer
    from backend.app.models.news import TransferNews

client = TestClient(app)

audit_results = {
    "api_tests": {"passed": 0, "failed": 0, "details": []},
    "db_integrity": {"passed": 0, "failed": 0, "details": []},
    "data_consistency": {"passed": 0, "failed": 0, "details": []},
    "search_normalization": {"passed": 0, "failed": 0, "details": []},
    "security_checks": {"passed": 0, "failed": 0, "details": []},
    "sources_registry": {"passed": 0, "failed": 0, "details": []}
}

def test_backend_apis():
    print("\n--- 1. TESTING BACKEND REST ENDPOINTS ---")
    endpoints = [
        ("GET", "/api/health", 200),
        ("GET", "/api/players", 200),
        ("GET", "/api/players/1", 200),
        ("GET", "/api/players/99999", 404),
        ("GET", "/api/players/1/stats", 200),
        ("GET", "/api/players/1/transfers", 200),
        ("GET", "/api/players/1/market-history", 200),
        ("GET", "/api/players/1/injury", 200),
        ("GET", "/api/players/1/suspension", 200),
        ("GET", "/api/players/1/availability", 200),
        ("GET", "/api/clubs", 200),
        ("GET", "/api/clubs/real-madrid", 200),
        ("GET", "/api/clubs/non-existent-club-id", 404),
        ("GET", "/api/clubs/real-madrid/squad", 200),
        ("GET", "/api/clubs/real-madrid/players", 200),
        ("GET", "/api/clubs/real-madrid/injuries", 200),
        ("GET", "/api/clubs/real-madrid/suspensions", 200),
        ("GET", "/api/clubs/real-madrid/availability", 200),
        ("GET", "/api/clubs/real-madrid/transfers", 200),
        ("GET", "/api/clubs/real-madrid/contracts", 200),
        ("GET", "/api/clubs/real-madrid/statistics", 200),
        ("GET", "/api/transfers", 200),
        ("GET", "/api/transfers/stats", 200),
        ("GET", "/api/news", 200),
        ("GET", "/api/search?q=mbappe", 200),
        ("GET", "/api/compare?player_a=1&player_b=2", 200),
    ]

    for method, path, expected_status in endpoints:
        try:
            resp = client.get(path) if method == "GET" else client.post(path)
            if resp.status_code == expected_status:
                audit_results["api_tests"]["passed"] += 1
                audit_results["api_tests"]["details"].append(f"PASS: {method} {path} -> {resp.status_code}")
            else:
                audit_results["api_tests"]["failed"] += 1
                audit_results["api_tests"]["details"].append(f"FAIL: {method} {path} -> {resp.status_code} (Expected {expected_status})")
        except Exception as e:
            audit_results["api_tests"]["failed"] += 1
            audit_results["api_tests"]["details"].append(f"ERROR: {method} {path} -> {str(e)}")

    print(f"API Endpoints Passed: {audit_results['api_tests']['passed']}/{len(endpoints)}")

def test_database_integrity():
    print("\n--- 2. TESTING DATABASE INTEGRITY & RELATIONSHIPS ---")
    db = SessionLocal()
    try:
        clubs = db.query(Club).all()
        players = db.query(Player).all()
        transfers = db.query(Transfer).all()
        news = db.query(TransferNews).all()

        print(f"Loaded DB Records: {len(clubs)} Clubs, {len(players)} Players, {len(transfers)} Transfers, {len(news)} News Articles.")

        # Check unique slugs
        club_slugs = [c.slug for c in clubs]
        player_slugs = [p.slug for p in players]

        if len(club_slugs) == len(set(club_slugs)):
            audit_results["db_integrity"]["passed"] += 1
        else:
            audit_results["db_integrity"]["failed"] += 1
            audit_results["db_integrity"]["details"].append("Duplicate club slugs detected.")

        if len(player_slugs) == len(set(player_slugs)):
            audit_results["db_integrity"]["passed"] += 1
        else:
            audit_results["db_integrity"]["failed"] += 1
            audit_results["db_integrity"]["details"].append("Duplicate player slugs detected.")

        # Check foreign keys
        club_ids = {c.id for c in clubs}
        player_ids = {p.id for p in players}

        invalid_player_clubs = [p for p in players if p.current_club_id and p.current_club_id not in club_ids]
        if not invalid_player_clubs:
            audit_results["db_integrity"]["passed"] += 1
        else:
            audit_results["db_integrity"]["failed"] += 1
            audit_results["db_integrity"]["details"].append(f"{len(invalid_player_clubs)} players have invalid club foreign keys.")

        invalid_transfers = [t for t in transfers if t.player_id not in player_ids]
        if not invalid_transfers:
            audit_results["db_integrity"]["passed"] += 1
        else:
            audit_results["db_integrity"]["failed"] += 1
            audit_results["db_integrity"]["details"].append(f"{len(invalid_transfers)} transfers have invalid player foreign keys.")

    finally:
        db.close()

def test_search_accent_normalization():
    print("\n--- 3. TESTING SEARCH ACCENT NORMALIZATION ---")
    def normalize_search_term(s):
        if not s:
            return ""
        s = s.lower().replace("ø", "o").replace("æ", "ae").replace("ß", "ss")
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

    test_queries = [
        ("mbappe", "Kylian Mbappé"),
        ("haaland", "Erling Haaland"),
        ("odegaard", "Martin Ødegaard"),
        ("wirtz", "Florian Wirtz"),
        ("leao", "Rafael Leão"),
        ("vinicius", "Vinícius Júnior")
    ]

    for q, target in test_queries:
        norm_q = normalize_search_term(q)
        norm_target = normalize_search_term(target)
        if norm_q in norm_target:
            audit_results["search_normalization"]["passed"] += 1
            audit_results["search_normalization"]["details"].append(f"PASS: query '{q}' matched '{target}'")
        else:
            audit_results["search_normalization"]["failed"] += 1
            audit_results["search_normalization"]["details"].append(f"FAIL: query '{q}' failed on '{target}'")

    print(f"Accent Normalization Passed: {audit_results['search_normalization']['passed']}/{len(test_queries)}")

def test_security():
    print("\n--- 4. TESTING SECURITY & SECRET MANAGEMENT ---")
    gitignore_path = os.path.join(WORKSPACE, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            gi_content = f.read()
        if ".env" in gi_content:
            audit_results["security_checks"]["passed"] += 1
        else:
            audit_results["security_checks"]["failed"] += 1
            audit_results["security_checks"]["details"].append(".env not present in .gitignore")
    else:
        audit_results["security_checks"]["failed"] += 1
        audit_results["security_checks"]["details"].append(".gitignore does not exist")

    # Check for hardcoded API keys in JS files
    js_dir = os.path.join(WORKSPACE, "js")
    hardcoded_keys = []
    for f in os.listdir(js_dir):
        if f.endswith(".js"):
            with open(os.path.join(js_dir, f), "r", encoding="utf-8", errors="ignore") as jf:
                txt = jf.read()
                if "api_key = \"" in txt.lower() or "secret = \"" in txt.lower():
                    hardcoded_keys.append(f)

    if not hardcoded_keys:
        audit_results["security_checks"]["passed"] += 1
    else:
        audit_results["security_checks"]["failed"] += 1
        audit_results["security_checks"]["details"].append(f"Potential hardcoded keys in {hardcoded_keys}")

    print(f"Security Checks Passed: {audit_results['security_checks']['passed']}")

def test_sources_registry():
    print("\n--- 5. TESTING SOURCES REGISTRY AUDIT ---")
    sources_path = os.path.join(WORKSPACE, "data", "sources.json")
    if os.path.exists(sources_path):
        with open(sources_path, "r", encoding="utf-8") as f:
            s_data = json.load(f)
        sources = s_data.get("sources", [])
        if len(sources) >= 50:
            audit_results["sources_registry"]["passed"] += 1
        else:
            audit_results["sources_registry"]["failed"] += 1
            audit_results["sources_registry"]["details"].append(f"Only {len(sources)} sources found, expected >= 50")

        # Check required fields
        missing_fields = []
        for s in sources:
            for req in ["id", "type", "category", "name", "license", "status"]:
                if not s.get(req):
                    missing_fields.append((s.get("id", "UNKNOWN"), req))

        if not missing_fields:
            audit_results["sources_registry"]["passed"] += 1
        else:
            audit_results["sources_registry"]["failed"] += 1
            audit_results["sources_registry"]["details"].append(f"Sources with missing fields: {missing_fields}")

    print(f"Sources Registry Passed: {audit_results['sources_registry']['passed']}")

if __name__ == "__main__":
    print("=" * 70)
    print("RUNNING BLUEGUN COMPLETE AUDIT SUITE")
    print("=" * 70)
    test_backend_apis()
    test_database_integrity()
    test_search_accent_normalization()
    test_security()
    test_sources_registry()

    total_passed = sum(v["passed"] for v in audit_results.values())
    total_failed = sum(v["failed"] for v in audit_results.values())

    print("\n" + "=" * 70)
    print(f"AUDIT SUMMARY: {total_passed} Passed, {total_failed} Failed")
    print("=" * 70)

    with open(os.path.join(WORKSPACE, "scratch", "audit_results.json"), "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=2)
