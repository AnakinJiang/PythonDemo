# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-10-01 10:02:37
# Description：matplotlib库测试

import matplotlib.pyplot as plt
import matplotlib

font = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")


def figure_size_test():
    """
    测试图片大小设置
    :return:
    """

    plt.rcParams['savefig.dpi'] = 400  # 图片像素
    print(plt.rcParams['figure.figsize'])
    print(plt.rcParams['figure.dpi'])
    print(plt.rcParams['savefig.dpi'])
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # 设置图标标题，中文支持
    # plt.title("Square Numbers", fontsize=24)
    plt.title("平方数", fontsize=24, fontproperties=font)

    # 设置坐标轴
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    # plt.axis('equal')
    plt.axis('off')
    plt.savefig('output/figure_size.png', dpi=300)  # 指定分辨率保存


def create_picture():
    """
    创建figure
    :return:
    """
    fig = plt.figure()
    plt.show()


def create_sub_picture():
    """
    测试如何在figure中创建子对象，使用add_subplot、add_axes
    """
    fig = plt.figure(num=1, figsize=(6.4, 4.8))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    ax5 = fig.add_axes([0.3, 0.2, 0.2, 0.5])
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    ax1.plot(input_values, squares, linewidth=5)
    ax1.set_title("Square Numbers")
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Square of Value")
    plt.show()


if __name__ == "__main__":
    # figure_size_test()
    # create_picture()
    create_sub_picture()