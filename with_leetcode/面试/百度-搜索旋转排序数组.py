# encoding: utf-8
# @author: fengr358
# @time: 2024/6/13 1:20
# @desc:# encoding: utf-8
# # @author: fengr358
# # @time: 2024/6/13 1:16
# # @desc: leetcode 33   https://leetcode.cn/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums, target) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if nums[0] <= nums[mid]:
            #     if nums[0] <= target < nums[mid]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else:
            #     if nums[mid] < target <= nums[len(nums) - 1]:
            #         l = mid + 1
            #     else:
            #         r = mid - 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1


print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))

# nums = [4,5,6,7,0,1,2], target = 0, 输出4
# nums = [4,5,6,7,0,1,2], target = 3, 输出-1
# nums = [1], target = 0, 输出-1