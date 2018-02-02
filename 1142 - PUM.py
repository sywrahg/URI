# -*- coding: utf-8 -*-

def main():
    N = int(input())

    for i in range(1, (N * 4) + 1):
        if i % 4 == 0:
            print('PUM')
        else:
            print (i,'', end='')

if __name__ == '__main__':
    main()
