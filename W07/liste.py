valori = [12,45, 67, 89, -1]

# ciclare su tutti gli elementi
# ciclo su elementi della lista

for dato in valori:
    print(dato)

print()

for indice in range(len(valori)):
    print(valori[indice])

    
print()

for (indice,dato) in enumerate(valori):
    print(f'{indice}:{dato}')
