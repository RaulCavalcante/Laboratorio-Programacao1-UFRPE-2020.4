'''
Faça um programa que lê o nome e a idade de n pessoas. Após coletar os dados das pessoas, o seu programa imprime quais das pessoas 
tem a maior, a que tem a menor idade e a média de idade dessas pessoas.

Entrada:                        Saida:
5                               João tem 25 anos, sendo a pessoa com maior idade.
João 25                         Maria tem 12 anos, sendo a pessoa com menor idade.
Maria 12                        Média de idade : 17 anos
Matheus 24
José 15
Pamela 13

'''
lista = []
quant = int(input())
# Adicionando valores na lista
for i in range(quant):
    lista.append(input().split(" "))
maior = int(lista[0][1])
nome_Maior = lista[0][0]
menor = int(lista[0][1])
nome_Menor = lista[0][0]
media = 0 
#Comparando 
for i in range(quant):
    media = media + int(lista[i][1])
    if int(lista[i][1]) > maior:
        maior = int(lista[i][1])
        nome_Maior = lista[i][0]
    if int(lista[i][1]) < menor:
        menor = int(lista[i][1])
        nome_Menor = lista[i][0]

print('{} tem {} anos, sendo a pessoa com maior idade.'.format(nome_Maior,maior))
print('{} tem {} anos, sendo a pessoa com menor idade.'.format(nome_Menor,menor))
print('Média de idade : {} anos'.format(int((media/quant))))