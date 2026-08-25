"""
Search Router
GET /api/search?q=   — Global categorized search across players, clubs, and news
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.player import Player
from app.models.club import Club
from app.models.news import TransferNews
from app.utils.helpers import success_response

router = APIRouter(prefix="/api/search", tags=["Search"])


@router.get(
    "",
    summary="Global search",
    description="Search across players, clubs, and transfer news simultaneously. Returns categorized results.",
)
def global_search(
    q: str = Query(..., min_length=2, description="Search query string"),
    limit: int = Query(10, le=50, description="Max results per category"),
    db: Session = Depends(get_db),
):
    term = f"%{q}%"

    # Players
    players = (
        db.query(Player)
        .filter(
            Player.name.ilike(term) |
            Player.nationality.ilike(term) |
            Player.position.ilike(term)
        )
        .limit(limit)
        .all()
    )

    # Clubs
    clubs = (
        db.query(Club)
        .filter(
            Club.name.ilike(term) |
            Club.league.ilike(term) |
            Club.country.ilike(term)
        )
        .limit(limit)
        .all()
    )

    # News
    news = (
        db.query(TransferNews)
        .filter(
            TransferNews.title.ilike(term) |
            TransferNews.description.ilike(term)
        )
        .order_by(TransferNews.published_at.desc())
        .limit(limit)
        .all()
    )

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
