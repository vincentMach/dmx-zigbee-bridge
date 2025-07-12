import json
import paho.mqtt.publish as publish
from ola.ClientWrapper import ClientWrapper

MQTT_HOST = "localhost"
CONFIG_PATH = "config.json"

with open(CONFIG_PATH) as f:
    dmx_map = json.load(f)

def dmx_callback(data):
    updates = {}
    for ch, val in enumerate(data):
        ch_str = str(ch + 1)
        if ch_str in dmx_map:
            device = dmx_map[ch_str]["device"]
            action = dmx_map[ch_str]["action"]
            if device not in updates:
                updates[device] = {}
            if action == "state":
                updates[device][action] = "ON" if val > 10 else "OFF"
            elif action.startswith("color_"):
                if "color" not in updates[device]:
                    updates[device]["color"] = {}
                updates[device]["color"][action[-1]] = val
            else:
                updates[device][action] = val

    for device, payload in updates.items():
        topic = f"zigbee2mqtt/{device}/set"
        publish.single(topic, payload=json.dumps(payload), hostname=MQTT_HOST)

wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(1, client.REGISTER, dmx_callback)
wrapper.Run()
