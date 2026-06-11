from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.core.database import Base


class Container(Base):
    __tablename__ = "container"

    container_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    container_no = Column(String(20), unique=True, nullable=False)

    status = Column(String(20), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)