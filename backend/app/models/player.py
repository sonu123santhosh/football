"""
Player Model Definition
Comprehensive scouting profile, performance metrics, radar stats, and Blue Lock ego indexes.
"""

from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(150), nullable=False, index=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    age = Column(Integer, nullable=False)
    date_of_birth = Column(String(50), nullable=True)
    nationality = Column(String(100), nullable=False, index=True)
    flag = Column(String(20), nullable=True, default="🌍")
    position = Column(String(100), nullable=False, index=True)
    preferred_foot = Column(String(20), nullable=True, default="Right")
    shirt_number = Column(Integer, nullable=True)
    
    current_club_id = Column(Integer, ForeignKey("clubs.id"), nullable=True)
    
    # Financial & Contract
    market_value = Column(String(50), nullable=False)
    market_value_raw = Column(Float, nullable=False, default=0.0) # in Millions EUR
    asking_price = Column(String(50), nullable=True)
    reported_offer = Column(String(100), nullable=True)
    contract_expiry = Column(String(50), nullable=True)
    image_url = Column(String(500), nullable=True)
    overview = Column(Text, nullable=True)

    # 12 Advanced Performance Scouting Metrics
    appearances = Column(Integer, default=0)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    xg = Column(Float, default=0.0) # Expected Goals
    xa = Column(Float, default=0.0) # Expected Assists
    shots = Column(Integer, default=0)
    key_passes = Column(Integer, default=0)
    dribbles = Column(Integer, default=0)
    pass_accuracy = Column(Float, default=0.0)
    tackles = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)

    # 6 Tactical Radar Attributes (0 - 99)
    pace = Column(Integer, default=75)
    shooting = Column(Integer, default=75)
    passing = Column(Integer, default=75)
    dribbling = Column(Integer, default=75)
    defending = Column(Integer, default=50)
    physical = Column(Integer, default=75)

    # Blue Lock Ego Intelligence Ratings (0 - 99)
    overall_rating = Column(Integer, default=85)
    ego_rating = Column(Integer, default=90)
    striker_index = Column(Integer, default=88)
    market_threat = Column(String(50), default="HIGH") # SUPREME, CRITICAL, VERY HIGH, HIGH, MEDIUM
    momentum = Column(Integer, default=80)

    # Relationships
    current_club = relationship("Club", back_populates="players", foreign_keys=[current_club_id])
    transfers = relationship("Transfer", back_populates="player", cascade="all, delete-orphan")
    news_items = relationship("TransferNews", back_populates="player")
    market_history = relationship("MarketValueHistory", back_populates="player", cascade="all, delete-orphan", order_by="MarketValueHistory.year_recorded")
