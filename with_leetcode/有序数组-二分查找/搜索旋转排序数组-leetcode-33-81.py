# encoding: utf-8
# @author: fengr358
# @time: 2021/4/27 23:08
# @desc:

# @question: 旋转有序数组，查找给定值
# @answer：


# 找出mid，该索引为 mid =（left + right）/ 2，但是这样写有可能溢出，所以我们需要改进一下写成
#
# mid = left +（right - left）/ 2 或者 left + ((right - left ) >> 1) 两者作用是一样的，都是为了找到两指针的中
#
# 间索引，使用位运算的速度更快。那么此时的 mid = 0 + (8-0) / 2 = 4

class Solution:
    def search_33(self, nums, target: int) -> int:
        if nums is None:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            # mid = (left + right) // 2
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search_81(self, nums, target: int) -> int:
        if nums is None:
            return None
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

print (Solution().search_33([4,5,6,7,0,1,2], 0))
print (Solution().search_81([4,4,5,6,7,0,0,1,2], 0))