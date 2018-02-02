# -*- coding: utf-8 -*-

def main():
    individuos = []
    contador, soma_idade = 0, 0
    while True:
        idade = int(input())
        if idade < 0:
            break
        else:
            individuos.append(idade)
            contador += 1

    for i in individuos:
        soma_idade = soma_idade + i
    media = soma_idade / contador
    print('%.2f' %(media))

if __name__ == '__main__':
    main()
