import scipy as sp
import matplotlib.pyplot as plt 

#----REading in the Data-----
data = sp.genfromtxt('web_traffic.tsv', delimiter = '\t')
print(data.shape)

#----Preprocessing and cleaning in the data----
x = data[:,0]
y = data[:,1]

#imprimir el total de nan en cada columna
print('Invalid data in x: ', sp.sum(sp.isnan(x)))
print('Invalid data in y: ', sp.sum(sp.isnan(y)))

#borrar los que tienen nan 
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

#graficar los datos
plt.scatter(x, y, linewidths=0.01)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hour')
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])

#before building our first model, approximation erro
def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)

#starting with a simple straight line
fp1, residuals, runk, sv, rcod = sp.polyfit(x, y, 1, full = True)
print('Model parameters: %s' % fp1)
#print(residuals, runk, sv, rcod)
f1 = sp.poly1d(fp1) #esta linea crea la funcion ax + b
print(error(f1, x, y))
fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth = 4, color = 'g')
plt.legend(['d = %i' % f1.order], loc = 'upper left')


#Towards some advanced stuff
f2p = sp.polyfit(x, y, 2)
print(f2p)
f2 = sp.poly1d(f2p)
print(f2)
print(error(f2, x, y))
f2x = sp.linspace(0, x[-1],  1000)
plt.plot(f2x, f2(f2x), linewidth = 4, color = 'r')
plt.legend(['d = %i' % f2.order], loc = 'upper left')

#Let's try it for degree 3, 10, and 100
f3p = sp.polyfit(x, y, 3)
f3 = sp.poly1d(f3p)
f3x = sp.linspace(0, x[-1],  1000)
plt.plot(f3x, f3(f3x), linewidth=4, color='k')
plt.legend(['d = %i' % f3.order], loc='upper left')

f100p = sp.polyfit(x, y, 50)

f100 = sp.poly1d(f100p)
f100x = sp.linspace(0, x[-1],  1000)
plt.plot(f100x, f100(f100x), linewidth = 4, color = 'y', linestyle = '--')

plt.autoscale(tight=True)
plt.grid()


#Stepping back to go forward - another look at our data
inflection = 3*7*24 
xa = x[:int(inflection)] #data before the inflection point
ya = y[:int(inflection)]
xb = x[int(inflection):]
yb = y[int(inflection):]#data after

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))
vector_x = sp.linspace(0, x[-1], 1000)
plt.plot(vector_x, fa(vector_x), 'r--')
plt.plot(vector_x, fb(vector_x), 'r--')
plt.show()

