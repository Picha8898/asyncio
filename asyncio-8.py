#example of runing a blocking io-bound task in asyncio 
import asyncio
import time 

# a blocking io-bound task
def blocking_task():
    #report a message
    print(f'{time.ctime()}Task staring...')
    # block for a while
    time.sleep(2)
    #report a message
    print(f'{time.ctime()} Task done')

#main coroutine
async def main():
    # report a message
    print(f'{time.ctime()} Main running the blocking task')
    # create a coroutine for the blocking task
    coro = asyncio.to_thread(blocking_task)
    # schedule the task
    task = asyncio.create_task(coro)
    #report a massage
    print(f'{time.ctime()} Main doing other things')
    # allow the scheduled task to start
    await asyncio.sleep(0)
    # await the task
    await task

#run the asynio program
asyncio.run(main())
