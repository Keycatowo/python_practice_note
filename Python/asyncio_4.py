"""
    把 coroutine 變成 task 的方法：
    + 方法2: 使用 asyncio.create_task()
        + 當 await 後面已經是一個 task 的時候
            + 就省略了再把 coroutine 變成 task 的步驟
    + 在這個範例中，在等待 task1 返回的時候，會執行 task2
        + 最終只會花費 2 秒鐘
"""
import asyncio
import time

async def say_after(delay ,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )
    
    task2 = asyncio.create_task(
        say_after(2, 'world')
    )
    
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")    

asyncio.run(main())