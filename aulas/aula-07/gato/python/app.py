# Aula 07 - Proj2 - Programa principal (Python)
# Cria duas instâncias da classe Gato e percorre a máquina de estados.

from classe.gato import Gato


def main():
    # Duas instâncias (objetos) da mesma classe, com dados diferentes
    gato1 = Gato("Mingau", "Persa")
    gato2 = Gato("Frajola", "Siamês")

    print("=== Estado inicial ===")
    print(gato1.status())
    print(gato2.status())

    print("\n=== Rotina do Mingau ===")
    gato1.brincar()
    gato1.brincar()
    gato1.brincar()
    gato1.brincar()      # energia baixa: transição negada
    gato1.comer()
    gato1.dormir()
    gato1.dormir()       # já está dormindo
    print(gato1.status())

    print("\n=== Rotina do Frajola ===")
    gato2.comer()        # sem fome: transição negada
    gato2.brincar()
    gato2.comer()
    gato2.dormir()
    gato2.brincar()      # acorda para brincar
    print(gato2.status())


if __name__ == "__main__":
    main()
