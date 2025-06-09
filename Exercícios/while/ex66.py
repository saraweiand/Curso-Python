'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

qnt = 0
soma = 0

while True:
    num = float(input('Digite um número: '))
    if num == 999:
        break
    qnt += 1
    soma += num

print('Foram digitados: {} números!'.format(qnt))
print('A soma entre os números digitados foi de: {}'.format(soma))