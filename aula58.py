"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
sao objetos
"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))

## repetiçoes while (enquanto), executa uma ação enquanto a condiçao for verdadeira"

#loop infinito = quando um código não tem fim


condicao = True

while condicao:
    nome= input('Qual é o seu nome:')
    print(f'Seu nome é{nome}')

    if nome == 'sair' :
        break

print('acabou')
