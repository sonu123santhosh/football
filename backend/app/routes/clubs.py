"""
Clubs Router
GET /api/clubs                   — List all clubs
GET /api/clubs/{id}              — Club detail (squad, transfers, targets)
GET /api/clubs/{id}/players      — Squad list
GET /api/clubs/{id}/transfers    — Incoming + outgoing transfers
"""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.club import Club
from app.models.player import Player
from app.models.transfer import Transfer
from app.utils.helpers import not_found, success_response

router = APIRouter(prefix="/api/clubs", tags=["Clubs"])


def _serialize_club_summary(club: Club) -> dict:
    return {
        "id": club.id,
        "slug": club.slug,
        "name": club.name,
        "short_name": club.short_name,
        "country": club.country,
        "flag": club.flag,
        "league": club.league,
        "stadium": club.stadium,
        "logo_url": club.logo_url,
        "squad_value": club.squad_value,
        "transfer_budget": club.transfer_budget,
        "wage_bill": club.wage_bill,
        "manager": club.manager,
        "president": club.president,
        "ego_rank": club.ego_rank,
        "description": club.description,
    }


def _serialize_player_mini(p: Player) -> dict:
    return {
        "id": p.id,
        "slug": p.slug,
        "name": p.name,
        "age": p.age,
        "position": p.position,
        "shirt_number": p.shirt_number,
        "market_value": p.market_value,
        "rating": p.overall_rating,
        "ego_rating": p.ego_rating,
        "image_url": p.image_url,
        "flag": p.flag,
    }


def _serialize_transfer_mini(t: Transfer, perspective: str = "incoming") -> dict:
    if perspective == "incoming":
        club_name = t.current_club.name if t.current_club else "Free Agent"
        player_name = t.player.name if t.player else "Unknown"
        fee = t.reported_offer or t.final_fee or t.market_value or "TBC"
    else:
        club_name = t.interested_club.name if t.interested_club else "Evaluating"
        player_name = t.player.name if t.player else "Unknown"
        fee = t.reported_offer or t.final_fee or t.market_value or "TBC"
    return {
        "id": t.id,
        "player_id": t.player_id,
        "player_name": player_name,
        "player_image": t.player.image_url if t.player else None,
        "club_name": club_name,
        "fee": fee,
        "status": t.status,
        "transfer_type": t.transfer_type,
    }


@router.get("", summary="Get all clubs", description="Returns all clubs with financial and squad details.")
def list_clubs(
    league: Optional[str] = Query(None, description="Filter by league"),
    country: Optional[str] = Query(None, description="Filter by country"),
    db: Session = Depends(get_db),
):
    query = db.query(Club)
    if league:
        query = query.filter(Club.league.ilike(f"%{league}%"))
    if country:
        query = query.filter(Club.country.ilike(f"%{country}%"))
    clubs = query.order_by(Club.squad_value_raw.desc()).all()
    return success_response(
        data=[_serialize_club_summary(c) for c in clubs],
        message=f"{len(clubs)} clubs retrieved"
    )


@router.get("/{club_id}", summary="Get club profile", description="Returns complete club dossier including squad and transfers.")
def get_club(club_id: int, db: Session = Depends(get_db)):
    club = db.query(Club).filter(Club.id == club_id).first()
    if not club:
        raise not_found("Club", club_id)

    squad = db.query(Player).filter(Player.current_club_id == club_id).order_by(Player.market_value_raw.desc()).all()
    incoming = db.query(Transfer).filter(Transfer.interested_club_id == club_id).all()
    outgoing = db.query(Transfer).filter(Transfer.current_club_id == club_id).all()

    data = _serialize_club_summary(club)
    data["squad"] = [_serialize_player_mini(p) for p in squad]
    data["incoming_transfers"] = [_serialize_transfer_mini(t, "incoming") for t in incoming]
    data["outgoing_transfers"] = [_serialize_transfer_mini(t, "outgoing") for t in outgoing]
    data["squad_count"] = len(squad)

    return success_response(data=data, message="Club profile retrieved")


@router.get("/{club_id}/players", summary="Get club squad", description="Returns all players currently at this club.")
def get_club_players(club_id: int, db: Session = Depends(get_db)):
    club = db.query(Club).filter(Club.id == club_id).first()
    if not club:
        raise not_found("Club", club_id)
    players = db.query(Player).filter(Player.current_club_id == club_id).order_by(Player.overall_rating.desc()).all()
    return success_response(
        data={
            "club_id": club_id,
            "club_name": club.name,
            "squad": [_serialize_player_mini(p) for p in players],
        },
        message=f"{len(players)} players retrieved"
    )


@router.get("/{club_id}/transfers", summary="Get club transfers", description="Returns incoming and outgoing transfer activity.")
def get_club_transfers(club_id: int, db: Session = Depends(get_db)):
    club = db.query(Club).filter(Club.id == club_id).first()
    if not club:
        raise not_found("Club", club_id)
    incoming = db.query(Transfer).filter(Transfer.interested_club_id == club_id).all()
    outgoing = db.query(Transfer).filter(Transfer.current_club_id == club_id).all()
    return success_response(
        data={
            "club_id": club_id,
            "club_name": club.name,
            "incoming": [_serialize_transfer_mini(t, "incoming") for t in incoming],
            "outgoing": [_serialize_transfer_mini(t, "outgoing") for t in outgoing],
        },
        message="Club transfer activity retrieved"
    )
