# -*- coding: utf-8 -*-

def main():
    funcionario, horas_trabalhadas, valor_hora = int(input()), int(input()), float(input())
    salario = horas_trabalhadas * valor_hora
    print('NUMBER = %d' %(funcionario))
    print('SALARY = U$ %.2f' %(salario))

if __name__ == '__main__':
    main()
