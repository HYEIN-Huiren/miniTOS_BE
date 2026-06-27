from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import BaseResponse
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.schemas.yard import (
    YardCreate,
    YardResponse,
)
from app.services import yard_service

router = APIRouter(
    prefix="/yards",
    tags=["Yards"],
)

@router.post("", response_model=YardResponse,)
def create_yard(
    request: YardCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    data = yard_service.create(
        db,
        request,
    )
    return BaseResponse(data= YardResponse.model_validate(data))


@router.get("", response_model=list[YardResponse],)
def get_yards(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    data = yard_service.get_all(db)
    return BaseResponse(data = data)


@router.get("/{yard_id}", response_model=YardResponse,)
def get_yard(
    yard_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    data = yard_service.get_by_id(
        db,
        yard_id,
    )
    return BaseResponse(data= YardResponse.model_validate(data))