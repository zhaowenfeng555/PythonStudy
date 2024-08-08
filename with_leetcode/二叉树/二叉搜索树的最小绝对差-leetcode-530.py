# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 22:28
# @desc:  https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/

# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
# root = [4,2,6,1,3]
#     4
#   2     6
# 1   3
# 输出：1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     stack, result = [], float('+inf')
    #     self.dfs(root, stack)
    #     print(stack)
    #     for i in range(1, len(stack)):
    #         result = min(result, stack[i] - stack[i - 1])
    #     return result

    # def dfs(self, root, stack):
    #     if not root:
    #         return
    #     self.dfs(root.left, stack)
    #     stack.append(root.val)
    #     self.dfs(root.right, stack)

        # if not root:
        #     return 0
        # self.pre, self.result = None, float('+inf')
        # self.dfs(root)
        # return self.result

    # def dfs(self, root):
    #     if not root:
    #         return
    #     self.dfs(root.left)
    #     if not self.pre:
    #         self.pre = root
    #     else:
    #         self.result = min(self.result, root.val - self.pre.val)
    #         self.pre = root
    #     self.dfs(root.right)


        if not root:
            return 0
        stack, result = [root], float('+inf')
        pre = None
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.val, cur.left])
            elif isinstance(cur, int):
                ## 特别注意，这儿如果写成 if not pre会出错，因为not 0 True,会认为 not 0  为True
                if pre is None:
                    pre = cur
                else:
                    result = min(result, cur-pre)
                    pre = cur
        return result