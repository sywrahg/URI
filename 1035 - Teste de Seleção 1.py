# -*- coding: utf-8 -*-

def main():
    A, B, C, D = ([int(i) for i in input().split()])
    somaAB = A + B
    somaCD = C + D
    if B > C and D > A and somaCD > somaAB and C > 0 and D > 0 and A % 2 == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')
if __name__ == '__main__':
    main()
