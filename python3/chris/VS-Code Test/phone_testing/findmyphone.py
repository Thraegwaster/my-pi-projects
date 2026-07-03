import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning...")

    devices = await BleakScanner.discover(timeout=5.0)
    
    for device in devices:
        if device.name == "Thraegwaster":
            print(f"The mighty Thraegwaster is here with address {device.address}")

asyncio.run(main())