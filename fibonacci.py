#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      fibonacci.py 
@time:      2018/09/23 
"""
import time

from utils import logger


def fibonacci(n):
    """
    F ( n ) = {
                0, if n = 0;
                1 , if n = 1;
                F ( n -1) + F ( n -2) if n >1;
            }
    :param n:
    :return:
    """
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


if __name__ == '__main__':
    t1 = time.process_time()
    logger.debug(list(map(fibonacci, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    t2 = time.process_time()
    logger.debug(f'take {t2-t1}s')
