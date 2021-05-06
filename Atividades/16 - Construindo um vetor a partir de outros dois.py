'''
Faça um programa que lê dois vetores de inteiros e imprime um vetor que corresponde à multiplicação dos vetores de entrada.

Seu programa deve:

Ler o valor n que informa o tamanho dos vetores.
Ler n valores e guardar no primeiro vetor.
Ler n valores e guardar no segundo vetor.
Calcular e armazenar em um terceiro vetor o resultado da multiplicação.
Imprimir o vetor que corresponde à multiplicação.
Exemplo: Suponha os dois vetores de entrada são [2,1,2] e [3,2,1]. O vetor resultante da multiplicação é obtido pelo cálculo [2x3,1x2,2x1] cujo resultado é [6,2,2]

Entrada:            Saida:
3                   [6, 2, 2]
2
1
2
3
2
1
'''

lista1 = []
lista2 = []
lista_Final = []

quantidade = int(input())

for i in range(quantidade):
    x = int(input())
    lista1.append(x)

for i in range(quantidade):
    x = int(input())
    lista2.append(x)

for i in range(quantidade):
    x = lista1[i] * lista2[i]
    lista_Final.append(x)

print(lista_Final)
