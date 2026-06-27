from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from app.schemas.yard import YardResponse


class ContainerCreate(BaseModel):
    container_no: str
    # status: str


class ContainerUpdate(BaseModel):
    status: str


class ContainerResponse(BaseModel):
    container_id: UUID
    container_no: str
    status: str
    yard: YardResponse | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True