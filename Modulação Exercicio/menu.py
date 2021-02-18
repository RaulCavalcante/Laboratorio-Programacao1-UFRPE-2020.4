import cores
def menu():
    menu=(f'{"-="*10}\n{"MENU":^20}\n{"-="*10}\n1-ADICIONAR PESSOA\n2-LER PESSOAS\n3-SAIR\n4-PESSOA MAIS VELHA\n5-PESSOA MAIS NOVA\n6-REMOVER ARQUIVO\n7-PESQUISAR')
    print(cores.pintura(C_L=35,msg=menu))


def leia_int(msg):

    while True:
        valor = str(input(cores.pintura(C_L=34, msg=msg)))

        if valor.isnumeric():
            return int(valor)
        else:
            print(cores.pintura(C_L=34, msg='VALOR INVALIDO!'))