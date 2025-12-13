from pydantic import BaseModel

class ActivitiesCreate(BaseModel):
    title: str
    description: str | None = None
    image_base64: str

class ActivitiesResponse(BaseModel):
    id: int
    title: str
    description: str | None
    img_url: str | None

    class Config:
        orm_mode = True
