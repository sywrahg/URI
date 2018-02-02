# -*- coding: utf-8 -*-

def main():
    teste = int(input())
    while teste != 2002:
        print('Senha Invalida')
        teste = int(input())
    else:
        print('Acesso Permitido')

if __name__ == '__main__':
    main()
