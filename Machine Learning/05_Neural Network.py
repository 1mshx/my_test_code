import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化权重和偏置
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros(output_size)

    def forward(self, X):
        # 前向传播计算预测值
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # 反向传播计算梯度
        self.error = output - y
        self.delta2 = self.error * self.sigmoid_derivative(self.z2)
        self.dW2 = np.dot(self.a1.T, self.delta2)
        self.db2 = np.sum(self.delta2, axis=0)
        self.delta1 = np.dot(self.delta2, self.W2.T) * self.sigmoid_derivative(self.z1)
        self.dW1 = np.dot(X.T, self.delta1)
        self.db1 = np.sum(self.delta1, axis=0)

    def update_weights(self, learning_rate):
        # 使用梯度下降法更新权重和偏置
        self.W1 -= learning_rate * self.dW1
        self.b1 -= learning_rate * self.db1
        self.W2 -= learning_rate * self.dW2
        self.b2 -= learning_rate * self.db2

    def train(self, X, y, epochs, learning_rate):
        # 训练网络
        for epoch in range(epochs):
            # 前向传播和预测值计算
            output = self.forward(X)
            # 反向传播和梯度计算
            self.backward(X, y, output)
            # 更新权重和偏置
            self.update_weights(learning_rate)

            # 打印每个epoch的损失函数（可选）
            loss = self.cross_entropy_loss(output, y)
            print(f"Epoch {epoch + 1}: Loss = {loss}")

    def predict(self, X):
        # 预测函数
        output = self.forward(X)
        predictions = (output > 0.5).astype(int)
        return predictions

    def sigmoid(self, z):
        # Sigmoid函数
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        # Sigmoid函数的导数
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def cross_entropy_loss(self, y_pred, y_true):
        # 交叉熵损失函数
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss


# 生成一些示例数据
np.random.seed(0)
X = np.random.rand(100, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

# 在输入特征中添加偏置项
X = np.column_stack((np.ones(len(X)), X))

# 初始化神经网络
input_size = X.shape[1]
hidden_size = 4
output_size = 1
nn = NeuralNetwork(input_size, hidden_size, output_size)

# 设置训练参数
epochs = 1000
learning_rate = 0.1

# 训练网络
nn.train(X, y, epochs, learning_rate)

# 使用训练好的网络进行预测
predictions = nn.predict(X)
print("Predictions:", predictions)