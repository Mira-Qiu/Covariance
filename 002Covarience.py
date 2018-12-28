from numpy import array
from numpy import var
v = array([1,2,3,4,5,6])
print(v)
result = var(v,ddof =1)
print(result)

#[1 2 3 4 5 6]
#3.5


from numpy import array
from numpy import var
M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
print(M)
col_mean = var(M,ddof = 1, axis = 0)
print(col_mean)
row_mean = var(M,ddof = 1, axis = 1)
print(row_mean)

