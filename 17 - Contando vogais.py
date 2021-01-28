'''
Faça um programa que receba uma frase como entrada, conta as vogais contidas na frase,
1e mostra uma lista com a ordem na qual as vogais apareceram no texto pela primeira vez.

Entrada:                                    Saida:
Laboratório de programação 1                Quantidade de vogais no texto : 10 
.                                           Vogais : ['a', 'o', 'i', 'e']
'''

vogais = []
texto = input()
texto = texto.lower()
a = 0
e = 0
iv = 0
o = 0
u = 0

for i in range(len(texto)):
    if texto[i] == "a":
        if a == 0:
            vogais.append('a')
        a += 1
    if texto[i] == "e":
        if e == 0:
            vogais.append('e')
        e += 1
    if texto[i] == "i":
        if iv == 0:
            vogais.append('i')
        iv += 1
    if texto[i] == "o":
        if o == 0:
            vogais.append('o')
        o += 1
    if texto[i] == "u":
        if u == 0:
            vogais.append('u')
        u += 1

print('Número de vogais encontradas : {}'.format((a+e+iv+o+u)))
print(vogais)

