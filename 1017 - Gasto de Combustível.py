# -*- coding: utf-8 -*-

def main():
    tempo, velocidade = int(input()), int(input())
    distancia = velocidade * tempo
    qtd_gasto = distancia / 12
    print('%.3f' %(qtd_gasto))

if __name__ == '__main__':
    main()
