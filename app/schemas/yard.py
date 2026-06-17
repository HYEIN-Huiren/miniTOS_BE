from pydantic import BaseModel, ConfigDict


class YardCreate(BaseModel):
    yard_name: str
    
class YardUpdate(BaseModel):
    yard_name: str | None = None

class YardResponse(BaseModel):
    yard_id: int
    yard_name: str

    model_config = ConfigDict(
        from_attributes=True
    )