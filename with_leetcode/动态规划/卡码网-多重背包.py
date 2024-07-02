# encoding: utf-8
# @author: fengr358
# @time: 2024/7/3 0:51
# @desc:

# 你是一名宇航员，即将前往一个遥远的行星。在这个行星上，有许多不同类型的矿石资源，每种矿石都有不同的重要性和价值。你需要选择哪些矿石带回地球，但你的宇航舱有一定的容量限制。
# 给定一个宇航舱，最大容量为 C。现在有 N 种不同类型的矿石，每种矿石有一个重量 w[i]，一个价值 v[i]，以及最多 k[i] 个可用。不同类型的矿石在地球上的市场价值不同。你需要计算如何在不超过宇航舱容量的情况下，最大化你所能获取的总价值。
#
# 输入共包括四行，第一行包含两个整数 C 和 N，分别表示宇航舱的容量和矿石的种类数量。
# 接下来的三行，每行包含 N 个正整数。具体如下：
# 第二行包含 N 个整数，表示 N 种矿石的重量。
# 第三行包含 N 个整数，表示 N 种矿石的价格。
# 第四行包含 N 个整数，表示 N 种矿石的可用数量上限。


class Solution(object):
    def beibao_duochong(self, bagweight, length, weights, values, uses):
        if bagweight < 0 or length < 0 or not weights or not values or not uses:
            return 0
        dp = [0] * (bagweight + 1)
        for i in range(length):
            for j in range(bagweight, weights[i] - 1, -1):
                for k in range(1, min(uses[i], j // weights[i]) + 1):
                    dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])
        print(dp)
        return dp[-1]

C, N = 10, 3
weights = [1, 3, 4]
values = [15, 20, 30]
uses = [2, 3, 2]
# uses = [2, 0, 0]
print(Solution().beibao_duochong(C, N, weights, values, uses))  # 90


## ## 标准答案
# C, N = input().split(" ")
# C, N = int(C), int(N)
#
# # value数组需要判断一下非空不然过不了
# weights = [int(x) for x in input().split(" ")]
# values = [int(x) for x in input().split(" ") if x]
# nums = [int(x) for x in input().split(" ")]
#
# dp = [0] * (C + 1)
# # 遍历背包容量
# for i in range(N):
#     for j in range(C, weights[i] - 1, -1):
#         for k in range(1, nums[i] + 1):
#             # 遍历 k，如果已经大于背包容量直接跳出循环
#             if k * weights[i] > j:
#                 break
#             dp[j] = max(dp[j], dp[j - weights[i] * k] + values[i] * k)
# print(dp[-1])
