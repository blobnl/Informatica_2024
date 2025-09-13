dizionarioVuoto = {}
dizionario = {'primo': 'a', 'secondo':'b'}

dizionario['terzo'] = 'c'

for chiave in dizionario:
    print(chiave, dizionario[chiave], sep = ':')
    
for elemento in dizionario.items():
    print(elemento[0], elemento[1], sep = ':')

for (chiave, valore) in dizionario.items():
    print(chiave, valore, sep = ':')