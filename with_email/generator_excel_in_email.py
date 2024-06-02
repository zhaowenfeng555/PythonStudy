# encoding=utf8
"""
根据 excel 模板生成对应的数据文件
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import time
from collections import defaultdict as df
import os

# 读取邮件模版
table_template = open('CONFIG_email_contents.template').read()
table_row = '''
               <tr>
                   <td width="100" align="center">{0}</td> 
                   <td width="100" align="center">{1}</td> 
                   <td width="100" align="center">{2}</td> 
                   <td width="100" align="center">{3}</td> 
                   <td width="100" align="center">{4}</td> 
               </tr>
               '''

list_row = []

list_date = []
for str_date in list_date:
    t1, t2, t3, t4, t5 = str_date.split()
    row_content = table_row.format(t1, t2, t3, t4, t5)
    list_row.append(row_content)
table_content = table_template.format(''.join(list_row))
filehtmlname = '{0}/{1}'.format('文件名称', '文件名称2')
with open(filehtmlname, 'w') as filehtml:
    filehtml.write(table_content)