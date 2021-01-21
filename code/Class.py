import math

class Quaternion:

  # Formato: w + x*i + y*j + z*k
  def __init__(self, w, x, y, z):  
    self.w = w
    self.x = x
    self.y = y
    self.z = z

  def copy(self,other):
    return Quaternion(other.w, other.x, other.y, other.z)

  # Operador '+'
  def __add__(self, other):
    return Quaternion(
      self.w + other.w,
      self.x + other.x,
      self.y + other.y,
      self.z + other.z
    )

  # Operador '*'
  def __mul__(self, other):
    return Quaternion(
      self.w *other.w - self.x*other.x - self.y*other.y - self.z*other.z,
      self.w *other.x + self.x*other.w + self.y*other.z - self.z*other.y,
      self.w *other.y - self.x*other.z + self.y*other.w + self.z*other.x,
      self.w *other.z + self.x*other.y - self.y*other.x + self.z*other.w 
    )
    
  # Operador '~'
  def __invert__(self):
    return Quaternion(
      self.w,
      -self.x,
      -self.y,
      -self.z
    )

  # Operador '[]'
  def __getitem__(self, key):
    # Switch (key):
    return {
      0: self.w,
      1: self.x,
      2: self.y,
      3: self.z
    }.get(key, float('inf'))  # Por defecto: Infinito


  def toList(self, decimals = 2):
    return [ round(self.x, decimals), round(self.y, decimals), round(self.z, decimals), round(self.w, decimals)]

  # vector: Vector unitario sobre el que se gira
  # theta: Radianes que se gira
  @staticmethod
  def VectorRotacional(vector, theta): 
    halfThetha = theta / 2
    sin_halfTheta = math.sin(halfThetha)

    return Quaternion(
      math.cos(halfThetha),
      vector[0] * sin_halfTheta,
      vector[1] * sin_halfTheta,
      vector[2] * sin_halfTheta,
    )


