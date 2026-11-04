'''
con le tuple si può fare assegnazione multipla di variabili
e.g.

(a,b,c) = (2,3,4)  --> a = 2  b = 3 c = 4

Come faccio a scambiare in maniera semplice due variabili?
Come faccio a scmabiare in maniera semplice due elementi di una lista

'''

lista = [1,2,3]

for (i,v) in enumerate(lista):
    print(i, v)
    
a = 10
b = 5

print(a,b)
a = b
b = a
print(a,b)