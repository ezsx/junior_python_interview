import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def scrape(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(url, session)
        soup = BeautifulSoup(html, 'html.parser')
        # Add your code here to parse the content and extract the desired information
        title = soup.find('title').text.strip()
        description = soup.find('meta', attrs={'name': 'description'})['content']
        main_image_url = soup.find('meta', attrs={'property': 'og:image'})['content']
        author = soup.find('span', attrs={'class': 'author'}).text.strip()
        # Print the extracted information
        print('Title:', title)
        print('Description:', description)
        print('Main image URL:', main_image_url)
        print('Author:', author)

async def main():
    urls = [
        'https://example.com/page1',
        'https://example.com/page2',
        'https://example.com/page3',
    ]

    tasks = [scrape(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
