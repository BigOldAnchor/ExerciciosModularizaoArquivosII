import os
# Declaração de arquivos
valor: int = 0
arq: str = "ex37.txt"
dir: str = "temp/"
lista = []

def fibonacci():
    global lista, valor
    a, b = 0, 1
    for i in range(1, valor):
        a, b = b, a + b
        lista.append(b)

def gravarArquivo():
    global valor, arq, dir, lista
    linha: str = ''
    file: str = ''
    tipo: str = ''
    enc: str = ''

    file = os.path.join(dir, arq)
    enc = 'utf-8'

    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.isfile(file):
            tipo = 'w'
        else:
            tipo = 'w'

    with open(file, tipo, encoding=enc) as file:
        for i in range(len(lista)):
            linha = f"{lista[i]}\n"
            file.write(linha)

def main():
    global valor
    valor = int(input("Insira um valor inteiro: \n"))
    fibonacci()
    gravarArquivo()

if __name__ == "__main__":
    main()
                
