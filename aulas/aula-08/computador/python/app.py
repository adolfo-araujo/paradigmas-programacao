# Aula 08 - Exercício 01 - Proj3 - Programa principal (Python)
from classe.computador import Computador


def main():
    # Duas instâncias da classe Computador com dados diferentes
    pc1 = Computador("Dell", 16, "NVIDIA GeForce RTX 4060")
    pc2 = Computador("Lenovo", 8, "Intel Iris Xe")

    print(pc1)
    print(pc2)
    print()

    pc1.processar("Renderização de vídeo")   # desligado: não processa
    pc1.ligar()
    pc1.processar("Renderização de vídeo")
    pc1.desligar()
    print()

    pc2.ligar()
    pc2.ligar()                               # já ligado
    pc2.processar("Planilha de notas")
    print(pc2)
    pc2.desligar()


if __name__ == "__main__":
    main()
