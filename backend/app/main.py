from fastapi import FastAPI
from app.api.config import router as config_router
from app.core.dmx_input import startup_listeners
from app.api.websocket import router as ws_router

app = FastAPI()
app.include_router(config_router, prefix="/api/config")
app.include_router(ws_router)

@app.on_event("startup")
async def on_startup():
    await startup_listeners()

@app.get("/")
async def root():
    return {"message": "DMX-Zigbee Bridge API"}
