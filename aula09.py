frase = 'Willian Silva'
print(frase[::2])
print(len(frase))
print(frase.upper())
print(frase.count('l'))
frase.count('l', 0, 7)
print(frase.find('Silva'))
print('Silva'.upper() in frase.upper())
valor = input('Digite o nome :').upper()
print(valor)
texto = input('Digite o texto :').strip().upper().title().split()
print(texto)