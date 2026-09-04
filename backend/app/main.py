"""
BLUEGUN — FastAPI Backend
Main application entry point.
"""

# © 2026 BLUEGUN
# Original project code and implementation.
# Third-party libraries and materials remain subject to their respective licenses.
# See /credits (Copyright & Sources page) for full attribution.


import os
import logging
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
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
    title="BLUEGUN — 2026 Football Transfer Intelligence API",
    description=(
        "⚡ Next-generation 2026 football transfer market intelligence and scouting analytics API. "
        "Provides real-time transfer feeds, player scouting files, club war rooms, "
        "market pressure valuations, global search, and ego clash comparisons. "
        "Frontend: http://localhost:3000 — Tagline: 'ENTER THE TRANSFER BATTLEFIELD.'"
    ),
    version="2.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    contact={"name": "BLUEGUN Transfer Intelligence", "email": "intel@bluegun.football"},
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


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    detail = exc.detail
    if isinstance(detail, dict):
        return JSONResponse(status_code=exc.status_code, content=detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": str(detail)},
    )


# Global exception handler (does not swallow HTTPException)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, StarletteHTTPException):
        return await http_exception_handler(request, exc)
    logger.error(f"Unhandled exception on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error"},
    )


from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

# Root directory of web project
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Serve static assets for standalone frontend hosting
if os.path.exists(os.path.join(PROJECT_ROOT, "css")):
    app.mount("/css", StaticFiles(directory=os.path.join(PROJECT_ROOT, "css")), name="css")
if os.path.exists(os.path.join(PROJECT_ROOT, "js")):
    app.mount("/js", StaticFiles(directory=os.path.join(PROJECT_ROOT, "js")), name="js")
if os.path.exists(os.path.join(PROJECT_ROOT, "assets")):
    app.mount("/assets", StaticFiles(directory=os.path.join(PROJECT_ROOT, "assets")), name="assets")
if os.path.exists(os.path.join(PROJECT_ROOT, "data")):
    app.mount("/data", StaticFiles(directory=os.path.join(PROJECT_ROOT, "data")), name="data")

@app.get("/health", tags=["Health"])
@app.get("/api/health", tags=["Health"])
def health_check():
    """Health check & API info."""
    return {
        "success": True,
        "message": "⚡ BLUEGUN — 2026 Football Transfer Intelligence API is live",
        "version": "2.0.0",
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

@app.get("/", tags=["App"])
@app.get("/app", tags=["App"])
def serve_app_or_root(request: Request):
    """Serves frontend index.html for browsers, or API info for JSON clients."""
    accept = request.headers.get("accept", "")
    index_file = os.path.join(PROJECT_ROOT, "index.html")
    if ("text/html" in accept or request.url.path == "/app") and os.path.exists(index_file):
        return FileResponse(index_file)
    return health_check()


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
