# Netmiko functions

from netmiko import ConnectHandler
from config import DEVICES

def run_command(device_name, command):
    device = DEVICES.get(device_name)

    if not device:
        return "Device not found"

    try:
        connection = ConnectHandler(**device)
        output = connection.send_command(command)
        connection.disconnect()
        return output
    except Exception as e:
        return str(e)