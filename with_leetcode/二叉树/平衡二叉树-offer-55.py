# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 21:40
# @desc:
# 平衡二叉树
# 思路：两种思路，自顶向下递归 和 自下向上递归
# 自顶向下：时间O(n^2), 空间：O(n)
# 自下向上：时间O(n), 空间O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    #     # 自顶向下递归
    #     def height(node):
    #         if node is None:
    #             return 0
    #         return max(height(node.left), height(node.right)) + 1

    #     if root is None:
    #         return True
    #     return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        # 自下向上
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1

        if root is None:
            return True
        return height(root) >= 0
