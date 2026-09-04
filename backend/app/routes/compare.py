"""
Compare Router
GET /api/compare?player1={id}&player2={id}  — Side-by-side player comparison matrix
"""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.player_service import resolve_player
from app.utils.helpers import not_found, success_response, bad_request

router = APIRouter(prefix="/api/compare", tags=["Comparison"])


def _stat_winner(val1, val2, lower_better: bool = False) -> str:
    if val1 == val2:
        return "tie"
    if lower_better:
        return "player1" if val1 < val2 else "player2"
    return "player1" if val1 > val2 else "player2"


@router.get(
    "",
    summary="Compare two players",
    description=(
        "Returns side-by-side scouting comparison including radar stats, "
        "performance metrics, and overall assessment. Provide player IDs as query params."
    ),
)
def compare_players(
    player1: Optional[int] = Query(None, description="ID of the first player"),
    player2: Optional[int] = Query(None, description="ID of the second player"),
    player_a: Optional[int] = Query(None, description="Alias for first player ID"),
    player_b: Optional[int] = Query(None, description="Alias for second player ID"),
    db: Session = Depends(get_db),
):
    p1_id = player1 or player_a
    p2_id = player2 or player_b

    if not p1_id or not p2_id:
        raise bad_request("Provide two player IDs to compare using ?player1={id}&player2={id} or ?player_a={id}&player_b={id}")

    if p1_id == p2_id:
        raise bad_request("Cannot compare a player with themselves. Provide two different player IDs.")

    p1 = resolve_player(db, p1_id)
    p2 = resolve_player(db, p2_id)

    if not p1:
        raise not_found("Player", p1_id)
    if not p2:
        raise not_found("Player", p2_id)

    def player_snapshot(p):
        return {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "nationality": p.nationality,
            "flag": p.flag,
            "position": p.position,
            "current_club": p.current_club.name if p.current_club else "Free Agent",
            "current_club_badge": p.current_club.logo_url if p.current_club else None,
            "market_value": p.market_value,
            "market_value_raw": p.market_value_raw,
            "image_url": p.image_url,
            "overall_rating": p.overall_rating,
            "ego_rating": p.ego_rating,
            "striker_index": p.striker_index,
            "momentum": p.momentum,
        }

    metrics = [
        {"label": "AGE", "key1": p1.age, "key2": p2.age, "lower_better": True},
        {"label": "MARKET VALUE (€M)", "key1": p1.market_value_raw, "key2": p2.market_value_raw, "lower_better": False},
        {"label": "OVERALL RATING", "key1": p1.overall_rating, "key2": p2.overall_rating, "lower_better": False},
        {"label": "EGO RATING", "key1": p1.ego_rating, "key2": p2.ego_rating, "lower_better": False},
        {"label": "GOALS", "key1": p1.goals, "key2": p2.goals, "lower_better": False},
        {"label": "ASSISTS", "key1": p1.assists, "key2": p2.assists, "lower_better": False},
        {"label": "xG", "key1": p1.xg, "key2": p2.xg, "lower_better": False},
        {"label": "xA", "key1": p1.xa, "key2": p2.xa, "lower_better": False},
        {"label": "KEY PASSES", "key1": p1.key_passes, "key2": p2.key_passes, "lower_better": False},
        {"label": "DRIBBLES COMPLETED", "key1": p1.dribbles, "key2": p2.dribbles, "lower_better": False},
        {"label": "PASS ACCURACY %", "key1": p1.pass_accuracy, "key2": p2.pass_accuracy, "lower_better": False},
        {"label": "PACE", "key1": p1.pace, "key2": p2.pace, "lower_better": False},
        {"label": "SHOOTING", "key1": p1.shooting, "key2": p2.shooting, "lower_better": False},
        {"label": "PASSING", "key1": p1.passing, "key2": p2.passing, "lower_better": False},
        {"label": "DRIBBLING", "key1": p1.dribbling, "key2": p2.dribbling, "lower_better": False},
        {"label": "DEFENDING", "key1": p1.defending, "key2": p2.defending, "lower_better": False},
        {"label": "PHYSICAL", "key1": p1.physical, "key2": p2.physical, "lower_better": False},
    ]

    head_to_head = []
    for m in metrics:
        winner = _stat_winner(m["key1"], m["key2"], m["lower_better"])
        head_to_head.append({
            "label": m["label"],
            "player1_value": m["key1"],
            "player2_value": m["key2"],
            "winner": winner,
        })

    p1_wins = sum(1 for m in head_to_head if m["winner"] == "player1")
    p2_wins = sum(1 for m in head_to_head if m["winner"] == "player2")

    return success_response(
        data={
            "player1": player_snapshot(p1),
            "player2": player_snapshot(p2),
            "radar": {
                "player1": {
                    "pace": p1.pace, "shooting": p1.shooting, "passing": p1.passing,
                    "dribbling": p1.dribbling, "defending": p1.defending, "physical": p1.physical,
                },
                "player2": {
                    "pace": p2.pace, "shooting": p2.shooting, "passing": p2.passing,
                    "dribbling": p2.dribbling, "defending": p2.defending, "physical": p2.physical,
                },
            },
            "head_to_head": head_to_head,
            "verdict": {
                "player1_advantages": p1_wins,
                "player2_advantages": p2_wins,
                "edge": (
                    p1.name if p1_wins > p2_wins
                    else (p2.name if p2_wins > p1_wins else "Even Match")
                ),
            },
            "note": "Comparison based on current season data in database."
        },
        message=f"Comparison: {p1.name} vs {p2.name}"
    )
