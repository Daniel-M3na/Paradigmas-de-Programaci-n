#
# Curvas Z-spline en n dimensiones
#
# Julián Sagredo ESFM IPN 2023
#

import numpy as np
from Curva import Curva,zspline
import matplotlib.pylot as plt
import math

#===================
# Cojunto de puntos
#===================
# Número de puntos
nump:np.int32 = 8
# Dimension
dim:np.int32 = 2
# Memoria para puntos
puntos = np.zeros(dim*nump,dtype = np.float64)
# Parametrización
X = np.linspace(0.0,2*np.pi,nump+1)
# Coordenada x
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
# Coordenada y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#==============================================================
# Curva Z-spline de n puntos zpline(p,d,n,m)
# p: puntos, d: dimension, n: segmentos de curva, m:continuidad
#==============================================================
n:np.int32 = 100
#x1,y1 = zspline(puntos,dim,n,2)
#x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(puntos,dim,n,0)
plt.plot(x3,y3,lw = 2, color = "orange")
#plt.plot(x2,y2, lw = 2, color = "red")
#plt.plot(x1,y1, lw = 2, color = "blue")
plt.scatter(puntos[0:nump],puntos[nump,2*nump],marker = "o", color = 'black')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Curva cerrada Z-spline en 2D")
plt.show()
