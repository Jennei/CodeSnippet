#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      binary_search.py 
@time:      2018/09/22 
"""
from decorates import logtime


@logtime()
def binary_search_loop(s: list, v: int):
    """
    二分查找：
        1.有序集合s中查找v,如果s的中间元素和v相等则返回，
        如果v大于s的中间元素则在s的前半部或者后半部分继续应用前面的规则。
    :param s:
    :param v:
    :return:
    """
    low, high = 0, len(s) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if s[mid] < v:
            low = mid + 1
        elif s[mid] > v:
            high = mid - 1
        else:
            return mid
    return None


#@logtime(number=1)
def binary_search_recursion(s: list, v: int, low: int, high: int):
    if low > high: return None

    mid = int((low + high) / 2)
    if v < s[mid]:
        return binary_search_recursion(s, v, low, mid - 1)
    elif v > s[mid]:
        return binary_search_recursion(s, v, mid + 1, high)
    else:
        return mid


if __name__ == '__main__':
    s = [3, 2, 5, 7, 1, 4, 6, 9, 8, 0]
    s.sort()
    print(binary_search_loop(s, 1))
    print(binary_search_recursion(s, 9, 0, len(s)-1))
    import timeit
    print(timeit.timeit(lambda :binary_search_recursion(s, 9, 0, len(s)-1)))