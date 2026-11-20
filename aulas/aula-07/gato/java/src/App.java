// Aula 07 - Projeto2 - Programa principal (Java)
// Cria duas instâncias da classe Gato e percorre a máquina de estados.
import classe.Gato;

public class App {
    public static void main(String[] args) {
        // Duas instâncias (objetos) da mesma classe, com dados diferentes
        Gato gato1 = new Gato("Mingau", "Persa");
        Gato gato2 = new Gato("Frajola", "Siamês");

        System.out.println("=== Estado inicial ===");
        System.out.println(gato1.status());
        System.out.println(gato2.status());

        System.out.println("\n=== Rotina do Mingau ===");
        gato1.brincar();
        gato1.brincar();
        gato1.brincar();
        gato1.brincar();      // energia baixa: transição negada
        gato1.comer();
        gato1.dormir();
        gato1.dormir();       // já está dormindo
        System.out.println(gato1.status());

        System.out.println("\n=== Rotina do Frajola ===");
        gato2.comer();        // sem fome: transição negada
        gato2.brincar();
        gato2.comer();
        gato2.dormir();
        gato2.brincar();      // acorda para brincar
        System.out.println(gato2.status());
    }
}
