"""iterando strings com while"""

#   012345678910

nome= "Luciana Miguel"
tamanho_do_nome= len(nome)
print (nome)
print(tamanho_do_nome)
print(nome[3])

indice =0
novo_nome= ''
while indice< len(nome):
        letra = nome[indice]
        novo_nome += f'* {letra}'
        indice += 1
novo_nome += '*'        
print(novo_nome)       
    
        