
import asyncio
import websockets
from temp import ReadChannel,CalcTempMCPDegC


async def readTempToClient(websocket):
        while True:
                await websocket.send(str(CalcTempMCPDegC(ReadChannel(1))[2]))
                await asyncio.sleep(1)

async def echo(websocket, path):
        async for message in websocket:
                print(f"Receive from client : {message}")
                await asyncio.gather(readTempToClient(websocket))#websocket.send(f"{message}"))

async def main():
        server = await websockets.serve(echo,"0.0.0.0",8765)
        print("Server Start,waiting for communication...")
        await server.wait_closed()

if __name__== "__main__":
        asyncio.run(main())
