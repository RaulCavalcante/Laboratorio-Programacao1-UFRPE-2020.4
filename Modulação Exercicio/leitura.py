from time import sleep
import cores

listagem_de_pessoas = list()


def leitura():
    corL = cores.cores_letra('verde')

    try:
       arquivo = open('lista_nomes.txt')

       for linha in arquivo:
            linha = cores.pintura(C_L=corL, msg=linha, E_L=1)
            print(linha, end='')

            sleep(0.6)

       arquivo.close()
    except:
        msg = ('\n         ARQUIVO INEXISTENTE\n          CADASTRE PESSOAS\n')
        print(cores.pintura(C_L=31,msg=msg))

def extremos(extremo):

    dados = dict()
    dados['nome'] = ''
    global listagem_de_pessoas
    listagem_de_pessoas.clear()
    try:
        arquivo = open('lista_nomes.txt')
        for linha in arquivo:
            linha_separada= linha.split()
            dados['nome'] =  linha_separada[0]
            dados['idade'] = linha_separada[1]
            listagem_de_pessoas.append(dados.copy())
        arquivo.close()
        ordem = sorted(listagem_de_pessoas, key=lambda k: k['idade'], reverse=True)
        if extremo =='maior':
            resultado=(f'\n---------------------------------------\nPESSOA MAIS VELHA É {ordem[0]["nome"]} COM {ordem[0]["idade"]} ANOS\n---------------------------------------\n')
            for c in resultado:
                print(c ,end='')
                sleep(0)
        else:
            resultado=(f'\n---------------------------------------\nPESSOA MAIS NOVA É {ordem[len(listagem_de_pessoas)-1]["nome"]} COM {ordem[len(listagem_de_pessoas)-1]["idade"]} ANOS\n---------------------------------------\n')
            for c in resultado:
                print(c, end='')
                sleep(0)
    except:
        print()
        resultado=('-'*22)
        resultado+=('\nARQUIVO NÃO ENCONTRADO\n')
        resultado+=('-' * 22)
        print(cores.pintura(C_L=31,msg=resultado))
        print()