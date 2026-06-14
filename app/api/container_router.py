from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.container import ContainerCreate, ContainerUpdate, ContainerResponse
from app.schemas.container_event import EventResponse
from app.schemas.response import BaseResponse
from app.services.container_service import ContainerService
from app.services.event_service import EventService


router = APIRouter(prefix="/containers", tags=["Containers"])

service = ContainerService()
event_service = EventService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create(payload: ContainerCreate, db: Session = Depends(get_db)):
    data = service.create(db, payload.container_no)
    return BaseResponse(data=ContainerResponse.model_validate(data))


@router.get("/{container_id}")
def get(container_id: str, db: Session = Depends(get_db)):
    data = service.get(db, container_id)
    return BaseResponse(data=ContainerResponse.model_validate(data))


@router.get("")
def list_all(db: Session = Depends(get_db)):
    data = service.get_all(db)
    return BaseResponse(data=data)


@router.patch("/{container_id}/status")
def update_status(container_id: str, payload: ContainerUpdate, db: Session = Depends(get_db)):
    data = service.update_status(db, container_id, payload.status)
    return BaseResponse(data=ContainerResponse.model_validate(data))


@router.delete("/{container_id}")
def delete(container_id: str, db: Session = Depends(get_db)):
    service.delete(db, container_id)
    return BaseResponse(message="deleted")

@router.get("/{container_id}/events")
def get_events(
    container_id: str,
    db: Session = Depends(get_db),
):
    events = event_service.get_by_container(
        db,
        container_id,
    )
    data = [
        EventResponse.model_validate(event)
        for event in events
    ]

    return BaseResponse(data=data)