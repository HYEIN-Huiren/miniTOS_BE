from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password
from fastapi import HTTPException, status


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def get_all(self, db):
        return self.repo.get_all(db)

    def create(self, db, payload):
        # username 중복 체크
        exist = self.repo.get_by_username(db, payload.username)
        if exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
    )

        user = User(
            username=payload.username,
            hashed_password=hash_password(payload.password),
            role=payload.role
        )

        return self.repo.create(db, user)