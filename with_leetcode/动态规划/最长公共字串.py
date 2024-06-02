# encoding: utf-8
# @author: fengr358
# @time: 2021/5/23 0:31
# @desc:


# encoding: utf-8
# @author: fengr358
# @time: 2021/5/23 0:19
# @desc:

# 最长公共子串
# https://blog.csdn.net/Andya_net/article/details/77500716


class Solution:
    def longestCommonString(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
    	    return 0

        m = len(text1)
        n = len(text2)
        dp = [[0] * n for _ in range(m)]

        res = ''
        max = 0

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

                    if dp[i][j] > max:
                        max = dp[i][j]
                        res = text1[i - dp[i][j] + 1: i+1]
        return res
print (Solution().longestCommonString('abcef', 'ceh'))
# ce
print (Solution().longestCommonString('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'))
# GTCGTCGGAAGCCGGCCGAA
