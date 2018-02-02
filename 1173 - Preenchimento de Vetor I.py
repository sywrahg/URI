# -*- coding: utf-8 -*-
def main():
    vetor = []
    indice = 0
    V = int(input())
    vetor.append(V)
    for item in vetor:
        if len(vetor) == 11:
            break
        else:
            vetor.append(item * 2)
            print('N[%d] = %d' % (indice, item))
            indice += 1

if __name__ == '__main__':
    main()
