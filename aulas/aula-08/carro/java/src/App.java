// Aula 08 - Exercício 04 - Projeto4 - Programa principal (Java)
import classe.Carro;

public class App {
    public static void main(String[] args) {
        // Duas instâncias da classe Carro com dados diferentes
        Carro carro1 = new Carro("Volkswagen", "Gol", "Prata", 2022, 72990.00);
        Carro carro2 = new Carro("Toyota", "Corolla", "Preto", 2024, 159990.00);

        System.out.println(carro1);
        System.out.println(carro2);
        System.out.println();

        carro1.acelerar(40);
        carro1.acelerar(20);
        carro1.frear(30);
        carro1.frear(30);
        carro1.frear();        // já parado
        System.out.println();

        carro2.acelerar(80);
        carro2.acelerar(150);  // limitado à velocidade máxima
        carro2.frear(50);
    }
}
