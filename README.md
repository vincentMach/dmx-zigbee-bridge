# DMX-to-Zigbee Bridge

A real-time bridge to convert DMX signals (via DMX cable, Art-Net, or sACN) into Zigbee commands for wireless smart lighting control.

## Features
- DMX, Art-Net & sACN input
- Real-time WebSocket streaming
- Scene & preset management
- Device discovery & auto-mapping
- Advanced color control & DMX input filtering/scaling

### Running
```bash
docker-compose up --build
```
Frontend on http://localhost:3000, Backend API on http://localhost:8000
