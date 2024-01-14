Nome = 'Álvaro de Assis'
altura = 1.62
peso = 40
imc = peso / (altura * altura)

linha_1 = f'{Nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos,'
linha_3 = f'e seu IMC é {imc:.2f}'

print(Nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)
print(linha_1)
print(linha_2)
print(linha_3)