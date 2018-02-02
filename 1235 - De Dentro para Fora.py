# -*- coding: utf-8 -*-

def main():
	N = int(input())
	for i in range(N):
		resposta = ''
		frase = input()
		metade = int(len(frase) / 2)
		resposta += frase[metade -1 ::-1] + frase[:metade -1:-1]
		print(resposta)


if __name__ == '__main__':
	main()
