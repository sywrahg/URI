# -*- coding: utf-8 -*-

import math
def main():
    x1, y1 = ([float(i) for i in input().split()])
    x2, y2 = ([float(i) for i in input().split()])
    diferenca_quadrado_x = (x2 - x1) ** 2
    diferenca_quadrado_y = (y2 - y1) ** 2
    distancia = math.sqrt(diferenca_quadrado_x + diferenca_quadrado_y)
    print('%.4f' %(distancia))

if __name__ == '__main__':
    main()
