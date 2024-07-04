# 特征缩放
import numpy as np

X = np.arange(1, 21)
X = X.reshape((5, 4))
X = np.array(X, dtype=float)
y = np.array([6, 15, 24, 33, 27], dtype=float)

print(X)


def format(X, y):
    """
    进行格式转换，方便后续进行运算出来是浮点数
    :param X: 特征
    :param y: 样本
    :return: 格式转换之后的特征和样本
    """
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    return X, y


def scaling(X, y, pattern):
    """
    对数据进行处理，根据选择输入的模式返回对应特征缩放后的数据
    :param X: 特征
    :param y: 样本
    :param pattern: 选择的模式
    :return:
    """
    m = len(y)
    n = X.shape[1]
    _X = {}
    sum_X = {}
    mean_X = {}
    max_X = {}
    min_X = {}
    S_X = {}
    for i in range(n):
        name = f'X{i}'
        value = X[:, i]
        _X[name] = value
        sum_X[name] = sum(value)
        mean_X[name] = sum(value) / m
        min_X[name] = min(value)
        max_X[name] = max(value)
        b = 0
        for j in range(len(value)):
            a = (value[j] - (sum(value) / m)) ** 2
            b = b + a
        S_X[name] = b / len(value)

    print("x", _X)
    print("sum", sum_X)
    print("mean", mean_X)
    print("min", min_X)
    print("max", max_X)
    print("S", S_X)
    if pattern == 1:
        min_max(X, _X, max_X, min_X)
    elif pattern == 2:
        Z_score(X, _X, mean_X, S_X)


def min_max(X, _X, max_X, min_X):
    n = X.shape[1]
    end_X = []
    for i in range(n):
        name = f'X{i}'
        m = len(_X[name])
        for j in range(m):
            _X[name][j] = (_X[name][j] - min_X[name]) / (max_X[name] - min_X[name])
            end_X.append(_X[name][j])
    end_X = np.reshape(end_X, X.T.shape).T
    print(end_X)
    return _X


def Z_score(X, _X, mean_X, S_X):
    n = X.shape[1]
    end_X = []
    for i in range(n):
        name = f'X{i}'
        m = len(_X[name])
        for j in range(m):
            _X[name][j] = (_X[name][j] - mean_X[name]) / S_X[name]
            end_X.append(_X[name][j])
    end_X = np.reshape(end_X, X.T.shape).T
    print(end_X)
    return _X


if __name__ == '__main__':
    pattern = int(input("请输入你想进行的特征缩放操作(1.min_max归一化  2.Z_score归一化):"))
    scaling(X, y, pattern)
