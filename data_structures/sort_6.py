# encoding: utf-8
# @author: fengr358
# @time: 2021/3/7 14:28
# @desc: python数据结构，排序算法整理

import numpy as np
import math
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def main(self, arr):
        # 异常判断
        if arr is None or len(arr) <= 0:
            return
        self.bubble_sort(arr)
        # self.bubble_sort_update(arr)
        # self.select_sort(arr)
        # self.insert_sort(arr)
        # self.shell_sort(arr)
        # self.merge_sort(arr)
        # self.quick_sort(arr)
        print ('result is ',)
        print (arr)

    def bubble_sort(self, arr):
        ## 冒泡排序，相邻比较
        # for i in range(0, len(arr)-1):
        #     for j in range(i):
        #         if arr[j] > arr[j+1]:
        #             arr[j], arr[j+1] = arr[j+1], arr[j]
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


    def bubble_sort_update(self, arr):
        # 如果没有交换，则早停
        exchang = True
        i = len(arr) -1
        while i > 0 and exchang:
            j = 0
            exchang = False
            while j < i:
                if arr[j] > arr[j+1]:
                    exchang = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def select_sort(self, arr):
        # 先选择， 再交换
        for i in range(len(arr)-1, 0, -1):
            max_index = i
            for j in range(0, i):
                if arr[max_index] < arr[j]:
                    max_index = j
            if max_index != j:
                arr[i], arr[max_index] = arr[max_index], arr[i]

    def insert_sort(self, arr):
        # 有插入的过程
        for i in range(1, len(arr)):
            j = i - 1
            current_element = arr[i]
            while j >= 0 and current_element < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current_element

    def shell_sort(self, arr):
        # 递减增量排序
        def gap_insert_sort(arr, start, gap):
            for i in range(start+gap, len(arr), gap):
                current_element = arr[i]
                j = i - gap
                while j >= 0 and current_element < arr[j]:
                    arr[j+gap] = arr[j]
                    j -= gap
                arr[j+gap] = current_element

        sublist_count = len(arr) // 2
        while sublist_count > 0:
            for start in range(sublist_count):
                gap_insert_sort(arr, start, sublist_count)
            sublist_count = sublist_count // 2

    def merge_sort(self, arr):
        print ('Split ** ', arr)
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[0: mid]
            right_half = arr[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
            print ('Merge', arr)

    def quick_sort(self, arr):
        def get_partition(arr, start, end):
            mark = start
            start = start + 1
            done = False
            while not done:
                while start <= end and arr[start] <= arr[mark]:
                    start += 1
                while start <= end and arr[end] >= arr[mark]:
                    end -= 1
                if start < end:
                    arr[start], arr[end] = arr[end], arr[start]
                    start += 1
                    end -= 1
                else:
                    done = True
            arr[mark], arr[end] = arr[end], arr[mark]
            return end
        def quick_sort_help(arr, start, end):
            if start < end:
                partition = get_partition(arr, start, end)
                quick_sort_help(arr, start, partition-1)
                quick_sort_help(arr, partition+1, end)

        quick_sort_help(arr, 0, len(arr)-1)

solution = Solution()
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
solution.main(arr)



