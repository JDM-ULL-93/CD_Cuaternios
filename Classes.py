from math import *

class Quaternion:

    def __init__(self, w,x,y,z): #w + x*i + y*j + z*k 
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    def copy(self,other):
        return Quaternion(other.w,other.x,other.y,other.z)

    def __add__(self, other):
        return Quaternion(
            self.w + other.w,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )
    def __mul__(self, other):
           return Quaternion(
               self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z,
               self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y,
               self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x,
               self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w 
               )
    
    def __invert__(self): #Conjugado
        return Quaternion(
            self.w,
            -self.x,
            -self.y,
            -self.z
            )

    def __getitem__(self, key):#Override [] operator
         return { #switch (key):
            0: self.w, #case 1...
            1: self.x, #case 2
            2: self.y,
            3: self.z
        }.get(key, float('inf'))  #default: -1

    def toList(self, decimals = 2):
        return [ round(self.x, decimals), round(self.y, decimals), round(self.z, decimals), round(self.w, decimals)]

    @staticmethod
    def VectorRotacional(vector, theta): #vector: vector unitario que indica dirección del giro, theta = Radianes que gira el vector 'vector'
        halfThetha = theta/2
        sin_halfTheta = sin(halfThetha)
        return Quaternion(
            cos(halfThetha),
            vector[0]*sin_halfTheta,
            vector[1]*sin_halfTheta,
            vector[2]*sin_halfTheta,
            )


