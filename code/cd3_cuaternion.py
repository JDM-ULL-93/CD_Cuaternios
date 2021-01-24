# -*- coding: utf-8 -*-
import numpy as np

from classes import Quaternion
from utils import show_robot, shows_origins

# ------ 1º articulación: Desplazamiento --------
l1 = float(input('Valor de longitud1 en metros: '))
t1 = 0

r1 = Quaternion(0, 0, 0, l1)

n1 = [0, 0, 1]
q1 = Quaternion.rotationalVector(n1, t1)

q1c = ~q1


# ------ 2º articulación: Rotación --------
t2 = float(input('Valor de theta2 en grados: '))
t2 = np.radians(t2)
a2 = 5

r2 = Quaternion(0, a2, 0, 0)

n2 = [0, 0, 1]
q2 = Quaternion.rotationalVector(n2, t2)

q2c = ~q2


# ------ 3º articulación: Desplazamiento --------
l3 = float(input('Valor de longitud3 en metros: '))
t3 = 0

r3 = Quaternion(0, l3, 0, 0)

n3 = [1, 0, 0]
q3 = Quaternion.rotationalVector(n3, t3)

q3c = ~q3


# ------ 4º articulación: Rotación --------
t4 = float(input('Valor de theta4 en grados: '))
t4 = np.radians(t4)
a4 = 0

r4 = Quaternion(0, a4, 0, 0)

n4 = [1, 0, 0]
q4 = Quaternion.rotationalVector(n4, t4)

q4c = ~q4


# ------ 5º articulación: Ramal con rotación --------
t5 = float(input('Valor de theta5 en grados: '))
t5 = np.radians(t5)
a5 = 2

r5 = Quaternion(0, a5, 0, 0)

# 5A
n5A = [0, -1, 0]
q5A = Quaternion.rotationalVector(n5A, t5)

q5Ac = ~q5A

# 5B
n5B = [0, 1, 0]
q5B = Quaternion.rotationalVector(n5B, t5)

q5Bc = ~q5B

# EF
nEF = [0, 1, 0]
qEF = Quaternion.rotationalVector(nEF, 0)

qEFc = ~qEF


# ------ Cálculo de las articulaciones --------
o0 = Quaternion(0, 0, 0, 0)
o1 = q1 * r1 * q1c
o2 = (q1 * q2) * r2 * (q2c * q1c) + o1
o3 = (q1 * q2 * q3) * r3 * (q3c * q2c * q1c) + o2
o4 = (q1 * q2 * q3 * q4) * r4 * (q4c * q3c * q2c * q1c) + o3
o5A = (q1 * q2 * q3 * q4 * q5A) * r5 * (q5Ac * q4c * q3c * q2c * q1c) + o4
o5B = (q1 * q2 * q3 * q4 * q5B) * r5 * (q5Bc * q4c * q3c * q2c * q1c) + o4
oEF = (q1 * q2 * q3 * q4 * qEF) * r5 * (qEFc * q4c * q3c * q2c * q1c) + o4



# ------ Articulaciones como lista --------
o0_0 = o0.toList()
o1_0 = o1.toList()
o2_0 = o2.toList()
o3_0 = o3.toList()
o4_0 = o4.toList()
o5A_0 = o5A.toList()
o5B_0 = o5B.toList()
oEF_0 = oEF.toList()

# ------ Resultados --------
shows_origins([ o0_0, o1_0, o2_0, o3_0, o4_0, [[o5A_0], [o5B_0]] ], oEF_0)
show_robot([ o0_0, o1_0, o2_0, o3_0, o4_0, [[o5A_0], [o5B_0]] ], oEF_0)
