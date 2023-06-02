import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

#-------------------------------------------------------
# Número de celdas
n = np.array([512,512])
# Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0])
# Constante de difusión
k = 0.2
# Pasos de tiempo
pasos = 100
#--------------------------------------------------------

# Tamaño de celdas
dx = L/n
udx2 = 1.0/(dx*dx)
#Paso de tiempo
dt = 0.25*(min(dx[0],dx[1])**2)/k
print("dt = ", dt)
# Total de celdas
nt = n[0]*n[1]
print("Celdas = ",nt)
# Llenar la solución con ceros
u = np.zeros(nt, dtype = np.float64) # arreglo de lectura
un = np.zeros(nt, dtype = np.float64) # arreglo de escritura

def evolucion(u,n,udx2,dt,i,k):
    jp1 = i + n[0]
