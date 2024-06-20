frase = 'o python é uma linguagem de programaçao' \
'multiparadigma' \
'criada por Guido von Rossum'

print(frase)
print(frase.count('i')) 

i= 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i< len(frase):
    letra_atual=frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu
    
    print(letra_atual , quantas_vezes_letra_apareceu)
    i+= 1