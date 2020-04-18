import math
import numpy as np
import pandas as pd
import scipy.stats
from scipy import stats, optimize, interpolate
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

score=0.5+sigmoid(140.85/-100)
print (score)


a = np.array([[72,80],[67,70],[70,75]])
data = pd.DataFrame(a, index=["a", "b","c"], columns=["one", "two"])

correlation, pvalue = scipy.stats.pearsonr(data.one, data.two)
print (correlation, pvalue)
print(data)
# 计算第一列和第二列的相关系数
print(data.one.corr(data.two))
# 1.0
# 返回一个相关系数矩阵
print(data.corr())

# 计算第一列和第二列的协方差
print(data.one.cov(data.two))
# 9.0
# 返回一个协方差矩阵
print(data.cov())