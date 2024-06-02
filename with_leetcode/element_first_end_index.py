# encoding: utf-8
# @author: fengr358
# @time: 2021/4/7 22:50
# @desc:

class Solution:

    def get_lower(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                right = mid
        if nums[left] == target:
            return left
        return -1

    def get_high(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 1
            print (str(mid) + ' ' + str(nums[mid]))
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid
        if nums[left] == target:
            return left
        return -1

    def searchRange(self, nums, target: int):
        if nums is None or len(nums) == 0:
            return [-1, -1]
        low = self.get_lower(nums, target)
        if low == -1:
            return [-1, -1]
        else:
            return [low, self.get_high(nums, target)]

nums = [5,7,7,8,8,10]
target = 8

nums = [2, 2]
target = 3

process = Solution().searchRange(nums, target)
print (process)

