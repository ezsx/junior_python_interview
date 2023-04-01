import threading
import requests
import time
import os

urls = [
    "https://example.com/page1.html",
    "https://example.com/page2.html",
    "https://example.com/page3.html",
    # Add more URLs as needed
]


def download_url_with_rate_limiting(url, rate_limit):
    global last_request_time

    interval = 1 / rate_limit
    elapsed_time = time.time() - last_request_time

    if elapsed_time < interval:
        time.sleep(interval - elapsed_time)

    response = requests.get(url)

    # Save the content to a file or process it as needed
    filename = os.path.basename(url)

    with open(filename, 'wb') as f:
        f.write(response.content)

    last_request_time = time.time()


threads = []
last_request_time = 0
for url in urls:
    # Create a new thread with the download_url_with_rate_limiting function and the URL as arguments
    thread = threading.Thread(target=download_url_with_rate_limiting, args=(url, 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All downloads finished.")
