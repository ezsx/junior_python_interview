import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def extract_titles(url):
    content = await fetch(url)
    soup = BeautifulSoup(content, "html.parser")
    titles = [title.text for title in soup.select(".title > a")]
    return titles


async def main():
    urls = ["https://news.ycombinator.com", "https://news.ycombinator.com/news?p=2"]
    tasks = [extract_titles(url) for url in urls]
    all_titles = await asyncio.gather(*tasks)

    for url, titles in zip(urls, all_titles):
        print(f"URL: {url}\nTitles:")
        for title in titles:
            print(f"- {title}")
            print()


asyncio.run(main())
