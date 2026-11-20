// Aula 08 - Exercício 04 - Projeto4 - Classe Carro (Java)
// Obs.: o slide cita "Carro.py" e "App.py", mas como o projeto é em Java
// os arquivos foram criados como Carro.java e App.java.
package classe;

public class Carro {

    public static final int VELOCIDADE_MAXIMA = 200;   // km/h

    // Atributos da classe
    private String marca;
    private String modelo;
    private String cor;
    private int ano;
    private double preco;
    private int velocidade;   // estado interno do objeto (km/h)

    public Carro(String marca, String modelo, String cor, int ano, double preco) {
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.preco = preco;
        this.velocidade = 0;
    }

    public void acelerar(int incremento) {
        velocidade = Math.min(VELOCIDADE_MAXIMA, velocidade + incremento);
        System.out.println(modelo + " acelerando... velocidade atual: " + velocidade + " km/h");
    }

    public void acelerar() { acelerar(10); }   // sobrecarga: incremento padrão

    public void frear(int decremento) {
        if (velocidade == 0) {
            System.out.println(modelo + " já está parado.");
            return;
        }
        velocidade = Math.max(0, velocidade - decremento);
        if (velocidade == 0) {
            System.out.println(modelo + " freou e parou.");
        } else {
            System.out.println(modelo + " freando... velocidade atual: " + velocidade + " km/h");
        }
    }

    public void frear() { frear(10); }         // sobrecarga: decremento padrão

    @Override
    public String toString() {
        String valor = String.format(java.util.Locale.forLanguageTag("pt-BR"), "%,.2f", preco);
        return marca + " " + modelo + " | " + cor + " | " + ano + " | R$ " + valor;
    }

    public String getMarca() { return marca; }
    public String getModelo() { return modelo; }
    public String getCor() { return cor; }
    public int getAno() { return ano; }
    public double getPreco() { return preco; }
    public int getVelocidade() { return velocidade; }
}
