# this is a processBar creator using python
# tqdm is a python process bar lib
import random

from tqdm import tqdm, trange
import math
import time
from joblib import Parallel, delayed


'''joblib是一个可以将Python代码转换为并行计算模式的包,
当Parallel中backend="multiprocessing"时指python⼯作进程的数量，
或者backend="threading"时指线程池⼤⼩。当n_jobs=-1时，使⽤所有的CPU执⾏并⾏计算。
当n_jobs=1时，就不会使⽤并⾏代码，即等同于顺序执⾏，可以在debug情况下使⽤。
另外，当n_jobs<-1时，将会使⽤(n_cpus + 1 + n_jobs)个CPU，例如n_jobs=-2时，
将会使⽤n_cpus-1个CPU核，其中n_cpus为CPU核的数量。当n_jobs=None 的情况等同于n_jobs=1'''


def math_factorial():
    results = [math.factorial(x) for x in tqdm(range(7000))]
    # 参数n_jobs来设置开启进程数
    results_2 = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in tqdm(range(15000)))

def custom_progress_bar():
    # tqdm.trange函数实际上是封装了一下tqdm()
    with trange(1000) as t:
        for i in t:
            t.set_description(f"Iteration number {i+1}")
            sleeping_time = random.randint(1, 100) / 100
            t.set_postfix(something=random.randint(0, 100),
                          sleeping_time=sleeping_time)
            time.sleep(sleeping_time)
            if i % 100 ==0:
                for _ in trange(10):
                    time.sleep(0.2)


if __name__ == '__main__':
   custom_progress_bar()