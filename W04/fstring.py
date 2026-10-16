'''
stringhe formattate
{valore:specificatore}
ampiezza: (intero) numero di caratteri totale 
allineamento: < > ^
segno: + -> forza segno
rappresentazione: s (str) d (int) f (float)
precisione: (solo per float) -> .n -> numero di cifre dopo la virgola

'''


lato = 10
area_quadrato = lato ** 2
flag = True
valore = 3.76876876867 / 34

#print("Il quadrato di lato", lato, "ha un'area di", area_quadrato)

# stampa di valori e loro quadrato, allineandoli in tabella

numero = 1
while numero < 10:
    print(f"{numero:15}{numero ** 2:15}")
    numero += 1