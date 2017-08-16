"""
python dict learning
"""
import numpy as np

# 隐藏层数
n_hiddens = 6

i = 0

# 定义权重矩阵
weights = {"out": "output layer"}

print(weights)

# 动态添加字典
for i in range(int(n_hiddens)):
    weights["h" + str(i)] = "hidden layer{0}".format(i)

print(weights)