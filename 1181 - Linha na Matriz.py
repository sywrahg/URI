# -*- coding: utf-8 -*-

def main():
    matriz11x11 =[]
    L = int(input())
    T = input().upper()
    for i in range(12):
        linha_matriz = []
        for i in range(12):
            numero = float(input())
            linha_matriz.append(numero)
        matriz11x11.append(linha_matriz)
    if T == 'S':
        soma = sum(matriz11x11[L])
        print('%.1f' %(soma))
    elif T == 'M':
        media = (sum(matriz11x11[L])) /12
        print('%.1f' %(media))

if __name__ == '__main__':
    main()
