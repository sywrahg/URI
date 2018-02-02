# -*- coding: utf-8 -*-

def main():
    A, B, C = ([float(i) for i in input().split()])
    triangulo_retangulo = (A * C) / 2
    circulo = 3.14159 * (C ** 2)
    trapezio = ((A + B) * C) / 2
    quadrado = B * B
    retangulo = A * B
    print('TRIANGULO: %.3f' %(triangulo_retangulo))
    print('CIRCULO: %.3f' %(circulo))
    print('TRAPEZIO: %.3f' %(trapezio))
    print('QUADRADO: %.3f' %(quadrado))
    print('RETANGULO: %.3f' %(retangulo))

if __name__ == '__main__':
    main()
