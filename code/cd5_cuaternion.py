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
a1_z=5
a1_y=2
r1 = Quaternion(0,0,a1_y,a1_z)
#   Rotación
t1=float(input('valor de theta1 en grados  '))
t1=t1*pi/180
n1=[0,0,1]
q1 = Quaternion.VectorRotacional(n1,t1)
q1c = ~q1



##  PARAMETROS 2º ESLABÓN
#   Traslación
a2_x=3
a2_y=-2
r2 = Quaternion(0,a2_x,a2_y,0)
#   Rotación
t2=float(input('valor de theta2 en grados  '))
t2=t2*pi/180
n2=[0,-1,0]
q2 = Quaternion.VectorRotacional(n2,t2) #Cuaternion de rotación
q2c = ~q2



##  PARAMETROS 3º ESLABÓN
#   Traslación
a3=5
r3 = Quaternion(0,a3,0,0)
#   Rotación
t3=float(input('valor de theta3 en grados  '))
t3=t3*pi/180
n3=[1,0,0]
q3 = Quaternion.VectorRotacional(n3,t3)
q3c = ~q3



##  PARAMETROS de los 2 4º ESLABÓNes
#   Traslación
a4=1
r4 = Quaternion(0,a4,0,0)
#   Rotación
t4=float(input('valor de theta4 en grados  '))
t4=t4*pi/180
# Para 4A
n4A=[0,1,0]
q4A = Quaternion.VectorRotacional(n4A,t4)
q4Ac = ~q4A
# Para 4B
n4B=[0,-1,0]
q4B = Quaternion.VectorRotacional(n4B,t4)
q4Bc = ~q4B


### Calculo coordenadas de cada origen:
o0=Quaternion(0,0,0,0)
# calculo del punto o1
o1 = q1 * r1 * q1c

# calculo del punto o2
o2 = (q1 *q2) * r2 * (q2c * q1c) + o1

# calculo del punto o3
o3 = (q1 * q2 * q3) * r3 * (q3c * q2c * q1c) + o2 

# calculo del punto o4A
o4A = (q1 * q2 * q3 * q4A) * r4 * (q4Ac * q3c * q2c * q1c) + o3

# calculo del punto o4B
o4B = (q1 * q2 * q3 * q4B) * r4 * (q4Bc * q3c * q2c * q1c) + o3


o0A=o0.toList()
o1A=o1.toList()
o2A=o2.toList()
o3A=o3.toList()
o4A_A=o4A.toList()
o4B_A=o4B.toList()
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
print('punto 4A del robot')
print(o4A_A)
print('punto 4B del robot')
print(o4B_A)

muestra_robot([o0A,o1A,o2A,o3A,[[o4A_A],[o4B_A]] ])
#La visualización del resultado difiere un poco del real porque para 
#mantener el problema simple,no se han añadido puntos para dividir 
#las diferentes componentes del vector translación r (por ej, en r1,
#hay una translación en eje Y y eje Z al mismo tiempo, para repetir
#el aspecto del manipulador 5 del problema, crear un punto intermedio [01A]
#que solo reciba una translación en eje Y [r1_1A= Quaternion(0,a1_y,0)] para
#que la conexión de ese punto con el punto 2 sea una translación solo en 
#el eje Z [r1A_2= Quaternion(0,0,0,a1_z)])






