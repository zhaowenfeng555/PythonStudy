class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 甲：这n天怎样买股票赚的多-------------------------------------
        n = len(prices)

        # 乙：dp[i]代表第i天-------------------------------------------
        # 乙：dp[i][0]代表第i天过后手上有股票时的最大收益
        # 乙：总之，今天过后我必有股票在手上，要么之前买的，要么今天买的
        # 乙：dp[i][1]代表第i天过后手上无股票时的最大收益
        # 乙：总之，今天过后我手上空空如也，要么本来就没有，有我也给卖了
        dp = [[0, 0] for _ in range(n)]

        # 乙： 今天是第一天---------------------------------------------
        # 乙： 保证必须有股票是吧，prices[0]块钱拿去，今天股票我买了
        # 乙： 保证没有股票，啥都不干就好了
        dp[0] = [-prices[0], 0]

        # 旁白： 时间一天天过去
        for i in range(1, n):
            # 甲： 今天是第i天，如果我一定要保证自己有股票，该怎么操作------
            # 乙： dp[i-1][0] 今天的股票太贵了，买之前的股票更划算
            # 乙： - prices[i] 今天的股票更便宜，我买了，prices[i]块钱拿去
            dp[i][0] = max(dp[i-1][0], - prices[i])

            # 甲： 今天是第i天，如果我一定要保证自己没有股票，该怎么操作------
            # 乙： dp[i-1][1] 今天股市不行，还是之前卖更划算
            # 乙： + prices[i] + dp[i-1][0] 今天的行情不错，股票卖掉，血赚prices[i]块钱，
            # dp[i-1][0]是我用低价买入花的钱
            dp[i][1] = max(dp[i-1][1], + prices[i] + dp[i-1][0])

        return dp[-1][-1]

# 作者：yyj
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solutions/2199035/yi-tao-mo-ban-ji-xing-dai-ma-bi-zhao-yan-0ap8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 限制交易最多1次：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], - prices[i])
            dp[i][1] = max(dp[i-1][1], + prices[i] + dp[i-1][0])
        return dp[-1][-1]

# 不限制交易
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], - prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], + prices[i] + dp[i-1][0])
        return dp[-1][-1]

# 限制交易最多2次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0,0,0] for _ in range(n)]
        dp[0]=[-prices[0],0,-prices[0],0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], + prices[i] + dp[i-1][0])
            dp[i][2] = max(dp[i-1][2], - prices[i] + dp[i-1][1])
            dp[i][3] = max(dp[i-1][3], + prices[i] + dp[i-1][2])
        return dp[-1][-1]
# 限制交易最多k次
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 正常动态规划
        if not prices or len(prices) <= 1 or k <= 0:
            return 0
        dp = [[0, 0] * k for _ in range(len(prices))]
        dp[0] = [-prices[0], 0] * k
        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][2*j] = max(dp[i-1][2*j], -prices[i] + (dp[i-1][2*j-1] if j != 0 else 0))
                dp[i][2*j+1] = max(dp[i-1][2*j+1], dp[i-1][2*j]+prices[i])
        return dp[-1][-1]

# 一天的冷静期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], - prices[i] + (dp[i-2][1] if i > 1 else 0))
            dp[i][1] = max(dp[i-1][1], + prices[i] + dp[i-1][0])
        return dp[-1][-1]

