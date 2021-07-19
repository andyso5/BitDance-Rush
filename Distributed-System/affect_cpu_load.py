import time
import math
import random
from multiprocessing import Process

def isPrime(num):
    """
    Args:
        num, positive int
    """
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    else:
        return True

def run_for_a_while(n=2000):
    res = [2]
    for num in range(3, n+1, 2):
        # print("num: %s" % num)
        # print("range: %s" % int(math.sqrt(num)))
        res.append(num) if isPrime(num) else None
    return res



if __name__ == "__main__":
    #    res = run_for_a_while(n=200000)
    #    print(res[:100])
    start_time = time.time()
    pool = []
    for i in range(20):
        # nums = random.randint(400000, 500000)
        nums = 800000
        p = Process(target=run_for_a_while, args=(nums, ))
        p.start()
        pool.append(p)
    
    for p in pool:
        p.join()
    # run_for_a_while(800000) # about 2.72s
    end_time = time.time()
    print("time consumer is %s s" % (end_time-start_time))

## record
"""
Process-num         range       time        max-cpu-load
    0               800000      0           0.91
    1               800000      2.72        0.97
   20               800000      14.16       6.92
    5               800000      4.12        1.41
    3               800000      2.75         -
    4               800000      2.80         -


1. 根据结果貌似, 线程只能负载到进程数为4, 到5时间就是延长, 这说明第五个进程一开始处于等待状态
2. 然而, 进程数从5变到4, 时间并不是原来的两倍, 这说明, 第五个进程不是等前面的进程结束后再进行的, 很可能在一个核内发生了并行
3. 测试机的CPU核数是8, 为什么进程数到4后就开始跳跃了, 而不是在8


"""


