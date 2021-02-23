# Projeto Lab 1 - PLE 2020.4<h1> 

### 1 -> Conteúdo a ser trabalhado com **[ IF , For, Lista e Sublista]** <h3>

#### Você é Dono de uma Loja da Samsung, sua grade de funcionarios consiste de **1 gerente**, **3 funcionários** e **1 estagiário**. Faça um programa que após receber a entrada de uma lista, no formato **[ [str,int,[str],str], [str,int,[str],str]... ]** , que em sua sublistas existe a seguinte ordem: **[str(nome do funcionario), int(quantidade vendida) , list(str(modelo do telefone)) , str(Nome do cliente) ]** e mostre na tela:
* O valor total de vendas da loja
* O cliente que mais comprou **( Valor gasto e quantidade )**
* Uma lista apenas para os modelos de telefone do cliente que mais  comprou 
* O nome funcionário que mais vendeu, quantidade e sua bonificação **(15% gerente, 10% funcionário e 5% estagiário)** do valor total das suas vendas, no valor integral do menu da loja, sem o cashback.
* O cliente tem direito a receber **5%** de cashback, se sua compra der mais de R$ 3000 ou **10%** se passar de 5000, para ser utilizado nas próximas comprar **(Se houver)**. 

### **Observações:**
* Ao mostrar a lista de telefones comprados pelo **cliente que mais comprou**, não pode repetir os telefones de mesmo modelo. **Ex: [ ‘S20’,’S20’,’M51’,’M51’ ] -> [ ’S20’,’M51’ ]** 
* A entrada do modelo sera pela sua sigla Ex: Samsung M51 -> **'M51'** 
* Entrada dos funcionarios: **gerente -> 'ger' | funcionario 1 -> 'fun1' | funcionario 2 -> 'fun2' | funcionario 3 -> 'fun3' | estagiario -> 'est'**
* Funcionamento do **"Cashback"** : 1 compra de joão, ele comprou 3 S10 , total a pagar R$ 7500 (3*2500) - cashback R$ 750. Na 2 compra de joão, ele comprou 3 S10, total a pagar R$ 6750 (7500 - 750) - cashback de R$ 675. 3 compra de joão, ele comprou 1 S10, total a pagar R$ 1850 (2500 - 650) - cashback de R$ 0. João gastou no total R$ 16100 (7500+6750+1850)
* Não terá **empate** em cliente que mais comprou e funcionario que mais vendeu   
* Cada programador tem sua forma de fazer. Logo, existem muitas formas de implementar este programa.

## Formato de Entrada

receber a entrada de uma lista, no formato **[ [str,int,[str],str], [str,int,[str],str]... ]** , que em sua sublistas existe a seguinte ordem: **[str(nome do funcionario), int(quantidade vendida) , list(str(modelo do telefone)) , str(Nome do cliente) ]**

## Formato de Saida

Faça a impressão dos dados: **Valor total das vendas , Nome do cliente que mais comprou junto com sua quantidade, Nome do cliente que mais comprou e sua lista de siglas do(s) modelo(s) comprado(s), nome do funcionario que mais vendeu junto com sua quantidade e sua bonificação**.  


## Menu

Modelo   | Preço
--------- | ------
Samsung M51 | R$ 2300
Samsung S10 | R$ 2500
Samsung NT20 | R$ 2700
Samsung A31 | R$ 1500
Samgung S20 | R$ 3200


## Entrada - Caso 1 

```python

#[ [str,int,[str],str] , [str,int,[str],str] , ... ]
[['ger',1,'M51','Pedro'] , ['fun1',3,'A31','Laura'] , ['fun2',2,'NT20','João'] , ['fun2',1,'S10','Matheus'] , ['est',4,'S10','Pedro'] , ['est',2,'S10','Pedro'] , ['fun2',4,'M51','Caio'] ]

```
## Saida - Caso 1 

```

Valor total das vendas do mês foi de R$ 37900.0
Cliente Fiel do mês é Pedro , que comprou 7 telefones no valor total de R$ 16300.0
Pedro comprou os telefones da marca ['M51', 'S10']
O funcionario que mais vendeu foi o funcionario 2 , com um total de 7 . Ele terá uma bonificação entra em seu salário de R$ 1710.0

```

## Entrada - Caso 2

```python

#[ [str,int,[str],str] , [str,int,[str],str] , ... ]
[['ger',4,'S10','Raul'],['ger',2,'A31','Raul'],['ger',4,'M51','Raul'],['fun3',15,'A31','Arthur'],['est',2,'S10','Ricardo'],['est',2,'S10','Ricardo']]

```

## Saida - Caso 2

```

Valor total das vendas do mês foi de R$ 53700.0
Cliente Fiel do mês é Arthur , que comprou 15 telefones no valor total de R$ 22500
Arthur comprou os telefones da marca ['A31']
O funcionario que mais vendeu foi o funcionario 3 , com um total de 15 . Ele terá uma bonificação entra em seu salário de R$ 2250.0

```
