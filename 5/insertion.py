# encoding= utf-8  
# @Time : 2020/9/8 16:53 
# @Author : Yao
# @File : insertion.py 
# @Software: PyCharm
#插入排序
def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
            A[j] = cur


def insert(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
            A[j] = cur

#冒泡
def bubble(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - i - 1):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]

A = [5,4,3,2,1]
B = [5,4,3,2,1]
bubble(A)
insert(B)
print(A,' ',B)