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
    
    def create_event(self, db, to_status, event_type, container_id=None, container_no=None):

        from_status = None

        # =========================
        # 1. 컨테이너 조회 or 생성
        # =========================
        if container_id:
            obj = self.container_service.get(db, container_id)
            from_status = obj.status

        else:
            if event_type != "REGISTER":
                raise Exception("Container not found")

            if not container_no:
                raise Exception("container_no required for REGISTER")
            
            to_status = "REGISTERED"
            from_status = None

            obj = self.container_service.create(
                db,
                container_no=container_no,
                status=to_status
            )

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
            to_status = to_status
        )
        
        db.commit()

        return updated