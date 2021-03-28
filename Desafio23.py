'''Faça um programa que leia um número de 0 a 999
e mostre na tela cada um dos digitos separados
Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

print('Programa leitor de números!')
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 1 % 10
c = n // 1 % 10
m = n // 1 % 10
print('Unidade: {}'
      '\nDezena: {}'
      '\nCentena: {}'
      '\nMilhar: {}'
      .format(u, d, c, m))
