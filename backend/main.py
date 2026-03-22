# backend/main.py
from fastapi import FastAPI

app = FastAPI(
    title="DefterX Backend",
    description="İleri seviye muhasebe yazılımı backend",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "DefterX backend çalışıyor! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "not connected yet"}