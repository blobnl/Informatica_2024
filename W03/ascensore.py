'''
condizioni: if condizione: ..... else: .....


scrivere un programma che simuli il controllo di un ascensore americano (no piano 13...)
input -> tasto premuto
output -> piano reale

leggi il piano
se il piano di arrivo è > 13
    pianoreale = piano - 1
altrimenti 
    painorale = piano

'''

piano = int(input("Inserire il piano di arrivo: "))

if piano > 13:
    pianoReale = piano - 1
else:
    pianoReale = piano
    

print("Piano reale = ", pianoReale)

