# -*- coding: utf-8 -*-

def main():
    N = int(input())
    lista = []
    for i in range(N):
        pokemon = input().lower()
        if pokemon not in lista:
            lista.append(pokemon)
    X = 151 - len(lista)
    print('Falta(m) %d pomekon(s).' %(X))

if __name__ == '__main__':
    main()
