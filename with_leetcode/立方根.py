# encoding: utf-8
# @author: fengr358
# @time: 2021/5/9 22:24
# @desc:

# @question: 不用库函数求某数的立方根，并限定它的误差范围。
# @answer：https://blog.csdn.net/qq_21997625/article/details/88220770



import math

class Solution:
    def __init__(self):
        pass

    def process(self, num, e):
        if num is None:
            return None
        if num in [0, -1, 1]:
            return num
        flag = 1
        if num < 0:
            flag = -1
            num = -num

        epi = 1
        new = num / 2.0
        while abs(new * new * new - num) >= e:
            epi /= 10.0
            while abs(new * new * new - num) >= e:
                new -= epi
                if new * new * new < num:
                    break
                print (new)
            if new * new * new < num:
                new = new + epi
        return new * flag

    def process_math(self, num, e):
        # 数据公式的方式
        flag, num = (-1, -num) if num < 0 else (1, num)
        real = math.exp(math.log(num, math.e) / 3.0)
        return round(real, e)

    def process_two_split(self, num, e):
        if num in [1, -1, 0]:
            return num
        left, right = (0, num) if num > 0 else (num, 0)
        while left < right:
            mid = (left + right) / 2.0
            multi = mid * mid * mid

            # 终止条件
            if abs(multi - num) <= math.pow(10, -e):
                return round(mid, e)

            if multi > num:
                right = mid
            else:
                left = mid

    def process_niuton(self, num, e):
        if num in [1, -1, 0]:
            return num
        guess = 1
        while True:
            # 终止条件
            if abs(guess * guess * guess - num) <= math.pow(10, -e):
                return round(guess, e)
            guess = guess + (num - guess * guess * guess) / (3 * guess * guess)

solution = Solution()
print ('process_math >>>')
for e in range(10):
    result = solution.process_math(-5, e)
    print (result)

print ('process_two_split >>>')
for e in range(10):
    result = solution.process_two_split(-5, e)
    print (result)

print ('process_niuton >>>')
for e in range(10):
    result = solution.process_niuton(-5, e)
    print (result)