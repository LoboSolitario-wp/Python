'''Crie um programa que leia o nome
de uma cidade e diga se ela começa ou não com o nome "SANTO"'''

print('Verificador de "Santo" no nome de cidades!')
cidade = input('Digite o nome de uma cidade: ').upper().strip()
print(cidade.startswith('SANTO'))
