# -*- coding: utf-8 -*-

def main():
    N = int(input())
    combinadas = []
    for caso in range(N):
        palavras = input().split(' ')
        combinadas.append(combinando(palavras[0], palavras[1]))
    for i in combinadas:
        print(i)


def combinando(lista1, lista2):
    resposta = []
    string = ''
    if len(lista1) == len(lista2):
        for i in zip(lista1, lista2):
            resposta.append(i[0]+i[1])
        for i in resposta:
            string += i
        return string
    else:
        if len(lista1) > len(lista2):
            maior = lista1
            menor = lista2

        elif len(lista1) < len(lista2):
            maior = lista2
            menor = lista1

        diferenca = (len(maior) - len(menor))
        for i in zip(lista1, lista2):
            resposta.append(i[0]+i[1])
        for item in maior[-diferenca:]:
            resposta.append(item)
        for i in resposta:
            string += i
        return string

if __name__ == '__main__':
    main()
