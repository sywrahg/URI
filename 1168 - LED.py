# -*- coding: utf-8 -*-
def main():
	mapa = {'1':2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
	N = int(input())
	resultados = []

	for i in range(N):
		numero = input()
		leds = 0
		for j in numero:
			leds += mapa[j]
		resultados.append(leds)

	for i in resultados:
		print ("%d leds" % (i))

if __name__ == '__main__':
	main()
