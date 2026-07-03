import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning...")

    devices = await BleakScanner.discover(return_adv=True, timeout=5.0)

    for address,(device,adv) in devices.items():
        print(
            f"properties: {dir(device)}"
        )

asyncio.run(main())