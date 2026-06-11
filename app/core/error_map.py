ERROR_MAP = {
    "CONTAINER_NOT_FOUND": {"status": 404, "message": "Container not found"},
    "INVALID_STATUS": {"status": 400, "message": "Invalid status transition"},
    "DUPLICATE_CONTAINER_NO": {"status": 409, "message": "Container already exists"},
}