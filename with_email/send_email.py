# encoding=utf8
"""
邮件发送
"""
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib
import os
from collections import defaultdict as df
import time

def send_mail(to_list, content, subject, att_filepath):
    """
    发邮件
    :param to_list:
    :param content:
    :param subject:
    :return:
    """
    # 发件人
    me = ''

    # 密送
    bcc_list = []
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    # 抄送
    msg['CC'] = ';'.join(to_list)
    msg['Bcc'] = ';'.join(bcc_list)

    # 附件1
    att1 = MIMEText(open(att_filepath, 'rb').read(), 'base64', 'utf8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename="hah_{0}.xls"'.format(arg_date)
    msg.attach(att1)

    # 正文
    cont = MIMEText(content, _subtype='html', _charset='utf8')
    msg.attach(cont)

    s = smtplib.SMTP()
    s.connect()
    s.sendmail(me, to_list + bcc_list, msg.as_string())
    s.quit()
    return 1

arg_date = 20201202
mail_receiver_list = list(mail_receiver_set)
htmlfile_path = 'CONFIG_email_contents.template'
# excel报表位置
att_filepath = 'output/report_total_{0}.xls'.format(arg_date)

if __name__ == '__main__':

    htmlcontent = open(htmlfile_path).read().format(arg_date=arg_date,
                                                    partner_data = ''.join([]),
                                                    channel_data = ''.join([]))

    mail_title_content = mail_title.format(arg_date)
    # 发送邮件
    sendret = send_mail(mail_receiver_list, htmlcontent, mail_title_content, att_filepath)
    if sendret == 1:
        print('send success')
    else:
        sys.stderr.write('send fail')
