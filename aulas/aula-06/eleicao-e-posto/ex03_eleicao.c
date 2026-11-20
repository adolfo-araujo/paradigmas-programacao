/* Aula 06 - Exercicio 03 - Eleicao da prefeitura do Rio de Janeiro (Linguagem C)
 *   [1] Antonio  [2] Jose  [3] Maria  [4] BRANCO  [0] encerra a votacao
 *   Qualquer outro numero e voto NULO.
 */
#include <stdio.h>

int main(void)
{
    const char *candidatos[3] = {"Antonio", "Jose", "Maria"};
    int votos[3] = {0, 0, 0};
    int brancos = 0, nulos = 0, eleitores = 0;
    int voto, lidos, c, i, maior, empates, vencedor = 0;

    printf("========= URNA ELETRONICA =========\n");
    printf("[1] Antonio\n[2] Jose\n[3] Maria\n[4] BRANCO\n[0] Encerrar votacao\n");
    printf("(qualquer outro numero = NULO)\n");

    while (1) {
        printf("\nDigite seu voto: ");
        lidos = scanf("%d", &voto);
        if (lidos == EOF)
            break;                       /* fim da entrada */
        while ((c = getchar()) != '\n' && c != EOF);
        if (lidos != 1)
            voto = -1;                   /* entrada nao numerica conta como NULO */

        if (voto == 0)                   /* encerra a votacao */
            break;

        eleitores++;
        if (voto >= 1 && voto <= 3)
            votos[voto - 1]++;
        else if (voto == 4)
            brancos++;
        else
            nulos++;
        printf("Voto registrado. FIM!\n");
    }

    /* ---------- Relatorio ---------- */
    printf("\n========= RELATORIO DA ELEICAO =========\n");
    for (i = 0; i < 3; i++)
        printf("%-8s: %d voto(s)\n", candidatos[i], votos[i]);
    printf("Brancos : %d\n", brancos);
    printf("Nulos   : %d\n", nulos);
    printf("\nTotal de eleitores que compareceram: %d\n", eleitores);

    maior = votos[0];
    for (i = 1; i < 3; i++)
        if (votos[i] > maior)
            maior = votos[i];

    empates = 0;
    for (i = 0; i < 3; i++)
        if (votos[i] == maior) {
            empates++;
            vencedor = i;
        }

    if (maior == 0)
        printf("Nenhum voto valido para candidatos.\n");
    else if (empates > 1)
        printf("VOTACAO EM SEGUNDO TURNO\n");
    else
        printf("Candidato vitorioso: %s\n", candidatos[vencedor]);

    return 0;
}
