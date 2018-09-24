#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      parallel_fibonacci.py 
@time:      2018/09/23 
"""
import time
import threading
import queue

from utils import logger
from fibonacci import fibonacci


shared_queue = queue.Queue()
queue_condition = threading.Condition()
fibo_dict = {}
input_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def fibonacci_task(condition):
    with condition:
        if shared_queue.empty():
            logger.info("[%s] - waiting for elements in queue.." % threading.current_thread().name)
        condition.wait_for(lambda :not shared_queue.empty())
        value = shared_queue.get()
        fibo_dict[value] = fibonacci(value)
        logger.debug(
            "[%s] fibonacci of key [%d] with result [%d]" % (
                threading.current_thread().name, value, fibo_dict[value]))
        shared_queue.task_done()


def queue_task(condition):
    logger.debug('Starting queue_task...')
    with condition:
        for item in input_list:
            shared_queue.put(item)

        logger.debug("Notifying fibonacci_task threads that the queue is ready to consume..")
        condition.notifyAll()


if __name__ == '__main__':
    t1 = time.process_time()
    threads = [threading.Thread(daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in range(len(input_list))]
    [thread.start() for thread in threads]
    prod = threading.Thread(name='queue_task_thread', target=queue_task, args=(queue_condition,), daemon=True)
    prod.start()
    prod.join()
    [thread.join() for thread in threads]
    t2 = time.process_time()
    logger.debug(fibo_dict)
    logger.debug(f"take {t2-t1}s")

