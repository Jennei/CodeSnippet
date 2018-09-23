#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      log_time.py 
@time:      2018/09/22 
""" 

from timeit import timeit
import functools


def logtime(number=1000000):
    def wrap(func):
        @functools.wraps(func)
        def inner_wrap(*args, **kwargs):
            t1 = timeit(lambda :func(*args, **kwargs), number=number)
            print(f"{func.__name__} run {number} times take {t1}s.")
            return func(*args, **kwargs)
        return inner_wrap
    return wrap