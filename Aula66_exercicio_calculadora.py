## Calculadora com while

while True:
    numero1= input('Digite um número: ')
    numero2= input('Digite outro número: ')
    operador= input('Digite um operador(+-/*):')

    numeros_validos= None

    try:
        num_1_float = float(numero1)
        num_2_float = float (numero2)
        numeros_validos= True

    except:
        numeros_validos = None

    if numeros_validos is None: 
        print('Um ou ambos os números digitados são inválidos') 
        continue      
    
    operadores_permitidos = '+-/*'

    if operador  not in operadores_permitidos:
        print("operador inválido")
        continue

    if len(operador) > 1:
         print(' Digite apenas um operador')


    if len(operador) > 1:
            print('Digite apenas um operador.')
    continue

    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')


    if sair is True:
        break 





    
