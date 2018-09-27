#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      parallel_crawler_rw.py 
@time:      2018/09/24 
"""

import threading
import collections
import multiprocessing

import tqdm


RUNNING, WAITTING, CANCELED, TERMINATING = ('RUNNING', 'WAITTING', 'CANCELED', 'TERMINATING')


class Task:
    def __init__(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    state = multiprocessing.Manager().Value('i', WAITTING)
    print(state.value)
    print(WAITTING == state.value)