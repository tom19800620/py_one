# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import time
from Tools.all_fun import *
from Tools.LogConfig import Log
from functools import wraps


def log_decorator(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        Log.Print.info('-----Begin {}{} : ----'.format(original_function.__name__, args, kwargs))
        t1: float = time.time()
        result = None
        try:
            result = original_function(*args, **kwargs)
        except Exception as e:
            Log.Print.error(e)
            # Traceback()
            t2: float = time.time() - t1
            Log.Print.info('Time : {} ran in = {}'.format(original_function.__name__, t2))
            # e.__traceback__()
            exit(1)
        t2 = time.time() - t1
        Log.Print.info('End Function: {} ran in = {}'.format(original_function.__name__, t2))
        return result

    return wrapper_function


# recursion
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@log_decorator
def fib1(n):
    t1: float = time.time()
    print(fib(n))
    t2 = time.time() - t1
    print('time taken {}'.format(t2))


# method 2 reguler fib function

def fibo(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        return 0
    if n <= 2:
        return 1
    for x in range(1, n):
        c = a + b
        a = b
        b = c
    return c

def fibot(n):
    t1: float = time.time()
    print(fibo(n))
    t2 = time.time() - t1
    print('time taken {}'.format(t2))

def rjustified(n):
    i=1
    result="#"
    while i<=n:
        result ="#"*i
        # print(f"{}")
        result.rjust(n)[:n]
        print(result)
        i=i+1

def summinmax(arr):
    i=0
    min1: float=0
    max1: float=0
    lena = len(arr)
    while i < lena:
        temp = 0
        j = 0
        while j < lena:
            if j != i:
                temp = temp+arr[j]
            j = j + 1
        if min1 > temp:
            min1 = temp
            print("min: {} and Max:{} and temp:{}".format(min1, max1,temp))
        if max1 < temp:
            max1 = temp
            print("min: {} and Max:{} and temp: {}".format(min1, max1,temp))
        if i == 0:
            min1 = temp
            max1 = temp
        print("temp:{}".format(temp))
        i = i + 1
    print(min1, max1)

def birthdayCakeCandles(candles):
    # Write your code here
    lena = len(candles)
    i = 0
    max_count = 0
    max = candles[i]
    while i < lena:
        if max < candles[i]:
            max = candles[i]
            max_count = 1
            # print("{} value: {} Count: {}".format(i,candles[i],max_count))
        elif max == candles[i]:
            max_count = max_count + 1
        print("{} value: {} Count: {}".format(i,max,max_count))
        i = i + 1
    print( max_count)


def convert24(tm):
    tm="12:30:34 AM"
    print("[:2]={}, [-2:]={}, [2,-2]={},[2:8]={}, [:8]={}".format(tm[:2], tm[-2:],tm[2:-2],tm[2:8],tm[:8]))
    if tm[-2:]=="PM":
        res = tm[:8] if tm[:2]=="12" else str(int(tm[:2])+12)+tm[2:8]
    if tm[-2:] =="AM":
        res = "00" + tm[2:8] if tm[:2] == "12" else tm[0:8]
    print(res)

def roundgrade(arr):
    lena = len(arr)
    i=0
    result=[]
    while i<lena:
        if arr[i]>5*math.ceil(arr[i]/5)-3 and arr[i]>=38:
            result.append(math.ceil(arr[i]/5)*5)
        else:
            result.append(arr[i])
        i=i+1
    print(arr)
    print(result)

def loops1(matrics):
    tran=[]
    print(matrics)
    for i in range(len(matrics[0])):
        tran_row=[]
        for r in matrics:
            tran_row.append(r[i])
        tran.append(tran_row)
    print(tran)

def even_odd(n):
    list= [str(i)+' - Even' if i%2==0 else str(i)+' - Odd' for i in range(n)]
    listE = [i  for i in range(n) if i % 2 == 0 ]
    listO = [i for i in range(n) if i % 2 != 0]
    print(list)
    print(listE)
    print(listO)

def no_loop(matrics):
    tran=[[row[i] for row in matrics] for i in range(len(matrics[0]))]
    print(tran)
    return tran
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # initiate logging
    # logging = initiate_Log()
    # loops1([[1,2,3,4],[4,5,6,7]])
    no_loop(no_loop([[1,2,3,4],[4,5,6,7]]))
    exit(0)
    # sleep(.5)
    # even_odd(100)

    # roundgrade([17,18,19,20,21,22,23,37,38,39,40,41,42,43])
    # rjustified(5)
    # summinmax([1.1,2.2,3.2,4.4,5.5])
    # birthdayCakeCandles([3,2,1,3])
    # convert24("10:30:34 PM")

    if Log.Print is None:
        print('not initiated')
    else:
        print('already initiated')

    Log.gets()
    fib1(35)
    fibot(35)
    # fib1(36)
    # fib1(37)
    exit(0)
    Log.gets()  # not printing which is good
    print("initiated log")
    Log.Print.debug("print debug")
    Log.Print.info("print info")
    Log.Print.warning("print warning")
    Log.Print.error("print error")
    Log.Print.critical("print critical")
    print_hi('pradeep')
    Unicode("this is a unicode")
    import sys

    print(sys.float_info)
    strRev('one two')
    mytuple()
    myswap()
    # reading a text file into df and checking the size in memory
    # the execution time of queries
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
