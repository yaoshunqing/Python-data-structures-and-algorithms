# encoding= utf-8  
# @Time : 2020/9/7 13:38 
# @Author : Yao
# @File : binary_search.py 
# @Software: PyCharm

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, high)



def binary_search_pos(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search_pos(data, target, low, mid - 1)
        elif target > data[mid]:
            return binary_search_pos(data, target, mid + 1, high)

def binary_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
    return False

a = [1,2,3,4,5]
print(binary_search_pos(a,1,0,4))
print(binary_iterative(a,3))