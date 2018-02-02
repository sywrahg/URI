# -*- coding: utf-8 -*-
def main():
    vetor = []
    while len(vetor) < 100:
        A = float(input())
        vetor.append(A)
    for i in range(100):
        if vetor[i] <= 10:
            print('A[%d] = %.1f' % (i ,vetor[i]))

if __name__ == '__main__':
    main()
