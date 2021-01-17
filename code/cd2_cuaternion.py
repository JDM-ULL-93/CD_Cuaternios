# -*- coding: utf-8 -*-
from math import * #Para pi

from Classes import Quaternion
from Funcs import muestra_robot
# resoluci?n de la cinem?tica directa mediante cuaterniones

# o1=Q1*(0,r1)*Q1c
# o2=Q1*Q2*(0,r2)*Q2c*Q1c + o1

## INTRODUCCIÖN VARIABLES
# parametros primer eslabón
a1=5
t1=float(input('valor de theta1 en grados  '))
t1=t1*pi/180
# parametro segundo eslabón
l2=float(input('valor de Longitud2 en m  '))
t2 = 0
# parametro tercer eslabón
a3 = 2
t3 = float(input('valor de theta3 en grados  '))
t3=t3*pi/180

## DEFINICIÓN VARIABLES
# cuaterniones de desplazamiento
r1 = Quaternion(0,0,0,a1)
r2 = Quaternion(0,l2,0,0)
r3 = Quaternion(0,a3,0,0)

# vectores de rotación
n1=[0,0,1]
n2=[0,0,0]
n3=[0,-1,0]

# calculo de los cuaterniones de rotación
q1 = Quaternion.VectorRotacional(n1,t1)
q1c= ~q1 #q1 conjugado

q2=Quaternion.VectorRotacional(n2,t2) 
q2c=~q2

q3=Quaternion.VectorRotacional(n3,t3) 
q3c=~q3

o0=Quaternion(0,0,0,0)
# calculo del punto o1
o1 = q1 * r1 * q1c
o1A=o1.toList()

# calculo del punto o2
o2 = (q1 *q2) * r2 * (q2c * q1c) + o1
#i2 = q1 * q2 * r2 * q2c * q1c
#o2 = o1 + i2
o2A=o2.toList()

# calculo del punto o3
o3 = (q1 * q2 * q3) * r3 * (q3c * q2c * q1c) + o2
#i3 = q1 * q2 * q3 * r2 * r3 * q3c * q2c * q1c
#o3 = o2 + i3
o3A=o3.toList()


o0A=o0.toList()
o1A=o1.toList()
o2A=o2.toList()
o3A=o3.toList()
# impresi?n de los resultados
print('')
print('punto uno del robot')
print(o0A)
print('punto uno del robot')
print(o1A)
print('punto dos del robot')
print(o2A)
print('punto tres del robot')
print(o3A)
muestra_robot([o0A,o1A,o2A,o3A ])







