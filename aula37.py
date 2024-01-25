primeirovalor= input("Digite um valor:")
segundovalor= input ("Digite outro valor:")

condicao1= primeirovalor > segundovalor
condicao2= segundovalor > primeirovalor
condicao3= primeirovalor == segundovalor

if condicao1 :
    print( "primeiro valor é maior que o segundo valor")
elif condicao2 :
    print ("primeiro valor é menor que o segundo valor")
else :
    print ("primeiro valor é igual ao segundo valor")    