import matplotlib.pyplot as plt
import numpy as np

W = np.array([[1, -3, 5], [2, 4, -6]])
b = np.array([-1, 1, 2])
a_in = np.array([-2, 4])


def g(x):
    x_out = 1 / (1 + np.exp(-x))
    return x_out


def dense(a_in, W, b, g):
    units = W.shape[1]
    a_out = np.zeros(units)
    for i in range(units):
        w = W[:, i]
        z = np.dot(w, a_in) + b[i]
        a_out = g(z)
        print(z)
        return a_out


a = dense(a_in, W, b, g)
print(a)