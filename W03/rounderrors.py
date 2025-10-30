import math

EPSILON = 1E-14

r = math.sqrt(2.0)
#if r * r == 2.0 :
#if abs(r * r - 2.0) < EPSILON:
if math.isclose(r * r, 2.0):
   print("sqrt(2.0) squared is 2.0")
else :
   print("sqrt(2.0) squared is not 2.0 but", r * r)

