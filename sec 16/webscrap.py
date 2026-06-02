''' 
https://docs.langchain.com/oss/python/deepagents/overview

https://docs.langchain.com/oss/python/deepagents/quickstart

https://docs.langchain.com/oss/python/deepagents/models

'''
'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. 
These tasks are I/O-bound because they spend a lot of time waiting for responses from servers. 
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.

'''

import requests  
from bs4 import BeautifulSoup
import threading 


urls = [
    'https://docs.langchain.com/oss/python/deepagents/overview',  
    'https://docs.langchain.com/oss/python/deepagents/quickstart',
    'https://docs.langchain.com/oss/python/deepagents/models'
]


def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched  {len(soup.text)} characters from {url}")

fetch_url(urls[0])
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
