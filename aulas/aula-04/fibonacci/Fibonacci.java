// Aula 04 - Exercício 2 - Série de Fibonacci com recursividade (Java)
import java.util.Scanner;

public class Fibonacci {

    // Retorna o k-ésimo termo da série (o 1º termo é 0 e o 2º é 1)
    static long fibonacci(int k) {
        if (k == 1) return 0;                          // caso base
        if (k == 2) return 1;                          // caso base
        return fibonacci(k - 1) + fibonacci(k - 2);    // chamada recursiva
    }

    static void exibirSerie(int n) {
        System.out.println("Os " + n + " primeiros termos da série de Fibonacci:");
        StringBuilder sb = new StringBuilder();
        for (int k = 1; k <= n; k++) {
            sb.append(fibonacci(k));
            if (k < n) sb.append(", ");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) {
        try (Scanner ent = new Scanner(System.in)) {
            int n = 0;
            while (n < 1) {
                System.out.print("Digite um número inteiro positivo (n): ");
                try {
                    n = Integer.parseInt(ent.nextLine().trim());
                } catch (NumberFormatException e) {
                    n = 0;
                }
                if (n < 1) System.out.println("Valor inválido! Digite um inteiro maior que zero.");
            }
            exibirSerie(n);
        }
    }
}
