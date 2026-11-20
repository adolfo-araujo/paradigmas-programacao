/* Aula 06 - Exercicio 04 - Posto de gasolina RENALF (Linguagem C) */
#include <stdio.h>

/* Le uma linha e converte para numero real, aceitando virgula ou ponto (ex.: 9,5 ou 9.5).
 * Retorna 1 se conseguiu ler um numero, 0 se a entrada for invalida e -1 no fim da entrada. */
int ler_real(float *valor)
{
    char linha[100];
    char *p;
    if (fgets(linha, sizeof linha, stdin) == NULL)
        return -1;
    for (p = linha; *p; p++)
        if (*p == ',')
            *p = '.';
    return sscanf(linha, "%f", valor) == 1;
}

int main(void)
{
    const char *combustiveis[4] = {"Alcool", "Diesel", "Gasolina", "GNV"};
    const float precos[4] = {5.69f, 2.96f, 6.07f, 4.15f};   /* preco por litro */
    float litros[4] = {0, 0, 0, 0};
    int clientes[4] = {0, 0, 0, 0};
    int op, lidos, c, i;
    float qtd, valor, total = 0;

    while (1) {
        printf("\n========= POSTO RENALF =========\n");
        for (i = 0; i < 4; i++)
            printf("[%d] %-9s R$ %.2f/litro\n", i + 1, combustiveis[i], precos[i]);
        printf("[0] Encerrar o dia\n");
        printf("Combustivel abastecido: ");

        lidos = scanf("%d", &op);
        if (lidos == EOF)
            break;
        while ((c = getchar()) != '\n' && c != EOF);
        if (lidos != 1)
            op = -1;

        if (op == 0)
            break;
        if (op < 1 || op > 4) {
            printf("Opcao invalida!\n");
            continue;
        }

        i = op - 1;
        printf("Litros de %s consumidos: ", combustiveis[i]);
        if (ler_real(&qtd) != 1)
            qtd = 0;
        if (qtd <= 0) {
            printf("Quantidade invalida! Abastecimento nao registrado.\n");
            continue;
        }

        litros[i] += qtd;
        clientes[i]++;
        printf("Valor a pagar: R$ %.2f\n", qtd * precos[i]);
    }

    /* ---------- Relatorio do dia ---------- */
    printf("\n================ RELATORIO DO DIA ================\n");
    printf("%-12s%12s%10s%16s\n", "Combustivel", "Litros", "Clientes", "Arrecadado");
    for (i = 0; i < 4; i++) {
        valor = litros[i] * precos[i];
        total += valor;
        printf("%-12s%12.2f%10d      R$ %7.2f\n", combustiveis[i], litros[i], clientes[i], valor);
    }
    printf("\nTotal arrecadado no dia: R$ %.2f\n", total);
    return 0;
}
