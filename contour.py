# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-10-04 16:07:20
# Descripttion： 等高线图作图细节
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def f(x, y):
    """
    计算高度的函数
    :param x: 向量
    :param y: 向量
    :return: dim(x)*dim(y)维的矩阵
    """
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


def draw_contour():
    """
    测试画等高线图
    :return:
    """
    x = np.linspace(-5, 5, 256)
    y = np.linspace(-5, 5, 256)
    x_mesh, y_mesh = np.meshgrid(x, y)  # 获得网格坐标矩阵
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.1, 0.6, 0.8])
    ax3 = fig.add_axes([0.75, 0.1, 0.1, 0.8])
    z = f(x_mesh, y_mesh)
    z_min = np.min(z)
    z_max = np.max(z)
    # 进行颜色填充
    CS = ax1.contourf(x_mesh, y_mesh, z, 4, cmap=plt.cm.rainbow)
    # 进行等高线绘制
    c = ax1.contour(x_mesh, y_mesh, z, 4, colors='gray')
    # 在等高线图里面加入每条线对应的值
    ax1.clabel(c, inline=True, fontsize=10)

    # cb = plt.colorbar(CS, ax=ax3)  # 增加颜色条
    cmap = mpl.cm.jet
    norm = mpl.colors.Normalize(vmin=z_min, vmax=z_max)
    bounds = [round(elem, 2) for elem in np.linspace(z_min, z_max, 8)]
    cb4 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, boundaries=bounds, norm=norm, spacing='proportional',
                                    orientation='vertical')
    cb4.set_label('mS/m')  # 设置标签
    plt.show()


def colorbar_test():
    """
    测试自定义colorbar
    :return:
    """
    fig = plt.figure(figsize=(3, 8))
    cmap = mpl.cm.jet
    ax1 = fig.add_axes([0, 0.1, 0.2, 0.8])  # 四个参数分别是左、下、宽、长
    norm = mpl.colors.Normalize(vmin=1.3, vmax=2.5)
    bounds = [round(elem, 2) for elem in np.linspace(1.3, 2.5, 14)]  #
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
                                    boundaries=[1.2] + bounds + [2.6],
                                    extend='both',
                                    ticks=bounds,  # optional
                                    spacing='proportional',
                                    orientation='vertical')
    cb1.set_label("123")
    ax2 = fig.add_axes([0.3, 0.1, 0.2, 0.8])  # 四个参数分别是左、下、宽、长
    cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
                                    # boundaries=[1.2] + bounds + [2.6],
                                    # extend='both',
                                    ticks=bounds,  # optional
                                    spacing='proportional',
                                    orientation='vertical')
    ax3 = fig.add_axes([0.6, 0.1, 0.2, 0.8])  # 四个参数分别是左、下、宽、长
    cb3 = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, norm=norm,
                                    boundaries=bounds,
                                    # extend='both',
                                    ticks=bounds,  # optional
                                    spacing='proportional',
                                    orientation='vertical')
    plt.show()


if __name__ == "__main__":
    # colorbar_test()
    draw_contour()
