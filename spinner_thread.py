#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      spinner_thread.py 
@time:      2018/09/27 
""" 

import threading
import itertools
import time
import sys
import collections


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\b' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    #write(' ' * len(status) + '\b' * len(status))

def show():
    time.sleep(3)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal), daemon=True)
    print('spinner object:', spinner)
    spinner.start()
    result = show()
    signal.go = False
    spinner.join()
    return result

if __name__ == '__main__':
    result = supervisor()
    print('Answer:', result)
