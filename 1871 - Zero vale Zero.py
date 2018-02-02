# -*- coding: utf-8 -*-

def main():
    M, N = (i for i in input().split(' '))
    resposta = ''
    while M != '0' and N != '0':
        soma = int(M) + int(N)
        for i in str(soma):
            if i == '0':
                continue
            else:
                resposta += i
        print(resposta)
        main()
        break

if __name__ == '__main__':
    main()
