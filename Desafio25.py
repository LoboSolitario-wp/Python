'''Crie um programa que leia o nome de
 uma pessoa e diga se tem o nome "SILVA" no nome'''

nome = input('Digite o nome completo: ').upper()
nomesplit = nome.split()
print('SILVA' in nomesplit)



