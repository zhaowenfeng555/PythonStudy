# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 22:28
# @desc:

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        # elif root.left is None and root.right is None:
        #     return 1
        # else:
        #     return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        result = 0

        while(len(queue)):
            # 该层有多少个数据
            number_level = len(queue)
            while number_level > 0:
                number_level -= 1
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result += 1
        return result