from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models.user import User
from .schema.user import UserCreate
from .router.activities import router as activities_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PandaTaekwondo", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://panda-taekwondo.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello World! Backend Python của bạn đang chạy!"}

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

# serve ảnh tĩnh
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# đăng ký router
app.include_router(activities_router)