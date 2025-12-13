from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Nếu bạn muốn test tạm thời mà chưa set env:
# DATABASE_URL = "postgresql+psycopg2://user:password@host:port/dbname"

if not DATABASE_URL:
    raise ValueError(
        "❌ DATABASE_URL chưa được thiết lập!\n"
        "Vui lòng tạo file .env trong thư mục gốc với nội dung:\n"
        "DATABASE_URL=postgresql+psycopg2://user:password@host:port/dbname"
    )

# ---------------------------------------------------------
# 2. Tạo engine kết nối PostgreSQL
# ---------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # kiểm tra kết nối tự động, tránh lỗi timeout
    echo=True             # Bật log SQL để debug (có thể tắt khi deploy)
)

# ---------------------------------------------------------
# 3. Tạo Session để thao tác database
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ---------------------------------------------------------
# 4. Base class để các model kế thừa
# ---------------------------------------------------------

Base = declarative_base()

# ---------------------------------------------------------
# 5. Dependency cho FastAPI để lấy session DB
# ---------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
