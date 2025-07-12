import asyncio, struct

SACN_PORT = 5568

class SACNProtocol(asyncio.DatagramProtocol):
    def __init__(self, callback): self.callback = callback
    def datagram_received(self, data, addr):
        if len(data)<126: return
        root=struct.unpack('>I', data[18:22])[0]
        if root!=0x00000004: return
        universe=struct.unpack('>H', data[113:115])[0]
        idx=38
        length=struct.unpack('>H', data[idx+1:idx+3])[0]-1
        dmx_data=data[idx+3:idx+3+length]
        asyncio.create_task(self.callback(universe, dmx_data))

async def start_sacn_listener(callback):
    loop = asyncio.get_running_loop()
    await loop.create_datagram_endpoint(lambda: SACNProtocol(callback),
                                        local_addr=('0.0.0.0', SACN_PORT))
    print(f"sACN listening on {SACN_PORT}")
