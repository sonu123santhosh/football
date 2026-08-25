"""
External Football & News API Service
Handles optional real-time data fetching with graceful fallback to local database.
Configure via .env: FOOTBALL_API_KEY and NEWS_API_KEY.
"""

import os
import logging
from typing import List, Dict, Any, Optional
import httpx
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

# Example external API endpoints (configure to your preferred provider)
FOOTBALL_API_BASE = "https://api-football-v1.p.rapidapi.com/v3"
NEWS_API_BASE = "https://newsapi.org/v2"

def is_football_api_configured() -> bool:
    """Check if external football API key is set and non-empty."""
    return bool(FOOTBALL_API_KEY and FOOTBALL_API_KEY.strip())

def is_news_api_configured() -> bool:
    """Check if external news API key is set and non-empty."""
    return bool(NEWS_API_KEY and NEWS_API_KEY.strip())

async def fetch_player_from_api(player_name: str) -> Optional[Dict[str, Any]]:
    """
    Fetch a player's real-time data from external football API.
    Returns None if API not configured or request fails — triggers local DB fallback.
    """
    if not is_football_api_configured():
        logger.info("FOOTBALL_API_KEY not configured — using local database fallback.")
        return None

    headers = {
        "X-RapidAPI-Key": FOOTBALL_API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{FOOTBALL_API_BASE}/players",
                headers=headers,
                params={"search": player_name, "league": "39", "season": "2024"},
            )
            response.raise_for_status()
            data = response.json()
            if data.get("results", 0) > 0:
                return data["response"][0]
    except Exception as e:
        logger.warning(f"External football API error for '{player_name}': {e}")
    return None

async def fetch_transfer_news_from_api(query: str = "football transfer") -> List[Dict[str, Any]]:
    """
    Fetch real transfer news from NewsAPI.
    Returns empty list if API not configured or request fails — triggers local DB fallback.
    """
    if not is_news_api_configured():
        logger.info("NEWS_API_KEY not configured — using local database fallback.")
        return []

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{NEWS_API_BASE}/everything",
                params={
                    "q": query,
                    "language": "en",
                    "sortBy": "publishedAt",
                    "pageSize": 20,
                    "apiKey": NEWS_API_KEY,
                },
            )
            response.raise_for_status()
            data = response.json()
            return data.get("articles", [])
    except Exception as e:
        logger.warning(f"External news API error: {e}")
    return []

def get_api_status() -> Dict[str, Any]:
    """Return current external API configuration status (safe for frontend)."""
    return {
        "football_api": "configured" if is_football_api_configured() else "not_configured (using local DB)",
        "news_api": "configured" if is_news_api_configured() else "not_configured (using local DB)",
        "fallback_mode": not (is_football_api_configured() or is_news_api_configured()),
    }
