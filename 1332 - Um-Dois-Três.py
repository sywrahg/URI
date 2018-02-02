# -*- coding: utf-8 -*-

def main():
    respostas = []
    N = int(input())
    one = 'one'
    for i in range(N):
        contador = 0
        palavra = input()
        for i in range(3):
            if palavra[i] in one[i]:
                contador += 1

        if contador > 1:
            numero = 1
        if contador <= 1:
            numero = 2
        if len(palavra) == 5:
            numero = 3
        respostas.append(numero)
    for item in respostas:
        print(item)

if __name__ == '__main__':
	main()
