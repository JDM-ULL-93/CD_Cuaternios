#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Robótica Computacional
# Grado en Ingeniería Informática (Cuarto)
# Práctica: Resolución de la cinemática directa mediante Denavit-Hartenberg.

# Ejemplo:
# ./cdDH.py 30 45

import sys
from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functools import reduce
import time
#from decTime import temporizadorGetTime, temporizador

# ******************************************************************************
# Declaración de funciones

def ramal(I,prev=[],base=0):
  # Convierte el robot a una secuencia de puntos para representar
  O = []
  if I:
    if isinstance(I[0][0],list):
      for j in range(len(I[0])):
        O.extend(ramal(I[0][j], prev, base or j < len(I[0])-1))
    else:
      O = [I[0]]
      O.extend(ramal(I[1:],I[0],base))
      if base:
        O.append(prev)
  return O

def muestra_robot(O,ef=[]):
  # Pinta en 3D
  OR = ramal(O)
  OT = np.array(OR).T
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  # Bounding box cúbico para simular el ratio de aspecto correcto
  max_range = np.array([OT[0].max()-OT[0].min()
                       ,OT[1].max()-OT[1].min()
                       ,OT[2].max()-OT[2].min()
                       ]).max()
  Xb = (0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten()
     + 0.5*(OT[0].max()+OT[0].min()))
  Yb = (0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten()
     + 0.5*(OT[1].max()+OT[1].min()))
  Zb = (0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten()
     + 0.5*(OT[2].max()+OT[2].min()))
  for xb, yb, zb in zip(Xb, Yb, Zb):
     ax.plot([xb], [yb], [zb], 'w')
  ax.plot3D(OT[0],OT[1],OT[2],marker='s')
  ax.plot3D([0],[0],[0],marker='o',color='k',ms=10)
  if not ef:
    ef = OR[-1]
  ax.plot3D([ef[0]],[ef[1]],[ef[2]],marker='s',color='r')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  plt.show()
  return

def arbol_origenes(O,base=0,sufijo=''):
  # Da formato a los origenes de coordenadas para mostrarlos por pantalla
  if isinstance(O[0],list):
    for i in range(len(O)):
      if isinstance(O[i][0],list):
        for j in range(len(O[i])):
          arbol_origenes(O[i][j],i+base,sufijo+str(j+1))
      else:
        print('(O'+str(i+base)+sufijo+')0\t= '+str([round(j,3) for j in O[i]]))
  else:
    print('(O'+str(base)+sufijo+')0\t= '+str([round(j,3) for j in O]))

def muestra_origenes(O,final=0):
  # Muestra los orígenes de coordenadas para cada articulación
  print('Orígenes de coordenadas:')
  arbol_origenes(O)
  if final:
    print('E.Final = '+str([round(j,3) for j in final]))

def matriz_T(d,theta,a,alpha):
  # Calcula la matriz T (ángulos de entrada en grados)
  th=theta*pi/180;
  al=alpha*pi/180;
  return [[cos(th), -sin(th)*cos(al),  sin(th)*sin(al), a*cos(th)]
         ,[sin(th),  cos(th)*cos(al), -sin(al)*cos(th), a*sin(th)]
         ,[      0,          sin(al),          cos(al),         d]
         ,[      0,                0,                0,         1]
         ]


def temporizador(func):
    def wrapper(args):
       print("Prueba con brazo robotico con {} articulaciones".format(args))
       start_time = time.perf_counter()
       func(args)
       end_time = time.perf_counter()
       print(end_time-start_time)
       return
    return wrapper
# ******************************************************************************




#pp = int(input('Numero de articulaciones del robot  '))
#cinDirMatrices(pp)
def multiplicaMatrix(matrix1,matrix2):
    I = len(matrix1)
    J = len(matrix2[0])
    K = len(matrix2)
    result = np.zeros((I,J))

    for i in range(I):
       # iterate through columns of Y
       for j in range(J):
           # iterate through rows of Y
           for k in range(K):
               result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Calcula el tiempo de recrear X puntos de X articulaciones con matrices
@temporizador
def cinDirMatrices(num):
    # Parámetros D-H:
    #        1    2
    d  = [0] * num
    th = [45] * num
    a  = [5] * num
    al = [0] * num

    # Orígenes para cada articulación
    origen = [0, 0, 0, 1]
    TX_Y = [matriz_T(d[i], th[i], a[i], al[i]) for i in range(num)] #Donde Y = X-1
    
    #Sin memorización --> O(n^2)
    TX_Yalreves = TX_Y[::-1]
    resultado = [[0, 0, 0, 1], np.dot(TX_Y[0], origen).tolist()]
    for i in range(1,num):
        res = reduce(lambda a, b: multiplicaMatrix(a, b), TX_Yalreves[:i])
        resultado.append(np.dot(res, origen).tolist())

    #Con memorización --> O(n)
    #resultado = [[0, 0, 0, 1]]
    #multp = TX_Y[0]
    #for i in range(0, num-1):
        #resultado.append(np.dot(multp, origen))
        #multp = multiplicaMatrix(multp,TX_Y[i+1])#np.dot(multp,TX_Y[i+1]) 
    # Mostrar resultado de la cinemática directa
    #muestra_origenes(resultado)
    #muestra_robot   (resultado)
    return

nA = [10, 100, 1000, 10000,100000, 1000000]
for n in nA:
    cinDirMatrices(n)




