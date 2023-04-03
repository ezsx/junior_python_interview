import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://httpbin.org/get", "https://httpbin.org/ip", "https://httpbin.org/uuid"]
    tasks = [fetch(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    for url, content in zip(urls, responses):
        print(f"URL: {url}\nContent: {content[:100]}...\n")

asyncio.run(main())
