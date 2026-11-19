'''
Dati due insiemi contenenti i nomi degli studenti 
iscritti a due diversi moduli formativi, 
ad esempio 
corso_python = {"Marco", "Anna", "Giuseppe", "Elena"} 
e corso_sql = {"Giuseppe", "Elena", "Paolo", "Sara"}, 
calcola e stampa l'insieme degli studenti che 
frequentano entrambi i corsi, 
e poi gli studenti iscritti esclusivamente al 
corso di Python

'''
corso_python = {"Marco", "Anna", "Giuseppe", "Elena"} 
corso_sql = {"Giuseppe", "Elena", "Paolo", "Sara"}

studenti_entrambi_corsi = corso_python.intersection(corso_sql)
solo_python = corso_python.difference(corso_sql)

print(f'GLi studenti che frequentano entrambi i cirsi sono {studenti_entrambi_corsi}')
print(f'Gli studenti che frequentano solo python sono {solo_python}')
