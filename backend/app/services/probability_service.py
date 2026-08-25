"""
Algorithmic Transfer Probability Scoring Service
Estimates transfer likelihood (0-100%) based on available intelligence signals.
Clearly labeled as ALGORITHMIC/ESTIMATED — not official predictions.
"""

from typing import Dict, Any

# Status base scores
STATUS_WEIGHTS = {
    "Confirmed": 100,
    "Negotiating": 72,
    "Rumour": 38,
    "Monitoring": 22,
    "Completed": 100,
    "Rejected": 0,
}

# Negotiation stage modifiers
STAGE_MODIFIERS = {
    "Official Bid Submitted": +20,
    "Personal Terms Agreed": +25,
    "Advanced Club Talks": +15,
    "Agent Meeting Held": +10,
    "Club Interest Confirmed": +5,
    "Initial Inquiry": -5,
    "Pre-contract Discussions": +12,
    "Monitoring": -10,
    "Contract Extension Signed": -40,   # Less likely to leave
}

# Source reliability modifiers
RELIABILITY_MODIFIERS = {
    (90, 100): +10,
    (75, 89): +5,
    (50, 74): 0,
    (25, 49): -10,
    (0, 24): -20,
}

THREAT_LEVELS = [
    (85, "EXTREME"),
    (70, "VERY HIGH"),
    (55, "HIGH"),
    (35, "MEDIUM"),
    (15, "LOW"),
    (0, "MINIMAL"),
]

def calculate_transfer_probability(
    status: str,
    negotiation_stage: str = None,
    contract_months_remaining: int = 24,
    has_offer: bool = False,
    offer_vs_asking_ratio: float = 0.8,
    source_reliability: int = 75,
    interested_clubs_count: int = 1,
) -> Dict[str, Any]:
    """
    Algorithmic transfer probability estimator.
    NOTE: This is an estimated, data-driven score — not an official prediction.

    Returns:
        {
            "probability": 78,
            "level": "VERY HIGH",
            "note": "Estimated algorithmic score"
        }
    """
    # Base score from status
    score = STATUS_WEIGHTS.get(status, 40)

    # Negotiation stage modifier
    if negotiation_stage:
        for stage_key, modifier in STAGE_MODIFIERS.items():
            if stage_key.lower() in negotiation_stage.lower():
                score += modifier
                break

    # Contract pressure — expiring contracts dramatically raise likelihood
    if contract_months_remaining <= 6:
        score += 20
    elif contract_months_remaining <= 12:
        score += 12
    elif contract_months_remaining <= 18:
        score += 5
    elif contract_months_remaining >= 36:
        score -= 10  # Locked in a long deal, less likely to move

    # Has a concrete monetary offer been made?
    if has_offer:
        score += 10

    # How close is the offer to the asking price?
    if offer_vs_asking_ratio >= 1.0:
        score += 15  # Offer matches or exceeds asking
    elif offer_vs_asking_ratio >= 0.9:
        score += 8
    elif offer_vs_asking_ratio >= 0.75:
        score += 2
    elif offer_vs_asking_ratio < 0.5:
        score -= 12  # Large gap, deal stalling

    # Source reliability
    for (low, high), modifier in RELIABILITY_MODIFIERS.items():
        if low <= source_reliability <= high:
            score += modifier
            break

    # Multiple clubs interested = bidding war pressure
    if interested_clubs_count >= 3:
        score += 8
    elif interested_clubs_count == 2:
        score += 4

    # Clamp to 0-100
    score = max(0, min(100, score))

    # Determine threat level label
    level = "MINIMAL"
    for threshold, label in THREAT_LEVELS:
        if score >= threshold:
            level = label
            break

    return {
        "probability": score,
        "level": level,
        "note": "Algorithmic estimated score — not an official transfer prediction",
    }
