def sono_anagrammi(parola1, parola2):
   return sorted(parola1.lower()) == sorted(parola2.lower())

# Funzione main per il test
def main():
   p1 = "attore"
   p2 = "teatro"
   print(sono_anagrammi(p1, p2))  
   # Output atteso: True

main()
