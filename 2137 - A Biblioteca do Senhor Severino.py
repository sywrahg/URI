# -*- coding: utf-8 -*-
def main():
    while True:
        try:
            ordenados = []
            N = int(input())
            for i in range(N):
                numero = input()
                ordenados.append(numero)
            ordenados.sort()
            for item in ordenados:
                print(item)

        except:
            break

if __name__ == '__main__':
    main()
