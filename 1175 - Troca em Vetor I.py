# -*- coding: utf-8 -*-


def main():
    vetor = []
    indice = 0
    while len(vetor) < 20:
        N = float(input())
        vetor.append(N)
    for item in reversed(vetor):
        print('N[%d] = %d' % (indice, item))
        indice += 1

if __name__ == '__main__':
    main()
