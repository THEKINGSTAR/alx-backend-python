#!/usr/bin/env python3

import asyncio
import time

async def main():
    
    started = time.time()
    
    print("Took you long time!!")
    task = asyncio.create_task(foo("TASK CREATED BEFORE CALLING FOO AND PRENTING 'Finished'!"))
    #await task
    await foo("Caling Foo")
    print("Finished")
    
    finished = time.time()
    print(f"TOOK THE PROGRAM TO RUN {finished - started}")


async def foo(text):
    await asyncio.sleep(1)
    print(text)
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
