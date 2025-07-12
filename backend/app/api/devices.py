from fastapi import APIRouter
from app.zigbee.device_manager import discover_devices, get_devices

router = APIRouter()

@router.get("")
async def list_devices():
    return get_devices()

@router.post("/discover")
async def trigger_discovery():
    await discover_devices()
    return {"detail": "Discovery started"}
