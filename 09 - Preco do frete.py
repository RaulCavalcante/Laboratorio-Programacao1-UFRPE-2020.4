'''
Faça um programa que calcula o preço do frete a partir do peso da carga e da distância até o destino. 
O cálculo do frete é feito usando a fórmula:

Txpeso * peso + Txdistancia * distância + 25

A taxa do peso (Txpeso) varia de acordo com a faixa de peso da carga.

(100Kg - 250Kg) = R$ 0.65
(250Kg - 400Kg) = R$ 0.75
(400Kg - 500Kg) = R$ 0.80
A taxa da distância (Txdistancia) varia de acordo com a faixa de distância.

(10Km - 300Km) = R$ 1.25
(300Km - 500Km) = R$ 1.35
Caso o peso ou a distância sejam além das faixas acima, o programa deve informa que a transportadora 
não pode fazer a entrega.

Entrada:            Saida:
150 200             Valor do frete: R$ 372.50
'''
peso,distancia = input().split(" ")
peso = float(peso)
distancia = float(distancia)
if 100 <= peso <= 500 or 10 <= distancia <= 500:
    if  100 <= peso < 250:
        precoPeso = peso * 0.65
    elif 250 <= peso < 400:
        precoPeso = peso * 0.75
    elif 400 <= peso <= 500:
        precoPeso = peso * 0.80
    
    if 10 <= distancia < 300:
        precoDistancia = distancia * 1.25
    elif 300 <= distancia <= 500:
        precoDistancia = distancia * 1.35

    valorTotal = precoPeso + precoDistancia + 25
    print('Valor do frete: R$ {:.2f}'.format(valorTotal))
else:
    print("A transportadora não tem condições de entregar o objeto.")
