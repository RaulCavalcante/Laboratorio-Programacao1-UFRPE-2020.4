'''
Faça um programa que recebe um valor inteiro entre 0 e 100 e sorteia valores (usando gerador de números aleatórios), até que o valor sorteado coincida com o valor recebido como entrada.

Caso o número dado como entrada esteja fora do intervalo acima, o programa pede uma nova entrada, até que receba o valor dentro do intervalo.

Quando um valor dentro do intervalo é digitado, o programa sorteia um valor dentro do intervalo. Se o valor sorteado coincidir com o valor dado como entrada, o programa para e imprime 
na saída uma mensagem de parabéns. Caso o valor sorteado seja diferente do valor dado como entrada, o programa repete o sorteio até que o número sorteado seja igual ao valor de entrada, quantas vezes for necessário, até que o número sorteado seja igual. Ao encontrar o valor digitado, o programa deve imprimir na saída as informações a seguir:

a quantidade total de números sorteados;
a quantidade de números sorteados que são menores do que o valor digitado;
a quantidade de números sorteados que são maiores do que o valor digitado;
a lista dos valores sorteados que são menores do que o valor digitado;
a lista dos valores sorteados que são maiores do que o valor digitado.
As duas listas indicadas acima não admitem repetição, ou seja, caso o seu programa sorteie duas (ou mais vezes) um mesmo valor, ele só aparece uma vez na lista.

Saida:                                                                                  Entrada:
Número de valores sorteados foi 89                                                      25
A quantidade de números menores que a entrada foi 27
A quantidade de números maiores que a entrada foi 62
A lista dos valores menores que a entrada 25 : [6, 1, 7, 12, 21, 24, 19, 8, 10, 17, 0, 22, 4, 18, 20] -> tamanho da lista : 15
A lista dos valores maiores que a entrada 25 : [60, 61, 86, 88, 87, 35, 95, 64, 84, 30, 45, 33, 89, 37, 29, 70, 26, 48, 46, 81, 68, 
69, 71, 62, 50, 57, 59, 83, 80, 90, 51, 58, 96, 97, 66, 53, 40, 36, 47, 73, 77] -> Tamanho da lista : 41

'''
from random import randrange

lista = [[],[]]
quant_Maior = []
quant_Menor = []
def adicionar_Lista (n,lista):
    if n > numero_Sorteado:
        quant_Maior.append(0)
        if not (n in lista[1]):
            lista[1].append(n)
    else:
        quant_Menor.append(0)
        if not (n in lista[0]):
            lista[0].append(n)
    return lista
# Loop com verificador de 0 <= x <= 100
loop = True
numero_Sorteado = 0
while loop:
    numero_Sorteado = int(input())
    if  numero_Sorteado >= 0 and numero_Sorteado <= 100:
        loop = False

# primeira tentantiva
loop = True
quant = 0
x = randrange(101)
if numero_Sorteado == x:
    print("Você é um sortudo! Acertou de primeira!")
else:
    lista = adicionar_Lista(x,lista)
    quant += 1
    # Loop até acerta o numero
    while loop :
        x = randrange(101)
        if numero_Sorteado == x:
            loop = False
        else:
            lista = adicionar_Lista(x,lista)
            quant += 1

print('Número de valores sorteados foi {}'.format(len(quant_Maior)+len(quant_Menor)))
print('A quantidade de números menores que a entrada foi {}'.format(len(quant_Menor)))
print('A quantidade de números maiores que a entrada foi {}'.format(len(quant_Maior)))
print('A lista dos valores menores que a entrada {} : {} -> tamanho da lista : {}'.format(numero_Sorteado,lista[0],len(lista[0])))
print('A lista dos valores maiores que a entrada {} : {} -> tamanho da lista : {}'.format(numero_Sorteado,lista[1],len(lista[1])))