"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome:")
idade = input ("Digite sua idade:")
nomeinvertido = f'{nome[::-1]}'

if nome and idade :
    print (f'{nome}')
    print(f'{nomeinvertido}')
    print ("Seu nome tem", (len(nome)), "letras")
    if " "in(nome) :
        print("Seu nome tem espaços")
    else:
     print("Seu nome não tem espaços") 

    print ("A primeira letra do seu nome é", nome[0])

    print ("a última letra do seu nome é", nome [-1 ])
       
else:
   print("Desculpe, você deixou campos em branco")