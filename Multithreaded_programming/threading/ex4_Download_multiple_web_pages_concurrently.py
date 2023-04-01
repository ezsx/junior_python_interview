import threading
import requests
import os

urls = [
    "https://example.com/file1.txt",
    "https://example.com/file2.txt",
    "https://example.com/file3.txt",
    "https://example.com/file4.txt",
    "https://example.com/file5.txt",

]


def download_url(url):
    # Download the content of the URL using the requests library
    response = requests.get(url)
    # Save the content to a file (you can use the URL's last part as the filename)
    filename = os.path.basename(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Create a list to store the threads
threads = []

# Iterate through the URLs, create a thread for each one, and start it
for url in urls:
    # Create a new thread and pass the download_url function and the URL as arguments
    cur_thread = threading.Thread(target=download_url, args=url)
    # Add the thread to the threads list and start it
    threads.append(cur_thread)
# Iterate through the threads list and call join() on each thread

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
