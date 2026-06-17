from sqlalchemy.orm import Session

from app.models.yard import Yard


def create(
    db: Session,
    yard: Yard,
) -> Yard:
    db.add(yard)
    db.commit()
    db.refresh(yard)

    return yard


def get_all(
    db: Session,
) -> list[Yard]:
    return (
        db.query(Yard)
        .order_by(Yard.code)
        .all()
    )


def get_by_id(
    db: Session,
    yard_id: int,
) -> Yard | None:
    return (
        db.query(Yard)
        .filter(Yard.yard_id == yard_id)
        .first()
    )