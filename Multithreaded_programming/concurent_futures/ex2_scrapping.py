import concurrent.futures
import requests
from bs4 import BeautifulSoup

URLS = [
    'https://www.example.com',
    'https://www.example.org',
    'https://www.example.net',
]

def fetch(url):
    response = requests.get(url)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    return title

def fetch_and_parse(url):
    html = fetch(url)
    title = parse(html)
    return title

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(fetch_and_parse, url): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                title = future.result()
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")
            else:
                print(f"{url} has title: {title}")

if __name__ == "__main__":
    main()
