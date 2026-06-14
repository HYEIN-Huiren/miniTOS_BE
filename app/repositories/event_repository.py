from app.models.container_event import ContainerEvent


class EventRepository:

    def get_by_container(
        self,
        db,
        container_id,
    ):
        return (
            db.query(ContainerEvent)
            .filter(
                ContainerEvent.container_id
                == container_id
            )
            .order_by(
                ContainerEvent.event_time.desc()
            )
            .all()
        )

    def get_recent(
        self,
        db,
        limit=100,
    ):
        return (
            db.query(ContainerEvent)
            .order_by(
                ContainerEvent.event_time.desc()
            )
            .limit(limit)
            .all()
        )