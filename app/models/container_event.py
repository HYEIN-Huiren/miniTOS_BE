from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.core.database import Base


class ContainerEvent(Base):
    __tablename__ = "container_event"

    event_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    container_id = Column(
        UUID(as_uuid=True),
        ForeignKey("container.container_id"),
        nullable=False,
    )
    # cycle_id = Column(UUID(as_uuid=True), nullable=True)
    
    event_type = Column(String(30), nullable=False)

    from_status = Column(String(20), nullable=True)

    status = Column(
        String(20),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
    )