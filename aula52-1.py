"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

que_hora= input ("Que horas são, amiguinho?")
hora_informada =  int(que_hora) 

if hora_informada >= 0 and hora_informada <= 12:
    print("Bom dia")
elif hora_informada >= 12 and hora_informada <= 17:
    print ("Boa tarde")
else:
    print ("Boa noite")
