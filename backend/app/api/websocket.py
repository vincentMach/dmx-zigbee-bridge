from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()
clients = []

@router.websocket("/ws/dmx")
async def websocket_dmx(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        clients.remove(ws)

async def broadcast_dmx(data):
    for ws in clients:
        await ws.send_json(data)
