"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    链接：  https://leetcode.cn/problems/binary-tree-inorder-traversal/

    中
左      右

前序遍历：中，左，右
中序遍历：左，中，右
后序遍历：左，右，中


"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # 二叉树格式
        # stack = deque()
        # result = []
        # if root is None:
        #     return result
        # stack.append(root)
        # while stack:
        #     current = stack.pop()
        #     result.append(current.val)
        #     if current.right:
        #         stack.append(current.right)
        #     if current.left:
        #         stack.append(current.left)
        # return result


        #  N叉树格式
        stack = deque()
        result = []
        if root is None:
            return result
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.children:
                for index in range(len(current.children)-1, -1, -1):
                    stack.append(current.children[index])
        return result



        #  诀绝子方案

        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
                stack, result = [root], []
                while stack:
                    current = stack.pop()
                    if isinstance(current, TreeNode):
                        stack.extend([current.right, current.left, current.val])


                        # stack.extend([current.right, current.left, current.val])  # 先序遍历
                        # stack.extend([current.right, current.val, current.left])  # 中序遍历
                        # stack.extend([current.val, current.right, current.left])  # 后续遍历

                    elif isinstance(current, int):
                        result.append(current)
                return result