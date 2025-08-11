from fastapi import FastAPI
from app.routers.events import router as events_router

app = FastAPI(title="Global Event Aggregator API")

app.include_router(events_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Global Event Aggregator API"}
