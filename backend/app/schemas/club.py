"""
Club Pydantic Schemas
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class ClubBase(BaseModel):
    name: str
    short_name: Optional[str] = None
    slug: str
    country: str
    flag: Optional[str] = "🌍"
    league: str
    stadium: Optional[str] = None
    logo_url: Optional[str] = None
    squad_value: Optional[str] = None
    squad_value_raw: Optional[float] = 0.0
    transfer_budget: Optional[str] = None
    transfer_budget_raw: Optional[float] = 0.0
    wage_bill: Optional[str] = None
    manager: Optional[str] = None
    president: Optional[str] = None
    ego_rank: Optional[str] = None
    description: Optional[str] = None

class ClubSummary(ClubBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ClubTransferMini(BaseModel):
    id: int
    player_name: str
    player_id: int
    player_image: Optional[str] = None
    club_name: str
    fee: Optional[str] = None
    status: str
    transfer_type: str

class ClubTargetMini(BaseModel):
    player_id: int
    player_name: str
    player_image: Optional[str] = None
    market_value: Optional[str] = None
    interest_level: str
    status: str

class ClubPlayerMini(BaseModel):
    id: int
    name: str
    slug: str
    age: int
    position: str
    shirt_number: Optional[int] = None
    market_value: str
    rating: int
    ego_rating: int
    image_url: Optional[str] = None
    flag: Optional[str] = None

class ClubDetail(ClubSummary):
    squad: List[ClubPlayerMini] = []
    incoming_transfers: List[ClubTransferMini] = []
    outgoing_transfers: List[ClubTransferMini] = []
    transfer_targets: List[ClubTargetMini] = []
