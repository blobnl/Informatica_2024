'''
Dato un insieme di strumenti di sviluppo chiamato 
tools = {"VS Code", "Python", "Git"} 
1. rimuovere il valore "Git" e 
2. aggiungere le due nuove tecnologie "MySQL" e "Docker«; 
3. alla fine stampa gli elementi dell’insiem risultante 
    in ordine alfabetico

'''

tools = {"VS Code", "Python", "Git"}
print(tools)

elemento = 'Git'
tools.discard(elemento)
#if elemento in tools:
#    tools.remove(elemento)

print(tools)

nuoviTools = ["MySQL", "Docker"]
tools.update(nuoviTools)

print(tools)


# ordinamento
# 1 creo lista esplicita e ordino
listaTools = list(tools)
print(listaTools)
listaTools.sort()
for tool in listaTools:
    print(tool)
    
print()
# 2 sorted() --> lista ordinata
for tool in sorted(tools):
    print(tool)