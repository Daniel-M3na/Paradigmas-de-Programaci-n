#===================================
# PROGRAMACIÓN ORIENTEADA A OBJETOS
#===================================

#=================================
# Una clase para un objeto vacio
# No está tan vacio, necesita
# la palabra pass = pasar
#=================================

class ObjetoVacio:
    pass

#========================
# Nada es un ObjetoVacio
#========================

nada = ObjetoVacio()
print(type(nada))

#=================
# La clase llanta
#=================
class Llanta:
    #=====================================
    # Variable cienta es de toda la clase
    #=====================================
    cuenta = 0
    #======================================
    # Función constructura de identidad
    # __init__ es una función reservada
    # comeinza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #======================================
    def __init__(self, rad = 50, wth = 30, prss = 1.5):
        #Variable de la estructura completa llanta
        Llanta.cuenta += 1
        #Variables exclusivas de cada objeto
        self.rad = rad
        self.wth = wth
        self.prss = prss

#========================
# Objetos (instanciados)
#========================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(prss = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#==================================
# Objeto que contiene otros objetos
#==================================
class Coche:
    def __init__(self,ll1,ll2,ll3,ll4):
        self.llanta1 = ll1
        self.llanta2 = ll2
        self.llanta3 = ll3
        self.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: ",Llanta.cuenta) # Variable global de la clase
print("Presión de la llanta 4: ",llanta4.prss) #Presión de la llanta 4
print("Radio de la llanta 4: ", llanta4.rad)
print("Radio de la llanta 3: ",llanta3.rad)
print("Presión de la llanta 1 de mi coche: ",micoche.llanta1.prss)

#=================
# Encapsulamiento
#=================

class Estudiante:
    def __init__(self):
        self.name = ''
    def ponerme_nombre(self,name):
        print("Se llamó a ponerme_nombre")
        self.__name = name
    def obtener_nombre(self):
        print("Se llamó a obtener_nombre")
        return self.__name
    name = property(obtener_nombre,ponerme_nombre)

#====================================
# Crear objeto estudiante sin nombre
#====================================
estudiante = Estudiante()

#======================================================================
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explícitamente la función)
#=======================================================================
estudiante.name = "Diego"

#==================================================================
# Obtener el nombre con el método obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explícitamente a la función obtener_nombre
#==================================================================
print(estudiante.name)

# Esto no funciona: print(estudiante.__nombre)

#===================
# Herencia de clases
#===================
class Cuadrilatero:
    def __init__(self,a,b,c,d):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
        self.lado4 = d

    def perimetro(self):
        p = self.lado1 + self.lado2 + self.lado3 + self.lado4
        print("Perimetro:",p)
        return p

#====================================
# Su hijo rectángulo
# Rectángulo es hijo de Cuadrilátero
# Rectángulo (Cuadrilátero)
#====================================
class Rectangulo(Cuadrilatero):
    def __init__(self,a,b):
        #=========================
        # Constructor de su madre
        #=========================
        super().__init__(a,b,a,b)

#=====================
# Su nietro Cuadrado
# Hijo de rectángulo
#=====================
class Cuadrado(Rectangulo):
    def __init__(self,a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

    # def perimetro(self):
    #   p = 4.0*self.lado1
    #   print("Perimetro:",p)
    #   return p

#===================
# Crear un cuadrado
#===================
cuadrado1 = Cuadrado(5)

#======================================================
# Llamar al método perímetro de su abuelo Cuadrilátero
#======================================================
perimetro1 = cuadrado1.perimetro()

#================================
# Llamar a su propio método área
#================================
area1= cuadrado1.area()

print("Perímetro =",perimetro1)
print("Area =",area1)

#================================================================
# Sobre-escribir un método de su madre o abuela o tatarabuela...
# Es volver a definir una función ya existente
#================================================================

#======================================
# La clase A tiene tres números reales
#======================================
class A:
    __a: float = 0.0
    __b: float = 0.0
    __c: float = 0.0

    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

#=====================================
# La clase B tiene dos números reales
#=====================================
class B:
    __d:float = 0.0
    __e:float = 0.0

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e

        #========================================
        # Método sumar todo (internos + externos)
        #========================================
        def sumar_todo(self,aa:float,bb:float):
            x:float = self.d + self.e +aa + bb
            return x

#============
# ASOCIACIÓN
#============
# Usando objetos independientes

objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)
#print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#============================================
# El objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
#=============================================
class C:
    __d:float = 0.0
    __e:float = 0.0
    __Aa:A = None

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        # A está intanciado adentro
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#=============================
# COMPOSICIÓN
# Contiene otro objeto dentro
#=============================
objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())


#==========================================
# Objeto D tiene dos reales y un objeto A
# definido por fuera
#==========================================
class D:
    __d:float = 0.0
    __e:float = 0.0
    __Aa:A = None

    def __init__(self,d:float,e:float,Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x:float = self.d +self.e +self.Aa.a +self.Aa.b
        return x

#=========================================
# AGREGACIÓN
# Construye el objeto agregado por fuera
#=========================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())

