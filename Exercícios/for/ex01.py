'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de aritifício,
indo de 10 até 0, com uma pausa de 1segundo entre eles.
'''
import time

print('-------- CONTAGEM REGRESSIVA --------')
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('FOGOS DE ARTIFÍCIOS VOAM PELO CÉU')