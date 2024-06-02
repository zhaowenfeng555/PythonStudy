# encoding: utf-8
# @author: fengr358
# @time: 2021/5/18 0:05
# @desc:

# [5, 2, 3] aim = 20  4*5 = 20 所以最少4张
# dp[i][j]  在可以任意使用nums[0...i] 货币的情况下，组成j所需的最小张数。
# dp[i][j] = min{dp[i-1][j], dp[i][j-arr[i]] + 1}

import numpy
class Solution:
    def __init__(self):
        pass

    def process(self, nums, target):
        if nums is None or target < 0:
            return -1

        dp = [[float('inf')] * (target+1) for _ in range(len(nums))]
        print (numpy.array(dp).shape)
        # 初始化：
        for i in range(target + 1):
            if i * nums[0] <= target:
                dp[0][i * int(nums[0])] = i

        for i in range(1, len(nums)):
            for j in range(target + 1):
                left = float('inf')
                if j - nums[i] >= 0:
                    left = dp[i][j-nums[i]]
                dp[i][j] = min(dp[i-1][j], left + 1)
        return dp[len(nums)-1][target] if dp[len(nums)-1][target] != float('inf') else 0


    def process_update(self, nums, target):
        if nums is None or target < 0:
            return -1

        dp = [float('inf')] * (target+1)
        # 初始化：
        for i in range(target + 1):
            if i * nums[0] <= target:
                dp[i * int(nums[0])] = i

        for i in range(1, len(nums)):
            for j in range(target + 1):
                left = float('inf')
                if j - nums[i] >= 0:
                    left = dp[j-nums[i]]
                dp[j] = min(dp[j], left + 1)
        return dp[target] if dp[target] != float('inf') else 0

result = Solution().process_update([5, 2, 3], 20)
print (result)
