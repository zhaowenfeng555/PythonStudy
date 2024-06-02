# encoding: utf-8
# @author: fengr358
# @time: 2021/5/15 0:38
# @desc:

class Solution:

    def get_lower(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def get_high(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def searchRange(self, nums, target: int):
        if nums is None or len(nums) == 0:
            return [-1, -1]
        low, high = self.get_lower(nums, target), self.get_high(nums, target)
        if low <= high:
            return [low, high]
        else:
            return [-1, -1]


    # def get_lower(self, nums, target):
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + ((right - left) >> 1)
    #         if target <= nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     if left < len(nums) and nums[left] == target:
    #         return left
    #     return -1
    #
    # def get_high(self, nums, target):
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + ((right - left) >> 1)
    #         if target < nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     if right < len(nums) and nums[right] == target:
    #         return right
    #     return -1
    #
    # def searchRange(self, nums, target: int):
    #     if nums is None or len(nums) == 0:
    #         return [-1, -1]
    #     low = self.get_lower(nums, target)
    #     if low == -1:
    #         return [-1, -1]
    #     else:
    #         return [low, self.get_high(nums, target)]

res = Solution().searchRange([5,7,7,8,8,10], 8)
print (res)