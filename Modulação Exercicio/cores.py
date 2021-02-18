'''
#Como utilizar cores no terminal.
#\033[style;tex;back m
#style- 0->nada/1->negrito/4->sublinhado/7->negativo
#text - 30branco/31vermelho/32verde/33amarelo/34azul/35roxo/36verde/37cinza
#back - 40branco/41vermelho/42verde/43amarelo/44azul/45roxo/46verde/47cinza
'''


def cores_fundo(cor=0, opções=False):
    cores=dict()
    cores['branco'] =   40
    cores['vermelho'] = 41
    cores['verde'] =    42
    cores['amarelo'] =  43
    cores['azul'] =     44
    cores['roxo'] =     45
    cores['cinza'] =    47
    if opções:
        for k in cores.keys():
            print(f'{k}', end='  ')
    if cor in cores.keys():
        for k,v in cores.items():
            if cor == k:
                return v
    else:
     #   print('VALOR INVALIDO NA FUNÇÃO CORES_FUNDO')
        pass

def cores_letra(cor=37, opções=False):

    cores = dict()

    cores['branco'] = 30

    cores['vermelho'] = 31

    cores['verde'] = 32

    cores['amarelo'] = 33

    cores['azul'] = 34

    cores['roxo'] = 35

    cores['cinza'] = 37
    if opções:
        for k in cores.keys():
            print(f'{k}', end='  ')

    if cor in cores.keys():
        for k, v in cores.items():
           if cor == k:
               return v
    else:
       # print('VALOR INVALIDO NA FUNÇÃO CORES_LETRA')
        pass

def estilo_letra(estil=0, opções=False):
    estilo=dict()

    estilo['nada'] = 0
    estilo['negrito'] = 1
    estilo['sublinhado'] = 4
    estilo['negativo'] = 7
    if opções:
        for k in estilo.keys():
            print(f'{k}', end='  ')
    if estil in estilo.keys():
        for k, v in estilo.items():
            if estil == k:
                return v
    else:
        print('VALOR INVALIDO NA FUNÇÃO ESTILO_LETRA')


def pintura(E_L=0,C_L=0, C_F=0, msg=''):

    return f'\033[{0};{C_L};{C_F}m{msg}\033[{0};{0};{0}m'