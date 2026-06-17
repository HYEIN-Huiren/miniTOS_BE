from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Yard(Base):
    __tablename__ = "yards"

    yard_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    yard_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # description: Mapped[str | None] = mapped_column(
    #     String(255),
    #     nullable=True,
    # )