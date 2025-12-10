from fastapi import FastAPI

app = FastAPI(title="My First Backend", version="1.0")

@app.get("/")
def home():
    return {"message": "Hello World! Backend Python của bạn đang chạy!"}

@app.get("/api/user")
def health_check():
    return {"user": "Quy Nguyen"}