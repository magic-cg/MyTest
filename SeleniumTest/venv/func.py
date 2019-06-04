# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):

    deta = b**2-4*a*c

    if a==0:

        print('error')

    elif deta > 0:

        x1 = (-b+math.sqrt(deta))/(2*a)

        x2 = (-b-math.sqrt(deta))/(2*a)

        print('该一元二次方程有两个根为:%.2f和%.2f' % (x1,x2))

    elif(deta==0):

        x1 = -b/(2*a)

        print('该一元二次方程有且仅有一个根为:%.2f' % x1)

    else:

        print('该方程无实根')

a = float(input('请输入a:'))

b = float(input('请输入b:'))

c = float(input('请输入c:'))
#调用该函数
quadratic(a,b,c)