import os.path
import cores
import menu
import pesquisa

def escrita():
    Narquivo='lista_nomes.txt'
    if not (os.path.exists(Narquivo)):
        arquivo = open(Narquivo, 'w')
    else:
        arquivo = open(Narquivo, 'a')

    nome = str(input(cores.pintura(C_L=36, msg='Informe o nome: '))).lower().capitalize()
    verif = verificar(nome)
        if verif == True:
            print(' Pessoa já cadastrada ')
        else:
            idade = menu.leia_int('Informe sua idade: ')

            texto=(f'{nome:<19}{idade:>17}\n')

            arquivo.write(texto)

    arquivo.close()
    return texto


def apagar_arquivo():
    try:
        os.remove('lista_nomes.txt')
        print()
        mensagem = ('='*25)
        mensagem += ('\nARQUIVO DE TEXTO DELETADO\n')
        mensagem +=('='*25)
        print(cores.pintura(C_L=36,msg=mensagem))
    except:
        msg = (f'{"-"*19:^30}')

        msg += (f'\n{"ARQUIVO INEXISTENTE":^30}\n{"CADASTRE PESSOAS":^30}\n')
        msg += (f'{"-"*19:^30}')

        from cores import pintura
        msg=pintura(C_L=31, msg=msg)
        print(msg)