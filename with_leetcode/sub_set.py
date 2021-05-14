import copy
class Solution:
    def get_sub_set(self, input):
        result = []
        result.append([])

        for i, item in enumerate(input):
            len_result = len(result)
            for j in range(len_result):
                tmp = copy.deepcopy(result[j])
                tmp.extend([item])
                result.append(tmp)
        return result

    def get_sub_set_binary(self, input):
        result = []
        n = len(input)
        for i in range(1 << n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(input[j])
            result.append(tmp)

        return result






result = Solution().get_sub_set_binary([1, 2, 3])
print (result)

