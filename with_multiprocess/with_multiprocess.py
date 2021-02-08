#coding: utf-8
#
# @date 20210208
# @author zhaowenfeng
# @desc 进程通讯
# @参考  https://www.cnblogs.com/kaituorensheng/p/4445418.htm
import multiprocessing
import time

def func(msg):
    print ("msg:", msg)
    time.sleep(3)
    print ("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in range(4):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print ("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print ("Sub-process(es) done.")