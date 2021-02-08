# -*- coding: utf-8 -
################################################################################

################################################################################
"""
test

Authors: test
Date:    2018/10/29 16:26:45
"""
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import codecs
import json

class Statistics(object):
    """
    【test】
    无
    """

    def __init__(self):
        """

        """
        pass

    def print_output(self, t1, t2):
        """
        打印输出
        """
        # try 用来过滤utf8解码不了的字节，utf8范围：U+0080----U+0&FF，而类似0xc0等不能解码
        try:
            print ("%s\t%s" % (t1, t2))
        except:
            pass

    def main(self):
        """
        主函数
        :return:
        """
        for line in sys.stdin:
            # 获取transform 传输的值，cuid 可能含有脏数据，进行过滤
            # 系统版本传输过来，是因为如果是脏版本，数据直接过滤掉
            try:
                t1, t2= line.strip().split('\t')
            except:
                continue
            self.print_output(t1, t2)


if __name__ == "__main__":
    """
    主函数
    """
    statistics = Statistics()
    statistics.main()
