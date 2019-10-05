# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-10-04 16:39:32
# Descripttion： 测试各类Python注释使用方法


def text(a: int, b: 'int > 0', c: '一头猪', d: 'int > 0' = 1) -> 'str':
    pass


if __name__ == "__main__":
    print(text.__annotations__)
