from app.routes.players import router as players_router
from app.routes.clubs import router as clubs_router
from app.routes.transfers import router as transfers_router
from app.routes.news import router as news_router
from app.routes.search import router as search_router
from app.routes.compare import router as compare_router

__all__ = [
    "players_router",
    "clubs_router",
    "transfers_router",
    "news_router",
    "search_router",
    "compare_router",
]
