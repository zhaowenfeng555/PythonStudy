from collections import Counter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None
        self.pre = None
        self.max_pv = float('-inf')
        self.cur_pv = 0
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if not self.pre:
            self.cur_pv = 1
            self.max_pv = 1
            self.result = [root.val]
        else:
            if root.val == self.pre.val:
                self.cur_pv += 1
                if self.cur_pv > self.max_pv:
                    self.max_pv = self.cur_pv
                    self.result = [root.val]
                elif self.cur_pv == self.max_pv:
                    self.result.append(root.val)
            else:
                self.cur_pv = 1

        pre = root
        self.dfs(root.right)

