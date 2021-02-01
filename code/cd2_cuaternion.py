# -*- coding: utf-8 -*-
import numpy as np

from classes import Quaternion
from utils import show_robot, shows_origins

# ------ 1º articulación: Rotación --------
t1 = float(input('Valor de theta1 en grados: '))
t1 = np.radians(t1)
a1 = 5

r1 = Quaternion(0, 0, 0, a1)

n1 = [0, 0, 1]
q1 = Quaternion.rotationalVector(n1, t1)

q1c = ~q1


# ------ 2º articulación: Desplazamiento --------
l2 = float(input('Valor de Longitud2 en metros: '))
t2 = 0

r2 = Quaternion(0, l2, 0, 0)

n2 = [1, 0, 0]
q2 = Quaternion.rotationalVector(n2, t2)

q2c = ~q2


# ------ 3º articulación: Rotación --------
t3 = float(input('Valor de theta3 en grados: '))
t3 = np.radians(t3)
a3 = 2

r3 = Quaternion(0, a3, 0, 0)

n3 = [0, -1, 0]
q3 = Quaternion.rotationalVector(n3, t3)

q3c = ~q3



# ------ Cálculo de las articulaciones --------
o0 = Quaternion(0, 0, 0, 0)
o1 = q1 * r1 * q1c
o2 = (q1 * q2) * r2 * (q2c * q1c) + o1
o3 = (q1 * q2 * q3) * r3 * (q3c * q2c * q1c) + o2


# ------ Articulaciones como lista --------
o0_0 = o0.toList()
o1_0 = o1.toList()
o2_0 = o2.toList()
o3_0 = o3.toList()

# ------ Resultados --------
shows_origins([ o0_0, o1_0, o2_0, o3_0 ])
show_robot([ o0_0, o1_0, o2_0, o3_0 ])
