"""
News Router
GET /api/news     — Filter by category, player, club, date
GET /api/news/{id} — Single news article
"""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.news_service import get_all_news, get_news_by_id
from app.utils.helpers import not_found, success_response

router = APIRouter(prefix="/api/news", tags=["News"])


def _serialize_news(n) -> dict:
    return {
        "id": n.id,
        "title": n.title,
        "description": n.description,
        "content": n.content,
        "image_url": n.image_url,
        "player_id": n.player_id,
        "player_name": n.player.name if n.player else None,
        "club_id": n.club_id,
        "club_name": n.club.name if n.club else None,
        "source": n.source,
        "source_url": n.source_url,
        "author": n.author,
        "retrieved_at": n.retrieved_at,
        "attribution_required": n.attribution_required,
        "published_at": n.published_at.isoformat() if n.published_at else None,
        "category": n.category,
        "reliability_score": n.reliability_score,
        "read_time": n.read_time,
        "ego_impact": n.ego_impact,
    }


@router.get(
    "",
    summary="Get transfer news",
    description="Returns latest transfer wire news. Filter by category, player, club, or date.",
)
def list_news(
    category: Optional[str] = Query(None, description="Confirmed, Rumour, Negotiation, Loan, Free Transfer"),
    player: Optional[str] = Query(None, description="Filter by player name"),
    club: Optional[str] = Query(None, description="Filter by club name"),
    date_from: Optional[str] = Query(None, description="ISO date string (e.g. 2024-01-01)"),
    limit: int = Query(20, le=100),
    offset: int = Query(0),
    db: Session = Depends(get_db),
):
    news = get_all_news(db, category=category, player=player, club=club, date_from=date_from, limit=limit, offset=offset)
    return success_response(data=[_serialize_news(n) for n in news], message=f"{len(news)} news items retrieved")


@router.get("/{news_id}", summary="Get news article by ID")
def get_news(news_id: int, db: Session = Depends(get_db)):
    article = get_news_by_id(db, news_id)
    if not article:
        raise not_found("News article", news_id)
    return success_response(data=_serialize_news(article), message="News article retrieved")
