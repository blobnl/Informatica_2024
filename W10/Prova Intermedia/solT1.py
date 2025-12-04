def conta_lettere(testo, elenco):
    contatore = 0
    for carattere in testo.lower():
        if carattere in elenco.lower():
            contatore += 1

    return contatore

def main():
    frase = "CiaO mondo"
    print(conta_lettere(frase, 'aeiou'))  
    # Output atteso: 5

main()
