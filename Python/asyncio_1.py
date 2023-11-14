"""
    + 談到coroutine的時候，可能有兩種東西
	+ coroutine function
		+ 以`async def`定義的函數
		+ 不是返回值，而是返回coroutine object
	+ coroutine object
 
    這個程式碼是用來說明 coroutine function 的概念
    若執行這個程式碼，會發現沒有任何輸出，並且會跳出警告訊息
    警告訊息如下:
    RuntimeWarning: coroutine 'main' was never awaited
    原因：main() 是一個 coroutine function，不是 coroutine object
    所以必須要用 await 來執行 coroutine function

"""
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1) # await is a coroutine
    print('... World!')
    
coro = main() # <- 返回一個 coroutine 物件，不會執行 main() 內的程式碼

