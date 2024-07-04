# 逻辑回归

import numpy as np


def sigmoid(z):
    # Sigmoid函数
    return 1 / (1 + np.exp(-z))


def compute_loss(X, y, theta):
    # 计算损失函数
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    loss = (-1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return loss


def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    losses = []

    for i in range(num_iterations):
        h = sigmoid(np.dot(X, theta))
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient

        # 计算并记录损失函数
        loss = compute_loss(X, y, theta)
        losses.append(loss)

        if i % 1000 == 0:
            print(f"Iteration {i}: Loss = {loss}")

    return theta, losses


# 生成一些示例数据
np.random.seed(0)
X = np.random.rand(100, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# 在输入特征中添加偏置项
X = np.column_stack((np.ones(len(X)), X))

# 初始化模型参数
initial_theta = np.zeros(X.shape[1])

# 设置学习率和迭代次数
learning_rate = 0.01
num_iterations = 100000

# 使用梯度下降法优化模型参数
optimal_theta, loss_history = gradient_descent(X, y, initial_theta, learning_rate, num_iterations)

# 打印最优参数和损失曲线
print("Optimal theta:", optimal_theta)
import matplotlib.pyplot as plt

plt.plot(loss_history)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("Loss Curve")
plt.show()
