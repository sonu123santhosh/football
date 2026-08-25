"""
Search Router
GET /api/search?q=   — Global categorized search across players, clubs, and news
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
import unicodedata

from app.database import get_db
from app.models.player import Player
from app.models.club import Club
from app.models.news import TransferNews
from app.utils.helpers import success_response

router = APIRouter(prefix="/api/search", tags=["Search"])


def _normalize(text: str) -> str:
    """Strip accents/diacritics and lowercase for fuzzy matching."""
    if not text:
        return ""
    text = (
        text.lower()
        .replace("ø", "o").replace("Ø", "o")
        .replace("æ", "ae").replace("Æ", "ae")
        .replace("ß", "ss")
    )
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


@router.get(
    "",
    summary="Global search",
    description="Search across players, clubs, and transfer news simultaneously. Returns categorized results.",
)
def global_search(
    q: str = Query(..., min_length=1, description="Search query string"),
    limit: int = Query(10, le=50, description="Max results per category"),
    db: Session = Depends(get_db),
):
    norm_q = _normalize(q)

    # Players — fetch all and filter in Python for accent-insensitive matching
    all_players = db.query(Player).limit(500).all()
    players = [
        p for p in all_players
        if norm_q in _normalize(p.name)
        or norm_q in _normalize(p.nationality or "")
        or norm_q in _normalize(p.position or "")
    ][:limit]

    # Clubs — same Python-side normalization
    all_clubs = db.query(Club).limit(100).all()
    clubs = [
        c for c in all_clubs
        if norm_q in _normalize(c.name)
        or norm_q in _normalize(c.league or "")
        or norm_q in _normalize(c.country or "")
    ][:limit]

    # News — Python-side
    all_news = db.query(TransferNews).order_by(TransferNews.published_at.desc()).limit(200).all()
    news = [
        n for n in all_news
        if norm_q in _normalize(n.title)
        or norm_q in _normalize(n.description or "")
    ][:limit]

    results = {
        "query": q,
        "total_results": len(players) + len(clubs) + len(news),
        "players": [
            {
                "id": p.id,
                "slug": p.slug,
                "name": p.name,
                "age": p.age,
                "position": p.position,
                "current_club": p.current_club.name if p.current_club else "Free Agent",
                "market_value": p.market_value,
                "ego_rating": p.ego_rating,
                "image_url": p.image_url,
                "flag": p.flag,
            }
            for p in players
        ],
        "clubs": [
            {
                "id": c.id,
                "slug": c.slug,
                "name": c.name,
                "league": c.league,
                "country": c.country,
                "logo_url": c.logo_url,
                "transfer_budget": c.transfer_budget,
                "ego_rank": c.ego_rank,
                "flag": c.flag,
            }
            for c in clubs
        ],
        "news": [
            {
                "id": n.id,
                "title": n.title,
                "category": n.category,
                "source": n.source,
                "published_at": n.published_at.isoformat() if n.published_at else None,
                "player_name": n.player.name if n.player else None,
            }
            for n in news
        ],
    }

    return success_response(data=results, message=f"Found {results['total_results']} results for '{q}'")
