age = int(input("inserisci età: "))
order = input("inserisci ordine: ")

if order == 'vino': #... genricamnet se contiene alcool
    if age >= 21:
        print("Ecco il vino servito")
    else:
        print("bla bla bla...")
else:
    print("Ti servo", order)

