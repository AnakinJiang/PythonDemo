# encoding:utf-8

class A(object):
    def __new__(cls, x):
        print('this is in A.__new__, and x is ', x)
        return super(A, cls).__new__(cls)

    def __init__(self, y):
        print('this is in A.__init__, and y is ', y)

class C(object):
    def __new__(cls, n):
        print('this is in C.__new__, and n is ', n)
        return super(C, cls).__new__(cls)

    def __init__(self, a):
        print('this is in C.__init__, and a is ', a)


class B(A):
    def __new__(cls, z):
        print('this is in B.__new__, and z is ', z)
        return A.__new__(cls, z)

    def __init__(self, m):
        print('this is in B.__init__, and m is ', m)

# class B(A):
#     def __new__(cls, z):
#         print 'this is in B.__new__, and z is ', z
#         return object.__new__(cls)
#     def __init__(self, m):
#         print 'this is ni B.__init__, and m is ', m

if __name__ == '__main__':
    a = A(100)
    print('=' * 20)
    b = B(200)
    print(type(b))