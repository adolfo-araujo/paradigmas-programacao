# Aula 08 - Exercício 03 - Proj4 - Programa principal (Python)
from classe.carro import Carro


def main():
    # Duas instâncias da classe Carro com dados diferentes
    carro1 = Carro("Volkswagen", "Gol", "Prata", 2022, 72990.00)
    carro2 = Carro("Toyota", "Corolla", "Preto", 2024, 159990.00)

    print(carro1)
    print(carro2)
    print()

    carro1.acelerar(40)
    carro1.acelerar(20)
    carro1.frear(30)
    carro1.frear(30)
    carro1.frear()        # já parado
    print()

    carro2.acelerar(80)
    carro2.acelerar(150)  # limitado à velocidade máxima
    carro2.frear(50)


if __name__ == "__main__":
    main()
