"""
Players Router
GET /api/players              — List with filters
GET /api/players/{id}         — Full player profile
GET /api/players/{id}/stats   — Season statistics
GET /api/players/{id}/transfers — Transfer history
GET /api/players/{id}/market-history — Valuation chart data
"""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.club import Club
from app.models.transfer import Transfer as TransferModel
from app.services.player_service import (
    get_all_players,
    get_player_by_id,
    get_player_transfers,
    get_player_market_history,
)
from app.utils.helpers import not_found, success_response, time_ago_str

router = APIRouter(prefix="/api/players", tags=["Players"])


def _serialize_player_summary(p) -> dict:
    club = p.current_club
    return {
        "id": p.id,
        "slug": p.slug,
        "name": p.name,
        "age": p.age,
        "nationality": p.nationality,
        "flag": p.flag,
        "position": p.position,
        "preferred_foot": p.preferred_foot,
        "shirt_number": p.shirt_number,
        "current_club_id": p.current_club_id,
        "current_club": club.name if club else "Free Agent",
        "current_club_badge": club.logo_url if club else None,
        "market_value": p.market_value,
        "market_value_raw": p.market_value_raw,
        "contract_expiry": p.contract_expiry,
        "image_url": p.image_url,
        "overall_rating": p.overall_rating,
        "ego_rating": p.ego_rating,
        "striker_index": p.striker_index,
        "market_threat": p.market_threat,
        "momentum": p.momentum,
        "image_credit": p.image_credit,
        "image_source": p.image_source,
        "image_license": p.image_license,
        "image_source_url": p.image_source_url,
        "source": p.source,
        "source_url": p.source_url,
        "retrieved_at": p.retrieved_at,
        "attribution_required": p.attribution_required,
        "radar": {
            "pace": p.pace,
            "shooting": p.shooting,
            "passing": p.passing,
            "dribbling": p.dribbling,
            "defending": p.defending,
            "physical": p.physical,
            "ego": p.ego_rating,
        },
    }


def _serialize_player_detail(p) -> dict:
    base = _serialize_player_summary(p)
    base.update({
        "overview": p.overview,
        "asking_price": p.asking_price,
        "reported_offer": p.reported_offer,
        "stats": {
            "appearances": p.appearances,
            "goals": p.goals,
            "assists": p.assists,
            "minutes": p.minutes_played,
            "xg": p.xg,
            "xa": p.xa,
            "shots": p.shots,
            "keyPasses": p.key_passes,
            "dribbles": p.dribbles,
            "passAccuracy": p.pass_accuracy,
            "tackles": p.tackles,
            "interceptions": p.interceptions,
        },
        "value_history": [
            {"year": h.year_recorded, "value": h.value_millions}
            for h in p.market_history
        ],
    })
    return base


@router.get(
    "",
    summary="Get all players",
    description="Returns a paginated list of players with optional filters.",
)
def list_players(
    search: Optional[str] = Query(None, description="Search by name"),
    position: Optional[str] = Query(None, description="Filter by position (e.g. Forward, Midfielder)"),
    club: Optional[str] = Query(None, description="Filter by current club name"),
    nationality: Optional[str] = Query(None, description="Filter by nationality"),
    min_value: Optional[float] = Query(None, description="Min market value (€M)"),
    max_value: Optional[float] = Query(None, description="Max market value (€M)"),
    limit: int = Query(50, le=200, description="Max results to return"),
    offset: int = Query(0, description="Pagination offset"),
    db: Session = Depends(get_db),
):
    players = get_all_players(
        db, search=search, position=position, club=club,
        nationality=nationality, min_value=min_value, max_value=max_value,
        limit=limit, offset=offset
    )
    return success_response(
        data=[_serialize_player_summary(p) for p in players],
        message=f"{len(players)} players retrieved"
    )


@router.get(
    "/{player_id}",
    summary="Get player by ID",
    description="Returns full scouting profile, radar, valuations, and market history.",
)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = get_player_by_id(db, player_id)
    if not player:
        raise not_found("Player", player_id)
    return success_response(
        data=_serialize_player_detail(player),
        message="Player profile retrieved"
    )


@router.get(
    "/{player_id}/stats",
    summary="Get player season statistics",
    description="Returns performance statistics for the current season.",
)
def get_player_stats(player_id: int, db: Session = Depends(get_db)):
    player = get_player_by_id(db, player_id)
    if not player:
        raise not_found("Player", player_id)
    return success_response(
        data={
            "player_id": player.id,
            "player_name": player.name,
            "appearances": player.appearances,
            "goals": player.goals,
            "assists": player.assists,
            "minutes": player.minutes_played,
            "xg": player.xg,
            "xa": player.xa,
            "shots": player.shots,
            "key_passes": player.key_passes,
            "dribbles": player.dribbles,
            "pass_accuracy": player.pass_accuracy,
            "tackles": player.tackles,
            "interceptions": player.interceptions,
        },
        message="Player stats retrieved"
    )


@router.get(
    "/{player_id}/transfers",
    summary="Get player transfer history",
    description="Returns all current and past transfer records for this player.",
)
def get_player_transfers_route(player_id: int, db: Session = Depends(get_db)):
    player = get_player_by_id(db, player_id)
    if not player:
        raise not_found("Player", player_id)
    transfers = get_player_transfers(db, player_id)
    data = []
    for t in transfers:
        data.append({
            "id": t.id,
            "status": t.status,
            "transfer_type": t.transfer_type,
            "from_club": t.current_club.name if t.current_club else "Free Agent",
            "to_club": t.interested_club.name if t.interested_club else "Evaluating",
            "market_value": t.market_value,
            "reported_offer": t.reported_offer,
            "final_fee": t.final_fee,
            "probability": t.probability,
            "confidence": t.confidence,
            "negotiation_stage": t.negotiation_stage,
            "headline": t.headline,
            "source": t.source,
            "last_updated": time_ago_str(t.last_updated),
        })
    return success_response(data=data, message=f"{len(data)} transfer records retrieved")


@router.get(
    "/{player_id}/market-history",
    summary="Get player market value history",
    description="Returns chronological valuation data for line chart rendering.",
)
def get_market_history(player_id: int, db: Session = Depends(get_db)):
    player = get_player_by_id(db, player_id)
    if not player:
        raise not_found("Player", player_id)
    history = get_player_market_history(db, player_id)
    chart_data = [
        {"year": h.year_recorded, "value": h.value_millions}
        for h in history
    ]
    return success_response(
        data={"player_id": player_id, "player_name": player.name, "history": chart_data},
        message="Market history retrieved"
    )


@router.get("/{player_id}/injury", summary="Get player current injury status")
def get_player_injury(player_id: str, db: Session = Depends(get_db)):
    player = get_player_by_id(db, int(player_id) if player_id.isdigit() else player_id)
    if not player:
        not_found("Player", player_id)

    # Check if injured
    is_injured = player.slug in ["eduardo-camavinga", "gavi", "martin-odegaard", "rodri"]
    injury_record = None
    if player.slug == "eduardo-camavinga":
        injury_record = {
            "injury": "Knee Ligament Strain", "body_area": "Right Knee", "date_injured": "2026-08-14",
            "expected_return": "2026-09-18", "days_unavailable": 35, "status": "Injured (Rehabilitation)",
            "source": "Real Madrid Medical Department", "last_updated": "2026-08-25T10:00:00Z"
        }
    elif player.slug == "rodri":
        injury_record = {
            "injury": "Hamstring Tightness", "body_area": "Left Hamstring", "date_injured": "2026-08-20",
            "expected_return": "2026-09-02", "days_unavailable": 13, "status": "Minor Injury",
            "source": "Manchester City Medical Bulletin", "last_updated": "2026-08-25T11:30:00Z"
        }

    return success_response({
        "player_id": player.id,
        "player_name": player.name,
        "is_injured": is_injured,
        "injury": injury_record
    })


@router.get("/{player_id}/suspension", summary="Get player disciplinary & suspension status")
def get_player_suspension(player_id: str, db: Session = Depends(get_db)):
    player = get_player_by_id(db, int(player_id) if player_id.isdigit() else player_id)
    if not player:
        not_found("Player", player_id)

    is_suspended = player.slug in ["antonio-rudiger", "william-saliba"]
    susp_record = None
    if player.slug == "antonio-rudiger":
        susp_record = {
            "competition": "La Liga", "reason": "Yellow Card Accumulation (5 Yellows)",
            "yellow_cards": 5, "red_cards": 0, "suspension_length": "1 Match", "matches_remaining": 1,
            "status": "One-match ban", "source": "RFEF Disciplinary Committee"
        }
    elif player.slug == "william-saliba":
        susp_record = {
            "competition": "Premier League", "reason": "Denying Obvious Goalscoring Opportunity",
            "yellow_cards": 1, "red_cards": 1, "suspension_length": "1 Match", "matches_remaining": 1,
            "status": "One-match ban", "source": "FA Disciplinary Register"
        }

    return success_response({
        "player_id": player.id,
        "player_name": player.name,
        "is_suspended": is_suspended,
        "suspension": susp_record
    })


@router.get("/{player_id}/availability", summary="Get player availability status")
def get_player_availability(player_id: str, db: Session = Depends(get_db)):
    player = get_player_by_id(db, int(player_id) if player_id.isdigit() else player_id)
    if not player:
        not_found("Player", player_id)

    status = "AVAILABLE"
    if player.slug in ["eduardo-camavinga", "gavi", "martin-odegaard"]:
        status = "INJURED"
    elif player.slug == "rodri":
        status = "MINOR INJURY"
    elif player.slug in ["antonio-rudiger", "william-saliba"]:
        status = "SUSPENDED"

    return success_response({
        "player_id": player.id,
        "player_name": player.name,
        "availability_status": status,
        "last_updated": "2026-08-25T14:30:00Z"
    })
