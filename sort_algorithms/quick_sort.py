#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      quick_sort.py 
@time:      2018/09/23 
"""


def partition(s: list, low: int, high: int):
    """
    将小于基准的放在数组左边，大于基准的放在数组右边,创建出基准两边的数组。
    """
    x = s[high]
    left_arr_last_index = low - 1

    for right_arr_cursor in range(low, high):
        if s[right_arr_cursor] <= x:
            left_arr_last_index += 1
            s[left_arr_last_index], s[right_arr_cursor] = s[right_arr_cursor], s[left_arr_last_index]  # 往左边数组append一个元素

    s[left_arr_last_index + 1], s[high] = s[high], s[left_arr_last_index + 1]

    return left_arr_last_index + 1


def quick_sort(s: list, low: int, high: int):
    """
    分治策略：
        1.选取数列中最后一个数字，作为排序基准，以基准分成两个数组，将数列中比基准小的放在左边数组，比基准大的放在右边数组。
        2.重复1
    """
    if low < high:
        base_index = partition(s, low, high)
        quick_sort(s, low, base_index - 1)
        quick_sort(s, base_index + 1, high)


if __name__ == '__main__':
    s = [3, 2, 5, 7, 1, 4, 6, 9, 8, 0]
    quick_sort(s, 0, len(s)-1)
    print(s)
