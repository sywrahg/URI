# -*- coding: utf-8 -*-
"""
FIBONACCI EM VETOR
"""

def main():
    fibonacci = [0, 1]
    T = int(input())
    while T > 0:
        N = int(input())
        for i in range(N):
            item = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(item)
        print('Fib(%d) = %d' %(N, fibonacci[N]))
        T -= 1

if __name__ == '__main__':
    main()
