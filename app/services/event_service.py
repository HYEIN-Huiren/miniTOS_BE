from app.repositories.event_repository import (
    EventRepository,
)


class EventService:

    def __init__(self):
        self.repo = EventRepository()

    def get_by_container(
        self,
        db,
        container_id,
    ):
        return self.repo.get_by_container(
            db,
            container_id,
        )

    def get_recent(
        self,
        db,
    ):
        return self.repo.get_recent(
            db,
        )