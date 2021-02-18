# Projeto Lab 1 - PLE 2020.4<h1> 

### 1 -> Conteúdo a ser trabalhado com **[ IF , For, Lista ]** <h3>

#### Você é Dono de uma Loja da Samsung, sua grade de funcionarios consiste de **1 gerente**, **3 funcionários** e **1 estagiário**. Faça um programa que após receber a entrada de uma lista, que em sua sublistas existe a quantidade de vendas do mês no formato **[ Funcionario, Cliente, Modelo_Tel_1, Modelo_Tel_2 ]**, e mostre na tela:
* O valor total de vendas da loja
* O cliente que mais comprou **{ Valor gasto e quantidade ( Uma lista apenas para os modelos de telefone que ele comprou ) }**
* O funcionário que mais vendeu recebe uma bonificação **(15% gerente, 10% funcionário e 5% estagiário)** do valor total das suas vendas.
* O cliente tem direito a recebe **5%** de cashback, se sua compra der mais de R$ 3000. Caso passe de 5000 recebe **10%**, para ser utilizado nas próximas comprar **(Se houver)**. 
 
## Menu

Modelo   | Preço
--------- | ------
Samsung M51 | R$ 2300
Samsung S10 | R$ 2500
Samsung Note 20 | R$ 2700
Samsung A31 | R$ 1490
Samgung S20 | R$ 3200

## Entrada

```python
    #[str,int,str,str]
    [ [ger,1,M51,Pedro] , [fun1,3,A31,Laura] , [fun2,2,Note20,João] , [fun2,1,S10,Matheus] , [est,4,S10,Pedro] , [est,2,S10,Pedro] , [fun2,3,M51,Caio] ]
```

## Saida -corrigir para valores reais da entrada proposta-

~~~python
    Valor total das vendas R$ 18790
    Cliente Fiel do mês é Pedro, que comprou 7 telefones no valor total de R$ 6500
    [‘S20’,’M51’,’A31’]
    O estagiario vendeu 6 telefones e terá uma bonificação de R$ 2495 em seu salário
~~~

# Regras
* Ao mostrar a lista de telefones comprados pelo **cliente fiel**, não pode repetir os telefones de mesmo modelo. **Ex: [ ‘S20’,’S20’,’M51’,’M51’ ] -> [ ’S20’,’M51’ ]** 
* A entrada do modelo sera pela sua sigla **Ex: Samsung M51 -> 'M51'** 
* Entrada dos funcionarios: **Gerente -> 'ger' | Funcionario 1 -> 'fun1' | Funcionario 2 -> 'fun2' | Funcionario 3 -> 'fun3' | Estagiario -> 'est'**
* Funcionamento do "Cashback":**1 compra de joão, ele comprou 3 S10 , total a pagar R$ 7500 (3*2500) - cashback R$ 750. Na 2 compra de joão, ele comprou 3 S10, total a pagar R$ 6750 (7500 - 750) - cashback de R$ 675. 3 compra de joão, ele comprou 1 S10, total a pagar R$ 1850 (2500 - 650) - cashback de R$ 0. João gastou no total R$ 16100 (7500+6750+1850)**      

