class Solution:
    def get_long_str(self, input):

        set_sub_str = set()
        rk = -1
        result = 0

        n = len(input)
        for i in range(n):
            if i != 0:
                # print (set_sub_str)
                # print (input[i-1])
                set_sub_str.remove(input[i-1])
            while rk + 1 < n and input[rk+1] not in set_sub_str:
                set_sub_str.add(input[rk+1])
                rk += 1
                # print ('cishi....' + str(set_sub_str))
            result = max(result, rk-i+1)

        return result

print (Solution().get_long_str(''))




