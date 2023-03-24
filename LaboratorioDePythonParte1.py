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














