"""
    運行 coroutine 程式需要滿足兩個條件
    + 1: 進入 async 模式(event loop)
        + 正常模式叫做 synchronize 模式
        + 適用一個入口函數`asyncio.run()`
    + 2: 把 coroutine 變成 task

"""
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1) # await is a coroutine
    print('... World!')
    
coro = main() 

asyncio.run(coro) # <- 這樣才會執行 main() 內的程式碼

