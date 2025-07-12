import asyncio
from app.listeners.artnet_listener import start_artnet_listener
from app.listeners.sacn_listener import start_sacn_listener
from app.api.websocket import broadcast_dmx

async def callback_factory(protocol):
    async def cb(universe, dmx_data):
        await broadcast_dmx({"protocol": protocol, "universe": universe, "channels": list(dmx_data)})
    return cb

async def startup_listeners():
    await asyncio.gather(
        start_artnet_listener(await callback_factory("artnet")),
        start_sacn_listener(await callback_factory("sacn")),
    )
