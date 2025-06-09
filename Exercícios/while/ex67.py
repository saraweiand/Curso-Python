''''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''

tabuada = 0
c = 0

print('---------- TABUADA ----------')

while True:
    num = int(input('Dgite um número: '))
    if num < 0:
        break
    while c < 10:
        c += 1
        tabuada = num * c
        print('{} X {} = {}'.format(c, num, tabuada))
    c = 0
    print('---------- TABUADA ----------')
