# Aula 04 - Exercício 2 - Série de Fibonacci com recursividade (Python)

def fibonacci(k):
    """Retorna o k-ésimo termo da série (o 1º termo é 0 e o 2º é 1)."""
    if k == 1:
        return 0          # caso base
    if k == 2:
        return 1          # caso base
    return fibonacci(k - 1) + fibonacci(k - 2)   # chamada recursiva


def exibir_serie(n):
    termos = [fibonacci(k) for k in range(1, n + 1)]
    print(f"Os {n} primeiros termos da série de Fibonacci:")
    print(", ".join(str(t) for t in termos))


n = 0
while n < 1:
    try:
        n = int(input("Digite um número inteiro positivo (n): "))
    except ValueError:
        n = 0
    if n < 1:
        print("Valor inválido! Digite um inteiro maior que zero.")

exibir_serie(n)
