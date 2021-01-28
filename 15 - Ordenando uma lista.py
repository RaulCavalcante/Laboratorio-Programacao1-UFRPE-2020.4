'''
Faça um programa que recebe um número n que corresponde a quantidade de valores inteiros que 
serão lidos e armazenados em uma lista. Como saída, o programa imprime os n valores lidos na ordem decrescente dos valores.

Entrada:        Saida:
3               [5, 4, 2]
2
5
4
'''

lista_Numeros = []
quantidade = int(input())
for i in range(quantidade):
    x = int(input())
    lista_Numeros.append(x)
lista_Numeros.sort(reverse=True)
print(lista_Numeros)