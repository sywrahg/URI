# -*- coding: utf-8 -*-
def main():
	N = int(input())
	for i in range(N):
		casos = []
		total = 0
		alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		valor = int(input())
		casos = [input().upper() for i in range(valor)]

		for item in range(len(casos)):
			for i in range(len(casos[item])):
				total += item + i + alfabeto.index(casos[item][i])
		print (total)

if __name__ == '__main__':
	main()
