"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo:
a soma do triplo do primeiro com o terceiro:
o terceiro elevado ao cubo:
"""
inteiro1 = int(input('Digite um número inteiro: '))
inteiro2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))
produto = (2 * inteiro1) * (inteiro2 / 2)
soma = (inteiro1 * 3) + real
cubo = real ** 3
print(produto)
print(soma)
print(cubo)