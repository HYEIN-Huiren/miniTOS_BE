from app.repositories.event_repository import (
    EventRepository,
)
from app.services.container_service import ContainerService
from app.models.container_event import ContainerEvent



class EventService:

    def __init__(self):
        self.repo = EventRepository()
        self.container_service = ContainerService()

    def get_by_container(self, db, container_id):
        return self.repo.get_by_container(db, container_id)

    def get_recent(self, db):
        return self.repo.get_recent(db)
    
    def create_event(self, db,container_id, to_status, event_type, yard_id = None):

        # =========================
        # 1. 컨테이너 조회 or 생성
        # =========================
        
        obj = self.container_service.get(db, container_id)
        from_status = obj.status

        # =========================
        # 2. event 생성
        # =========================
        event = ContainerEvent(
            container_id=obj.container_id,
            event_type=event_type,
            from_status=from_status,
            status=to_status,
        )
        db.add(event)

        # =========================
        # 3. container status update
        # =========================

        updated = self.container_service.update_status(
            db,
            obj.container_id,
            to_status = to_status,
            yard_id = yard_id
        )
        
        db.commit()

        return updated