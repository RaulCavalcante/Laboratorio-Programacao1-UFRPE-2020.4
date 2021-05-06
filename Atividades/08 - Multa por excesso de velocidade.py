'''
O programa deve calcular se o motorista será multado por excesso de velocidade, a partir das velocidades capturadas pelo radar em três diferentes trechos da rodovia.

As velocidades máximas em cada trecho da rodovia são:

Trecho 1 : 40Km/h
Trecho 2 : 80Km/h
Trecho 3 : 100Km/h

Entrada:        Saida:
10 50 120       Multado
'''
x,y,z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)
if x > 40 or y > 80 or z > 100:
    print("Multado")
else:
    print("Não multado") 