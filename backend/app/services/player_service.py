"""
Player Service — Business Logic Layer
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.player import Player
from app.models.club import Club
from app.models.transfer import Transfer
from app.models.market_history import MarketValueHistory


def get_all_players(
    db: Session,
    search: Optional[str] = None,
    position: Optional[str] = None,
    club: Optional[str] = None,
    nationality: Optional[str] = None,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    limit: int = 100,
    offset: int = 0,
) -> List[Player]:
    query = db.query(Player)

    if search:
        query = query.filter(Player.name.ilike(f"%{search}%"))
    if position:
        query = query.filter(Player.position.ilike(f"%{position}%"))
    if nationality:
        query = query.filter(Player.nationality.ilike(f"%{nationality}%"))
    if min_value is not None:
        query = query.filter(Player.market_value_raw >= min_value)
    if max_value is not None:
        query = query.filter(Player.market_value_raw <= max_value)
    if club:
        query = query.join(Club, Player.current_club_id == Club.id)
        query = query.filter(Club.name.ilike(f"%{club}%"))

    return query.order_by(Player.market_value_raw.desc()).offset(offset).limit(limit).all()


def get_player_by_id(db: Session, player_id: int) -> Optional[Player]:
    return db.query(Player).filter(Player.id == player_id).first()


def get_player_by_slug(db: Session, slug: str) -> Optional[Player]:
    return db.query(Player).filter(Player.slug == slug).first()


def get_player_transfers(db: Session, player_id: int) -> List[Transfer]:
    return db.query(Transfer).filter(Transfer.player_id == player_id).all()


def get_player_market_history(db: Session, player_id: int) -> List[MarketValueHistory]:
    return (
        db.query(MarketValueHistory)
        .filter(MarketValueHistory.player_id == player_id)
        .order_by(MarketValueHistory.year_recorded)
        .all()
    )


def get_players_for_comparison(db: Session, player1_id: int, player2_id: int):
    p1 = get_player_by_id(db, player1_id)
    p2 = get_player_by_id(db, player2_id)
    return p1, p2
