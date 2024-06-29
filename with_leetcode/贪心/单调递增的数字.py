# encoding: utf-8
# @author: fengr358
# @time: 2024/6/30 0:27
# @desc:


# 当且仅当每个相邻位数上的数字
# x和y满足 x <= y时，我们称这个整数是单调递增的。
#
# 给定一个整数n ，返回小于或等于n的最大数字，且数字呈单调递增 。
#
# 示例
#
# 输入: n = 10
# 输出: 9
#
#
# 输入: n = 1234
# 输出: 1234
#
#
# 输入: n = 332
# 输出: 299

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # if n <= 0 or len(str(n)) == 1:
        #     return n
        # strn = str(n)
        # start = len(strn)
        # for i in range(len(strn) - 2, -1, -1):
        #     if strn[i] > strn[i + 1]:
        #         start = i
        #         strn = strn[: i] + str(int(strn[i]) - 1) + strn[i+1:]
        # strn = strn[: start+1] + '9' * (len(strn) - start - 1)
        # return int(strn)

        if n <= 0 or len(str(n)) == 1:
            return n
        n = str(n)
        start = len(n)
        for i in range(len(n) - 2, -1, -1):
            if n[i] > n[i + 1]:
                start = i
                n = n[: i] + str(int(n[i]) - 1) + n[i + 1:]
        n = n[: start + 1] + '9' * (len(n) - start - 1)
        return int(n)

