# encoding= utf-8  
# @Time : 2020/9/8 19:45 
# @Author : Yao
# @File : two_dimension.py 
# @Software: PyCharm

data0 = ([0] * 2) * 2 #Wrong[0,0,0,0]
data1 = [[0] * 2] * 2 #Wrong形式上没问题但是指向了同一个实例
data2 = [[0] * 2 for _ in range(2)] #Yes

print(data0)
print(data1)
print(data2)