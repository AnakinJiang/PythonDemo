'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: 变量作用域测试
@Date: 2019-07-27 19:54:24
@LastEditors: AnakinJiang
@LastEditTime: 2019-07-27 21:25:57
'''
def if_for_test():
    '''测试if/elif/else/ try/except for/while的作用域
    '''    

    if True:
        a = 'I am A!'
    for i in range(1,3):
        b=i
    print(a) #输出：I am A!
    print(b) #输出：2

def def_test():
    """测试函数
    """
    g = 1  #全局的
    def fun1():
        g = 2 #局部的
        return g

    print(fun1())# 结果为2
    print(g)# 结果为1
        
    var = 1
    def fun2():
        b = var + 1
        print(var)
        # var = 200
        return b

    print(fun2())

    var = 1
    def fun3():
        b = 2
        var = b + 2
        # var = var + 1
        return var
        
    print(fun3())

def closure_test():
    a = 1
    def external():
        global a
        a = 300
        print(a)

        b = 100
        def internal():
            nonlocal b
            print(b)
            b = 200
            return b

        internal()
        print(b)
        return a

    print(external())

if __name__ == '__main__':
    # if_for_test()
    # def_test()
    closure_test()
