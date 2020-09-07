# encoding= utf-8  
# @Time : 2020/9/7 18:55 
# @Author : Yao
# @File : fibonacci.py 
# @Software: PyCharm


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)


