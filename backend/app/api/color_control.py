from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChannelConfig(BaseModel):
    channel: int
    scale_min: float = 0.0
    scale_max: float = 1.0
    filter_curve: str = "linear"

channel_configs = {}

@router.post("/channel", response_model=ChannelConfig)
async def set_channel(cfg: ChannelConfig):
    channel_configs[cfg.channel] = cfg
    return cfg

@router.get("/channel/{channel}", response_model=ChannelConfig)
async def get_channel(channel: int):
    return channel_configs.get(channel)
