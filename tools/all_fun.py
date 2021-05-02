import logging
#logger = logging.getLogger(__name__)
from main import log_decorator


# def initiate_Log():
#     logging.basicConfig(level=logging.DEBUG,format='%(asctime)s | %(name)s | %(funcName)s | (%(lineno)d) | %(levelname)s | %(message)s',filename="C:\\temp\\Log\\file.log")
#
#     # logger = logging.getLogger(__name__)
#
#     # Create handlers
#     c_handler = logging.StreamHandler()
#     c_handler.setLevel(logging.DEBUG)
#
#     # Create formatters and add it to handlers
#     c_format = logging.Formatter('%(asctime)s | %(name)s | %(funcName)s | (%(lineno)d) | %(levelname)s | %(message)s')
#     c_handler.setFormatter(c_format)
#
#     # Add handlers to the logger
#     logging.getLogger('').addHandler(c_handler)
#
#     # logging.debug("print debug")
#     # logging.info("print info")
#     # logging.warning("print warning")
#     # logging.error("print error")
#     # logging.critical("print critical")
#
#     print("initiated log in function")
#     return logging

@log_decorator
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name=name.upper()
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(1+True+True)
    print(1/0)



def Unicode(str1):
    #logging = initiate_Log(logging)
    print(str1)
    print(type(str1))
    print("string in utf-8")
    str2=str1.encode('utf-8')
    print(str2)
    str3=str2.decode('utf-8')
    print(str3)

def strRev(str1):
    str2 = str1[::-1]
    print(str2)

def mytuple():
    tplnum = (1,2,4)
    tplstr = ('one', 'two', 'four')
    print("search 3 in numbers, match=" )
    print(3 in tplnum)
    print("search 4 in numbers, match=")
    print(4 in tplnum)

def myswap():
    # tuple swap in python
    a, b = 1, 4
    print("a = ", a, " b= ", b)
    print("perform swap")
    a, b = b, a  # swap
    print("a = ", a, " b= ", b)