import asyncio

discovered_devices = []

async def discover_devices():
    await asyncio.sleep(1)
    discovered_devices.clear()
    discovered_devices.extend([
        {"id": "zigbee-1", "name": "Living Room Light"},
        {"id": "zigbee-2", "name": "Kitchen Light"},
    ])

def get_devices():
    return discovered_devices
