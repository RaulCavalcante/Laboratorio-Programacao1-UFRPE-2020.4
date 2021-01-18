'''
Faça um programa que recebe um número e faz a impressão da tabuada de 0 a 10 desse número.

Saida:                                            Entrada:
5 * 0 = 0                                         5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''
x = int(input())
for i in range(11):
    print('{} * {} = {}'.format(x,i,(i*x)))