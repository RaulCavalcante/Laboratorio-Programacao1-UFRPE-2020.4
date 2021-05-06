primo = [] 
Nao_Primo = []

def selecao ( n ):
    y = True
    quant = []
    x = n
    for i in range(n+1):
        if i != 0 and x % i == 0:
            quant.append(i)
    if len(quant) > 2:
        y = False
    return y    

'''
Faça um programa que recebe os extremos de um intervalo e separa os números desse intervalo em primos e não primos.

Saida:                                                                                  Entrada:
Números primos: [5, 7, 11, 13, 17, 19, 23]                                              5 25
Números não primos: [6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24]
'''
a,b = input().split(" ")
a = int(a)
b = int(b)

for i in range(b-a):
    if selecao(a) == True:
        primo.append(a)
    else:
        Nao_Primo.append(a)
    a += 1
    
print("Números Primos:",primo)
print("Números não primos:",Nao_Primo)
