import os
#Declaração de varíaveis
valor: int = 0
arq: str = 'ex31_1.txt'
dir: str = 'temp/'

def gravarArquivo():
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
        for i in range(10, 151):
            linha = f"{i ** 2} \n"
            file.write(linha)

def main():
    gravarArquivo()
    
if __name__ == "__main__":
    main()
