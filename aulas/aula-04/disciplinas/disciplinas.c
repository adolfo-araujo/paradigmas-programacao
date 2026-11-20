/* Aula 04 - Exercicio 1 - Relatorio estatistico das disciplinas (Linguagem C)
 * Obs.: os textos estao sem acento para aparecerem corretamente no terminal do Windows.
 */
#include <stdio.h>
#include <ctype.h>

const char *DISCIPLINAS[4] = {
    "Calculo de uma Variavel",
    "Bases de Programacao",
    "Modelagem de Novos Negocios",
    "Paradigmas de Linguagens de Programacao"
};

void mostrar_menu(void)
{
    int i;
    printf("+-----------------------------------------------+\n");
    printf("| Escolha sua Disciplina                        |\n");
    printf("|                                               |\n");
    for (i = 0; i < 4; i++)
        printf("| [%d] %-42s|\n", i + 1, DISCIPLINAS[i]);
    printf("+-----------------------------------------------+\n");
}

void limpar_buffer(void)
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

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

int ler_escolha(void)
{
    int op;
    while (1) {
        printf("\nQual a sua escolha? ");
        if (scanf("%d", &op) == 1 && op >= 1 && op <= 4) {
            limpar_buffer();
            return op;
        }
        limpar_buffer();
        printf("Opcao invalida! Digite um numero de 1 a 4.\n");
    }
}

float ler_media(const char *disciplina)
{
    float media;
    while (1) {
        printf("Sua media em %s: ", disciplina);
        int r = ler_real(&media);
        if (r == -1)
            return 0;
        if (r == 1 && media >= 0 && media <= 10)
            return media;
        printf("Media invalida! Digite um valor entre 0 e 10.\n");
    }
}

int main(void)
{
    int quantidade[4] = {0, 0, 0, 0};
    float soma_medias[4] = {0, 0, 0, 0};
    int total_alunos = 0;
    int op, i, maior, empates;
    char continuar = 'S';

    while (continuar == 'S') {
        mostrar_menu();
        op = ler_escolha();
        quantidade[op - 1]++;
        soma_medias[op - 1] += ler_media(DISCIPLINAS[op - 1]);
        total_alunos++;

        printf("\nRegistrar outro aluno? (S/N) ");
        if (scanf(" %c", &continuar) != 1)
            continuar = 'N';
        limpar_buffer();
        continuar = (char) toupper((unsigned char) continuar);
    }

    /* ---------- Relatorio ---------- */
    printf("\n========== RELATORIO ESTATISTICO ==========\n");
    for (i = 0; i < 4; i++) {
        float media_geral = quantidade[i] > 0 ? soma_medias[i] / quantidade[i] : 0;
        printf("%s\n   Alunos: %d   Media das medias: %.2f\n",
               DISCIPLINAS[i], quantidade[i], media_geral);
    }
    printf("\nTotal de alunos que participaram: %d\n", total_alunos);

    maior = quantidade[0];
    for (i = 1; i < 4; i++)
        if (quantidade[i] > maior)
            maior = quantidade[i];

    empates = 0;
    for (i = 0; i < 4; i++)
        if (quantidade[i] == maior)
            empates++;

    if (empates == 1) {
        for (i = 0; i < 4; i++)
            if (quantidade[i] == maior)
                printf("Disciplina com MAIOR adesao: %s (%d alunos)\n", DISCIPLINAS[i], maior);
    } else {
        printf("Empate na MAIOR adesao (%d alunos):\n", maior);
        for (i = 0; i < 4; i++)
            if (quantidade[i] == maior)
                printf("   - %s\n", DISCIPLINAS[i]);
    }
    return 0;
}
