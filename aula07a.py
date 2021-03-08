n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, '
      '\n o produto é {}, '
      '\n e a divisão é {:.3f}'
      .format(s, m, d), end='. ')
print('Divisão inteira é {} e potência é {}'.format(di, e))

ni = int(input('Digite o número, será transformado em inteiro: '))
print('O número inserido foi {} '
      '\n -> Seu número antecessor é {} '
      '\n -> Sucessor é {}'.format(ni, ni-1, ni+1))

algoritimo = int(input('Digite o número: '))
print('-> O dobro = {}\n -> O triplo = {}\n -> Raiz quadrada = {:.2f}'
      .format(algoritimo*2, algoritimo*3, algoritimo**(1/2)))

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
print('A média entre {} e {} é = {:.1f}'.format(nota1, nota2, (nota1+nota2)/2))

medir = int(input('Digite uma distância em metros: '))
print('-> A media de {:.1f}m(s) corresponde a ' 
      '\n{:.3f}km'
      '\n{:.2f}hm'
      '\n{:.1f}dam'
      '\n{}dm'
      '\n{}cm'
      '\n{}mm'.format(medir, medir/1000, medir/100, medir/10, medir*10, medir*100, medir*1000))

tabuada = int(input('Digite um número para realizar a tabulada: '))
print('\n')
print('-'*12)
print('{} x {:2} = {:2}'.format(tabuada, 1, tabuada*1))
print('{} x {:2} = {:2}'.format(tabuada, 2, tabuada*2))
print('{} x {:2} = {:2}'.format(tabuada, 3, tabuada*3))
print('{} x {:2} = {:2}'.format(tabuada, 4, tabuada*4))
print('{} x {:2} = {:2}'.format(tabuada, 5, tabuada*5))
print('{} x {:2} = {:2}'.format(tabuada, 6, tabuada*6))
print('{} x {:2} = {:2}'.format(tabuada, 7, tabuada*7))
print('{} x {:2} = {:2}'.format(tabuada, 8, tabuada*8))
print('{} x {:2} = {:2}'.format(tabuada, 9, tabuada*9))
print('{} x {:2} = {:2}'.format(tabuada, 10, tabuada*10))
print('-'*12)

print('\nCalculadora de Doláres;'
      '\nSaiba quantos doláres pode compras com o dinheiro que tem')
reais = float(input('Digite o valor que tem: '))
print('Você pode comprar U${:.2f} (doláres)'.format(reais/3.27))

print('\nCalculadora de tinta necessária;'
      '\nCada lata de tinta pode pintar uma área 2m²')
larg = float(input('Informe a largura da parede (em metros: '))
alt = float(input('Informe a altura da parede (em metros): '))
perímetro = (larg*alt)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, perímetro))
tinta = perímetro / 2
print('Para pintar essa parede, você precisa de {}l de tinta'.format(tinta))

print('\nCalculadora de desconto (5%)')
valor = float(input('Insira o valor do produto: R$'))
print('O valor do produto com 5% será R${:.2f}'.format(valor*0.95))

print('\nCalculadora de novo salário (15%)')
salário = float(input('Insira o valor do salário atual: R$'))
print('O valor do novo salário  (+5%) será R${:.2f}'.format(salário*1.15))
