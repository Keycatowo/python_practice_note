"""
    把 coroutine 變成 task 的方法：
    + 方法1: 使用 await
        + await 會把 coroutine 變成 task
        + await 會等待 task 執行完畢，才會繼續執行下一行程式碼
        + 會 yield 當前的 task，並且把控制權交給 event loop
    + 在這個範例中，在等待 task1 返回的時候，task2 還不存在
        + task1 完成後，才會建立 task2 並等待
        + 最終會花費 3 秒鐘
"""
import asyncio
import time

async def say_after(delay ,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello') # coroutine 被包裝成 task，並且被排入 event loop。 建立依賴關係————目前的task需要等待say_after(1, 'hello')執行完畢。
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")    

asyncio.run(main())