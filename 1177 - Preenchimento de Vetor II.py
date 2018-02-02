# -*- coding: utf-8 -*-

def main():
    vetor = []
    T = int(input())
    contador = 0
    while len(vetor) < 1000:
        vetor.append(contador)
        contador += 1
        if contador == T:
            contador = 0
    for i in range(1000):
        print('N[%d] = %d' % (i, vetor[i]))

if __name__ == '__main__':
    main()
