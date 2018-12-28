# Covariance

## variance 方差 
表示为函数：
```py
Var[x]
```
variance 计算方法，分布中每个值与期望值的平均差异。或者与期望值的预期平方差
```py
Var[x] = sum(p(x1) . (x1-E[x])ˆ2, p(x2).(x2 - E[x])ˆ2,..., p(x1).(xn - E[x]ˆ2)
````
在统计中，方差可以通过从该领域中抽取的实例来估计。样本的方差用sigma表示，用上标2表示平方。平方差的总和乘以实例数减1的倒数以修正偏差。
```py
sigmaˆ2 = sum from 1 to n ( ( xi - mu )ˆ2) .1/(n - 1)
```
在numpy 中,可以用var() 函数为矢量或矩阵计算方差。 
var()默认计算总体方差
计算样本的方差，必须将ddof参数设置为值1

## standard deviation
标准差为方差的平方根，用小写“s“ 表示
```py
s = sqrt(sigmaˆ2)
```
Numpy  提供std()函数计算标准差的函数。ddof参数必须设置为1，以计算无偏差样本标准差， axis 设置参数0/1来计算列/行标准偏差。
```py
from numpy import array
from numpy import std
M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(M)
col_mean = std(M,ddof =1,axis = 0)
print(col_mean)
row_mean = std(M,ddof = 1, axis = 1)
print(row_mean)
```


