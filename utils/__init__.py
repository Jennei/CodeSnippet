#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      __init__.py.py 
@time:      2018/09/23 
""" 

import logging


formatter = logging.Formatter('%(asctime)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
