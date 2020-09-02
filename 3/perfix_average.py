# encoding= utf-8  
# @Time : 2020/9/2 20:19 
# @Author : Yao
# @File : perfix_average.py 
# @Software: PyCharm

def prefix_average1(S):
#   O(n^2)
    n = len(S)
    A = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += S[j]
        A[j] = total / (j + 1)
    return A

print(prefix_average1([1,2,4,4,4]))

def prefix_average2(S):
#   O(n)
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)
    return A

print(prefix_average2([1,2,4,4,4]))