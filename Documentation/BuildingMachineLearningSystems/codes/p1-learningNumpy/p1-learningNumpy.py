import numpy as np
print("version de Numpy: ", np.version.full_version)
a = np.array([0,1,2,3,4,5])
print("a = ", a)
print("dimension del array a: ", a.ndim)
print("shape of a: ", a.shape)

#We can now transform this array in to a 2D matrix
b = a.reshape((3,2))
print("Matriz hecha a partir de a = b = ", b)
print("dimension de la matriz b: ", b.ndim)
print("shape of b: ", b.shape)

#it avoids copies wherever ppossible
b[1][0] = 77
print("b fue modificado: \n b = \n", b)
print("como b fue modificado, a tambien \n a = ", a)

#ahora crearemos una copia, a y c son copias totalmente independientes
c = a.reshape((3,2)).copy()
print("copia de a reformada: c = ", c)
c[0][0] = -99
print("c modificado: c = ", c)
print("vemos que a no se ha modificado a = ", a)

#operaciones con a
print("a*2 = ", a*2)
print("a**2 = ", a**2)
'''Contrast that to ordinary Python lists:
    >> [1,2,3,4,5]*2
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    >> [1,2,3,4,5]**2
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for ** or pow(): 'list' and
        int '''

#Indexing
print('------Indexing-------')
#In addition to normal list indexing, it allows us to use arrays themselves as indices.
print("indexando con un array", a[np.array([2,3,4])])
print("a > 4 = ", a > 4)
print("a[a > 4] = ", a[a > 4])

#This can also be used to trim outliers.

'''As this is a frequent use case, there is a special clip function for it, clipping the values
at both ends of an interval with one function call as follows:'''
print('la funcion clip() hace lo mismo que lo anterior \n a.clip(0,4) = ', a.clip(0, 4))
print("a = ", a)

a[a > 4] = 4
print("a[a > 4] = 4, a = ", a)

#handling non-existing values
print('------handling non-existing values------')
c = np.array([1, 2, np.NAN, 3, 4])
print("c = ", c)
print("np.isnan(c) = ", np.isnan(c))
print("c[~np.isnan(c)] = ", c[~np.isnan(c)])#no modifica c
print("c = ", c)
print("np.mean(c[~np.isnan(c)]) = ", np.mean(c[~np.isnan(c)]))

#Comparing runtime behaviors
print('-----------------Comparing runtime behaviors------------------')
import timeit 
#normal_py_sec = timeit.timeit('sum(x*x for x in np.arange(1000))', number = 10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup = "import numpy as np; na = np.arange(1000)", number = 10000)
good_np_sec = timeit.timeit('na.dot(na)', setup = "import numpy as np; na = np.arange(1000)", number = 10000)

#print("Normal Python: %f sec" % normal_py_sec)
print("Naive NumPy: %f sec" % naive_np_sec)
print("Good NumPy: %f sec" % good_np_sec)

'''However, the speed comes at a price. Using NumPy arrays, we no longer have the
incredible fexibility of Python lists, which can hold basically anything. NumPy
arrays always have only one datatype.
'''
print('------------Numpy datatype -------------')
a = np.array([1,2,3])
print(a.dtype)

'''If we try to use elements of different types, NumPy will do its best to coerce them
to the most reasonable common datatype:'''

print('np.array([1, "stringy"]) = ', np.array([1, "stringy"]))
print('np.array([1, "stringy", set([1,2,3])]) = ',
      np.array([1, "stringy", set([1, 2, 3])]))


