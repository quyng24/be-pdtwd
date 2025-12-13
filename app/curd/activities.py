import os
import base64
import uuid
from app.models.activities import Activities
from sqlalchemy.orm import Session

UPLOAD_DIR = "uploads/activities/"


def save_image_from_base64(image_base64: str) -> str:
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # tách phần header: data:image/jpeg;base64,
    base64_data = image_base64.split(",")[1]

    img_bytes = base64.b64decode(base64_data)

    file_name = f"{uuid.uuid4().hex}.jpg"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as f:
        f.write(img_bytes)

    return f"/uploads/activities/{file_name}"


def create_activity(db: Session, data):
    img_url = save_image_from_base64(data.image_base64)

    new_activity = Activities(
        title=data.title,
        description=data.description,
        img_url=img_url
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


def get_all_activities(db: Session):
    return db.query(Activities).all()
