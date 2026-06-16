from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.role import require_roles

from app.schemas.container import ContainerCreate, ContainerResponse
from app.schemas.container_event import EventCreate
from app.schemas.container_event import EventResponse
from app.schemas.response import BaseResponse
from app.services.container_service import ContainerService
from app.services.event_service import EventService

from app.core.database import get_db

router = APIRouter(prefix="/containers", tags=["Containers"])

service = ContainerService()
event_service = EventService()

@router.post("")
def create(payload: ContainerCreate, 
            db: Session = Depends(get_db), 
            current_user = Depends(require_roles("ADMIN", "OPERATOR"))
         ):

    data = event_service.create_event(db, to_status="REGISTERED",event_type="REGISTER", container_no=payload.container_no)
    return BaseResponse(data=ContainerResponse.model_validate(data))


@router.get("/{container_id}")
def get(container_id: str, 
        db: Session = Depends(get_db), 
        current_user = Depends(get_current_user)
    ):
    data = service.get(db, container_id)
    return BaseResponse(data=ContainerResponse.model_validate(data))


@router.get("")
def list_all(
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    data = service.get_all(db)
    return BaseResponse(data=data)


# @router.patch("/{container_id}/status")
# def update_status(
#     container_id: str, 
#     payload: ContainerUpdate, 
#     db: Session = Depends(get_db), 
#     current_user = Depends(require_roles("ADMIN", "OPERATOR"))
# ):
#     data = service.update_status(db, container_id, payload.status)
#     return BaseResponse(data=ContainerResponse.model_validate(data))


@router.delete("/{container_id}")
def delete(
    container_id: str, 
    db: Session = Depends(get_db), 
    current_user = Depends(require_roles("ADMIN", "OPERATOR"))
):
    service.delete(db, container_id, current_user)
    return BaseResponse(message="deleted")


@router.get("/{container_id}/events")
def get_events(
    container_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
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

# =========================
# REGISTER (container 생성 + event 자동 발생)
# =========================
@router.post("")
def register_container(
    payload: ContainerCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_roles("ADMIN", "OPERATOR"))
):
    data = event_service.create_event(
        db=db,
        container_id=None,
        container_no=payload.container_no,
        event_type="REGISTER",
        to_status="REGISTERED",
    )

    return BaseResponse(data=ContainerResponse.model_validate(data))


# =========================
# EVENT (CORE FLOW)
# =========================
@router.post("/{container_id}/events")
def create_event(
    container_id: str,
    payload: EventCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_roles("ADMIN", "OPERATOR"))
):
    data = event_service.create_event(
        db=db,
        container_id=container_id,
        event_type=payload.event_type,
        to_status=payload.status,
    )

    return BaseResponse(data=ContainerResponse.model_validate(data))