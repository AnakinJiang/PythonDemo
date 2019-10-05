# lis = [x*x for x in range(10)]
# print(lis)
# #生成器
# generator_ex = (x*x for x in range(10))
# print(generator_ex)

# generator_ex = (x*x for x in range(10))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
# print(next(generator_ex))
def fib(max):
    n,a,b =0,0,1
    while n < max:
        a,b =b,a+b
        yield b
        n = n+1
        # print(a)
    return 'done'
def test_fib():
    #fibonacci数列
    a = fib(10)
    print(fib(10))

if __name__ == "__main__":
    test_fib()