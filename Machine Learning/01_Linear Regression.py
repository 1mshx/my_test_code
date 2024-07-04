# 线性回归

import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# 绘制损失函数平面
def make_loss_picture(x, y):
    w_i = np.linspace(-5, 5, 50)
    b_i = np.linspace(-5, 5, 50)
    W, B = np.meshgrid(w_i, b_i)

    m = len(x)
    dj = 0

    for i in range(m):
        f_wb_i = W * x[i] + B
        dj_i = f_wb_i - y[i]
        dj = dj + dj_i
    dj = dj * dj
    Z = (1 / (2 * m)) * dj

    # 创建三维坐标系
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制平面
    ax.plot_surface(W, B, Z, cmap='cool')

    # 设置坐标轴标签
    ax.set_xlabel('w')
    ax.set_ylabel('b')
    ax.set_zlabel('Z')

    # 设置视角
    ax.view_init(elev=10, azim=45)

    # 显示图形
    plt.show()


# 生成散点和线性图
def scatter_line(x, y, w1, w2, b):
    z = w1 * x + w2 * (x ** 0.5) + b
    plt.scatter(x, y, c='r')
    plt.plot(x, z)
    plt.show()


# 寻找最优参数
def gradient_descent(X, y, learning_rate=0.01, num_iterations=100):
    """

    :param X: 特征
    :param y: 样本
    :param learning_rate: 学习率，范围是0到1
    :param num_iterations: 学习次数
    :return: 模型参数，第一个是b
    """

    m = len(y)  # 样本数量
    n = X.shape[1]  # 特征数量
    theta = np.zeros(n)  # 初始化参数向量

    for _ in range(num_iterations):
        # 计算预测值
        y_pred = np.dot(X, theta)

        # 计算误差0
        error = y_pred - y

        # 更新参数
        gradient = np.dot(X.T, error) / m
        theta -= learning_rate * gradient

    return theta


if __name__ == '__main__':
    # 指定随机种子
    random.seed(66)

    # 生成x和y
    X = np.arange(1, 21)
    X2 = np.c_[np.array(X ** 0.5), X]
    y = (random.sample(range(1, 41), 20))
    y.sort()
    print(y)

    # 添加一列全为1的截距项
    X1 = np.c_[np.ones(X.shape[0]), X2]

    # 调用梯度下降函数
    theta = gradient_descent(X1, y)

    print("模型参数：", theta)
    b = theta[0]
    w2 = theta[1]
    w1 = theta[2]

    make_loss_picture(X, y)
    scatter_line(X, y, w1, w2, b)
