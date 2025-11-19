dati = []

with open('input.txt', 'r', encoding = 'utf-8') as fileInput:

    riga = fileInput.readline()
    while riga != '':
        valore = float(riga)
        dati.append(valore)
        riga = fileInput.readline()

print(dati)
with open('output.txt', 'w', encoding = 'utf-8') as fileOutput:
    for dato in dati:
        #fileOutput.write(f'{dato:8.2f}\n')
        print(f'{dato:8.2f}', file = fileOutput)

    fileOutput.write(f'Totale = {sum(dati):.2f}\nMedia = {sum(dati)/len(dati):.2f}')

