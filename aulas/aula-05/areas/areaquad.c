/* Aula 05 - Situacao-problema: funcao areaquad() - area do quadrado (Linguagem C) */
#include <stdio.h>

/* Recebe o lado do quadrado e retorna a area (A = L^2) */
float areaquad(float lado)
{
    return lado * lado;
}

int main(void)
{
    float lado;
    printf("Digite o valor do lado do quadrado: ");
    scanf("%f", &lado);
    printf("A area do quadrado de lado %.2f e %.2f\n", lado, areaquad(lado));
    return 0;
}
