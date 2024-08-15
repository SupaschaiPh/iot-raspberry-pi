from temp import ReadChannel,CalcTempMCPDegC
import asyncio
import websockets
# Cancel Not Use Anymore

async def readTempToServer(websocket):
        while True:
                await websocket.send(str(CalcTempMCPDegC(ReadChannel(1))[2]))
                await asyncio.sleep(1)

async def communicate():
        uri = "ws://2ac26287329fd0.lhr.life"
        async with websockets.connect(uri) as websocket:
               while True:
                    await asyncio.gather(readTempToServer(websocket))
                    await asyncio.sleep(1)


if __name__== "__main__":
        asyncio.run(communicate())
