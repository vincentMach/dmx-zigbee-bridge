import asyncio
from app.listeners.artnet_listener import start_artnet_listener
from app.listeners.sacn_listener import start_sacn_listener
from app.api.websocket import broadcast_dmx

async def dmx_data_callback(protocol, universe, data):
    await broadcast_dmx({"protocol": protocol, "universe": universe, "channels": list(data)})

async def startup_listeners():
    await asyncio.gather(
        start_artnet_listener(lambda u,d: dmx_data_callback("artnet", u, d)),
        start_sacn_listener(lambda u,d: dmx_data_callback("sacn", u, d)),
    )
