# Aula 06 - Exercício 02 - Posto de gasolina RENALF (Python)

COMBUSTIVEIS = ["Álcool", "Diesel", "Gasolina", "GNV"]
PRECOS = [5.69, 2.96, 6.07, 4.15]      # preço por litro (tabela do posto)

litros = [0.0, 0.0, 0.0, 0.0]
clientes = [0, 0, 0, 0]


def moeda(valor):
    """Formata no padrão brasileiro: R$ 1.234,56"""
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


while True:
    print("\n========= POSTO RENALF =========")
    for i, nome in enumerate(COMBUSTIVEIS, start=1):
        print(f"[{i}] {nome:<9} {moeda(PRECOS[i - 1])}/litro")
    print("[0] Encerrar o dia")
    op = input("Combustível abastecido: ").strip()

    if op == "0":
        break
    if op not in ("1", "2", "3", "4"):
        print("Opção inválida!")
        continue

    i = int(op) - 1
    try:
        qtd = float(input(f"Litros de {COMBUSTIVEIS[i]} consumidos: ").replace(",", "."))
    except ValueError:
        qtd = 0
    if qtd <= 0:
        print("Quantidade inválida! Abastecimento não registrado.")
        continue

    litros[i] += qtd
    clientes[i] += 1
    print(f"Valor a pagar: {moeda(qtd * PRECOS[i])}")

# ---------- Relatório do dia ----------
print("\n================ RELATÓRIO DO DIA ================")
print(f"{'Combustível':<12}{'Litros':>12}{'Clientes':>10}{'Arrecadado':>16}")
total = 0
for i, nome in enumerate(COMBUSTIVEIS):
    valor = litros[i] * PRECOS[i]
    total += valor
    print(f"{nome:<12}{litros[i]:>12.2f}{clientes[i]:>10}{moeda(valor):>16}")
print(f"\nTotal arrecadado no dia: {moeda(total)}")
