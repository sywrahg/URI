# -*- coding: utf-8 -*-

def main():
    while True:
        try:
            sentenca = str(input())
            sentenca_dancante = ""
            contador = 0
            for letra in sentenca:
                if letra == " ":
                    sentenca_dancante += " "
                elif contador % 2 == 0:
                    sentenca_dancante += letra.upper()
                    contador += 1
                elif contador % 2 != 0:
                    sentenca_dancante += letra.lower()
                    contador += 1
            print(sentenca_dancante)

        except:
            break
if __name__ == '__main__':
    main()
