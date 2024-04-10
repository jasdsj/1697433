import numpy as np

a = np.array([3, 4, 1])
b = np.array([6, 7, 2])

print(b.dot(a))

c = np.array([[3, 2, 1, 4], [9, 4, 2, 1], [5, 2, 1, 2], [2, 2, 2, 2]])
d = np.array([[7, 4, 5], [9, 1, 2], [3, 2, 1]])

print(c)
print(c.max(axis=1))
print(c.max(axis=0))

print(d)
print(d.max(axis=1))
print(d.max(axis=0))

e = np.array([1.2, 4.2, 1.1])

print(a.dot(e))

