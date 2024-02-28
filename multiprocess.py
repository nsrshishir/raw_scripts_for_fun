from os import getpid
from time import perf_counter, sleep
from multiprocessing import Pool, cpu_count

# function that sleeps for 1 second
def fun_1(a):
    sleep(1)
    return a * a

# without multiprocessing
atime = perf_counter()
print('Without multiprocessing')

res = [fun_1(i) for i in range(10)]

print(f"Result without multiprocessing: {res}")
print(f"Time taken without multiprocessing: {perf_counter() - atime}\n")

# with multiprocessing
atime = perf_counter()
print('With multiprocessing')

with Pool(processes=cpu_count()) as pool:
    res = pool.map(fun_1, range(10))

print(f"Result with multiprocessing: {res}")
print(f"Time taken with multiprocessing: {perf_counter() - atime}")
