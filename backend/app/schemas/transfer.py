"""
Transfer Pydantic Schemas
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TransferBase(BaseModel):
    player_id: int
    current_club_id: Optional[int] = None
    interested_club_id: Optional[int] = None
    market_value: Optional[str] = None
    asking_price: Optional[str] = None
    reported_offer: Optional[str] = None
    final_fee: Optional[str] = None
    transfer_type: str = "Permanent"
    status: str = "Negotiating"
    probability: int = 50
    confidence: int = 50
    negotiation_stage: Optional[str] = None
    contract_status: Optional[str] = None
    headline: Optional[str] = None
    source: Optional[str] = "BlueLock Tactical Wire"
    source_url: Optional[str] = None
    time_ago: Optional[str] = "Recently"

class TransferResponse(TransferBase):
    id: int
    player_name: str
    player_image: Optional[str] = None
    player_age: int
    player_position: str
    ego_threat: str
    from_club_name: Optional[str] = "Free Agent"
    from_club_badge: Optional[str] = None
    to_club_name: Optional[str] = "Evaluating"
    to_club_badge: Optional[str] = None
    last_updated: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class TransferFilterParams(BaseModel):
    status: Optional[str] = None
    transfer_type: Optional[str] = None
    club: Optional[str] = None
    player: Optional[str] = None
    league: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
