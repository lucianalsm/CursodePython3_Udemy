"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

digitar_numero= input("Digite um numero inteiro:  ")

if digitar_numero.isdigit():

   numero_inteiro = int(digitar_numero)
   if numero_inteiro % 2 == 0:   
    print("O seu numero é par")
   elif  numero_inteiro % 2 !=0:
    print ('O seu numero é impar') 

else:    
  
  print("Voce nao digitou um numero inteiro")

    

