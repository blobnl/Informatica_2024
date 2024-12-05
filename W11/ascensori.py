'''
L’azienda XYZ vuole lanciare una campagna di risparmio energetico, chiedendo a tutti i lavoratori della sua sede di Torino 
di usare l’ascensore soltanto per salire tra i piani e usare le scale per scendere tra i piani. Prima di promuovere 
l’iniziativa, l’azienda XYZ vi chiede di sviluppare un programma per stimare il reale risparmio energetico ottenibile 
con questa iniziativa.
Scrivete un programma che legga da file una serie di due interi (piano di partenza e piano di arrivo dello spostamento 
di un dipendente) e in uscita stampi la differenza di consumo energetico usando l’ascensore sempre o solo per gli 
spostamenti in salita. 
L’azienda ha un solo ascensore, che inizialmente si trova al piano 0, e lo spostamento di un piano richiede un 
consumo di 100W
Gli spostamenti nell’arco di una giornata sono stati registrati in un file «piani.txt» che contiene per ogni riga due interi:
<piano di chiamata> <piano di arrivo>


ALGORITMO:
---------
per ogni riga nel file
    leggi partenza e arrivo
    aggiorna sìascesore senza risparmio
    se partenza < arrvo
        aggiorna ascensore con risparmio

stampa report

(piano, spostamenti)
spostamenti -> abd(partenza - piano) + abs(arrivo - partenza)


'''

WATT = 100

def aggiorna(ascensore, partenza, arrivo):
    spostamenti = abs(ascensore['piano'] - partenza) + abs(partenza - arrivo)
    ascensore['sp'] += spostamenti
    ascensore['piano'] = arrivo

def main():
    sr = {'piano': 0, 'sp': 0}
    cr = {'piano': 0, 'sp': 0}

    with open('movimenti.txt', 'r') as file:
        for line in file:
            parti = line.strip().split()
            partenza = int(parti[0])
            arrivo = int(parti[1])

            aggiorna(sr, partenza, arrivo)
            if partenza < arrivo:
                aggiorna(cr, partenza, arrivo)

    print('senza risparmio\n', sr)
    print('con risparmio\n', cr)

main()