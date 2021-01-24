# -*- coding: utf-8 -*-
import numpy as np

from classes import Quaternion
from utils import show_robot, shows_origins

# ------ 1º articulación: Rotación --------
# Longitud y ángulo
t1 = float(input('Valor de theta1 en grados: '))
t1 = np.radians(t1)
a1 = 10

# Traslación
r1 = Quaternion(0, a1, 0, 0)

# Rotación 
n1 = [0, 0, 1]
q1 = Quaternion.rotationalVector(n1, t1)

# Conjugado
q1c = ~q1



# ------ 2º articulación: Rotación --------
t2 =float(input('Valor de theta2 en grados  '))
t2 = np.radians(t2)
a2 = 5

r2 = Quaternion(0, a2, 0, 0)

n2=[0, 0, 1]
q2=Quaternion.rotationalVector(n2, t2) 

q2c = ~q2


# ------ Cálculo de las articulaciones --------
o0 = Quaternion(0, 0, 0, 0)
o1 = q1 * r1 * q1c
o2 = (q1 * q2) * r2 * (q2c * q1c) + o1


# ------ Articulaciones como lista --------
o0_0 = o0.toList()
o1_0 = o1.toList()
o2_0 = o2.toList()

# ------ Resultados --------
shows_origins([ o0_0, o1_0, o2_0 ])
show_robot([ o0_0, o1_0, o2_0 ])
