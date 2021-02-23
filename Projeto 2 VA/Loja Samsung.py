# Exemplos de entradas (teste)
##lista_Vendas = [['ger',1,'M51','Pedro'], ['fun1',3,'A31','Laura'] , ['fun2',2,'NT20','João'] , 
##['fun2',1,'S10','Matheus'] , ['est',4,'S10','Pedro'] , ['est',2,'S10','Pedro'] , ['fun2',4,'M51','Caio'] ]
#lista_Vendas = [['ger',4,'S10','Raul'],['ger',2,'A31','Raul'],['ger',4,'M51','Raul'],['fun3',15,'A31','Arthur'],['est',2,'S10','Ricardo'],['est',2,'S10','Ricardo']]
#lista_Vendas = [['ger',3,'M51','A'],['est',1,'A31','B'],['fun1',5,'S10','A'],['fun3',3,'NT20','C'],['ger',10,'S20','B']]

lista_Vendas = eval(input("Digite sua lista: "))

#print(lista_Vendas)

menu = [['M51',2300],['S10',2500],['NT20',2700],['A31',1500],['S20',3200]] # Menu da loja Samsung 
funcionario = [['ger',0,0],['fun1',0,0],['fun2',0,0],['fun3',0,0],['est',0,0]] #['nome',quant,valor] no final valor = bonificação
compradores = [] #['nome',quant,[modelo_tel],valor,cashback]
quantidade_Vendas = len(lista_Vendas)
valor_Total = 0

def add_Nome_Compradores (lista): # adciona os nome na lista_Vendas na lista nomes_compradores
    a = []
    for i in range(len(lista)):
        a.append(lista[i][3])
    a = list(set(a))
    return a

def calcular_Valor (quantidade,modelo): # Calcula o valor da quantidade e preço do modelo da venda e retorna o valor
    for i in range(len(menu)):
        if modelo == menu[i][0]:
            return quantidade * menu[i][1]

def calcular_Valor_cashback (quantidade,modelo): #Calcula o valor da primeira compra e retorna o cashback 
    for i in range(len(menu)):
        if modelo == menu[i][0]:
            cash = (quantidade * menu[i][1])
            if 5000 > cash > 3000:
                valor = (cash * 5)/100
            elif cash > 5000:
                valor = (cash/10)
            else:
                valor = 0
    return valor

def calcular_Valor_cashback_2 (valor):      #Calcula o cashback e retorna o valor da segunda compra e seguintes 
    if 5000 > valor > 3000:
        valor = (valor * 5)/100
    elif valor > 5000:
        valor = (valor/10)
    else:
        valor = 0
    return valor

def verificar_Nome (lista,nome):    #Verifica se o nome ja esta na lista de e retorna um bool
    bool = True
    for i in range(len(lista)):
        if lista[i][0] == nome:
            bool = False
    return bool
    
def valor_Total (lista):    #Retorna o valor total gasto pelos compradores 
    valor = 0
    for i in range(len(lista)):
        valor += lista[i][3]
    return valor

def cliente_fiel(lista):    #Retorna uma lista com o compradore que mais comprou e todos os seus dados
    nome = lista[0][0]
    quantidade = lista[0][1]
    modelo = lista[0][2]
    valor = lista[0][3]
    for i in range(len(lista)):
        if quantidade < lista[i][1]:
            nome = lista[i][0]
            quantidade = lista[i][1]
            modelo = lista[i][2]
            valor = lista[i][3]
    a = [nome,quantidade,modelo,valor]
    return a

def melhor_funcionario (lista):     #Retorna uma lista com o funcionario que mais vendeu e sua bonificação
    nome = lista[0][0]
    quantidade = lista[0][1]
    valor = lista[0][2]
    for i in range(len(lista)):
        if quantidade < lista[i][1]:
            nome = lista[i][0]
            quantidade = lista[i][1]
            valor = lista[i][2]
    if nome == 'ger':
        bonificacao = ( valor * 15 )/100
        nome = 'gerente'
    elif nome == 'fun1':
        bonificacao = ( valor * 10 )/100
        nome = 'funcionario 1'
    elif nome == 'fun2': 
        bonificacao = ( valor * 10 )/100
        nome = 'funcionario 2'
    elif nome == 'fun3':
        bonificacao = ( valor * 10 )/100
        nome = 'funcionario 3'
    else:
        bonificacao = ( valor * 10 )/100
        nome = 'estagiario'
    a = [nome,quantidade,bonificacao]
    return a

# compradores
nomes_Compradores = add_Nome_Compradores(lista_Vendas)

for i in range(len(nomes_Compradores)):
    compras = 0
    prov = [nomes_Compradores[i],0,[],0,0]                  #['nome',quant,[modelo_tel],valor,cashback]
    for j in range(len(lista_Vendas)):
        if nomes_Compradores[i] == lista_Vendas[j][3]:                          # verifica se os nomes são iguais 
            prov[1] += lista_Vendas[j][1]                                       # adiciona a quantidade de compras feitas
            if lista_Vendas[j][2] not in prov[2]:                               #verificar a adicao da sigla na lista do compradores individuasi
                prov[2].append(lista_Vendas[j][2])
            if compras == 0:
                prov[4] = calcular_Valor_cashback(lista_Vendas[j][1],lista_Vendas[j][2]) #cashback
                prov[3] = calcular_Valor(lista_Vendas[j][1],lista_Vendas[j][2])
                compras += 1
            elif compras != 0:
                produto_Desconto = (calcular_Valor(lista_Vendas[j][1],lista_Vendas[j][2])-prov[4]) # valor da segunda compra - cashback
                prov[4] =  calcular_Valor_cashback_2(produto_Desconto)
                prov[3] += produto_Desconto
    compradores.append(prov)

# vendedores
for i in range(len(funcionario)):
    for j in range(len(lista_Vendas)):
        if funcionario[i][0] == lista_Vendas[j][0]:
            funcionario[i][1] += lista_Vendas[j][1]
            funcionario[i][2] += calcular_Valor(lista_Vendas[j][1],lista_Vendas[j][2])

#print(nomes_Compradores)
#print(compradores)
#print(funcionario)
print('Valor total das vendas do mês foi de R$ {}'.format(valor_Total(compradores)))
cliente = cliente_fiel(compradores)
print('Cliente Fiel do mês é {} , que comprou {} telefones no valor total de R$ {}'.format(cliente[0],cliente[1],cliente[3]))
print('{} comprou os telefones da marca {}'.format(cliente[0],cliente[2]))
empregado = melhor_funcionario(funcionario)
print('O funcionario que mais vendeu foi o {} , com um total de {} . Ele terá uma bonificação entra em seu salário de R$ {}'.format(empregado[0],empregado[1],empregado[2]))
