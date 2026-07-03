
import asyncio
from bleak import BleakScanner

IPHONE_NAME = "Thraegwaster"

async def main():
    print("Scanning for Bluetooth devices...")

    devices = await BleakScanner.discover(timeout=5.0)

    for device in devices:
        print(f"Name: {device.name}, Address: {device.address}")

        if device.name == IPHONE_NAME:
            print(f"\n✅ {IPHONE_NAME} is nearby")
            return

    print(f"\n❌ {IPHONE_NAME} was not detected")

asyncio.run(main())
