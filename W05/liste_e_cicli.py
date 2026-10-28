'''
Iterazioni con cicli:
- con while
- con for
    * diretto su elementi lista
    * indiretto tramite indice
    * con enumerate -> (idx, elemento)

Attenzione a modifiche in ciclo

'''

voti = [28, 15, 30, 24, 15, 18, 32, 22] 
sufficienti = []

for voto in voti:
    if voto >= 18:
        sufficienti.append(voto)
        
print(f"Voti sufficienti = {",".join(sufficienti)}, numero = {len(sufficienti)}")
    
media = sum(sufficienti) / len(sufficienti)
print(f"media =  {media}")