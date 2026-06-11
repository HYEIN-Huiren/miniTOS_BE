from pydantic import BaseModel
from typing import Any, Optional


class BaseResponse(BaseModel):
    success: bool = True
    message: str = "success"
    data: Optional[Any] = None