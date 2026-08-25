"""
Player Pydantic Schemas
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.club import ClubSummary

class RadarStats(BaseModel):
    pace: int
    shooting: int
    passing: int
    dribbling: int
    defending: int
    physical: int
    ego: int

class PerformanceStats(BaseModel):
    appearances: int
    goals: int
    assists: int
    minutes_played: int
    xg: float
    xa: float
    shots: int
    key_passes: int
    dribbles: int
    pass_accuracy: float
    tackles: int
    interceptions: int

class MarketHistoryPoint(BaseModel):
    year: str
    value: float
    model_config = ConfigDict(from_attributes=True)

class PlayerBase(BaseModel):
    name: str
    slug: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: int
    date_of_birth: Optional[str] = None
    nationality: str
    flag: Optional[str] = "🌍"
    position: str
    preferred_foot: Optional[str] = "Right"
    shirt_number: Optional[int] = None
    current_club_id: Optional[int] = None
    market_value: str
    market_value_raw: float
    asking_price: Optional[str] = None
    reported_offer: Optional[str] = None
    contract_expiry: Optional[str] = None
    image_url: Optional[str] = None
    overview: Optional[str] = None
    overall_rating: int = 85
    ego_rating: int = 90
    striker_index: int = 88
    market_threat: str = "HIGH"
    momentum: int = 80

class PlayerSummary(PlayerBase):
    id: int
    current_club_name: Optional[str] = None
    current_club_badge: Optional[str] = None
    radar: RadarStats
    model_config = ConfigDict(from_attributes=True)

class InterestedClubInfo(BaseModel):
    club_id: int
    name: str
    badge: Optional[str] = None
    league: str
    interest: str
    offer: Optional[str] = None
    status: str
    probability: int

class PlayerDetail(PlayerSummary):
    stats: PerformanceStats
    value_history: List[MarketHistoryPoint] = []
    interested_clubs: List[InterestedClubInfo] = []
