# DMX-to-Zigbee Bridge (Raspberry Pi)

Control Zigbee smart lights (via Zigbee2MQTT) using a DMX controller. Includes a web UI to map DMX channels to Zigbee devices and actions.

## Features
- DMX input via RS485 (OLA)
- Output to Zigbee via MQTT (Zigbee2MQTT)
- Web UI to map DMX channels to Zigbee lights and actions
- Supports brightness, on/off, RGB color, etc.

## Requirements
- Raspberry Pi 3/4 with Raspberry Pi OS
- Zigbee USB stick (CC2652, ConBee II, Sonoff ZBDongle, etc.)
- USB RS485 DMX input
- Zigbee2MQTT & OLA installed

## Setup

### 1. Install dependencies
```bash
sudo apt install python3-pip ola mosquitto
pip3 install -r requirements.txt
```

### 2. Start services
```bash
python3 ui.py         # Start web UI at http://<pi_ip>:5000
python3 dmx_bridge.py # Start DMX-to-Zigbee bridge
```

### 3. Configure mapping
Go to `http://<raspberry_pi_ip>:5000`, map DMX channels to Zigbee devices and actions.

## Actions Supported
- `brightness` — 0–255
- `state` — ON/OFF toggle
- `color_r`, `color_g`, `color_b` — RGB control

## Auto-start on boot (optional)
Use the provided systemd units in `systemd/` to auto-start services.
