# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def generator_tree(self, nums, root):
        # if len(nums) <= 0:
        #     return None

        mid = len(nums) // 2
        root.val = nums[mid]
        print('1....')
        print(root)
        if mid - 1 > 0:
            root.left = TreeNode()
            self.generator_tree(nums[0: mid], root.left)
        print('2....')
        print(root)
        if mid + 1 <= len(nums) - 1:
            root.right = TreeNode()
            self.generator_tree(nums[mid + 1: len(nums)], root.right)
        print('3....')

    def sortedArrayToBST(self, nums):
        root = TreeNode()
        self.generator_tree(nums, root)
        return root

print (Solution().sortedArrayToBST([-10,-3,0,5,9]))