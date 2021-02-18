import cores
def pesquisa(nome):
    print(f'PESQUISA: {nome}')
    for c in leitura_da_listagem():
        if c['nome'] == nome:
            resultado = f'O {c["nome"]} tem {c["idade"]} anos'
            return resultado
    return 'Infelizmente não encontramos esta pessoa'

def verificar(nome):
    for c in leitura_da_listagem():
        if c['nome'] == nome:
            presente = True
            return presente

def leitura_da_listagem():
    dados=dict()
    from leitura import listagem_de_pessoas
    try:
        arquivo = open('lista_nomes.txt')

        for linha in arquivo:
            linha_separada = linha.split()
            dados['nome'] = linha_separada[0]
            dados['idade'] = linha_separada[1]
            listagem_de_pessoas.append(dados.copy())
        arquivo.close()
    except:
        resultado = ('-' * 22)
        resultado += ('\nARQUIVO PARA PESQUISA \n   NÃO ENCONTRADO\n')
        resultado += ('-' * 22)
        print(cores.pintura(C_L=31, msg=resultado))
        return []

    else:
        return listagem_de_pessoas