'''
Scrivi una funzione converti_temperatura che prenda in 
ingresso un valore numerico rappresentante i gradi Celsius 
e un parametro opzionale scala impostato di default su "F". 
Se la scala è "F", la funzione deve calcolare e restituire la 
temperatura in Fahrenheit usando la formula (celsius * 9/5) + 32, 
mentre se la scala viene impostata su "K" deve restituire 
la temperatura in Kelvin celsius + 273.15.

'''

def convertiCelsius(celsius, scala = 'F'):
    if scala == 'F':
        return (celsius * 9/5) + 32
    elif scala == 'K':
        return celsius + 273.15
    else:
        print("Errore: scala nn riconosciuta")
        return 0

def main():
    celsius = float(input("Inerire temperatura: "))
    kelvin = convertiCelsius(celsius, scala = 'K')
    far = convertiCelsius(celsius)
    print(f"Kelvin = {kelvin} Fahrenheit = {far}")
    
main()
