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

## Covariance
协方差：两个随机变量的联合概率度量，描述两个变量怎样一起变化。
```py
cov(X, Y) = E[(X - E[X]).(Y - E[Y])]
```
协方差计算为每个随机变量与期望值之差乘积的期望或平均值
假设X与Y的期望值已经计算出来，协方差可以计算为x值与它的期望值的差值乘以y值
```py
cov(X, Y) = sum (x - E[X]) * (y - E[Y]) * 1/n
```
样本的协方差可以使用相同的计算方法，修正偏差与方差相同
```py
cov(X, Y) = sum (x - E[X]) * (y - E[Y]) * 1/(n - 1)
```
NumPy 没有函数可以直接计算两个变量直接的协方差。cov() 函数可以计算矩阵的协方差。默认情况下，cov()函数将计算提供的随机变量之间的无偏差（unbiased)或样本协方差
```py
from numpy import array
from numpy import cov
x = array([1,2,3,4,5,6,7,8,9])
print(x)
y = array([9,8,7,6,5,4,3,2,1])
print(y)
Sigma = cov(x,y)[0,1]
print(Sigma)
```
可将协方差归一化在-1和1之间的分数，以通过除以X和Y的标准差来使它的大小可解释。结果被称为变量的相关性，也称为皮尔逊相关系数。<br>
使用np.corrcoef(a)可计算行与行之间的相关系数，np.corrcoef(a,rowvar=0)用于计算各列之间的相关系数，输出为相关系数矩阵。<br>
应用公式0.5\*value+0.5可以将相关系数矩阵的值域由[-1,1]映射为[0,1]。
```py
from numpy import array
from numpy import corrcoef
x = array([1,2,3,4,5,6,7,8,9])
print(x)
y = array([9,8,7,6,5,4,3,2,1])
print(y)
Sigma = corrcoef(x,y)
print(Sigma)
```








