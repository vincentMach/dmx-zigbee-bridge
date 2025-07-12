from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
current_input_source = "dmx"

class InputSourceUpdate(BaseModel):
    source: str  # 'dmx', 'artnet', 'sacn'

@router.post("")
async def set_input_source(update: InputSourceUpdate):
    global current_input_source
    if update.source not in ["dmx", "artnet", "sacn"]:
        return {"error": "Invalid source"}
    current_input_source = update.source
    return {"source": current_input_source}
