# -*- coding: utf-8 -*-

def main():
    N = int(input())
    cont_total = 0
    coelho = 0
    rato = 0
    sapo = 0
    while N > 0:
        caso_teste, tipo_cobaia = (i for i in input().split())
        caso_teste = int(caso_teste)
        cont_total = cont_total + caso_teste
        if tipo_cobaia == 'C':
            coelho = coelho + caso_teste
            N -= 1
        elif tipo_cobaia == 'R':
            rato = rato + caso_teste
            N -= 1
        elif tipo_cobaia == 'S':
            sapo = sapo + caso_teste
            N -= 1
    percentual_coelho = (coelho / cont_total) * 100
    percentual_rato = (rato / cont_total) * 100
    percentual_sapo = (sapo / cont_total) * 100

    print('Total: %d cobaias' %(cont_total))
    print('Total de coelhos: %d' % (coelho))
    print('Total de ratos: %d' %(rato))
    print('Total de sapos: %d' % (sapo))
    print('Percentual de coelhos: %.2f %%' %(percentual_coelho))
    print('Percentual de ratos: %.2f %%' %(percentual_rato))
    print('Percentual de sapos: %.2f %%' %(percentual_sapo))

if __name__ == '__main__':
    main()
