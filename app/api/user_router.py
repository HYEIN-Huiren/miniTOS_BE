from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

service = UserService()


# =========================
# ADMIN 체크 함수
# =========================
def admin_only(user):
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")


# =========================
# GET USERS
# =========================
@router.get("", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    admin_only(current_user)
    return service.get_all(db)


# =========================
# CREATE USER
# =========================
@router.post("", response_model=UserResponse)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    admin_only(current_user)
    return service.create(db, payload)