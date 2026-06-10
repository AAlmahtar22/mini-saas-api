from fastapi import FastAPI
from app.routers.tasks import router as tasks_router
from app.db.database import Base, engine
from app.routers import auth

tags_metadata = [
    #{"name": "Home", "description": "Health check / root endpoint"},
    {"name": "Authentication", "description": "Authentication endpoints"},
    {"name": "Tasks", "description": "Task management endpoints"}
]

app = FastAPI(
    openapi_tags=tags_metadata
)


app.include_router(tasks_router)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

#@app.get("/", tags=["Home"])
#def home():
   # return {"message": "Running"}