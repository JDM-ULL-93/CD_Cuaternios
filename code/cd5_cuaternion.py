# -*- coding: utf-8 -*-
import numpy as np

import sys
from classes import Quaternion
from utils import show_robot, shows_origins

# ------ Variables ------

# Número de variables
number_var = 4 
if len(sys.argv) != number_var + 1:
  sys.exit('El número de articulaciones no es el correcto (' + str(number_var) + ')')


variable = [float(i) for i in sys.argv[1 : number_var + 1]]

t1 = np.radians(variable[0])
t2 = np.radians(variable[1])
t3 = np.radians(variable[2])
t4 = np.radians(variable[3])


# ------ Traslación ------
r0P = Quaternion(0, 0, 0, 5)
r1 = Quaternion(0, 0, 2, 0)
r1P = Quaternion(0, 3, 0, 0)
r2 = Quaternion(0, 0, -2, 0)
r3 = Quaternion(0, 5, 0, 0)

r4A = Quaternion(0, 1, 0, 0)
r4B = Quaternion(0, 1, 0, 0)

rEF = Quaternion(0, 1, 0, 0)


# ------ Rotación ------

# Eje de giro
n0P = [0, 0, 1]
n1 = [0, 1, 0]
n1P = [0, -1, 0]
n2 = [0, -1, 0]
n3 = [1, 0, 0]

n4A = [0, -1, 0]
n4B = [0, 1, 0]

nEF = [0, 1, 0]

# Cuaternión
q0P = Quaternion.rotationalVector(n0P, t1)
q1 = Quaternion.rotationalVector(n1, 0)
q1P = Quaternion.rotationalVector(n1P, t2)
q2 = Quaternion.rotationalVector(n2, 0)
q3 = Quaternion.rotationalVector(n3, t3)

q4A = Quaternion.rotationalVector(n4A, t4)
q4B = Quaternion.rotationalVector(n4B, t4)

qEF = Quaternion.rotationalVector(nEF, 0)


# ------ Inverso ------
q0Pc = ~q0P
q1c = ~q1
q1Pc = ~q1P
q2c = ~q2
q3c = ~q3

q4Ac = ~q4A
q4Bc = ~q4B

qEFc = ~qEF


# ------ Cálculo de las articulaciones --------
o0 = Quaternion(0, 0, 0, 0)
o0P = q0P * r0P * q0Pc
o1 = (q0P * q1) * r1 * (q1c * q0Pc) + o0P
o1P = (q0P * q1 * q1P) * r1P * (q1Pc * q1c * q0Pc) + o1
o2 = (q0P * q1 * q1P * q2) * r2 * (q2c * q1Pc * q1c * q0Pc) + o1P
o3 = (q0P * q1 * q1P * q2 * q3) * r3 * (q3c * q2c * q1Pc * q1c * q0Pc) + o2

o4A = (q0P * q1 * q1P * q2 * q3 * q4A) * r4A * (q4Ac * q3c * q2c * q1Pc * q1c * q0Pc) + o3
o4B = (q0P * q1 * q1P * q2 * q3 * q4B) * r4B * (q4Bc * q3c * q2c * q1Pc * q1c * q0Pc) + o3

oEF = (q0P * q1 * q1P * q2 * q3 * qEF) * rEF * (qEFc * q3c * q2c * q1Pc * q1c * q0Pc) + o3


# ------ Articulaciones como lista --------
o0_0 = o0.toList() 
o0P_0 = o0P.toList() 
o1_0 = o1.toList() 
o1P_0 = o1P.toList() 
o2_0 = o2.toList() 
o3_0 = o3.toList() 

o4A_0 = o4A.toList() 
o4B_0 = o4B.toList() 

oEF_0 = oEF.toList() 


# ------ Resultados --------
shows_origins([ o0_0, o1_0, o2_0, o3_0, [[o4A_0], [o4B_0]] ], oEF_0)
show_robot([ o0_0, o0P_0, o1_0, o1P_0, o2_0, o3_0, [[o4A_0], [o4B_0]] ], oEF_0)

# Se tiene que agregar dos puntos auxiliares, ya que hay traslaciones en dos ejes
# al mismo tiempo (z, y) y (x, y). Los puntos agregados son o0P y o1P.
