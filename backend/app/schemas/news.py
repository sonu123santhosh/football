"""
Transfer News Pydantic Schemas
"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class NewsBase(BaseModel):
    title: str
    description: str
    content: Optional[str] = None
    image_url: Optional[str] = None
    player_id: Optional[int] = None
    club_id: Optional[int] = None
    source: str = "BLUEGUN Intelligence Wire"
    source_url: Optional[str] = None
    author: Optional[str] = "Transfer Desk"
    retrieved_at: Optional[str] = None
    attribution_required: Optional[int] = 1
    category: str = "Negotiation"
    reliability_score: int = 85
    read_time: str = "3 min read"
    ego_impact: Optional[str] = None

class NewsResponse(NewsBase):
    id: int
    published_at: datetime
    player_name: Optional[str] = None
    club_name: Optional[str] = None
    involved_clubs: List[str] = []
    model_config = ConfigDict(from_attributes=True)
