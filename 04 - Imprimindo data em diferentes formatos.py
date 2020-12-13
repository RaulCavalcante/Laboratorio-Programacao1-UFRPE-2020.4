'''
Programas de computador precisam formatar as datas de acordo com o
 gosto dos usuários. Faça um programa que lê uma data no formato DD/MM/AA e
  imprime esta mesma data nos formatos a seguir:

MM/DD/AA
AA/MM/DD
DD-MM-AA

Entrada: 01/02/03         Saida: 02/01/03
                                 03/02/01
                                 01-02-03

'''
data = input()
dia = data[0:2]
mes = data[3:5]
ano = data[6:9]
print('{}/{}/{}'.format(mes,dia,ano))
print('{}/{}/{}'.format(ano,mes,dia))
print('{}-{}-{}'.format(dia,mes,ano))
