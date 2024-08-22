
import asyncio
import websockets
import smbus3
import time

# Get I2C bus
bus = smbus3.SMBus(1)


connected_clients = set()

async def read_spi_temp():
        bus.write_i2c_block_data(0x44, 0x2C, [0x06])
        data = bus.read_i2c_block_data(0x44, 0x00, 6)
        temp = data[0] * 256 + data[1]
        cTemp = -45 + (175 * temp / 65535.0)  
        return f"{cTemp:.2f}"


async def handle_client(websocket, path):
        connected_clients.add(websocket)
        while True:
            time.sleep(1)
            websockets.broadcast(connected_clients, await read_spi_temp())
            # await asyncio.gather(*[client.send(await read_spi_temp()) for client in connected_clients])

async def main():
        server = await websockets.serve(handle_client,"0.0.0.0",8765)
        print("Server Start,waiting for communication...")
        await server.wait_closed()

if __name__== "__main__":
        asyncio.run(main())
