#example of getting the current task from the main coroutine
import asyncio 
import time

# define amain coroutine
async def main():
    # report a massage
    print('main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its detals
    print(task)

# start the asyncio program 
asyncio.run(main())

