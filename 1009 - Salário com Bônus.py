# -*- coding: utf-8 -*-

def main():
    nome_vendedor, salario_fixo, total_vendas = input(), float(input()), float(input())
    salario_final = salario_fixo + total_vendas * 0.15
    print('TOTAL = R$ %.2f' %(salario_final))

if __name__ == '__main__':
    main()
