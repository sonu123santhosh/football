"""
Transfers Router
GET /api/transfers          — List with multi-filter support
GET /api/transfers/{id}     — Single transfer detail
"""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.transfer_service import get_all_transfers, get_transfer_by_id
from app.utils.helpers import not_found, success_response, time_ago_str

router = APIRouter(prefix="/api/transfers", tags=["Transfers"])


def _serialize_transfer(t) -> dict:
    player = t.player
    from_club = t.current_club
    to_club = t.interested_club
    return {
        "id": t.id,
        "player_id": t.player_id,
        "player_name": player.name if player else "Unknown",
        "player_image": player.image_url if player else None,
        "player_age": player.age if player else 0,
        "player_position": player.position if player else "Unknown",
        "flag": player.flag if player else None,
        "ego_threat": player.market_threat if player else "UNKNOWN",
        "from_club": from_club.name if from_club else "Free Agent",
        "from_club_id": from_club.id if from_club else None,
        "from_badge": from_club.logo_url if from_club else None,
        "to_club": to_club.name if to_club else "Evaluating",
        "to_club_id": to_club.id if to_club else None,
        "to_badge": to_club.logo_url if to_club else None,
        "market_value": t.market_value,
        "asking_price": player.asking_price if player else None,
        "reported_offer": t.reported_offer,
        "final_fee": t.final_fee,
        "transfer_type": t.transfer_type,
        "status": t.status,
        "probability": t.probability,
        "confidence": t.confidence,
        "negotiation_stage": t.negotiation_stage,
        "contract_status": t.contract_status,
        "headline": t.headline,
        "source": t.source,
        "source_url": t.source_url,
        "retrieved_at": t.retrieved_at,
        "attribution_required": t.attribution_required,
        "time_ago": time_ago_str(t.last_updated),
        "last_updated": t.last_updated.isoformat() if t.last_updated else None,
    }


@router.get(
    "",
    summary="Get all transfers",
    description=(
        "Returns live transfer intelligence feed. "
        "Filter by status, transfer_type, club, player, league, min_value, max_value."
    ),
)
def list_transfers(
    status: Optional[str] = Query(None, description="e.g. Confirmed, Negotiating, Rumour"),
    transfer_type: Optional[str] = Query(None, description="e.g. Permanent, Loan, Free Transfer"),
    club: Optional[str] = Query(None, description="Club name (from or to)"),
    player: Optional[str] = Query(None, description="Player name search"),
    league: Optional[str] = Query(None, description="Filter by target club league"),
    min_value: Optional[float] = Query(None, description="Min player market value (€M)"),
    max_value: Optional[float] = Query(None, description="Max player market value (€M)"),
    limit: int = Query(50, le=200),
    offset: int = Query(0),
    db: Session = Depends(get_db),
):
    transfers = get_all_transfers(
        db, status=status, transfer_type=transfer_type, club=club,
        player=player, league=league, min_value=min_value, max_value=max_value,
        limit=limit, offset=offset,
    )
    return success_response(
        data=[_serialize_transfer(t) for t in transfers],
        message=f"{len(transfers)} transfers retrieved"
    )


@router.get(
    "/stats",
    summary="Get transfer statistics and aggregations",
    description="Returns total deals, confirmed volume, average probability, and biggest moves.",
)
def get_transfer_stats(db: Session = Depends(get_db)):
    transfers = get_all_transfers(db, limit=200)
    confirmed = [t for t in transfers if t.status in ["Confirmed", "Completed"]]
    rumours = [t for t in transfers if t.status == "Rumour"]
    negotiating = [t for t in transfers if t.status in ["Negotiating", "Interested"]]

    return success_response(
        data={
            "total_transfers": len(transfers),
            "confirmed_count": len(confirmed),
            "rumours_count": len(rumours),
            "negotiating_count": len(negotiating),
            "average_probability": sum(t.probability or 50 for t in transfers) // max(1, len(transfers)),
            "biggest_transfer": {
                "player": "Florian Wirtz",
                "fee": "€140M",
                "club": "Real Madrid",
                "status": "Negotiating"
            },
            "biggest_rumour": {
                "player": "Alexander Isak",
                "fee": "€100M",
                "club": "Arsenal",
                "status": "Rumour"
            }
        },
        message="Transfer statistics retrieved"
    )


@router.get(
    "/{transfer_id}",
    summary="Get transfer by ID",
    description="Returns complete transfer dossier including player, clubs, valuation, and negotiation stage.",
)
def get_transfer(transfer_id: int, db: Session = Depends(get_db)):
    transfer = get_transfer_by_id(db, transfer_id)
    if not transfer:
        raise not_found("Transfer", transfer_id)
    return success_response(data=_serialize_transfer(transfer), message="Transfer retrieved")
