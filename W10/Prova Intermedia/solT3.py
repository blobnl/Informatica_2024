def conta_parole(testo):
    contatore = len(testo.strip().split())
    #contatore = testo.count(' ') + 1
    return contatore

def main():
    frase = "Ciao a tutti da Python"
    print(conta_parole(frase))  
    # Output atteso: 5

main()
