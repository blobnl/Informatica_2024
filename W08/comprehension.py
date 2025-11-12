listaInteri = [1,2,3,4,5]
listaStr = [str(valore) for valore in listaInteri]

print(", ".join(listaStr))

righe = 'ABCD'
colonne = '123'

caselle = [r + c for r in righe
    for c in colonne 
    ]

print(caselle)