"""
Utility helpers - formatting, error responses, value parsing.
"""

from typing import Any, Optional
from fastapi import HTTPException
from datetime import datetime, timezone

def format_millions(value_raw: float) -> str:
    """Convert raw float (e.g. 180.0) to display string (e.g. '€180M')."""
    if value_raw is None:
        return "N/A"
    if value_raw >= 1000:
        return f"€{value_raw/1000:.2f}B"
    return f"€{int(value_raw)}M" if value_raw == int(value_raw) else f"€{value_raw}M"

def parse_millions(value_str: str) -> float:
    """Parse '€180M' or '€1.36B' to raw float."""
    if not value_str:
        return 0.0
    s = value_str.replace("€", "").replace(",", "").strip()
    try:
        if "B" in s:
            return float(s.replace("B", "")) * 1000
        elif "M" in s:
            return float(s.replace("M", ""))
        return float(s)
    except ValueError:
        return 0.0

def not_found(entity: str, identifier: Any) -> HTTPException:
    return HTTPException(
        status_code=404,
        detail={"success": False, "error": f"{entity} not found", "id": str(identifier)}
    )

def bad_request(detail: str) -> HTTPException:
    return HTTPException(
        status_code=400,
        detail={"success": False, "error": detail}
    )

def success_response(data: Any, message: str = "Success") -> dict:
    return {"success": True, "data": data, "message": message}

def time_ago_str(dt: Optional[datetime]) -> str:
    if not dt:
        return "Recently"
    now = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    diff_seconds = int((now - dt).total_seconds())
    if diff_seconds < 60:
        return f"{diff_seconds} sec ago"
    elif diff_seconds < 3600:
        return f"{diff_seconds // 60} min ago"
    elif diff_seconds < 86400:
        return f"{diff_seconds // 3600} hr ago"
    else:
        return f"{diff_seconds // 86400} days ago"
