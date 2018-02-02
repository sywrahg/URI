# -*- coding: utf-8 -*-

def main():
    while True:
        try:
            L = int(input())
            if L > 0:
                nivel1 = 0
                nivel2 = 0
                nivel3 = 0
                lista_vi = ([int(i) for i in input().split()])
                for i in lista_vi:
                    if i >= 20:
                        nivel3 += 1
                    elif i >= 10 and i < 20:
                        nivel2 += 1
                    elif i < 10:
                        nivel1 += 1
                if nivel3 > 0:
                    print('3')
                elif nivel2 > 0:
                    print('2')
                else:
                    print('1')
        except:
            break
if __name__ == '__main__':
    main()
