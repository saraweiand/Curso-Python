'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
import random

venceu = 0

while True:
    escolha = int(input('Digite um número para o PAR ou ÍMPAR: '))
    escolha_pc = random.randint(0, 100)
    res = escolha + escolha_pc
    if escolha % 2 == 0:
        if res % 2 == 0:
            print('VOCÊ venceu! O computador jogou {} e você jogou {}.'.format(escolha_pc, escolha))
            print('Total de {} deu PAR'.format(res))
            venceu += 1
        else:
            print('COMPUTADOR venceu! O computador jogou {} e você jogou {}.'.format(escolha_pc, escolha))
            print('Total de {} deu ÍMPAR'.format(res))
            break
    else:
        if res % 2 == 0:
            print('COMPUTADOR venceu! O computador jogou {} e você jogou {}.'.format(escolha_pc, escolha))
            print('Total de {} deu PAR'.format(res))
            break
        else:
            print('VOCÊ venceu! O computador jogou {} e você jogou {}.'.format(escolha_pc, escolha))
            print('Total de {} deu ÍMPAR'.format(res))
            venceu += 1
print('Você venceu {} partidas. Parabéns!'.format(venceu))
