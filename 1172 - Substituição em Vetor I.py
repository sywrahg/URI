# -*- coding: utf-8 -*-

def main():
    X = []
    while len(X) < 10:
        y = int(input())
        if y <= 0:
            X.append(1)
        else:
            X.append(y)
    contador = 0
    for i in X:
        print ('X[%d] = %d' % (contador, i))
        contador += 1

if __name__ == '__main__':
    main()
