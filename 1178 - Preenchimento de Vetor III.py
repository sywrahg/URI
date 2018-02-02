# -*- coding: utf-8 -*-
def main():
    vetor = []
    X = float(input())
    vetor.append(X)
    for i in range(100):
        vetor.append(vetor[i] / 2)
        print('N[%d] = %.4f' % (i, vetor[i]))

if __name__ == '__main__':
    main()
