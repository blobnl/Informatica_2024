'''
1. scomporre il numero in blocchi
2. per ogni blocco, tradurre il numero del blocco e inserire 
valore del blocco

'''


def main():
    numero = int(input("Inserire cifra: "))
    stringa = ''
    blocco = 0
    while numero > 0:
        valore = numero % 1000
        numero = numero // 1000
        stringa = converti(valore) + " " + peso(blocco) + " " + stringa
        blocco += 1

    print(stringa)

'''
1. se >= 100
    codifica centinaia estrai resto
2. se >= 20
    codifica decina e estrai ersto (unità)
altrimenti se valore >= 10
    codifica teen
    resto = 0
3. se resto > 0
    codifica unità
'''

def converti(valore):
    nome = ''

    if valore >= 100:
        centinaia = valore // 100
        valore = valore % 100
        nome = traduciCifra(centinaia) + " hundred"

    if valore >= 20:
        decina = valore // 10
        valore = valore % 10
        nome = nome + " " + traduciDecina(decina)
    elif valore >= 10:
        nome = nome + " " + traduciTeen(valore)
        valore = 0

    if valore > 0:
        nome = nome + " " + traduciCifra(valore)

    return nome








'''
funzioni di traduzione (da numero a stringa)
per i vari casi
'''

def peso(indice):
    if indice == 0:
        return ""
    elif indice == 1:
        return "thousand"
    elif indice == 2:
        return "milion"
    elif indice == 3:
        return "bilion"
    else:
        return ""

def traduciCifra(cifra):
    if cifra == 1:
        return "one"
    elif cifra == 2:
        return "two"
    elif cifra == 3:
        return "three"
    elif cifra == 4:
        return "four"
    elif cifra == 5:
        return "five"
    elif cifra == 6:
        return "six"
    elif cifra == 7:
        return "seven"
    elif cifra == 8:
        return "eight"
    elif cifra == 9:
        return "nine"
    
    return ""
    

def traduciTeen(cifra):
    if cifra == 10:
        return "ten"
    elif cifra == 11:
        return "eleven"
    elif cifra == 12:
        return "twelve"
    elif cifra == 13:
        return "thirteen"
    elif cifra == 14:
        return "fourteen"
    elif cifra == 15:
        return "fifteen"
    elif cifra == 16:
        return "sixteen"
    elif cifra == 17:
        return "seventeen"
    elif cifra == 18:
        return "eighteen"
    elif cifra == 19:
        return "nineteen"
    
    return ""

def traduciDecina(cifra):
    if cifra == 2:
        return "twenty"
    elif cifra == 3:
        return "thirty"
    elif cifra == 4:
        return "fourty"
    elif cifra == 5:
        return "fifty"
    elif cifra == 6:
        return "sixty"
    elif cifra == 7:
        return "seventy"
    elif cifra == 8:
        return "eighty"
    elif cifra == 9:
        return "ninety"
    
    return ""


main()