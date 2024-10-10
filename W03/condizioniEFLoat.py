import math

dato = 2.0
radice = math.sqrt(dato)

print(dato, radice * radice)

if math.isclose(dato, radice * radice):
    print("uguali")
else:
    print("diversi")