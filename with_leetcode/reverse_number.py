# encoding: utf-8
# @author: fengr358
# @time: 2021/4/9 22:25
# @desc:

def reverse(x: int) -> int:
    if x == 0:
        return 0
    result = '' if x > 0 else '-'
    y = str(x).strip('-')
    y = y[::-1].strip('0')

    result += y
    try:
        wuw = int(result)
    except:
        wuw = 0

    if wuw > 2 ** 31 - 1 or wuw < -2 ** 31:
        wuw = 0

    return wuw

print (reverse(1534236469))