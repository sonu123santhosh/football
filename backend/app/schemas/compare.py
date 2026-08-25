"""
Player Comparison Pydantic Schemas
"""

from typing import Dict, Any, List
from pydantic import BaseModel
from app.schemas.player import PlayerDetail

class ComparisonStatMetric(BaseModel):
    label: str
    player1_value: Any
    player2_value: Any
    winner: str # 'player1', 'player2', or 'tie'
    advantage_delta: Optional[str] = None

class PlayerComparisonResponse(BaseModel):
    player1: PlayerDetail
    player2: PlayerDetail
    radar_comparison: Dict[str, Any]
    head_to_head_matrix: List[ComparisonStatMetric]
