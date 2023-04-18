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
print(estudiante.nombre)

# Esto no funciona: print(estudiante.__nombre)

#=================
# Herencia
#=================
