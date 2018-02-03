# -*- coding: utf-8 -*-

def main():
    id_peca1, numero_pecas1, valor_u_peca1 = ([float(i) for i in input().split()])
    id_peca2, numero_pecas2, valor_u_peca2 = ([float(i) for i in input().split()])
    valor_total = (numero_pecas1 * valor_u_peca1) + (numero_pecas2 * valor_u_peca2)
    print('VALOR A PAGAR: R$ %.2f' %(valor_total))

if __name__ == '__main__':
    main()
