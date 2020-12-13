'''
Você vai fazer um programa para ajudar uma corretora de imóveis a calcular o valor da locação de 
um imóvel a partir do número de diárias do aluguel, do número de dias de TV a cabo e de Internet 
que serão contratados.

No cálculo considere:

Que o aluguel é cobrado por dia. A diária custa R$ 150.
O cliente pode optar por contratar TV a cabo (R$ 10 por dia) e Internet (R$ 15 por dia).

Entrada: 5          Saida: 840.00
         3
         4  
'''

diaria_casa = 150
tv_Cabo = 10
internet = 15
casa = int(input())
cabo = int(input())
inter = int(input())
aluguel = (diaria_casa*casa)+(tv_Cabo*cabo)+(internet*inter)
print("%0.2f" % aluguel)