from fastapi import HTTPException, status

from app.models.container import Container
from app.repositories.container_repository import ContainerRepository
from app.core.logger import logger
from app.core.exceptions import NotFoundException

from app.models.container_event import ContainerEvent


class ContainerService:

    def __init__(self):
        self.repo = ContainerRepository()

    def create(self, db, container_no):
        logger.info("create_container", container_no=container_no)
        
        obj = Container(
            container_no=container_no,
            status= "INBOUND"
        )
        
        obj = self.repo.create(db, obj)
        
        event = ContainerEvent(
            container_id=obj.container_id,
            status="INBOUND"
        )
        
        db.add(event)
        db.commit()
        
        return obj

    def get(self, db, container_id):
        obj = self.repo.get(db, container_id)
        
        if not obj:
            raise NotFoundException("Container not found")

        return obj

    def get_all(self, db):
        return self.repo.get_all(db)

    def update_status(self, db, container_id, status):
        obj = self.repo.update_status(
            db,
            container_id,
            status
        )
        
        event = ContainerEvent(
            container_id=obj.container_id,
            status=status
        )
        
        db.add(event)
        db.commit()
        
        return obj

    def delete(self, db, container_id, current_user):
        
        if current_user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Admin only",
            )
        return self.repo.delete(db, container_id)