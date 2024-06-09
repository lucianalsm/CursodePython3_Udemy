"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_do_usuario = input("Digite o seu nome, amiguinho : ")
quantidade_de_letras = len(nome_do_usuario)

if quantidade_de_letras <= 4:
    print ("Seu nome é curto")

elif quantidade_de_letras <=5 and quantidade_de_letras >= 6:
    print ("seu nome é normal")

else :
    print ( " seu nome é muito grande ")