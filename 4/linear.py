# encoding= utf-8  
# @Time : 2020/9/7 19:32 
# @Author : Yao
# @File : linear.py 
# @Software: PyCharm


def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]


def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def power_better(x, n):
    if n == 0:
        return 1
    else:
        partial = power_better(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


