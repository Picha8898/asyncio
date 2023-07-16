# example of starting many task and getting access to all tasks
import asyncio
import time

# corotine for a task
async def task_coroutine(value):
    # report a message
    print(f'{time.ctime()} task {value} is running')
    # block for a moment 
    await asyncio.sleep(1)

# definea main coroutine
async def main():
    # report a message
    print(f'{time.ctime()} main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # allow some of the tasks time to start
    await asyncio.sleep()
    # get all tasks
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')
    # wait for all tasks to complete
    for task in started_tasks:
        await task

# start the asyncio program
asyncio.run(main())