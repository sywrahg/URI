# -*- coding: utf-8 -*-
"""
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois
valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
"""
def main():
    N = int(input())
    while N > 0:
        A, B = ([i for i in input().split()])
        inversoA = A[::-1]
        inversoB = B[::-1]
        tamanhoB = len(B)
        resposta = str.find(inversoA, inversoB, 0, tamanhoB)
        if resposta == -1:
            print('nao encaixa')
        else:
            print('encaixa')
        N -= 1

if __name__ == '__main__':
    main()
