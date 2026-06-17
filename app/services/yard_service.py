from sqlalchemy.orm import Session

from app.models.yard import Yard
from app.repositories import yard_repository
from app.schemas.yard import YardCreate


def create(
    db: Session,
    request: YardCreate,
) -> Yard:
    yard = Yard(
        yard_name=request.yard_name,
    )

    return yard_repository.create(
        db,
        yard,
    )


def get_all(
    db: Session,
):
    return yard_repository.get_all(db)


def get_by_id(
    db: Session,
    yard_id: int,
):
    return yard_repository.get_by_id(
        db,
        yard_id,
    )