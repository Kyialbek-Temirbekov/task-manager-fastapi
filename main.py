from fastapi import FastAPI, Depends

from app.api.routers import users, tasks
from sqlalchemy.orm import Session
from app.db.database import engine, Base

from app.db.database import get_db

async def lifespan_handler(app):
    # Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan_handler)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Welcome to Task Manager API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
