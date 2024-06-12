# encoding: utf-8
# @author: fengr358
# @time: 2024/6/5 0:50
# @desc: #  https://zhuanlan.zhihu.com/p/673571423

# 相邻不同的字符串个数
# 一个字符串由 '0', '1', '2', '?' 四种字符组成，请将所有 '?' 字符替换为 ['0', '1', '2'] 里面的任意一种，
# 但是需保证替换后的相邻字符不同，一共能够生成多少种替换方式
#
# 示例：
# 输入: S = '?0'
# 输出: 2
# 解释: 替换为 '10', '20'。'00'不符合要求，因为和后一个字符相等
#
# 输入: S = '??'
# 输出: Result = 6
# 解释: 01, 02,10,12,20,21
#
# 输入: std::string s = "?0??????2??201???";
# 输出: 1376

def calc_cnt(input):
    def dfs(ss, i, rlist):
        if i == len(input):
            rlist.append(ss)
        else:
            if input[i] == '?':
                for idx in ['0', '1', '2']:
                    if i == 0 or ss[i-1] != idx:  # 判断和左边字符不同
                        if i == len(input)-1 or input[i+1] != idx:  # 判断和右边字符不同
                            dfs(ss+idx, i+1, rlist)
            else:
                dfs(ss+input[i], i+1, rlist)

    rlist = []
    dfs('', 0, rlist)
    return len(rlist)



print(calc_cnt('?0'))
print(calc_cnt('??'))
print(calc_cnt('?0??????2??201???'))
print(calc_cnt('???'))
print('********************')