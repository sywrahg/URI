# -*- coding: utf-8 -*-

def main():
    A, B, C = ([float(i) for i in input().split()])
    maiorAB = (A + B + abs(A - B))/2
    maior_maior = (maiorAB + C + abs(maiorAB - C))/2
    print('%d eh o maior' %(maior_maior))
if __name__ == '__main__':
    main()
