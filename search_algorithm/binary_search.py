#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      binary_search.py 
@time:      2018/09/22 
"""


def binary_search_loop(s: list, v: str):
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


def binary_search_recursion(s: list, v: str, low: int, high: int):
    if low > high: return None

    mid = int((low + high) / 2)
    if v < s[mid]:
        return binary_search_recursion(s, v, low, mid - 1)
    elif v > s[mid]:
        return binary_search_recursion(s, v, mid + 1, high)
    else:
        return mid


if __name__ == '__main__':
    import timeit

    t1 = timeit.Timer('binary_search_recursion([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 0, 10)', 'from __main__ import binary_search_recursion')
    t2 = timeit.Timer('binary_search_loop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)', 'from __main__ import binary_search_loop')
    print(f"recursive:{t1.timeit()}")
    print(f"loop:{t2.timeit()}")
