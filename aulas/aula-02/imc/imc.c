/* Aula 02 - Calculo do IMC - Indice de Massa Corporal (Linguagem C)
 * Versao corrigida do codigo do slide:
 *  - main() passa a ser "int main(void)" e retorna 0;
 *  - aspas tipograficas (" ") trocadas por aspas retas;
 *  - getch() (conio.h, so existe no Windows) removido;
 *  - "\n" adicionado nas mensagens que nao quebravam linha.
 */
#include <stdio.h>

int main(void)
{
    float peso = 0;
    float altura = 0;
    float imc = 0;

    printf("Digite seu peso em Kg: ");
    scanf("%f", &peso);
    printf("Digite sua altura em metros: ");
    scanf("%f", &altura);

    /* Vamos calcular o IMC */
    imc = peso / (altura * altura);
    printf("Seu IMC e: %.2f\n", imc);

    if (imc < 16)
        printf("Magreza grave\n");
    else if (imc < 17)
        printf("Magreza moderada\n");
    else if (imc < 18.5)
        printf("Magreza leve\n");
    else if (imc < 25)
        printf("Saudavel\n");
    else if (imc < 30)
        printf("Sobrepeso\n");
    else if (imc < 35)
        printf("Obesidade Grau I (acentuada)\n");
    else if (imc < 40)
        printf("Obesidade Grau II (severa)\n");
    else
        printf("Obesidade Grau III (morbida)\n");

    return 0;
}
