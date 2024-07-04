# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_classification
# from sklearn.linear_model import LogisticRegression
#
# # 生成多类别示例数据
# X, y = make_classification(n_samples=300, n_features=2, n_classes=3, n_clusters_per_class=1, n_redundant=0,
#                            random_state=42)
#
#
# # 定义决策边界绘制函数
# def plot_decision_boundary(model, X, y):
#     # 绘制数据点
#     plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
#
#     # 确定坐标轴范围
#     x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
#     y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
#                          np.arange(y_min, y_max, 0.01))
#
#     # 获取决策边界的预测值
#     Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#
#     # 绘制决策边界
#     plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.5)
#     plt.colorbar()
#
#     # 设置图像标题和标签
#     plt.title('Decision Boundary')
#     plt.xlabel('Feature 1')
#     plt.ylabel('Feature 2')
#
#
# # 构建一个示例分类模型
# model = LogisticRegression()
#
# # 拟合模型
# model.fit(X, y)
#
# # 绘制决策边界
# plot_decision_boundary(model, X, y)
#
# # 显示图像
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_classification
# from sklearn.linear_model import LogisticRegression
#
# # 生成多类别示例数据
# X, y = make_classification(n_samples=500, n_features=3, n_classes=4, n_clusters_per_class=1, n_redundant=0,
#                            random_state=42)
#
#
# # 定义决策边界绘制函数
# def plot_decision_boundary(model, X, y):
#     # 绘制数据点
#     ax = plt.axes(projection='3d')
#     ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.Paired)
#
#     # 确定坐标轴范围
#     x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
#     y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
#     z_min, z_max = X[:, 2].min() - 0.5, X[:, 2].max() + 0.5
#     xx, yy, zz = np.meshgrid(np.arange(x_min, x_max, 0.01),
#                              np.arange(y_min, y_max, 0.01),
#                              np.arange(z_min, z_max, 0.01))
#
#     # 获取决策边界的预测值
#     Z = model.predict(np.c_[xx.ravel(), yy.ravel(), zz.ravel()])
#     Z = Z.reshape(xx.shape)
#
#     # 绘制决策边界
#     ax.contour3D(xx, yy, zz, Z, cmap=plt.cm.Paired)
#     ax.set_xlabel('Feature 1')
#     ax.set_ylabel('Feature 2')
#     ax.set_zlabel('Feature 3')
#
#     # 设置图像标题
#     plt.title('Decision Boundary')
#
#
# # 构建一个示例分类模型
# model = LogisticRegression()
#
# # 拟合模型
# model.fit(X, y)
#
# # 绘制决策边界
# plot_decision_boundary(model, X, y)
#
# # 显示图像
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# 生成多类别示例数据
X, y = make_classification(n_samples=300, n_features=2, n_classes=3, n_clusters_per_class=1, n_redundant=0,
                           random_state=42)


# 定义决策边界绘制函数
def plot_decision_boundary(model, X, y):
    # 绘制数据点
    plt.scatter(X[:, 0], X[:, 1], c=y)

    # 确定坐标轴范围
    x_min, x_max = min(X[:, 0]) - 0.5, max(X[:, 0] + 0.5)
    y_min, y_max = min(X[:, 1]) - 0.5, max(X[:, 1] + 0.5)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    # 获取决策边界的预测值
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 绘制决策边界
    plt.contourf(xx, yy, Z, alpha=0.5)
    plt.colorbar()

    # 设置标题
    plt.title('Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')


# 构建一个分类模型
model = LogisticRegression()

# 拟合模型
model.fit(X, y)

# 绘制决策边界
plot_decision_boundary(model, X, y)

# 显示图像
plt.show()
