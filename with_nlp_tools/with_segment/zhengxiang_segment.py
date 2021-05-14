# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 08:57:56 2018

@author: zhaowenfeng
"""

test_file = 'data/train.txt'#训练语料
test_file2 = 'data/test.txt'#测试语料
test_file3 = 'data/test_sc_zhengxiang.txt'#生成结果

def get_dic(test_file): #读取文本返回列表
    with open(test_file, 'r', encoding='utf-8') as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars

dic = get_dic(test_file)

def readfile(test_file2):
    max_length = 5

    h = open(test_file3, 'w', encoding='utf-8',)
    with open(test_file2, 'r', encoding='utf-8',) as f:
        lines = f.readlines()

    for line in lines:
        #分别对每行进行正向最大匹配处理
        max_length = 5
        my_list = []
        len_hang = len(line)
        while len_hang > 0:
            tryWord = line[0: max_length]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[0: len(tryWord)-1]
            my_list.append(tryWord)
            line = line[len(tryWord):]
            len_hang = len(line)

        for t in my_list:#将分词结果写入生成文件
            if t == '\n' :
                h.write('\n')
            else:
                h.write(t + "  ")
        print(my_list)
    h.close()

def readfile_reverse(test_file2):
    max_length = 5

    h = open(test_file3, 'w', encoding='utf-8',)
    with open(test_file2, 'r', encoding='utf-8',) as f:
        lines = f.readlines()

    for line in lines:
        #分别对每行进行正向最大匹配处理
        max_length = 5
        my_list = []
        len_hang = len(line)
        while len_hang > 0:
            tryWord = line[-1 * max_length:]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = line[-1 * (min(max_length, len(tryWord)-1)):]
            my_list.append(tryWord)
            line = line[: -1 * len(tryWord)]
            len_hang = len(line)

        my_list.reverse()
        for t in my_list:#将分词结果写入生成文件
            if t == '\n' :
                h.write('\n')
            else:
                h.write(t + "  ")

        print (my_list)
    h.close()

readfile(test_file2)
readfile_reverse(test_file2)