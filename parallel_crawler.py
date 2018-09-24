#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      parallel_crawler.py 
@time:      2018/09/23 
"""

import re
import sys
import threading
import concurrent.futures
import queue

import requests
from tqdm import tqdm

from utils import logger


html_link_regex = re.compile(r'<img\s(?:.*?\s)*?src=[\'"](.*?)[\'"].*?>')
urls = queue.Queue()
urls.put('https://github.com/')
urls.put('https://www.gitee.com/')
urls.put('http://www.imooc.com/')
result_dict = {}


def group_urls_task(urls):
    try:
        url = urls.get(True, 0.05)
        result_dict[url] = None
        logger.info("[%s] putting url [%s] in dictionary..." % (
            threading.current_thread().name, url))
    except queue.Empty:
        logger.error('Nothing to be done, queue is empty')


def crawl_task(url):
    links = []
    try:
        html = requests.get(url)
        logger.info("[%s] crawling url [%s] ..." % (
            threading.current_thread().name, url))
        links = html_link_regex.findall(html.text)
    except:
        logger.error(sys.exc_info()[0])
        raise
    finally:
        return (url, links)


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as group_link_threads:
    for i in range(urls.qsize()):
        group_link_threads.submit(group_urls_task, urls)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as crawler_link_threads:
    future_tasks = {crawler_link_threads.submit(crawl_task, url): url for url in result_dict.keys()}
    done_iter = concurrent.futures.as_completed(future_tasks)
    done_iter = tqdm(done_iter, total=len(result_dict))
    for future in done_iter:
        result_dict[future.result()[0]] = future.result()[1]

if __name__ == '__main__':
    for url, links in result_dict.items():
        logger.info("[%s] with links : %s" % (url, links))