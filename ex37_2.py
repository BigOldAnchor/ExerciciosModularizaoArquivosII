import os

lista = []
dir: str = 'temp/'
arq = 'ex37_1.txt'
arqAnterior = 'ex37.txt'
lista = [] 

def ehImpar(n):
    if n % 2 != 0:
        return True
    else:
        return False

def gravarArquivo(n):
    global valor, arq, dir
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
        for i in range(0, len(n)):
            linha = str(n[i]) + "\n"
            file.write(linha)

def ler():
    global dir, arqAnterior
    file = ''
    enc = ''
    linha = ''

    file = os.path.join(dir, arqAnterior)
    enc = 'utf-8'

    if os.path.exists(file) and os.path.isfile(file):
        with open(file, 'r', encoding=enc) as file:
            for linha in file:
                    if ehImpar(int(linha.strip())):
                        lista.append(int(linha.strip()))
                    else:
                        lista.append('-1')
        gravarArquivo(lista)
    else:

def main():
    ler()

if __name__ == "__main__":
    main()
