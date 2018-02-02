# -*- coding: utf-8 -*-
def main():
    while True:
        D, N = ([i for i in input().split()])
        V = 0
        if D != '0' and N != '0':
            for i in N:
                if D == i and i == i:
                    pass
                else:
                    V = N.replace(D, '')
            print(int(V))
        else:
            return False

if __name__ == '__main__':
    main()
