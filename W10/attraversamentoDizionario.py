'''
opzioni per "attraversamento" contenuti di un dizionario
'''

contatti = {'Carlo': 349456789, 'Anna': 789456123, 
            'Giorgio':159483267, 'Lucia':19685742}

print('\nAccesso per chiave')
for key in contatti:
    print(f'chiave = {key} : valore = {contatti[key]}')


print('\nAccesso per chiave (esplicito)')
for key in contatti.keys():
    print(f'chiave = {key} : valore = {contatti[key]}')


print('\nAccesso per chiave ordinata')
for key in sorted(contatti):
    print(f'chiave = {key} : valore = {contatti[key]}')


print('\nAccesso per elemento (chiave,valore)')
for (key, value) in contatti.items():
    print(f'chiave = {key} : valore = {value}')

    
print('\nAccesso per elemento (chiave,valore)')
for elemento in contatti.items():
    print(f'chiave = {elemento[0]} : valore = {elemento[1]}')


print('\nAccesso ai soli valori')
for value in contatti.values():
    print(f'valore = {value}')