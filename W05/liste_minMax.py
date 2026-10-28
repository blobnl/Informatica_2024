'''
trovare minimo e massimo su lista
'''

lista = [3, 12, 67, -34, -7, 123, 8, -11]
massimo = lista[0]
for i in range(1,len(lista)):
    if lista[i] > massimo:
        massimo = lista[i]
        
print(f"Massimo = {massimo}")

print(f"Massimo = {max(lista)} Minimo = {min(lista)}")
