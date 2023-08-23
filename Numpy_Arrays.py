import numpy as np

a = np.array([ 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])

b = np.array([0. , 0.25, 0.5 , 0.75, 1. ])

re = a.reshape(5,2)
re2 = b.reshape(5,1)

rr = re + re2

c = rr.transpose()

produto = c @ b

result = np.sum(produto)

print(re)
print(re2)
print(rr)

print(c)

print(result)



