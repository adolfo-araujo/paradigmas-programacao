// Aula 08 - Exercício 02 - Projeto3 - Programa principal (Java)
import classe.Computador;

public class App {
    public static void main(String[] args) {
        // Duas instâncias da classe Computador com dados diferentes
        Computador pc1 = new Computador("Dell", 16, "NVIDIA GeForce RTX 4060");
        Computador pc2 = new Computador("Lenovo", 8, "Intel Iris Xe");

        System.out.println(pc1);
        System.out.println(pc2);
        System.out.println();

        pc1.processar("Renderização de vídeo");   // desligado: não processa
        pc1.ligar();
        pc1.processar("Renderização de vídeo");
        pc1.desligar();
        System.out.println();

        pc2.ligar();
        pc2.ligar();                               // já ligado
        pc2.processar("Planilha de notas");
        System.out.println(pc2);
        pc2.desligar();
    }
}
