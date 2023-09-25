"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
sexo = int(input('Digite seu sexo, sendo que 1. para Sexo Masculino e 2. para Sexo Feminino: '))
pi = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7
if p < pi:
	print('Abaixo do peso ideal! ')
elif p == pi:
	print('Dentro do peso ideal! ')
else:
	print('Acima do peso ideal! ')
print ('Peso: %.2f / Peso ideal: %.2f' %(p, pi))
