# Aula 05 - Situação-problema: função areaquad() - área do quadrado (Python)

def areaquad(lado=0):
    """Recebe o lado do quadrado e retorna a área (A = L²)."""
    return lado ** 2


lado = float(input("Digite o valor do lado do quadrado: ").replace(",", "."))
print(f"A área do quadrado de lado {lado} é {areaquad(lado):.2f}")
