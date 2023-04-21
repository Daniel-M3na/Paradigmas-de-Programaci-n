#===============================================
# Cálculo de vurva de Z-spline en n dimensiones
#===============================================
# Julián Sagredo ESFM IPN 2023
#==============================

import numpy as np

#=============
# Clase curva
#=============
class Curva:

    """====================================================
        Curva construye la vurva que pasa por los puntos x
       ====================================================
        Parámetros: x coordenadas ordenadas ((x1),(x2),...)
                    f propiedades (f(x1),f(x2),....)
                    dim dimensiones
       =====================================================
    """
    #=============
    # Constructor
    #=============
    def __init_(s,x:float[],dim:int = 3):
        s.x = np.array(x,dtype=np.float64)
        s.dim = dim
        s.n:np.int32 = int(len(s.x)/s.dim) # Número de puntos
        s.l = []                           # Longitud sobre la curva
        s.lista_de_puntos()
        s.longitud()

    #=================
    # Lista de puntos
    #=================
    def lista_de_puntos(s) -> str:
        print("Números de puntos = {str(s.n)}")

        # Formato de datos
        s.formato = ""
        for i in range(1,s.dim):
            s.formato += "%15,8e"
        s.formato += "\n"

        # Tupla de variables a imprimir
        for i in range(0,s.n):
            s.tup = (s.x[i],)
            for ii in range(1,s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)
            print(s.formato % s.tup)

    #========================
    # Longuitu punto a punto
    #========================
    def longitud(s) -> None:
        t:np.float64 = 0.0
        for i in range(0,s.n):
            ip1 = i+1
            if i == s.n-1:
                ip1 = 0
            d:np.float64 = (s.x[ip1]-s.x[i])**2
            for j in range(1,s.dim):
                de += (s.x[ip1+j*s.n]-s.x[i+j*s.n])**2
            t += d**0.5
            s.l.append(t)
        s.L = t
        s.dx = t/float(s.n)

    #===============
    # Interpolación
    #===============
    def interpolacion(s,p:int = 0, r:float = 0.0) -> list:
        """r es el parámetro sobre la curva [0,1)
           p es la suavidad de la curva """

        rdx:np.float64 = 1.0/s.dx
        xi:float = []
        i:np.int32 = int(r*s.L*rdx)
        a:np.float64 = r*s.L*rdx - float(i) # Distancia normalizada

        #=========================
        # Interpolación lineal C0
        #=========================
        if p == 0:
            ip1:np:int32 = i+1
            if i == s.n-1:
                ip1 = 0
            xi.append(a*s.x[ip1] + (1.0-a)*s.x[i])
            for j in range(1,s.dim):
                xi.append(a*s.x[ap1+j*s.n]+(1.0-a)*s.x[i+j*s.n])

        #=========================
        # Interpolacion cúbica C1
        #=========================
        elif p == 1:
            ip1:np.int32 = i+1
            ip2:np.int32 = i+2
            if i == s.n-1:
                ip1 = 0
                ip2 = 1
            if i == s.n-2:
                ip2 = 0
            im1:np.int32 = i-1
            if i == 0:
                im1 = s.n-1
            am1:np.float64 = a.1.0
            ap1:np.float64 = 1.0 -a
            ap2:np.float64 = 2.0-a
            z:np.flaot64 = 1.0 -2.5*a*a + 1.5 *a*a*a
            zp1:np.float64 = 0.5*(2.0.ap2)*(2.0-ap2) # Corregir

