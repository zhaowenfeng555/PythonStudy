# encoding: utf-8
# @author: fengr358
# @time: 2021/5/12 22:38
# @desc:
# import copy
# class Solution:
#     # 使用二进制 迭代法
#     def process(self, nums):
#         result = []
#         if nums is None:
#             return None
#         length = len(nums)


#         size = 1 << length
#         for index in range(size):
#             list_sub = []
#             for j in range(length):
#                 if (index >> j) & 1 == 1:
#                     list_sub.append(num[j])
#             result.append(list_sub)
#         return result
#
#     # 枚举
#     def process_meiju(self, nums):
#         result = [[]]
#         if nums is None:
#             return None
#         for item in nums:
#             length = len(result)
#             for j in range(length):
#                 sub_tmp = copy.deepcopy(result[j])
#                 sub_tmp.append(item)
#                 result.append(sub_tmp)
#         return result
#
# result = Solution().process([1, 2, 3])
# print (result)
# print (Solution().process_meiju([1, 2, 3]))

import copy
import math
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        if nums is None:
            return None
        start = 0
        nums.sort()
        for i, item in enumerate(nums):
            if i >= 1 and nums[i] == nums[i - 1]:
                pass
            else:
                start = 0

            length = len(result)
            for j in range(start, length):
                sub_list = copy.deepcopy(result[j])
                sub_list.append(item)
                result.append(sub_list)
            start = length
        return result

print (Solution().subsetsWithDup([5, 5, 5, 5, 5]))