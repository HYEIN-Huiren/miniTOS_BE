from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.yard import (
    YardCreate,
    YardResponse,
)
from app.services import yard_service

router = APIRouter(
    prefix="/yards",
    tags=["Yards"],
)


@router.post(
    "",
    response_model=YardResponse,
)
def create_yard(
    request: YardCreate,
    db: Session = Depends(get_db),
):
    return yard_service.create(
        db,
        request,
    )


@router.get(
    "",
    response_model=list[YardResponse],
)
def get_yards(
    db: Session = Depends(get_db),
):
    return yard_service.get_all(db)


@router.get(
    "/{yard_id}",
    response_model=YardResponse,
)
def get_yard(
    yard_id: int,
    db: Session = Depends(get_db),
):
    return yard_service.get_by_id(
        db,
        yard_id,
    )