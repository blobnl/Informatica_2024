# stampare elementi lista concatenati
# el1 sep el2 sep eln

lista = [1, 2, 3, 4, 5]
separatore = " :: "
result = ""

for i in range(len(lista)):
    valore = str(lista[i])
    if i > 0:
        result = result + separatore
    result = result + valore

print(result)

listaStringhe = []
for elemento in lista:
    listaStringhe.append(str(elemento))

stampa = separatore.join(listaStringhe)
print(stampa)
