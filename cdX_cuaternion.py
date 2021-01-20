# -*- coding: utf-8 -*-
from math import * #Para pi
import time
import random
from Classes import Quaternion
from Funcs import muestra_robot

def temporizador(func):
    def wrapper(args):
       print("Prueba con brazo robotico con {} articulaciones".format(args))
       start_time = time.perf_counter()
       func(args)
       end_time = time.perf_counter()
       print(end_time-start_time)
       return
    return wrapper

pp = int(input('Numero de articulaciones del robot  '))

@temporizador
def cinDirCuaternion(p):
    aX = [5] * p #aX = [random.randint(5, 10) for i in range(p)]
    tX = [45*pi/180] * p#tX = [random.randint(-360, 360)*pi/180 for i in range(p)]
    nX = [[0,0,1]]*p#nX = [[0,0,random.randint(-1,1)] for i in range(p)]


    origen = Quaternion(0,0,0,0)
    rX = [Quaternion(0,aX[0],0,0)] * p
    qX = [Quaternion.VectorRotacional(nX[0],tX[0])] * p
    qXc = [~qX[0]]*p

   
    #Con memorizáción, la complejidad del algoritmo es O(N)
    multp = qX[0]
    multp_C = qXc[0]
    Ox = [multp*rX[0]*multp_C+origen]
    for i in range(1,p):
        multp = multp * qX[i]
        multp_C = qXc[i] * multp_C
        Ox.append(multp * rX[i]* multp_C + Ox[i-1])
    return Ox

cinDirCuaternion(pp)