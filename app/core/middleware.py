import time
from fastapi import Request
from app.core.logger import logger


async def log_requests(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    logger.info(
        "request_log",
        method=request.method,
        url=str(request.url),
        status_code=response.status_code,
        process_time=round(process_time, 4)
    )

    return response