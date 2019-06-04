# -*- coding: utf-8 -*-
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    print s
power(5,4)

def regedit(name,sex,area='nanjing',years='18'):

    print ('name',name)
    print ('sex',sex)
    print('area',area)
    print ('years',years)

regedit('chen','man')
# # 使用num为list方式调用
# def chal(num):
#     sum  = 0
#     for n in num:
#         sum = sum + n*n
#     print sum
#
# chal([1,2,3])
# # 使用num为tuple方式调用
# def chal2(*num1):
#     sum  = 0
#     for a in num1:
#         sum = sum + a*a
#     print sum
#
# chal2(2,3,4)
def chal3(n):
    if n == 1:
        return 1
    return n * chal3(n-1)
chal3(5)