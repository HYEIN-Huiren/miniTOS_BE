from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import Base, engine
from app.core.middleware import log_requests
from app.api.container_router import router as container_router


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
app.include_router(container_router)


# =========================
# Health Check
# =========================
@app.get("/")
def health():
    return {"status": "ok"}