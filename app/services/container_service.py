from app.models.container import Container
from app.repositories.container_repository import ContainerRepository
from app.core.logger import logger
from app.core.exceptions import NotFoundException


class ContainerService:

    def __init__(self):
        self.repo = ContainerRepository()

    def create(self, db, container_no):
        logger.info("create_container", container_no=container_no)
        
        obj = Container(
            container_no=container_no,
            status= "INBOUND"
        )
        return self.repo.create(db, obj)

    def get(self, db, container_id):
        obj = self.repo.get(db, container_id)
        
        if not obj:
            raise NotFoundException("Container not found")

        return obj

    def get_all(self, db):
        return self.repo.get_all(db)

    def update_status(self, db, container_id, status):
        return self.repo.update_status(db, container_id, status)

    def delete(self, db, container_id):
        return self.repo.delete(db, container_id)