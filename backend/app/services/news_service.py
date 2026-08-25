"""
News Service — Business Logic + Scheduled Background Sync
"""

import logging
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.news import TransferNews
from app.models.player import Player
from app.models.club import Club
from app.services.football_api_service import fetch_transfer_news_from_api

logger = logging.getLogger(__name__)


def get_all_news(
    db: Session,
    category: Optional[str] = None,
    player: Optional[str] = None,
    club: Optional[str] = None,
    date_from: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> List[TransferNews]:
    query = db.query(TransferNews)

    if category:
        query = query.filter(TransferNews.category.ilike(f"%{category}%"))
    if player:
        query = query.join(Player, TransferNews.player_id == Player.id, isouter=True)
        query = query.filter(Player.name.ilike(f"%{player}%"))
    if club:
        query = query.join(Club, TransferNews.club_id == Club.id, isouter=True)
        query = query.filter(Club.name.ilike(f"%{club}%"))
    if date_from:
        try:
            dt = datetime.fromisoformat(date_from)
            query = query.filter(TransferNews.published_at >= dt)
        except ValueError:
            pass

    return query.order_by(TransferNews.published_at.desc()).offset(offset).limit(limit).all()


def get_news_by_id(db: Session, news_id: int) -> Optional[TransferNews]:
    return db.query(TransferNews).filter(TransferNews.id == news_id).first()


async def sync_news_from_external(db: Session) -> int:
    """
    Fetch news from external NewsAPI and save new records.
    Runs as a background task every SYNC_INTERVAL_MINUTES.
    Returns count of new records added.
    """
    articles = await fetch_transfer_news_from_api("football transfer rumour")
    if not articles:
        logger.info("No external news returned — local database is up to date.")
        return 0

    added = 0
    for article in articles:
        title = article.get("title", "")
        if not title or "[Removed]" in title:
            continue
        # Avoid duplicate titles
        existing = db.query(TransferNews).filter(TransferNews.title == title).first()
        if existing:
            continue
        news = TransferNews(
            title=title,
            description=article.get("description") or article.get("content", "")[:300],
            content=article.get("content"),
            image_url=article.get("urlToImage"),
            source=article.get("source", {}).get("name", "External Feed"),
            source_url=article.get("url"),
            published_at=datetime.utcnow(),
            category="Rumour",
            reliability_score=65,  # External sources get moderate reliability
        )
        db.add(news)
        added += 1

    db.commit()
    logger.info(f"News sync complete — {added} new records added.")
    return added
