# -*- coding: utf-8 -*-
from math import * #Para pi

from Classes import Quaternion
from Funcs import muestra_robot
# resoluci?n de la cinem?tica directa mediante cuaterniones

# o1=Q1*(0,r1)*Q1c
# o2=Q1*Q2*(0,r2)*Q2c*Q1c + o1

### INTRODUCCIÓN PARAMETROS (constantes + variables)
##  PARAMETROS 1º ESLABÓN
# Traslación
a1=10
r1 = Quaternion(0,a1,0,0) # cuaterniones de desplazamiento (Cuaternion puro)
#Rotación 
t1=float(input('valor de theta1 en grados  '))
t1=t1*pi/180
n1=[0,0,1]# vector de rotación
q1 = Quaternion.VectorRotacional(n1,t1) #cuaternion de rotación
q1c= ~q1 #q1 conjugado



##  PARAMETROS 2º ESLABÓN
# Traslación
a2=5
r2 = Quaternion(0,a2,0,0)
# Rotación
t2=float(input('valor de theta2 en grados  '))
t2=t2*pi/180
n2=[0,0,1]

q2=Quaternion.VectorRotacional(n2,t2) 
q2c=~q2



# introducción de las variables articulares
print('')




# calculo de los cuaterniones de rotación



o0 = Quaternion(0,0,0,0)
o0A = o0.toList()
# calculo del punto o1
o1 = q1 * r1 * q1c
o1A=o1.toList()

# calculo del punto o2
o2 = q1 *q2 * r2 * q2c * q1c + o1
o2A= o2.toList()


# impresi?n de los resultados
print('')
print('punto uno del robot')
print(o1A)
print('')
print('punto dos del robot')
print(o2A)

muestra_robot([o0A,o1A,o2A ])







