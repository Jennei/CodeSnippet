#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      bubble_sort.py 
@time:      2018/09/27 
""" 

def bubble_sort(l:list):
    for cursor1 in range(len(l)):
        for cursor2 in range(cursor1 + 1, len(l)):
            if l[cursor1] > l[cursor2]:
                l[cursor1], l[cursor2] = l[cursor2], l[cursor1]

if __name__ == '__main__':
    s = [3, 2, 5, 7, 1, 4, 6, 9, 8, 0]
    bubble_sort(s)
    print(s)