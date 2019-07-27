'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: 类的生命周期
@Date: 2019-07-27 21:25:51
@LastEditors: AnakinJiang
@LastEditTime: 2019-07-27 22:01:54
'''

class A(object):
    def __new__(cls, x):
        print('this is in A.__new__, and x is ', x)
        return super(A, cls).__new__(cls)

    def __init__(self, y):
        print('this is in A.__init__, and y is ', y)

class B(A):
    def __new__(cls, z):
        print('this is in B.__new__, and z is ', z)
        return A.__new__(cls, z)

    def __init__(self, m):
        print('this is in B.__init__, and m is ', m)

a = B(2)
