# encoding: utf-8
# @author: fengr358
# @time: 2024/7/4 10:10
# @desc:
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
#
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # #  递归方法
    # def rob(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return self.robtravesal(root)

    # def robtravesal(self, root):
    #     if not root:
    #         return 0
    #     if not root.left and not root.right:
    #         return root.val
    #     # 访问根：
    #     v1 = root.val
    #     if root.left:
    #         v1 += self.robtravesal(root.left.left) + self.robtravesal(root.left.right)
    #     if root.right:
    #         v1 += self.robtravesal(root.right.left) + self.robtravesal(root.right.right)

    #     # 不访问根：
    #     v2 = self.robtravesal(root.left) + self.robtravesal(root.right)
    #     return max(v1, v2)

    # 动态规划

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.robtravesal(root))

    def robtravesal(self, root):  # 不访问， 访问
        if not root:
            return (0, 0)
        if not root.left and not root.right:
            return (0, root.val)
        left = self.robtravesal(root.left)
        right = self.robtravesal(root.right)
        return (max(left) + max(right), root.val + left[0] + right[0])