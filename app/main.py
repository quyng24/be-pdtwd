from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .model.modeluser import User
from .schema.schemauser import UserCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PandaTaekwondo", version="1.0")

@app.post("/users")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=data.name,
        birthday=data.birthday
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "User created successfully",
        "data": {
            "id": new_user.id,
            "name": new_user.name,
            "birthday": str(new_user.birthday)
        }
    }