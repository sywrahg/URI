# -*- coding: utf-8 -*-

def main():
    C = int(input())
    resultados = []
    item = ''
    for i in range(C):
        inicio, fim = (int(i) for i in input().split(' '))
        lista_decrescente = ''
        for i in range(inicio, fim + 1):
            item += str(i)
            lista_decrescente += str(i)
        for j in lista_decrescente[::-1]:
            item += str(j)
        resultados.append(item)
        item = ''
    for sequencia in resultados:
        print(sequencia)

if __name__ == '__main__':
    main()
