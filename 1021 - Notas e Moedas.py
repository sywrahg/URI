# -*- coding: utf-8 -*-
def main():
    valor = float(input())
    moeda = (valor % 2) * 100
    nota100, nota50, nota20, nota10, nota5, nota2 = 0, 0, 0, 0, 0, 0
    moeda100, moeda50, moeda25, moeda10, moeda05, moeda01 = 0, 0, 0, 0, 0, 0

    while valor >= 100:
        nota100 += 1
        valor -= 100
    while valor >= 50:
        nota50 += 1
        valor -= 50
    while valor >= 20:
        nota20 += 1
        valor -= 20
    while valor >= 10:
        nota10 += 1
        valor -= 10
    while valor >= 5:
        nota5 += 1
        valor -= 5
    while valor >= 2:
        nota2 += 1
        valor -= 2

    moeda = valor * 100
    if moeda >= 100:
        moeda100 += 1
        moeda -= 100
    while moeda >= 50:
        moeda50 += 1
        moeda -= 50
    while moeda >= 25:
        moeda25 += 1
        moeda -= 25
    while moeda >= 10:
        moeda10 += 1
        moeda -= 10
    while moeda >= 5:
        moeda05 += 1
        moeda -= 5
    while moeda >= 1:
        moeda01 += 1
        moeda -= 1

    print('NOTAS:')
    print('%d nota(s) de R$ 100.00'% nota100)
    print('%d nota(s) de R$ 50.00'% nota50)
    print('%d nota(s) de R$ 20.00' % nota20)
    print('%d nota(s) de R$ 10.00' % nota10)
    print('%d nota(s) de R$ 5.00' % nota5)
    print('%d nota(s) de R$ 2.00' % nota2)
    print('MOEDAS:')
    print('%d moeda(s) de R$ 1.00' % moeda100)
    print('%d moeda(s) de R$ 0.50' % moeda50)
    print('%d moeda(s) de R$ 0.25' % moeda25)
    print('%d moeda(s) de R$ 0.10' % moeda10)
    print('%d moeda(s) de R$ 0.05' % moeda05)
    print('%d moeda(s) de R$ 0.01' % moeda01)

if __name__ == '__main__':
    main()
