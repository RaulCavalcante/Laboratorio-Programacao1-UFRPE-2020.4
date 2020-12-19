'''
Faça um programa que calcule a média aritmética a partir de duas notas e mostre a situação acadêmica do aluno. A situação acadêmica deve ser impressa seguindo as regras a seguir.

Média >= 7.0 : Aprovado
Média < 3.0 : Reprovado
3.0 <= Média < 7.0 : Recuperação

Entrada         Saida 
10 5            Aprovado

'''
x,y = input().split(" ")
x = float(x)
y = float(y)
media = (x+y)/2
if media >= 7:
    print("Aprovado")
elif 3 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")