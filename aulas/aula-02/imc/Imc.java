// Aula 02 - Cálculo do IMC - Índice de Massa Corporal (Java)
import java.util.Scanner;

public class Imc {
    public static void main(String[] args) {
        try (Scanner ent = new Scanner(System.in)) {
            System.out.print("Digite seu peso em Kg: ");
            double peso = Double.parseDouble(ent.nextLine().replace(',', '.'));
            System.out.print("Digite sua altura em metros: ");
            double altura = Double.parseDouble(ent.nextLine().replace(',', '.'));

            // Vamos calcular o IMC
            double imc = peso / (altura * altura);
            System.out.printf("Seu IMC é: %.2f%n", imc);

            if (imc < 16) {
                System.out.println("Magreza grave");
            } else if (imc < 17) {
                System.out.println("Magreza moderada");
            } else if (imc < 18.5) {
                System.out.println("Magreza leve");
            } else if (imc < 25) {
                System.out.println("Saudável");
            } else if (imc < 30) {
                System.out.println("Sobrepeso");
            } else if (imc < 35) {
                System.out.println("Obesidade Grau I (acentuada)");
            } else if (imc < 40) {
                System.out.println("Obesidade Grau II (severa)");
            } else {
                System.out.println("Obesidade Grau III (mórbida)");
            }
        }
    }
}
