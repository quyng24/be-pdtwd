from fastapi import FastAPI

app = FastAPI(title="PandaTaekwondo", version="1.0")

@app.get("/")
def home():
    return {"message": "Hello World! Backend Python của bạn đang chạy!"}

@app.get("/api/user")
def get_user():
    return {"user": "Quy Nguyen"}