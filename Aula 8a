import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))

import math
# Desafio 16
# Crie um programa que leia um número Real qualquer pelo
# teclado e mostre a sua porção inteira
#   Ex:
#   Digite um número: 6.127
#   O número 6.127 tem a parte inteira 6

print('Transformar em número inteiro!')
número = float(input('Digite o número :'))
print('O valor digitado foi :', número, 'tem a parte inteira ', math.floor(número))

print(40*'-')

# Desafio 17
#Faça um programa leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

print('Calcular comprimento de um Triângulo Retângulo!')
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O comprimento da Hipotenusa desse triangulo retângulo é: {:.2f}'.format(hi))

print(40*'-')

# Desafio 18
# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse angulo

print('Calculo de Seno, Cosseno e tangente do Angulo!')
angulo = int(input('Informe o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}º tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}º tem o TANGENTE de {:.2f}'.format(angulo, tangente))

print(40*'-')

# Desafio 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido

import random
print('Sorteio de aluno que apagará o Quadro!')
a1 = str(input('Insira o nome do aluno 1: '))
a2 = str(input('Insira o nome do aluno 2: '))
a3 = str(input('Insira o nome do aluno 3: '))
a4 = str(input('Insira o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno sorteado entre ({}, {}, {} e {}) foi: {}'.format(a1, a2, a3, a4, escolhido))

print(40*'-')

# Desafio 20
# O mesmo professor do desafio anterior quer
# sortear a ordem de apresentação de trabalhos dos alunos.
# de trabalhos dos alunos. Faça um programa que leia o
# nome dos quatro alunos e mostre a ordem sorteada.

print('Sortear a ordem de apresentação dos trabalhos!')
n1 = str(input('Insira o nome do aluno 1: '))
n2 = str(input('Insira o nome do aluno 2: '))
n3 = str(input('Insira o nome do aluno 3: '))
n4 = str(input('Insira o nome do aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será;')
print(lista)

print(40*'-')
