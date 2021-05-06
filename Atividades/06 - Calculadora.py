'''
Faça um programa que simula uma calculadora com 4 operações (+, -, *, /).

Entrada             Saida
2 + 3               2 + 3 = 5

'''
x,operacao,y = input().split(" ")
x = int(x)
y = int(y)
if operacao == "+":
    z = x + y
    print('{} {} {} = {}'.format(x,operacao,y,z))
elif operacao == "-":
    z = x - y
    print('{} {} {} = {}'.format(x,operacao,y,z))
elif operacao == "/":
    z = x / y
    print('{} {} {} = {}'.format(x,operacao,y,z))
elif operacao == "*":
    z = x * y
    print('{} {} {} = {}'.format(x,operacao,y,z))
