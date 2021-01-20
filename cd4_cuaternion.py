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
a1=2
r1 = Quaternion(0,a1,0,l1)
#   Rotación
t1=0
n1=[0,0,0]
q1 = Quaternion.VectorRotacional(n1,t1)
q1c = ~q1



##  PARAMETROS 2º ESLABÓN
#   Traslación
a2=2
r2 = Quaternion(0,a2,0,0)
#   Rotación
t2=float(input('valor de theta2 en grados  '))
t2=t2*pi/180
n2=[0,0,1]
q2 = Quaternion.VectorRotacional(n2,t2) #Cuaternion de rotación
q2c = ~q2



##  PARAMETROS 3º ESLABÓN
#   Traslación
a3=0
r3 = Quaternion(0,a3,0,0)
#   Rotación
t3=float(input('valor de theta3 en grados  '))
t3=t3*pi/180
n3=[0,-1,0]
q3 = Quaternion.VectorRotacional(n3,t3)
q3c = ~q3



##  PARAMETROS 4º ESLABÓN
#   Traslación
a4=5
r4 = Quaternion(0,a4,0,0)
#   Rotación
t4=float(input('valor de theta4 en grados  '))
t4=t4*pi/180
n4=[1,0,0]
q4 = Quaternion.VectorRotacional(n4,t4)
q4c = ~q4



##  PARAMETROS los dos 5º ESLABÓNes
#   Traslación
a5=1
l5=float(input('valor de longitud5 en cm  '))
r5A=Quaternion(0,a5,0,l5)
r5B=Quaternion(0,a5,0,-l5)
#   Rotación
t5=0
n5=[0,0,0]
q5 =  Quaternion.VectorRotacional(n5,t5)
q5c = ~q5
##  PARAMETROS los dos 6º ESLABÓNes(diferencia solo en calculo)
#   Traslación
l6=float(input('valor de longitud6 en cm  '))
r6=Quaternion(0,l6,0,0)
#   Rotación
t6=0
n6=[0,0,0]
q6 =  Quaternion.VectorRotacional(n6,t6)
q6c = ~q6


### Calculo coordenadas de cada origen:
o0=Quaternion(0,0,0,0)

##Complejidad(Tn) : (2*x*y* + 1)n  . 
#Donde:
#       x = nº eslabones que preceden al actual + el actual,
#       y = 16 = multiplicaciones y sumas intrinsecas en multiplicación cuaterniones
# Conviene destacar que se puede optimizar, por ejemplo: 
# no se aprovechan multiplicaciones previas ya realizadas
#(un ejemplo de esta optimización se da usando las variables multp y multp_C para o1,o2 y o3)
# calculo del punto o1
o1 = q1 * r1 * q1c #3 2*1*y +1 = 3

multp = q1 * q2
multp_c =  q2c * q1c
# calculo del punto o2
o2 = multp * r2 * multp_c + o1 #2*2*y +1

multp = multp * q3
multp_c = q3c * multp_c
# calculo del punto o3
o3 = multp * r3 * multp_c + o2 #  2*3*y +1

multp = multp * q4
multp_c = q4c * multp_c
# calculo del punto o4
o4 = multp * r4 * multp_c + o3 # 2*4*y +1

multp = multp * q5
multp_c = q5c * multp_c
# calculo del punto o5A
o5A = multp * r5A * multp_c + o4 # 2*5*y +1
# calculo del punto o5B
o5B = multp * r5B * multp_c + o4

multp = multp * q6
multp = q6c * multp
# calculo del punto o6A
o6A = multp * r6 * q6c * multp_c + o5A
# calculo del punto o6B
o6B = multp * r6 * q6c * multp_c + o5B

o0A=o0.toList()
o1A=o1.toList()
o2A=o2.toList()
o3A=o3.toList()
o4A=o4.toList()
o5A_A=o5A.toList()
o5B_A=o5B.toList()
o6A_A=o6A.toList()
o6B_A=o6B.toList()
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
print('punto 6_a del robot')
print(o6A_A)
print('punto 5_b del robot')
print(o5B_A)
print('punto 6_b del robot')
print(o6B_A)

muestra_robot([o0A,o1A,o2A,o3A,o4A, [[o5A_A,o6A_A],[o5B_A,o6B_A]] ])
#La visualización del resultado difiere un poco del real porque para 
#mantener el problema simple, no se han añadido puntos para dividir 
#las diferentes componentes del vector translación r (por ej, en r1, hay una 
#translación en eje X y eje Z al mismo tiempo, para repetir el aspecto del 
#manipulador 4 del problema, crear un punto intermedio [01A] que solo reciba 
#una translación en eje X [r1_1A= Quaternion(0,a1,0,0)] para que la conexión
#de ese punto con el punto 2 sea una translación solo en
# el eje Z [r1A_2= Quaternion(0,0,0,l1)])






