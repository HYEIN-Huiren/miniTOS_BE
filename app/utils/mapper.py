def container_to_dict(c):
    return {
        "container_id": str(c.container_id),
        "container_no": c.container_no,
        "status": c.status,
    }