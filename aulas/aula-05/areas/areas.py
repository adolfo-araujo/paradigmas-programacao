# Aula 05 - Atividade Dirigida - Área de figuras geométricas (Python)
# Uma função para cada figura, seguindo o modelo da função areaquad().

PI = 3.14   # valor de Pi indicado no slide


def areatriang(base, altura):
    return (base * altura) / 2          # A = (b . h) / 2


def areacirc(raio):
    return PI * raio ** 2               # A = Pi . r²


def arealosango(diag_maior, diag_menor):
    return (diag_maior * diag_menor) / 2   # A = (D . d) / 2


def arearet(base, altura):
    return base * altura                # A = b . h


def areatrap(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2   # A = ((B + b) . h) / 2


def ler(msg):
    """Lê um número real positivo (aceita vírgula ou ponto)."""
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor > 0:
                return valor
        except ValueError:
            pass
        print("Valor inválido! Digite um número maior que zero.")


def menu():
    print("\n===== ÁREA DE FIGURAS GEOMÉTRICAS =====")
    print("[1] Triângulo")
    print("[2] Círculo")
    print("[3] Losango")
    print("[4] Retângulo")
    print("[5] Trapézio")
    print("[0] Sair")
    return input("Escolha a figura: ").strip()


while True:
    op = menu()
    if op == "1":
        b = ler("Base: ")
        h = ler("Altura: ")
        print(f"Área do triângulo = {areatriang(b, h):.2f}")
    elif op == "2":
        r = ler("Raio: ")
        print(f"Área do círculo = {areacirc(r):.2f}")
    elif op == "3":
        D = ler("Diagonal maior: ")
        d = ler("Diagonal menor: ")
        print(f"Área do losango = {arealosango(D, d):.2f}")
    elif op == "4":
        b = ler("Base: ")
        h = ler("Altura: ")
        print(f"Área do retângulo = {arearet(b, h):.2f}")
    elif op == "5":
        B = ler("Base maior: ")
        b = ler("Base menor: ")
        h = ler("Altura: ")
        print(f"Área do trapézio = {areatrap(B, b, h):.2f}")
    elif op == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção Incorreta!")
