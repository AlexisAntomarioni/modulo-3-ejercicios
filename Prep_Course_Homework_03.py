#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
print("punto 1")
nuemro = 134
print(nuemro)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print("punto 2")
print(type(8.5))






# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print("punto 3")
print(type(nuemro))




# 4) Crear una variable que contenga tu nombre

# In[2]:
aux_name ="Alexis Antomarioni"



# 5) Crear una variable que contenga un número complejo

# In[3]:
print("punto 5")
num_comp = 3 + 4j






# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print("punto 6")
print(type(num_comp))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import numpy

# In[1]:
pi = round(numpy.pi, 4)




# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
lo_mismo = True
lo_mismo2 = lo_mismo

# Ambas vaiables contienen el mismoresultado, son diferentes variables de un igual valor




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print("punto 9")
print(type(lo_mismo))
print(type(lo_mismo2))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

num_suma = 14 + 12.22




# 11) Realizar una operación de suma de números complejos

# In[2]:
print("punto 11")
num_comp = 2 + 3j
num_comp2 = 7 + 5j

print(num_comp + num_comp2)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
print("punto 12")
print(13.44 + num_comp2)




# 13) Realizar una operación de multiplicación

# In[5]:
print("punto 13")
print(34*3)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print("punto 14")
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
print("punto 15")
resul = 27 / 4
print(resul)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print("punto 16")
resul = int(resul)
print(resul)
print (27//4)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print("punto 17")
print(27%4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print("punto 18")
print (4*(27//4)+(27%4))




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
print("punto 19")
nombre = "Alexis"
apellido = "Antmarioni"
full_name = nombre + " " + apellido
print(full_name)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:#
# son dos tipos diferentes de datos, uno es str y el otro int por lo tanto son diferentes




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
aux = int("2")
#de esa manera convertiria el "2" en numero para poder compara sobre un mismo tipo




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

# En python para los numeros reales se utiliza el punto "." para separacion no la coma
 

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
print("punto 23")
aux = 3
aux -= 1
print (aux)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
aux = 1 < 2
print(aux)
#el resulta es la evalucion de la accion que arroja un dato boolean, el sistema numerico binario es el sistem utilizado por los datos booleanos





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
# es lo mismo que em uno delos ejerciocios anteriores, son dos datos diferentes, no se puede sumar un caracter y un numero, si los dos datos 
# son del mismo tipo siempre van a ser el mismo resultado





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
aux = "Repetir "
aux2 = 5
print(aux * aux2 + "por " + str(aux2))





