import sys
import xlrd
import xlwt
import re
import os
import shutil
import time
import csv

# excel 读
book = xlrd.open_workbook('./in/error_all.xlsx')  # 得到Excel文件的book对象，实例化对象
# count = len(book.sheets())  # sheet数量
for sheet in book.sheets():
    sheet_name = sheet.name  # sheet名称
    if sheet_name != '搜狗全没有的':
        continue

    nrows = sheet.nrows  # 获取行总数
    # 循环打印每一行的内容
    insert = 0
    for i in range(1, nrows):
        row_value = sheet.row_values(i)
        word = row_value[0]
        flag = row_value[1]

# csv 读
with open('./in/indexs.csv', encoding = 'utf16') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for line in f_csv:
        row_value = line[0].strip().split('\t')
        # print (line)
        word = row_value[0]
        flag = row_value[1].upper()


# excel 写
book_write = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
sheet_name = 'write_sheet'
sheet_write = book_write.add_sheet(sheet_name)

j_line_write = 1
sheet_write.write(j_line_write, 0, label='label1')
sheet_write.write(j_line_write, 1, label='label2')

book_write.save('./weibo_clear/out/' + 'zwf' + '.xls')

