#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      merge_sort.py 
@time:      2018/09/22 
"""


def merge(a: list, b: list):
    """
    两个有序数组排序：
        1.同时比较两个数组的首个元素，将较小的元素放到空集合，同时指针后移。
        2.回到第一步，直到两个数组中的一个，元素已经比较完毕，这时将另一个数组剩余元素之间添加到结果集合尾部。
    :param a:
    :param b:
    :return:
    """
    sorted_items = []
    cursor_left = cursor_right = 0
    len_a = len(a)
    len_b = len(b)

    while cursor_left < len_a and cursor_right < len_b:
        if a[cursor_left] < b[cursor_right]:
            sorted_items.append(a[cursor_left])
            cursor_left += 1
        else:
            sorted_items.append(b[cursor_right])
            cursor_right += 1

    if cursor_left == len_a:
        sorted_items.extend(b[cursor_right:])
    else:
        sorted_items.extend(a[cursor_left:])

    return sorted_items


def merge_sort(s: list):
    """
    归并排序：
        分治法(The divide and conquer technique),将无序集合递归分解为直到可以处理的最小单位，然后合并。
    :param s:
    :return:
    """
    if not isinstance(s, list): raise TypeError('s should be a list type.')
    len_s = len(s)
    middle = int(len_s / 2)
    if len_s <= 1: return s
    sorted_left = merge_sort(s[:middle])
    sorted_right = merge_sort(s[middle:])
    return merge(sorted_left, sorted_right)


if __name__ == '__main__':
    s = [3, 2, 5, 7, 1, 4, 6, 9, 8, 0]
    print(merge_sort(s))
