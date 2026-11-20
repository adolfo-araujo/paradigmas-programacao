# Aula 02 - Cálculo do IMC - Índice de Massa Corporal (Python)
# Versão corrigida do código do slide:
#  - faltava o prefixo f na f-string: print("Seu IMC é: {imc}") imprimia o texto "{imc}";
#  - aspas tipográficas trocadas por aspas retas;
#  - os.system("pause") removido (só funciona no Windows).

peso = float(input("Digite seu peso em Kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

# Vamos calcular o IMC
imc = peso / altura ** 2
print(f"Seu IMC é: {imc:.2f}")

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I (acentuada)")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
