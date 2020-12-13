'''
Faça um programa que lê um CPF no formato XXX.YYY.ZZZ-DD 
e imprime os quatro blocos de números em separado, um em cada linha.

Entrada: 120.120.120-00         Saida:  120
                                        120
                                        120
                                        00
'''
cpf = input()
print(cpf[0:3])
print(cpf[4:7])
print(cpf[8:11])
print(cpf[12:14])