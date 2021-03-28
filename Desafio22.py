"""Crie um programa que leia o nome completo de uma pessoa
e mostre:


- O nome com todas as letras maiúsculas
- O nome com todas minusculas
- Quantas letras ao todos (sem considerar espaços)
- Quantas letras tem o primeiro nome"""

print('Leitor de Nomes!')
nome = input('Digite um nome completo :').title().split()
nomesemespaço = ''.join(nome)
nomecorrig = ' '.join(nome)
print('Você digitou "{}", '.format(nomecorrig))
print('Nome em minúsculo: {}'.format(nomecorrig).upper())
print('Nome em minúsculo: {}'.format(nomecorrig.lower()))
print('Desconsiderando os espaços, o nome digitado '
      'tem {} caracteres!'.format(len(nomesemespaço)))
print('O primerio nome "{}" tem {} letras!'.format(nome[0], len(nome[0])))