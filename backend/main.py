from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/submit", response_model=schemas.Content)
async def submit(content: schemas.ContentBase, db: Session = Depends(get_db)):
    return crud.create_content(db=db, content=content)