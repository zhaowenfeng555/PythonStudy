# encoding: utf-8
# @author: fengr358
# @time: 2021/5/22 22:27
# @desc:
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # 层次遍历， 使用deque
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root is None:
            return result

        queue = collections.deque()

        queue.append(root)
        while queue:
            num = len(queue)
            list_node_tmp = []
            while num > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                list_node_tmp.append(node.val)
                num -= 1
            result.append(list_node_tmp)
        result.reverse()
        return result

    # 层次遍历， 只使用数组
    def levelOrderBottom(self, root: TreeNode) -> int:
        list_node = []
        list_node.append(root)
        head = 0
        tail = 1
        result = 0
        while tail - head > 0:
            result += 1
            len_list_node = tail - head
            while len_list_node > 0:
                len_list_node -= 1
                current = list_node[head]
                head += 1
                if current.left:
                    tail += 1
                    list_node.append(current.left)
                if current.right:
                    tail += 1
                    list_node.append(current.right)
        return result