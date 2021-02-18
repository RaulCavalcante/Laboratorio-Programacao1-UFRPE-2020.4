from menu import menu
from escrita import escrita
from leitura import leitura
import cores
from leitura import extremos
from escrita import apagar_arquivo
from menu import leia_int
from pesquisa import pesquisa


def exibição():
    corL=cores.cores_letra('azul')
    introdução=(f'---------PESSOAS CADASTRADAS--------\nNOME{"IDADE":>32}')
    introdução=cores.pintura(C_L=corL, msg=introdução)
    print(introdução)
    leitura()
    print(cores.pintura(C_L=corL, msg='------FIM DA LEITURA DO ARQUIVO-----'))



while True:
    menu()
    escolha=leia_int('ESCOLHA: ')
    if escolha == 1:
        escrita()
    elif escolha == 2:
        exibição()
    elif escolha == 4:
        extremos('maior')
    elif escolha == 6:
        apagar_arquivo()
    elif escolha == 5:
        extremos('menor')
    elif escolha == 7:
       resposta = pesquisa(str(input('Nome desejado: ')).lower().capitalize())
       print(resposta)
    else:
        corL=cores.cores_letra('vermelho')
        fim=(f'{" "*10}FIM DO PROGRAMA')
        fim= cores.pintura(C_L=corL, msg=fim)
        print(fim)
        break