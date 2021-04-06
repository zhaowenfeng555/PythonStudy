import numpy
import copy

# encoding: utf-8
# @author: fengr358
# @time: 2021/4/3 23:49
# @desc: 斐波那契数列



class Solution:

    def climbStairs(self, n: int) -> int:

        # 暴力 O(2^n)
        # if n <= 2:
        #     return n
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)







        # 从左到右计算 O(n)
        # if n <= 2:
        #     return n
        # pre = 1
        # current = 2
        # for i in range(3, n+1):
        #     pre, current = current, current + pre
        # return current







        # 矩阵相乘 O(log(n))

        # def multi_matrix(m, n):
        #     res = [[0] * len(n[0]) for _ in range(len(m)) ]
        #     for i in range(len(m)):
        #         for j in range(len(n[0])):
        #             for k in range(len(m[0])):
        #                 res[i][j] += m[i][k] * n[k][j]
        #     return res

        # def power_matrix(m, p):
        #     res = [[0] * len(m) for _ in range(len(m))]
        #     for i in range(len(m)):
        #         res[i][i] = 1

        #     tmp = copy.deepcopy(m)

        #     while p > 0:
        #         if (p & 1) != 0:
        #             res = multi_matrix(res, tmp)
        #         tmp = multi_matrix(tmp, tmp)

        #         p = p >> 1
        #     return res

        # if n <= 2:
        #     return n
        # base = [[1, 1],
        #         [1, 0]]

        # result = power_matrix(base, n-2)
        # return 2 * result[0][0] + result[1][0]




        # map 缓存结果
        def map_climb_stairs(n, mapping):
            result = 0
            if n <= 2:
                result = n
            else:
                for i in range(1, 3):
                    tmp_map = mapping[n - i]
                    if tmp_map != 0:
                        result += 0 if tmp_map == -1 else tmp_map
                    else:
                        result += map_climb_stairs(n - i, mapping)
            mapping[n] = -1 if result == 0 else result
            return result

        mapping = [0] * (n + 1)
        return map_climb_stairs(n, mapping)





