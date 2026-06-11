from sqlalchemy.orm import Session
from app.models.container import Container


class ContainerRepository:

    def create(self, db: Session, obj: Container):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get(self, db: Session, container_id):
        return db.query(Container).filter(Container.container_id == container_id).first()

    def get_all(self, db: Session):
        return db.query(Container).all()

    def update_status(self, db: Session, container_id, status: str):
        obj = self.get(db, container_id)
        if obj:
            obj.status = status
            db.commit()
            db.refresh(obj)
        return obj

    def delete(self, db: Session, container_id):
        obj = self.get(db, container_id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj