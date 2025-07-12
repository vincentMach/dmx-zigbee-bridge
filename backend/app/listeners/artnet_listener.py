import asyncio, struct

ARTNET_PORT = 6454
ARTNET_HEADER = b"Art-Net\x00"
OP_DMX = 0x5000

class ArtNetProtocol(asyncio.DatagramProtocol):
    def __init__(self, callback):
        self.callback = callback
    def datagram_received(self, data, addr):
        if not data.startswith(ARTNET_HEADER): return
        if struct.unpack('<H', data[8:10])[0] != OP_DMX: return
        universe = struct.unpack('<H', data[14:16])[0]
        length = struct.unpack('>H', data[16:18])[0]
        dmx = data[18:18+length]
        asyncio.create_task(self.callback(universe, dmx))

async def start_artnet_listener(callback):
    loop = asyncio.get_running_loop()
    await loop.create_datagram_endpoint(lambda: ArtNetProtocol(callback), local_addr=('0.0.0.0', ARTNET_PORT))
    print(f"Art-Net listening on {ARTNET_PORT}")
