# -*- coding: utf-8 -*-
from math import * #Para pi

from Classes import Quaternion
from Funcs import muestra_robot
# resoluci?n de la cinem?tica directa mediante cuaterniones

# o1=Q1*(0,r1)*Q1c
# o2=Q1*Q2*(0,r2)*Q2c*Q1c + o1

### INTRODUCCIÓN PARAMETROS (constantes + variables)
##  PARAMETROS 1º ESLABÓN
#   Traslación
l1=float(input('valor de longitud1 en cm  '))
r1 = Quaternion(0,0,0,l1)
#   Rotación
t1=0
n1=[0,0,0]
q1 = Quaternion.VectorRotacional(n1,t1)
q1c = ~q1



##  PARAMETROS 2º ESLABÓN
#   Traslación
a2=5
r2 = Quaternion(0,a2,0,0)
#   Rotación
t2=float(input('valor de theta2 en grados  '))
t2=t2*pi/180
n2=[0,0,1]
q2 = Quaternion.VectorRotacional(n2,t2) #Cuaternion de rotación
q2c = ~q2



##  PARAMETROS 3º ESLABÓN
#   Traslación
l3=float(input('valor de longitud3 en cm  '))
r3 = Quaternion(0,l3,0,0)
#   Rotación
t3=0
n3=[0,0,0]
q3 = Quaternion.VectorRotacional(n3,t3)
q3c = ~q3



##  PARAMETROS 4º ESLABÓN
#   Traslación
a4=0
r4 = Quaternion(0,a4,0,0)
#   Rotación
t4=float(input('valor de theta4 en grados  '))
t4=t4*pi/180
n4=[1,0,0]
q4 = Quaternion.VectorRotacional(n4,t4)
q4c = ~q4



##  PARAMETROS los dos 5º ESLABÓN
#   Traslación
a5=2
r5=Quaternion(0,a5,0,0)
#   Rotación
t5=float(input('valor de theta5 en grados  '))
t5=t5*pi/180
# Para 5A 
n5A=[0,-1,0]
q5A = Quaternion.VectorRotacional(n5A,t5)
q5Ac = ~q5A
# Para 5B
n5B=[0,1,0]
q5B = Quaternion.VectorRotacional(n5B,t5)
q5Bc = ~q5B


### Calculo coordenadas de cada origen:
o0=Quaternion(0,0,0,0)
# calculo del punto o1
o1 = q1 * r1 * q1c 

# calculo del punto o2
o2 = (q1 *q2) * r2 * (q2c * q1c) + o1

# calculo del punto o3
o3 = (q1 * q2 * q3) * r3 * (q3c * q2c * q1c) + o2

# calculo del punto o4
o4 = (q1 * q2 * q3 * q4) * r4 * (q4c * q3c * q2c * q1c) + o3

# calculo del punto o5A
o5A = (q1 * q2 * q3 * q4 * q5A) * r5 * (q5Ac * q4c * q3c * q2c * q1c) + o4

# calculo del punto o5B
o5B = (q1 * q2 * q3 * q4 * q5B) * r5 * (q5Bc * q4c * q3c * q2c * q1c) + o4

o0A=o0.toList()
o1A=o1.toList()
o2A=o2.toList()
o3A=o3.toList()
o4A=o4.toList()
o5A_A=o5A.toList()
o5B_A=o5B.toList()
# impresi?n de los resultados
print('')
print('punto 0 del robot')
print(o0A)
print('punto 1 del robot')
print(o1A)
print('punto 2 del robot')
print(o2A)
print('punto 3 del robot')
print(o3A)
print('punto 4 del robot')
print(o4A)
print('punto 5_a del robot')
print(o5A_A)
print('punto 5_b del robot')
print(o5B_A)

muestra_robot([o0A,o1A,o2A,o3A,o4A, [[o5A_A],[o5B_A]] ])







