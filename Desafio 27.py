'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e ultimo nome separadamente

Ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza'''

print('Mostrar primeiro e último nome!')
nome = str(input('Digite o nome :'))
print('''O nome digitado foi: {} 
      O primeiro nome é: {}
      O último nome é: {}'''
      .format(' '.join(nome.split()), nome.split()[0], nome.split()[-1]))
