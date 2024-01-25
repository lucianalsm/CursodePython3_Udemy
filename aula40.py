# strings em python são iteráveis
#operadores in e not in

nome = 'Otavio'

print (nome[3])
print (nome[-2])

print('vio'in nome)
print ('z'not in nome)
print (10 * 'b')

nome= input ('Digite seu nome:')
encontrar = input ('Digite o que deseja encontrar:')

if encontrar in nome :
    print ( f'{encontrar} pertence ao nome digitado')
else :
    print ( f'{encontrar} não pertence ao nome')
