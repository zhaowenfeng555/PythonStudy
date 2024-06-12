# encoding: utf-8
# @author: fengr358
# @time: 2024/6/13 1:22
# @desc:  53  https://leetcode.cn/problems/maximum-subarray/description/

# 给你一个整数数组
# nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组
# 是数组中的一个连续部分。
#
# 输入：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6
# 解释：连续子数组[4, -1, 2, 1]的和最大，为6 。
#
# 输入：nums = [1]
# 输出：1
#
# 输入：nums = [5, 4, -1, 7, 8]
# 输出：23


class Solution:
    def maxSubArray(self, nums) -> int:
        pre, max_sum = 0, nums[0]
        for ele in nums:
            pre = max(pre+ele, ele)
            max_sum = max(max_sum, pre)
        return max_sum

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))