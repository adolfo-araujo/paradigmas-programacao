# Aula 06 - Exercício 01 - Eleição da prefeitura do Rio de Janeiro (Python)
#   [1] Antonio  [2] José  [3] Maria  [4] BRANCO  [0] encerra a votação
#   Qualquer outro número é voto NULO.

candidatos = ["Antonio", "José", "Maria"]
votos = [0, 0, 0]
brancos = 0
nulos = 0
eleitores = 0

print("========= URNA ELETRÔNICA =========")
print("[1] Antonio\n[2] José\n[3] Maria\n[4] BRANCO\n[0] Encerrar votação")
print("(qualquer outro número = NULO)")

while True:
    try:
        voto = int(input("\nDigite seu voto: "))
    except ValueError:
        voto = -1          # entrada não numérica conta como NULO

    if voto == 0:          # encerra a votação
        break

    eleitores += 1
    if 1 <= voto <= 3:
        votos[voto - 1] += 1
    elif voto == 4:
        brancos += 1
    else:
        nulos += 1
    print("Voto registrado. FIM!")

# ---------- Relatório ----------
print("\n========= RELATÓRIO DA ELEIÇÃO =========")
for nome, qtd in zip(candidatos, votos):
    print(f"{nome:<8}: {qtd} voto(s)")
print(f"Brancos : {brancos}")
print(f"Nulos   : {nulos}")
print(f"\nTotal de eleitores que compareceram: {eleitores}")

maior = max(votos)
if maior == 0:
    print("Nenhum voto válido para candidatos.")
elif votos.count(maior) > 1:
    print("VOTAÇÃO EM SEGUNDO TURNO")
else:
    print(f"Candidato vitorioso: {candidatos[votos.index(maior)]}")
