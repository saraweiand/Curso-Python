'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

n = 0

for c in range(1, 11):
    dez_primeiros = termo + (c-1) * razao
    print('Termo {}: {}'.format(c, dez_primeiros))