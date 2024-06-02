# encoding: utf-8
# @author: fengr358
# @time: 2021/5/15 14:10
# @desc:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return None
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

# [4,5,6,7,0,1,2]
# [0,1,2,4,5,6,7]
# [3,1,2]