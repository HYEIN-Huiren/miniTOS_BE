from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.core.middleware import log_requests
from app.api.container_router import router as container_router
from app.api.auth_router import router as auth_router
from app.api.user_router import router as user_router
from app.api.yard_router import router as yard_router
from app.core.config import settings


# =========================
# App Lifespan (startup hook)
# =========================
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    Base.metadata.create_all(bind=engine)
    yield
    # shutdown (추후 cleanup 가능)


app = FastAPI(
    title="Mini TOS V1",
    lifespan=lifespan
)


# =========================
# Middleware
# =========================
app.middleware("http")(log_requests)


# =========================
# Routers
# =========================
app.include_router(auth_router)
app.include_router(container_router)
app.include_router(user_router)
app.include_router(yard_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FE_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Health Check
# =========================
@app.get("/")
def health():
    return {"status": "ok"}