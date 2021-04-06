# encoding: utf-8
# @author: fengr358
# @time: 2021/4/4 10:54
# @desc: 最长子序列

class Solution:

    def get_dp(self, nums):
        dp = []
        n = len(nums)
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    def get_result(self, nums, dp):
        n = len(nums)
        result_len = 0
        index = 0
        for i in range(n):
            if dp[i] > result_len:
                result_len = dp[i]
                index = i
        result = [1] * result_len
        result_len -= 1
        result[result_len] = nums[index]

        for i in range(index-1, -1, -1):
            if nums[i] < nums[index] and dp[i] + 1 == dp[index]:
                index = i
                result_len -= 1
                result[result_len] = nums[i]
        return result

    def lengthOfLIS(self, nums) -> int:
        dp = self.get_dp(nums)

        result = self.get_result(nums, dp)
        print (dp)
        print (result)
        return max(dp)


re = Solution().lengthOfLIS([2, 1, 5, 3, 6, 4, 8, 9, 7])
print (re)



