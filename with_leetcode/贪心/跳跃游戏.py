# encoding: utf-8
# @author: fengr358
# @time: 2024/6/28 9:22
# @desc:

# leetcode = 45
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳  1  步，然后跳  3  步到达数组的最后一个位置。
# 说明: 假设你总是可以到达数组的最后一个位置。

class Solution(object):
    def min_jump_nums(self, input):
        if not input or len(input) <= 1:
            return 0
        curdis, nextdis, result = 0, 0, 0
        for i in range(len(input)):
            nextdis = max(nextdis, i + input[i])
            if i == curdis:
                curdis = nextdis
                result += 1
                if nextdis >= len(input) - 1:
                    return result
        return -1

input = [2, 3, 1, 1, 4]
print(Solution().min_jump_nums(input))

