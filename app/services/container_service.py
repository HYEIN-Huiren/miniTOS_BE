from fastapi import HTTPException, status

from app.models.container import Container
from app.repositories.container_repository import ContainerRepository
from app.core.logger import logger
from app.core.exceptions import NotFoundException

class ContainerService:

    def __init__(self):
        self.repo = ContainerRepository()

    def create(self, db, container_no, status="REGISTERED"):
        logger.info("create_container", container_no=container_no)
        obj = Container(container_no=container_no, status = status)
        return self.repo.create(db, obj)

    def get(self, db, container_id):
        obj = self.repo.get(db, container_id)
        
        if not obj:
            raise NotFoundException("Container not found")

        return obj

    def get_all(self, db):
        return self.repo.get_all(db)

    def update_status(self, db, container_id, to_status, yard_id = None):
        obj = self.repo.update_status(
            db,
            container_id,
            status=to_status,
            yard_id = yard_id
        )
        return obj


    def delete(self, db, container_id, current_user):
        
        if current_user.role not in ["ADMIN", "OPERATOR"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Admin or Operator only",
            )

        return self.repo.delete(db, container_id)