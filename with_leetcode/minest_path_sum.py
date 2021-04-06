# encoding: utf-8
# @author: fengr358
# @time: 2021/4/5 20:55
# @desc: 矩阵的最小路径和

import numpy as np


class Solution:

    def print_normal(self, grid, dp):
        print(dp)
        m, n = np.array(grid).shape
        result = []
        i = m - 1
        j = n - 1
        result.append((m - 1, n - 1, grid[m - 1][n - 1]))
        while i >= 1 and j >= 1:
            if dp[i - 1][j] < dp[i][j - 1]:
                result.append((i - 1, j, grid[i - 1][j]))
                i -= 1
            else:
                result.append((i, j - 1, grid[i][j - 1]))
                j -= 1
        print(result)
        while i > 0:
            result.append((i - 1, 0, grid[i - 1][0]))
            i -= 1
        while j > 0:
            result.append((0, j - 1, grid[0][j - 1]))
            j -= 1
        print(result)


    def minPathSum(self, grid) -> int:
        # 普通方法
        # if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        #     return 0
        #
        # m, n = np.array(grid).shape
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # self.print_normal(self, grid, dp)
        # return dp[m-1][n-1]

        # 空间压缩方法
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = np.array(grid).shape
        bool_row_more = True if m > n else False
        more, less = (m, n) if bool_row_more else (n, m)
        dp = [0] * less
        dp[0] = grid[0][0]

        for i in range(1, less):
            dp[i] = dp[i - 1] + (grid[0][i] if bool_row_more else grid[i][0])

        for i in range(1, more):
            dp[0] = dp[0] + (grid[i][0] if bool_row_more else grid[0][i])
            for j in range(1, less):
                dp[j] = min(dp[j], dp[j - 1]) + (grid[i][j] if bool_row_more else grid[j][i])
        self.print_update(grid, dp)
        return dp[less - 1]

input = [[1, 3, 5, 9],
         [8, 1, 3, 4],
         [5, 0, 6, 1],
         [8, 8, 4, 0]]
solution = Solution()
print (solution.minPathSum(input))



