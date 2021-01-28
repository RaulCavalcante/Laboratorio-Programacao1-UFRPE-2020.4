'''
Faça um programa que recebe um número inteiro n de alunos e coleta, para cada aluno: nome, primeira nota e segunda nota. Como saída, 
este programa imprime:

uma tupla com o nome e a média do aluno com maior média;
uma tupla com o nome e a média do aluno com menor média.
A média de cada aluno é a média aritmética das suas duas notas.

Entrada:                Saida:
3                       (Maria, 9.6)
João                    (João, 8.3)
10
6.6
Maria
9.7
9.5
José
8.5
8.9
'''
aluno = []

quantidade = int(input())

for i in range(quantidade):
    nome_Aluno = input()
    nome_Aluno.strip()
    nome_Aluno.replace("\r","")
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1+nota2)/2
    sublista = (nome_Aluno,media)
    aluno.append(sublista)

ordenar_Media = lambda alu: alu[1]
aluno.sort(key=ordenar_Media, reverse=True)

if quantidade > 1 :
    if aluno[0][1] == aluno[1][1]: 
        maior_Nome = aluno[1][0].replace('\r','')
        maior_Numero = aluno[1][1]
    else:
        maior_Nome = aluno[0][0].replace('\r','')
        maior_Numero = aluno[0][1]
else:
        maior_Nome = aluno[0][0].replace('\r','')
        maior_Numero = aluno[0][1]
print("('{}', {})".format(maior_Nome,maior_Numero))

menor_Nome = aluno[quantidade-1][0].replace('\r','')
menor_Numero = aluno[quantidade-1][1]

print("('{}', {})".format(menor_Nome,menor_Numero))
