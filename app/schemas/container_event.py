from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict

class EventCreate(BaseModel):
    event_type: str
    status: str
    yard_id : int | None = None
    
class EventResponse(BaseModel):
    event_id: UUID
    container_id: UUID

    event_type: str
    from_status: str | None
    status: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )