#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      singleton.py 
@time:      2018/09/27 
""" 

class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance:
            return self.instance
        else:
            self.instance = self.cls(*args, **kwargs)
            return self.instance


if __name__ == '__main__':
    @Singleton
    class StateManager:
        def __init__(self, name):
            self.name = name

    a = StateManager('A')
    b = StateManager('B')

    print(id(a))
    print(id(b))
    print(a is b)
    print(a.name)
    print(b.name)