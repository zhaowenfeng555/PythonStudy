# encoding: utf-8
# @author: fengr358
# @time: 2021/5/12 21:39
# @desc:


# 第三种， 二叉树格式的：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rob_base(self, nums) -> int:
        if nums is None:
            return None

        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            first, second = second, max(first + nums[index], second)
        return second

    def rob_continuation(nums):
        def rob_sub(start, end):
            if start > end:
                return 0
            if start == end:
                return nums[start]
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for index in range(start + 2, end + 1):
                first, second = second, max(first + nums[index], second)
            return second

        if nums is None:
            return None

        if len(nums) == 1:
            return nums[0]

        return max(rob_sub(0, len(nums) - 2), rob_sub(1, len(nums) - 1))

    def rob_binary_tree(self, root: TreeNode) -> int:
        f = {}
        g = {}

        def dfs(node):
            if node is None:
                return None

            dfs(node.left)
            dfs(node.right)

            f[node] = g.get(node.left, 0) + g.get(node.right, 0) + node.val
            g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + \
                      max(f.get(node.right, 0), g.get(node.right, 0))

        if root is None:
            return None
        dfs(root)
        return max(f.get(root, 0), g.get(root, 0))