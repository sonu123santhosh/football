"""
BLUELOCK // TRANSFER IQ — FastAPI Backend
Main application entry point.
"""

import os
import logging
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

from app.database import engine, SessionLocal, Base
import app.models  # noqa: F401 — triggers model registration before create_all
from app.routes import (
    players_router,
    clubs_router,
    transfers_router,
    news_router,
    search_router,
    compare_router,
)
from app.services.news_service import sync_news_from_external
from app.services.football_api_service import get_api_status

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# Scheduler for background sync
scheduler = AsyncIOScheduler()
SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL_MINUTES", "30"))

# CORS configuration
raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
ALLOWED_ORIGINS = [o.strip() for o in raw_origins.split(",")]


async def scheduled_news_sync():
    """Periodic background task — fetches external news if API key configured."""
    db = SessionLocal()
    try:
        count = await sync_news_from_external(db)
        logger.info(f"Scheduled sync complete: {count} new news items.")
    except Exception as e:
        logger.error(f"Scheduled sync error: {e}")
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create all tables
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables ready.")

    # Start scheduler
    scheduler.add_job(
        scheduled_news_sync,
        "interval",
        minutes=SYNC_INTERVAL,
        id="news_sync",
        replace_existing=True,
    )
    scheduler.start()
    logger.info(f"Background scheduler started — syncing every {SYNC_INTERVAL} minutes.")
    logger.info(f"External API status: {get_api_status()}")

    yield

    # Shutdown
    scheduler.shutdown(wait=False)
    logger.info("Scheduler stopped.")


app = FastAPI(
    title="BLUELOCK // TRANSFER IQ API",
    description=(
        "🔵 Futuristic football transfer intelligence platform API. "
        "Provides real-time transfer feeds, player profiles, club dossiers, "
        "market valuations, global search, and player comparison. "
        "Frontend: http://localhost:3000"
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    contact={"name": "BlueLock Transfer IQ", "email": "intel@bluelocktransferiq.com"},
)

# CORS Middleware — allows frontend to consume the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(players_router)
app.include_router(clubs_router)
app.include_router(transfers_router)
app.include_router(news_router)
app.include_router(search_router)
app.include_router(compare_router)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error", "details": str(exc)},
    )


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"success": False, "error": "Resource not found"},
    )


@app.get("/", tags=["Health"])
@app.get("/health", tags=["Health"])
def root():
    """Health check & API info."""
    return {
        "success": True,
        "message": "⚽ BLUELOCK // TRANSFER IQ API is live",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "players": "/api/players",
            "clubs": "/api/clubs",
            "transfers": "/api/transfers",
            "news": "/api/news",
            "search": "/api/search?q=",
            "compare": "/api/compare?player1=1&player2=2",
        },
        "external_apis": get_api_status(),
    }


@app.get("/api/status", tags=["Health"])
def api_status():
    """Returns API health and external API configuration status."""
    return {
        "success": True,
        "data": {
            "status": "healthy",
            "external_apis": get_api_status(),
            "scheduler": "running" if scheduler.running else "stopped",
        },
        "message": "Backend is operational",
    }
