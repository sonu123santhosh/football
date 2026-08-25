"""
Global Categorized Search Pydantic Schemas
"""

from typing import List, Optional
from pydantic import BaseModel

class SearchPlayerItem(BaseModel):
    id: int
    name: str
    slug: str
    age: int
    position: str
    current_club: str
    market_value: str
    ego_rating: int
    image_url: Optional[str] = None
    flag: Optional[str] = None

class SearchClubItem(BaseModel):
    id: int
    name: str
    slug: str
    league: str
    country: str
    logo_url: Optional[str] = None
    transfer_budget: Optional[str] = None
    ego_rank: Optional[str] = None
    flag: Optional[str] = None

class SearchNewsItem(BaseModel):
    id: int
    title: str
    category: str
    source: str
    published_at: str
    player_name: Optional[str] = None

class GlobalSearchResponse(BaseModel):
    query: str
    total_results: int
    players: List[SearchPlayerItem] = []
    clubs: List[SearchClubItem] = []
    news: List[SearchNewsItem] = []
