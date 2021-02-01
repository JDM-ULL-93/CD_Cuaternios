# -*- coding: utf-8 -*-
import numpy as np

import sys
from classes import Quaternion
from utils import show_robot, shows_origins

# ------ Variables ------

# Número de variables
number_var = 6 
if len(sys.argv) != number_var + 1:
  sys.exit('El número de articulaciones no es el correcto (' + str(number_var) + ')')


variable = [float(i) for i in sys.argv[1 : number_var + 1]]

l1 = variable[0]
t2 = np.radians(variable[1])
t3 = np.radians(variable[2])
t4 = np.radians(variable[3])
l5 = variable[4]
l6 = variable[5]


# ------ Traslación ------
r0P = Quaternion(0, 0, 0, l1)
r1 = Quaternion(0, 2, 0, 0)
r2 = Quaternion(0, 2, 0, 0)
r3 = Quaternion(0, 0, 0, 0)
r4 = Quaternion(0, 5, 0, 0)

r4A = Quaternion(0, 0, 0, l5)
r5A = Quaternion(0, 1, 0, 0)
r6A = Quaternion(0, l6, 0, 0)

r4B = Quaternion(0, 0, 0, -l5)
r5B = Quaternion(0, 1, 0, 0)
r6B = Quaternion(0, l6, 0, 0)

rEF = Quaternion(0, 1 + l6, 0, 0)


# ------ Rotación ------

# Eje de giro
n0P = [0, 0, 1]
n1 = [1, 0, 0]
n2 = [0, 0, 1]
n3 = [0, -1, 0]
n4 = [1, 0, 0]

n4A = [0, 0, 1]
n5A = [1, 0, 0]
n6A = [1, 0, 0]

n4B = [0, 0, -1]
n5B = [1, 0, 0]
n6B = [1, 0, 0]

nEF = [1, 0, 0]

# Cuaternión
q0P = Quaternion.rotationalVector(n0P, 0)
q1 = Quaternion.rotationalVector(n1, 0)
q2 = Quaternion.rotationalVector(n2, t2)
q3 = Quaternion.rotationalVector(n3, t3)
q4 = Quaternion.rotationalVector(n4, t4)

q4A = Quaternion.rotationalVector(n4A, 0)
q5A = Quaternion.rotationalVector(n5A, 0)
q6A = Quaternion.rotationalVector(n6A, 0)

q4B = Quaternion.rotationalVector(n4B, 0)
q5B = Quaternion.rotationalVector(n5B, 0)
q6B = Quaternion.rotationalVector(n6B, 0)

qEF = Quaternion.rotationalVector(nEF, 0)


# ------ Inverso ------
q0Pc = ~q0P
q1c = ~q1
q2c = ~q2
q3c = ~q3
q4c = ~q4

q4Ac = ~q4A
q5Ac = ~q5A
q6Ac = ~q6A

q4Bc = ~q4B
q5Bc = ~q5B
q6Bc = ~q6B

qEFc = ~qEF

# # ------ Cálculo de rotaciones acumuladas ------
# q0P_q1 = q0P * q1
# q0P_q2 = q0P_q1 * q2
# q0P_q3 = q0P_q2 * q3
# q0P_q4 = q0P_q3 * q4

# q0P_q4A = q0P_q4 * q4A
# q0P_q5A = q0P_q4A * q5A
# q0P_q6A = q0P_q5A * q6A

# q0P_q4B = q0P_q4 * q4B
# q0P_q5B = q0P_q4B * q5B
# q0P_q6B = q0P_q5B * q6B

# q0P_qEF = q0P_q4 * qEF


# ------ Cálculo de las articulaciones --------
o0 = Quaternion(0, 0, 0, 0)
o0P = q0P * r0P * q0Pc
o1 = (q0P * q1) * r1 * (q1c * q0Pc) + o0P
o2 = (q0P * q1 * q2) * r2 * (q2c * q1c * q0Pc) + o1
o3 = (q0P * q1 * q2 * q3) * r3 * (q3c * q2c * q1c * q0Pc) + o2
o4 = (q0P * q1 * q2 * q3 * q4) * r4 * (q4c * q3c * q2c * q1c * q0Pc) + o3

o4A = (q0P * q1 * q2 * q3 * q4 * q4A) * r4A * (q4Ac * q4c * q3c * q2c * q1c * q0Pc) + o4
o5A = (q0P * q1 * q2 * q3 * q4 * q4A * q5A) * r5A * (q5Ac * q4Ac * q4c * q3c * q2c * q1c * q0Pc) + o4A
o6A = (q0P * q1 * q2 * q3 * q4 * q4A * q6A) * r6A * (q6Ac * q5Ac * q4Ac * q4c * q3c * q2c * q1c * q0Pc) + o5A

o4B = (q0P * q1 * q2 * q3 * q4 * q4B) * r4B * (q4Bc * q4c * q3c * q2c * q1c * q0Pc) + o4
o5B = (q0P * q1 * q2 * q3 * q4 * q4B * q5B) * r5B * (q5Bc * q4Bc * q4c * q3c * q2c * q1c * q0Pc) + o4B
o6B = (q0P * q1 * q2 * q3 * q4 * q4B * q6B) * r6B * (q6Bc * q5Bc * q4Bc * q4c * q3c * q2c * q1c * q0Pc) + o5B

oEF = (q0P * q1 * q2 * q3 * q4 * qEF) * rEF * (qEFc * q4c * q3c * q2c * q1c * q0Pc) + o4


# ------ Articulaciones como lista --------

o0_0 = o0.toList() 
o0P_0 = o0P.toList() 
o1_0 = o1.toList() 
o2_0 = o2.toList() 
o3_0 = o3.toList() 
o4_0 = o4.toList() 

o4A_0 = o4A.toList() 
o5A_0 = o5A.toList() 
o6A_0 = o6A.toList() 

o4B_0 = o4B.toList() 
o5B_0 = o5B.toList() 
o6B_0 = o6B.toList() 

oEF_0 = oEF.toList() 


# ------ Resultados --------
shows_origins([ o0_0, o1_0, o2_0, o3_0, o4_0, [[o5A_0, o6A_0], [o5B_0, o6B_0]] ], oEF_0)
show_robot([ o0_0, o0P_0, o1_0, o2_0, o3_0, o4_0, [[o4A_0, o5A_0, o6A_0], [o4B_0, o5B_0, o6B_0]] ], oEF_0)

# Se tiene que agregar un punto auxiliar, ya que hay una traslación en dos ejes
# al mismo tiempo (x, z). El punto agregado es o0P





