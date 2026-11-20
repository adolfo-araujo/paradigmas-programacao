// Aula 04 - Exercício 1 - Relatório estatístico das disciplinas (Java)
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Disciplinas {

    static final String[] DISCIPLINAS = {
        "Cálculo de uma Variável",
        "Bases de Programação",
        "Modelagem de Novos Negócios",
        "Paradigmas de Linguagens de Programação"
    };

    static final Scanner ent = new Scanner(System.in);

    static void mostrarMenu() {
        System.out.println("+-----------------------------------------------+");
        System.out.println("| Escolha sua Disciplina                        |");
        System.out.println("|                                               |");
        for (int i = 0; i < DISCIPLINAS.length; i++) {
            System.out.printf("| [%d] %-42s|%n", i + 1, DISCIPLINAS[i]);
        }
        System.out.println("+-----------------------------------------------+");
    }

    static int lerEscolha() {
        while (true) {
            System.out.print("\nQual a sua escolha? ");
            try {
                int op = Integer.parseInt(ent.nextLine().trim());
                if (op >= 1 && op <= 4) return op;
            } catch (NumberFormatException e) { /* entrada inválida */ }
            System.out.println("Opção inválida! Digite um número de 1 a 4.");
        }
    }

    static double lerMedia(String disciplina) {
        while (true) {
            System.out.print("Sua média em " + disciplina + ": ");
            try {
                double media = Double.parseDouble(ent.nextLine().trim().replace(',', '.'));
                if (media >= 0 && media <= 10) return media;
            } catch (NumberFormatException e) { /* entrada inválida */ }
            System.out.println("Média inválida! Digite um valor entre 0 e 10.");
        }
    }

    public static void main(String[] args) {
        int[] quantidade = new int[4];
        double[] somaMedias = new double[4];
        int totalAlunos = 0;

        String continuar = "S";
        while (continuar.equals("S")) {
            mostrarMenu();
            int op = lerEscolha();
            double media = lerMedia(DISCIPLINAS[op - 1]);

            quantidade[op - 1]++;
            somaMedias[op - 1] += media;
            totalAlunos++;

            System.out.print("\nRegistrar outro aluno? (S/N) ");
            String resp = ent.hasNextLine() ? ent.nextLine().trim().toUpperCase() : "N";
            continuar = resp.isEmpty() ? "N" : resp.substring(0, 1);
        }

        // ---------- Relatório ----------
        System.out.println("\n========== RELATÓRIO ESTATÍSTICO ==========");
        for (int i = 0; i < 4; i++) {
            double mediaGeral = quantidade[i] > 0 ? somaMedias[i] / quantidade[i] : 0;
            System.out.println(DISCIPLINAS[i]);
            System.out.printf("   Alunos: %d   Média das médias: %.2f%n", quantidade[i], mediaGeral);
        }
        System.out.println("\nTotal de alunos que participaram: " + totalAlunos);

        int maior = 0;
        for (int q : quantidade) maior = Math.max(maior, q);
        List<String> vencedoras = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            if (quantidade[i] == maior) vencedoras.add(DISCIPLINAS[i]);
        }
        if (vencedoras.size() == 1) {
            System.out.printf("Disciplina com MAIOR adesão: %s (%d alunos)%n", vencedoras.get(0), maior);
        } else {
            System.out.printf("Empate na MAIOR adesão (%d alunos): %s%n", maior, String.join(", ", vencedoras));
        }
    }
}
