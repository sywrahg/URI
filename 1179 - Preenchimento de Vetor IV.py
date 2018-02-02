# -*- coding: utf-8 -*-

def main():
    pares = []
    impares = []

    for i in range(15):
        valor = int(input())
        if valor % 2 == 0:
            pares.append(valor)
            if (len(pares)) == 5:
                exibe(pares, 'par')
                pares = []
        else:
            impares.append(valor)
            if (len(impares)) == 5:
                exibe(impares, 'impar')
                impares = []

    exibe(impares, 'impar')
    exibe(pares, 'par')


def exibe(lista, tipo):
    for i in range(len(lista)):
        print('%s[%d] = %d' % (tipo, i, lista[i]))


if __name__ == '__main__':
    main()
