# -*- coding: utf-8 -*-
def main():
    N = int(input())
    vetor = []
    while len(vetor) < N:
        vetor = [int(i) for i in input().split()]
    menor = min(vetor)
    posicao = vetor.index(menor)
    print('Menor valor: %d' %(menor))
    print('Posicao: %d' %(posicao))

if __name__ == '__main__':
    main()
