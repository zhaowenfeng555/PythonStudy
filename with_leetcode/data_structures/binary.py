# encoding: utf-8
# @author: fengr358
# @time: 2021/5/13 22:10
# @desc:

import collections
import math
import sys
import numpy as np

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass

    def create_binary(self, list_input):
        def create_binary_sorted(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = create_binary_sorted(nums, start, mid - 1)
            root.right = create_binary_sorted(nums, mid + 1, end)
            return root
        return create_binary_sorted(list_input, 0, len(list_input) - 1)


    def pre_order_recursion(self, head, list_output):
        if head is not None:
            list_output.append(head.val)
            if head.left:
                self.pre_order_recursion(head.left, list_output)
            if head.right:
                self.pre_order_recursion(head.right, list_output)

    def in_order_recursion(self, head, list_output):
        if head is not None:
            if head.left:
                self.in_order_recursion(head.left, list_output)
            list_output.append(head.val)
            if head.right:
                self.in_order_recursion(head.right, list_output)

    def post_order_recursion(self, head, list_output):
        if head is not None:
            if head.left:
                self.post_order_recursion(head.left, list_output)
            if head.right:
                self.post_order_recursion(head.right, list_output)
            list_output.append(head.val)

    def level_order_recursion(self, head, list_output):
        def helper(tree, level):
            if len(list_output) == level:
                list_output.append([])
            list_output[level].append(tree.val)
            if tree.left:
                helper(tree.left, level + 1)
            if tree.right:
                helper(tree.right, level + 1)

        if head is None:
            return None
        helper(head, 0)



    # 非递归
    def pre_order_not(self, head, list_output):
        stack = collections.deque()
        if head is None:
            return None
        stack.append(head)
        while stack:
            p = stack.pop()
            list_output.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

    def in_order_not(self, head, list_output):
        pass

    def post_order_not(self, head, list_output):
        pass

    def level_order_not(self, head, list_output):
        queue = collections.deque()
        if head is None:
            return None

        queue.append(head)
        while queue:
            p = queue.popleft()
            list_output.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

    def pre_order_not_with_array(self, head, list_output):
        pass

    def in_order_not_with_array(self, head, list_output):
        pass

    def post_order_not_with_array(self, head, list_output):
        pass

    def level_order_not_with_array(self, head, list_output):
        array = []
        font, rear = -1, 0
        if head is None:
            return None
        array.append(head)

        while font != rear:
            font += 1
            p = array[font]
            list_output.append(p.val)
            if p.left:
                rear += 1
                array.append(p.left)
            if p.right:
                rear += 1
                array.append(p.right)







solution = Solution()
root = solution.create_binary([-10, -3, 0, 5, 9])
#         0
#     10       5
# null -3   null 9

list_output_pre_recu = []
list_output_in_recu = []
list_output_post_recu = []
list_output_level_recu = []

list_output_pre_not = []
list_output_in_not = []
list_output_post_not = []
list_output_level_not = []

list_output_pre_not_with_array = []
list_output_in_not_with_array = []
list_output_post_not_with_array = []
list_output_level_not_with_array = []



solution.pre_order_recursion(root, list_output_pre_recu)
solution.in_order_recursion(root, list_output_in_recu)
solution.post_order_recursion(root, list_output_post_recu)
solution.level_order_recursion(root, list_output_level_recu)

solution.pre_order_not(root, list_output_pre_not)
solution.in_order_not(root, list_output_in_not)
solution.post_order_not(root, list_output_post_not)
solution.level_order_not(root, list_output_level_not)

solution.pre_order_not_with_array(root, list_output_pre_not_with_array)
solution.in_order_not_with_array(root, list_output_in_not_with_array)
solution.post_order_not_with_array(root, list_output_post_not_with_array)
solution.level_order_not_with_array(root, list_output_level_not_with_array)

print ('深度优先：先序递归遍历：' + str(list_output_pre_recu))
print ('深度优先：中序递归遍历：' + str(list_output_in_recu))
print ('深度优先：后序递归遍历：' + str(list_output_post_recu))
print ('宽度优先：层此递归遍历：' + str(list_output_level_recu))
print ('\n')

print ('深度优先：先序非递归(使用栈)遍历：' + str(list_output_pre_not))
print ('深度优先：中序非递归(使用数组)遍历：' + str(list_output_in_not))
print ('深度优先：后序非递归(使用数组)遍历：' + str(list_output_post_not))
print ('宽度优先：层此非递归(使用数组)遍历：' + str(list_output_level_not))
print ('\n')


print ('深度优先：先序非递归(使用数组)遍历：' + str(list_output_pre_not_with_array))
print ('深度优先：中序非递归(使用数组)遍历：' + str(list_output_in_not_with_array))
print ('深度优先：后序非递归(使用数组)遍历：' + str(list_output_post_not_with_array))
print ('宽度优先：层此非递归(使用数组)遍历：' + str(list_output_level_not_with_array))
print ('\n')



