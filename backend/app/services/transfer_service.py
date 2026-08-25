"""
Transfer Service — Business Logic Layer
"""

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.transfer import Transfer
from app.models.player import Player
from app.models.club import Club


def get_all_transfers(
    db: Session,
    status: Optional[str] = None,
    transfer_type: Optional[str] = None,
    club: Optional[str] = None,
    player: Optional[str] = None,
    league: Optional[str] = None,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    limit: int = 50,
    offset: int = 0,
) -> List[Transfer]:
    query = (
        db.query(Transfer)
        .options(
            joinedload(Transfer.player),
            joinedload(Transfer.current_club),
            joinedload(Transfer.interested_club),
        )
    )

    if status:
        query = query.filter(Transfer.status.ilike(f"%{status}%"))
    if transfer_type:
        query = query.filter(Transfer.transfer_type.ilike(f"%{transfer_type}%"))
    if player:
        query = query.join(Player, Transfer.player_id == Player.id)
        query = query.filter(Player.name.ilike(f"%{player}%"))
    if club:
        from_alias = db.query(Club).filter(Club.name.ilike(f"%{club}%")).all()
        club_ids = [c.id for c in from_alias]
        if club_ids:
            query = query.filter(
                (Transfer.current_club_id.in_(club_ids)) |
                (Transfer.interested_club_id.in_(club_ids))
            )
    if league:
        query = (
            query
            .join(Club, Transfer.interested_club_id == Club.id)
            .filter(Club.league.ilike(f"%{league}%"))
        )
    if min_value is not None:
        query = query.join(Player, Transfer.player_id == Player.id, isouter=True)
        query = query.filter(Player.market_value_raw >= min_value)
    if max_value is not None:
        query = query.filter(Player.market_value_raw <= max_value)

    return (
        query
        .order_by(Transfer.last_updated.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_transfer_by_id(db: Session, transfer_id: int) -> Optional[Transfer]:
    return (
        db.query(Transfer)
        .options(
            joinedload(Transfer.player),
            joinedload(Transfer.current_club),
            joinedload(Transfer.interested_club),
        )
        .filter(Transfer.id == transfer_id)
        .first()
    )
