from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict

class EventCreate(BaseModel):
    container_id: UUID
    status: str

class EventResponse(BaseModel):
    event_id: UUID
    container_id: UUID
    status: str
    event_time: datetime
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )