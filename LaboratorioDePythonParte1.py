''' ESTE ES UN SUPER COMENTARIO DE INICIO DE A NUESTRO RESUMEN'''

#===============================
# LABORATORIO DE PYTHON PARTE 1
#===============================


#===================
#Operaciones básicas
#===================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) # raíz cuadrada.
print (10%2)
print (10%0.1) # exclusivo en python.

#=========================================
#Para saber el tipo de objeto se usa "type"
#=========================================

t=0
print(typetype(t)) # entero
t=3.6
print(type(t)) # real (flotante)
t=True
print(type(t)) # booleano (bool)

#===================
#Mensajes a pantalla
#===================

print   ("Este es un comando de python. ", "Este es otro enunciado.",t)
print('id: ',1)
print('First Name: ', 'Steve')
print('Last Name: ','Jobs')
print("Vamos a sumar esto"+"con esto otor")

#=============================================
#COntinuar una instrucción en varios renglones 
#=============================================

print("Hola"); print("tu!!") #Se considera mala práctica

#==============================================
#Usando paréntesis redondos, cuadrados o llaves
#se puede escribir en varios renglones
#==============================================

list = [1, 2, 3, 4, 
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8].[9,10,11,12] ]

print(list)
print(matriz)

#===============================================================
#Identación estricta para procesos dependiente de : (dos puntos)
#===============================================================

if 10>5:
    print ("diez es mayor que cinco")
    print("otra indentación")
for i in list:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20
        print("verdadero")
elif 5>3:   #comienza segundo condicional
    print ("esto no se imprimirá")
else:
    print ("aquí nunca llega")

#=========
#Funciones
#=========

def say_hello(name):
    print("Hello",name)
    print("Welcome to Python Tutorials")

say_hello("Daniel")



#===============================
# LABORATORIO DE PYTHON PARTE 2
#===============================

#====================
# Conjunto de Python
#====================
even_nums = {2, 4, 6, 8, 10}
print(even_nums)

#El bool no es parte del conjunto
emp = {1,'Steve', 10.5, True} # Conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#==================================
# Convertir secuencia a conjunto
# NO lo genera en orden
#==================================

s = set('Hello')
print(s)
s = set((1,2,3,4,5)) # Tupla a conjunto
print(s)

#===============================================
# De diccionario a conjunto: Conjunto de llaves
#===============================================

d = {1: 'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2 #Union
print(su)

si = s1&s2 #Interseccion
print(si)

sr = s1-s2 #Diferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2 #Diferencia simetrica
print(ss)


#=====================
# Uso de diccionarios 
#=====================

capitals = {"USA": "Washington D.C", "France": "Paris", "India": "New Delhi"}
print(capitals)

#===============
# Llave : Valor
#===============
#Diccionario vacio
d = {}

#Llave entera, valor string
numNames = {1: "One", 2: " Two", 3: "Three"}

#Llave real, valor string
decNames = {1.5: "One and Half", 2.5: "Two and Half", 3.5:"Three and half"}

#Llave tupla, valor string
items = {("Parker","Reynolds","Camlin"): "Pen", ("LG","Whirlpool","Samsung"): "Refrigerator"}

#Llave string, valor int
romNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romNums)
print(romNums["I"])

print(capitals.get("India")
print(capitals.get("india"))


# Reportar llave y valor 
for k in capitals:
    print("Key =" + k + "Value =", + capitals[K])

#Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romanNums.key())

#Reportar valores
print(romanNums.values())

# Juicio de llaves (esta o no esta la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNUms)
print("XX" in romanNums)

#=============================================
# Listas
# Las listas pueden ser de objetos diferentes
#=============================================
miprimerlista = [] # Lista vacia
print(miprimerlista)

#==================
# Llenado de lista
#==================
miprimerlista = {1, "Javier", 1.34, "Bosco", "Angel", "Abigail", True}
print(miprimerlista)

#=========================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#=========================
nums = list(range(1,61))

for i in nums:
    print(i)

#=======================================
# Incluir nuevos elementos en la lista
#=======================================
nums.append(61)
nums.append(62) 
nums.append(61)
print(nums)

#=============================
# Quitar elemento con indice i
#=============================
i = 61
del nums[i]
print[nums]

#================
# Borra la lista
#================
del nums

#=============
# Sumar listas
#=============
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2]

#================
# Llenado a mano
#================
pitencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#===============================
# Genera una tupla con la lista
#===============================
potencial = tuple(potencial)
print(potencial[100])












