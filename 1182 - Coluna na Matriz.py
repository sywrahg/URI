# -*- coding: utf-8 -*-
def main():
    matriz11x11 =[]
    soma = 0
    C = int(input())
    T = input().upper()
    for i in range(12):
        linha_matriz = []
        for i in range(12):
            numero = float(input())
            linha_matriz.append(numero)
        matriz11x11.append(linha_matriz)

    for i in range(len(matriz11x11)):
        soma += matriz11x11[i][C]
    if T == 'S':
        print('%.1f' %(soma))
    elif T == 'M':
        print('%.1f' %(soma /12))

if __name__ == '__main__':
    main()
