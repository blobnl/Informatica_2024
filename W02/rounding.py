'''
attenzione ai float e agli arrotondamenti
'''
import math

print(0.1 + 0.2)

valore = 3.0
radice = math.sqrt(valore)

EPSILON = 0.000000001

#if radice * radice == valore:
#if abs(radice * radice - valore) < EPSILON:
if math.isclose(radice * radice, valore) :
    print("Corretto")
else:
    print("sbagliato...")
