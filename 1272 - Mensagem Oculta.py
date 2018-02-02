# -*- coding: utf-8 -*-
def main():
    N = int(input())
    respostas = []
    item = ''
    for i in range(N):
        mensagem = input().split(' ')
        for palavra in mensagem:
            if len(palavra) > 0:
                item += palavra[0]
        respostas.append(item)
        item = ''
    for i in respostas:
        print(i)

if __name__ == '__main__':
    main()
