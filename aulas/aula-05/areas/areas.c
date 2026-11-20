/* Aula 05 - Atividade Dirigida - Area de figuras geometricas (Linguagem C)
 * Uma funcao para cada figura, seguindo o modelo da funcao areaquad().
 */
#include <stdio.h>

#define PI 3.14   /* valor de Pi indicado no slide */

float areatriang(float base, float altura)    { return (base * altura) / 2; }         /* (b.h)/2   */
float areacirc(float raio)                    { return PI * raio * raio; }             /* Pi.r^2    */
float arealosango(float dmaior, float dmenor) { return (dmaior * dmenor) / 2; }        /* (D.d)/2   */
float arearet(float base, float altura)       { return base * altura; }                /* b.h       */
float areatrap(float bmaior, float bmenor, float altura)
{
    return ((bmaior + bmenor) * altura) / 2;                                           /* ((B+b).h)/2 */
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

/* Le um numero real positivo */
float ler(const char *msg)
{
    float valor;
    while (1) {
        printf("%s", msg);
        int r = ler_real(&valor);
        if (r == -1)
            return 0;
        if (r == 1 && valor > 0)
            return valor;
        printf("Valor invalido! Digite um numero maior que zero.\n");
    }
}

int main(void)
{
    int op = -1;
    float a, b, c;

    while (op != 0) {
        printf("\n===== AREA DE FIGURAS GEOMETRICAS =====\n");
        printf("[1] Triangulo\n[2] Circulo\n[3] Losango\n[4] Retangulo\n[5] Trapezio\n[0] Sair\n");
        printf("Escolha a figura: ");
        int lidos = scanf("%d", &op);
        if (lidos == EOF)
            op = 0;            /* fim da entrada: encerra */
        else if (lidos != 1)
            op = -1;
        limpar_buffer();

        switch (op) {
        case 1:
            a = ler("Base: ");
            b = ler("Altura: ");
            printf("Area do triangulo = %.2f\n", areatriang(a, b));
            break;
        case 2:
            a = ler("Raio: ");
            printf("Area do circulo = %.2f\n", areacirc(a));
            break;
        case 3:
            a = ler("Diagonal maior: ");
            b = ler("Diagonal menor: ");
            printf("Area do losango = %.2f\n", arealosango(a, b));
            break;
        case 4:
            a = ler("Base: ");
            b = ler("Altura: ");
            printf("Area do retangulo = %.2f\n", arearet(a, b));
            break;
        case 5:
            a = ler("Base maior: ");
            b = ler("Base menor: ");
            c = ler("Altura: ");
            printf("Area do trapezio = %.2f\n", areatrap(a, b, c));
            break;
        case 0:
            printf("Programa encerrado.\n");
            break;
        default:
            printf("Opcao Incorreta!\n");
        }
    }
    return 0;
}
