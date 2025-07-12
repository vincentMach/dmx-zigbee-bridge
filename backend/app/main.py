from fastapi import FastAPI
from app.api.config import router as config_router
from app.api.scenes import router as scenes_router
from app.api.devices import router as devices_router
from app.api.color_control import router as color_router
from app.api.websocket import router as ws_router
from app.database import init_db
from app.core.dmx_input import startup_listeners

app = FastAPI(title="DMX-to-Zigbee Bridge API")

app.include_router(config_router, prefix="/api/config", tags=["config"])
app.include_router(scenes_router, prefix="/api/scenes", tags=["scenes"])
app.include_router(devices_router, prefix="/api/devices", tags=["devices"])
app.include_router(color_router, prefix="/api/color_control", tags=["color_control"])
app.include_router(ws_router)

@app.on_event("startup")
async def on_startup():
    init_db()
    await startup_listeners()

@app.get("/")
async def root():
    return {"message": "DMX-to-Zigbee Bridge API"}
