# -*- coding: utf-8 -*-
# def fact(n=2):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print fact(2)

def move(n, a, b, c):
    if n == 1:
        print('move',a , '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
i = int(input('请输入圆盘数量：'))
move(i, 'A', 'B', 'C')


