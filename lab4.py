import numpy as np

#a = np.array([0, 1])
#print(a)

#a = np.arange(2)
#print(a)
#print(type(a))

#a = np.arange(2, dtype='int32')
#print(a.dtype)
#b = a.astype('float')
#print(b)
#print(b.dtype)
#print(b.shape)

#print(a.ndim)

#m = np.array((np.arange(2), np.arange(2)))
#print(m.shape)

#m1 = np.array([[5, 4, 5],[4, 8, 3]])
#print(m1)
#print(m1.shape)
#print(m1.ndim)

#zera = np.zeros((5, 5))
#jedynki = np.ones((4,4))
#print(zera)
#print(jedynki)
#print(zera.dtype)
#print(jedynki.dtype)

#pusta = np.empty((2,2))
#print(pusta)
#poz_1 = pusta[1, 1]
#poz_2 = pusta[0, 1]
#print(poz_1)
#print(poz_2)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1, 2, 5)
print(liczby_lin)

z = np.indices((5, 3))
print(z)

