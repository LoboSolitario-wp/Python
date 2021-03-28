'''Faça um programa que leia uma frase pelo teclado e mostre:

 Quantas vezes aparece a letra "A"

 Em que posição ela aparece a primeira vez

 Em que posição aparece pela ultima vez'''

print('Verificador de frases, quantas vezes aparece o "A"!')
frase = str(input('Digite a frase: ')).upper().strip()
print('A letra "a" aparece {} vezes'.format(frase.count('A')))
print('Aparece a primeira vez na posição', frase.find('A'))
print('Aparece pela última vez na posição', frase.rfind('A'))
