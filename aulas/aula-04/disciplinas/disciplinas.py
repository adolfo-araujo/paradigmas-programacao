# Aula 04 - Exercício 1 - Relatório estatístico das disciplinas (Python)

DISCIPLINAS = [
    "Cálculo de uma Variável",
    "Bases de Programação",
    "Modelagem de Novos Negócios",
    "Paradigmas de Linguagens de Programação",
]


def mostrar_menu():
    print("+-----------------------------------------------+")
    print("| Escolha sua Disciplina                        |")
    print("|                                               |")
    for i, nome in enumerate(DISCIPLINAS, start=1):
        print(f"| [{i}] {nome:<42}|")
    print("+-----------------------------------------------+")


def ler_escolha():
    while True:
        try:
            op = int(input("\nQual a sua escolha? "))
            if 1 <= op <= 4:
                return op
        except ValueError:
            pass
        print("Opção inválida! Digite um número de 1 a 4.")


def ler_media(disciplina):
    while True:
        try:
            media = float(input(f"Sua média em {disciplina}: ").replace(",", "."))
            if 0 <= media <= 10:
                return media
        except ValueError:
            pass
        print("Média inválida! Digite um valor entre 0 e 10.")


def main():
    quantidade = [0, 0, 0, 0]   # alunos por disciplina
    soma_medias = [0.0, 0.0, 0.0, 0.0]
    total_alunos = 0

    continuar = "S"
    while continuar == "S":
        mostrar_menu()
        op = ler_escolha()
        media = ler_media(DISCIPLINAS[op - 1])

        quantidade[op - 1] += 1
        soma_medias[op - 1] += media
        total_alunos += 1

        continuar = input("\nRegistrar outro aluno? (S/N) ").strip().upper()[:1]

    # ---------- Relatório ----------
    print("\n========== RELATÓRIO ESTATÍSTICO ==========")
    for i, nome in enumerate(DISCIPLINAS):
        media_geral = soma_medias[i] / quantidade[i] if quantidade[i] > 0 else 0
        print(f"{nome}")
        print(f"   Alunos: {quantidade[i]}   Média das médias: {media_geral:.2f}")

    print(f"\nTotal de alunos que participaram: {total_alunos}")

    maior = max(quantidade)
    vencedoras = [DISCIPLINAS[i] for i in range(4) if quantidade[i] == maior]
    if len(vencedoras) == 1:
        print(f"Disciplina com MAIOR adesão: {vencedoras[0]} ({maior} alunos)")
    else:
        print(f"Empate na MAIOR adesão ({maior} alunos): {', '.join(vencedoras)}")


main()
