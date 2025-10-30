'''
stimare il valore di pi con metodo monte carlo
'''

import random
import math

CAMPIONI = 100000
nelCerchio = 0

# genereo casualmente punti nel quadrato [-1,1] e conto quelli nel cerchio
for i in range(0, CAMPIONI):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if math.sqrt( x * x + y * y) <= 1:
        nelCerchio += 1

piStimato = 4 * nelCerchio / CAMPIONI
print(f"{piStimato=} diff: {abs(math.pi - piStimato)}")