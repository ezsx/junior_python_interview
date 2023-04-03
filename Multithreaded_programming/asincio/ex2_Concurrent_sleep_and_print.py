import asyncio

async def sleep_and_print(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    tasks = [
        sleep_and_print(1, "Hello, Alice!"),
        sleep_and_print(2, "Hello, Bob!"),
        sleep_and_print(3, "Hello, Charlie!")
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
