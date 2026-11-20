/* Aula 04 - Exercicio 2 - Serie de Fibonacci com recursividade (Linguagem C) */
#include <stdio.h>

/* Retorna o k-esimo termo da serie (o 1o termo e 0 e o 2o e 1) */
long long fibonacci(int k)
{
    if (k == 1)
        return 0;                               /* caso base */
    if (k == 2)
        return 1;                               /* caso base */
    return fibonacci(k - 1) + fibonacci(k - 2); /* chamada recursiva */
}

void exibir_serie(int n)
{
    int k;
    printf("Os %d primeiros termos da serie de Fibonacci:\n", n);
    for (k = 1; k <= n; k++)
        printf("%lld%s", fibonacci(k), k < n ? ", " : "\n");
}

int main(void)
{
    int n = 0;
    int c;
    while (n < 1) {
        printf("Digite um numero inteiro positivo (n): ");
        if (scanf("%d", &n) != 1)
            n = 0;
        while ((c = getchar()) != '\n' && c != EOF);
        if (n < 1)
            printf("Valor invalido! Digite um inteiro maior que zero.\n");
    }
    exibir_serie(n);
    return 0;
}
