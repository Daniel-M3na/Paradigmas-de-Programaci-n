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
print(type(t)) # entero
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

lista = [1, 2, 3, 4, 
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#===============================================================
#Identación estricta para procesos dependiente de : (dos puntos)
#===============================================================

if 10>5:
    print ("diez es mayor que cinco")
    print("otra indentación")
for i in lista:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
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

print(capitals.get("India"))
print(capitals.get("india"))


# Reportar llave y valor 
for k in capitals:
    print("Key =" + k + ",Value =" + capitals[k])

#Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romNums.keys())

#Reportar valores
print(romNums.values())

# Juicio de llaves (esta o no esta la llave en el diccionario)
print("I" in romNums)
print("X" in romNums)
print("XX" in romNums)

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
Nums = list(range(1,61))

for i in Nums:
    print(i)

#=======================================
# Incluir nuevos elementos en la lista
#=======================================
Nums.append(61)
Nums.append(62) 
Nums.append(61)
print(Nums)

#=============================
# Quitar elemento con indice i
#=============================
i = 61
del Nums[i]
print(Nums)

#================
# Borra la lista
#================
del Nums

#=============
# Sumar listas
#=============
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#================
# Llenado a mano
#================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#===============================
# Genera una tupla con la lista
#===============================
potencial = tuple(potencial)
print(potencial[100])


#===============================
# LABORATORIO DE PYTHON PARTE 3
#===============================
  
#================
# Condicionales
#================

precio = 50

#==============
# Si esto...
#==============
if precio <50:
    print('El precio es menor que 50')

#==========================
# Si no... si esto otro...
#==========================
elif precio > 50:
    print('El precio es mayor a 50')

#========================
# Si nada de lo anterior
#========================

else:
    print('El precio es 50')

precio = 50
cantidad = 5
total = precio*cantidad

#========================
# Condicionales anidados
#========================
if total > 100:
    if total > 500:
        print('Total es mayor que 500')
    else:
        if total < 500 and total > 400:
            print('Total es menor que 500 pero mayor que 400')
        elif total < 500 and total > 300:
            print('Total entre 300 y 500')
        else:
            print('Total entre 100 y 300')

#================================
# Condicion de igualdad con  ==
#================================ 
elif total == 100:
    print('Total es igual a 100')
else: 
    print('Total menor que 100')

#==============================================
# Contador mientras la condicion sea verdadera
#==============================================
num = 0
while num < 5:
    num = num + 1
    print('num = ',num)

num = 0
while num < 5:
    num += 1        #num += 1 es lo mismo que num = num + 1
    print('num = ', num)
    if num == 3:    #Condicion antes de salir del bucle
        break

num = 0
while num < 5:
    num += 1
    if num > 3:
        continue    #Evita lo que sigue, continua con las iteraciones
    print('num = ', num)

#==================
# Bucle sobre lista
#==================
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#=======================
# Bucle sobre un string
#=======================
for char in 'Hello':
    print(char)

#============================
# Bucle sobre un diccionario
# items = elementos
#============================
numNames = {1: 'One', 2: 'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#=========================
# Bucle sobre diccionario 
# key = llave
# value = valor
#==========================

for k,v in numNames.items():
    print("key =", k, ", value =", v)


#================
# Primera funcion
#================
def saludo():
    #===================================
    # Documentacion rapida de la funcion
    #===================================
    """Esta funcion saluda"""
    print('¡Quiuboles!, ¿como estas?')

#=======================
# Llamado de la funcion
#=======================
saludo()

#==============================
# S ejecuta pero no se asigna
#==============================
salida = saludo()

#==================
# Esto no funciona
#=================
print(salida)

#=======================
# Mostrar documentacion 
#=======================
# help()

#======================
# Función con argumento
#======================
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("Qué onda ese",nombre,"!")

salu2("Julián")
salu2("Ángel")

#==========================================
# Ahorrar trabajo del intérprete
# nombre: str la variable nombre es un str
#==========================================
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("¡Que onda ese",nombre ,"!")
saludos("Julián")
a = 123
print(type(a))
saludos(a)

#===============================
# FUnción con muchos argumentos
#===============================
def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola",nombre1,",",nombre2,",",nombre3)
saludos_multiples("Hugo","Paco","Luis")

#===========================================
# Funcion con cuaqluier numero de argumentos
#===========================================
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que quieras"""
    i = 0
    #=================================
    # end= es para ponerlo de corrido
    #=================================
    print("Hola",end="")
    while len(nombres)>i:
        #Ultimo nombre
        if (i== len(nombres)-1):
            print(nombres[i])
        else:
            #Cualquier otro nombre 
            print(nombres[i],end= "")
        i+=1

muchos_saludos("Bosco","Angel","David","Tamara","Mili","Edwin","Luis","Abigail")

def greet(firstname, lastname):
    print("Hello",firstname, lastname)

#============================================
# Llamar funcion con argumentos en desorden
#============================================
greet(lastname="Jobs", firstname="Steve") # Se pueden especificar las variables en desorden

#=====================================
# Funcion con argumentos escondidos **
#======================================
def greet(**person):
    #===================================================
    # persona tiene características firstname y lastname
    #===================================================
    print("Hello",person["firstname"],person["lastname"])

greet(firstname="Steve", lastname="Jobs")
greet(lastname="Jobs", firstname="Steve")
greet(firstname="Bill",lastname="Gates", age=55) # Se pueden pasar mas parametros de los necesarios


#======================
# Funcion con resultado
#======================

def suma(a,b):
    return a+b

#==================================
# Programacion funcional
# Se pueden funciones en funciones
#==================================
total = suma(5,suma(10,20))
print(total)

#================================================
# Calculo lambda
# nombre de la funcion = lambda variable: funcion
#================================================
x_al_cuadrado = lambda x:  x*x
a1 = x_al_cuadrado(5)
print(a1)

#===========================
# Lambda de varias variables
#===========================
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))

#=========================================
# Uso de alguna funcion anonima
# El argumento va afuera entre parentesis
#=========================================
print((lambda x: x*x)(6)) #Funcion anonima

#=============================
# Funcion con variable global
# EVITE EL EXCESO !!!!!
#=============================
name = "Steve"
def greet():
    global name # Para utilizar una varibale global (que viene del bloque)
    name = "Bill"
    print("Hello",name)

greet()

