"""
Transfer Model Definition
Tracks live market operations, club-to-club movements, valuation spreads, and probability intelligence.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, index=True)
    current_club_id = Column(Integer, ForeignKey("clubs.id"), nullable=True, index=True)
    interested_club_id = Column(Integer, ForeignKey("clubs.id"), nullable=True, index=True)

    market_value = Column(String(50), nullable=True)
    asking_price = Column(String(50), nullable=True)
    reported_offer = Column(String(100), nullable=True)
    final_fee = Column(String(50), nullable=True)

    transfer_type = Column(String(50), default="Permanent") # Permanent, Loan, Loan with option to buy, Free Transfer
    status = Column(String(50), default="Negotiating", index=True) # Confirmed, Negotiating, Rumour, Monitoring, Completed, Rejected
    probability = Column(Integer, default=50) # 0 - 100%
    confidence = Column(Integer, default=50) # 0 - 100%
    negotiation_stage = Column(String(100), nullable=True) # Official Bid, Personal Terms Agreed, Club Talks, Initial Inquiry
    contract_status = Column(String(100), nullable=True)
    headline = Column(Text, nullable=True)
    
    source = Column(String(150), nullable=True, default="BlueLock Tactical Wire")
    source_url = Column(String(500), nullable=True)
    time_ago = Column(String(50), nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    player = relationship("Player", back_populates="transfers")
    current_club = relationship("Club", foreign_keys=[current_club_id], back_populates="outgoing_transfers")
    interested_club = relationship("Club", foreign_keys=[interested_club_id], back_populates="incoming_transfers")
