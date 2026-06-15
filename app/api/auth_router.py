from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)

from app.services import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):

    token = auth_service.login(
        db,
        payload.username,
        payload.password,
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return TokenResponse(
        access_token=token,
    )