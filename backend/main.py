from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine, Base

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Partzzo App API",
    description="Backend for Partzzo mobile app",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Partzzo API"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Simple query to check database connection
        db.execute("SELECT 1")
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
