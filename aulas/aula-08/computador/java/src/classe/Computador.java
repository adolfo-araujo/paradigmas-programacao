// Aula 08 - Exercício 02 - Projeto3 - Classe Computador (Java)
package classe;

public class Computador {

    // Atributos da classe
    private String marca;
    private int ram;          // memória RAM em GB
    private String placa;     // placa de vídeo
    private boolean ligado;   // estado interno do objeto

    public Computador(String marca, int ram, String placa) {
        this.marca = marca;
        this.ram = ram;
        this.placa = placa;
        this.ligado = false;
    }

    public void ligar() {
        if (ligado) {
            System.out.println("O computador " + marca + " já está ligado.");
        } else {
            ligado = true;
            System.out.println("Ligando o computador " + marca + "... Sistema iniciado com " + ram + " GB de RAM.");
        }
    }

    public void desligar() {
        if (!ligado) {
            System.out.println("O computador " + marca + " já está desligado.");
        } else {
            ligado = false;
            System.out.println("Desligando o computador " + marca + "... Até logo!");
        }
    }

    public void processar(String tarefa) {
        if (!ligado) {
            System.out.println("Não é possível processar '" + tarefa + "': o computador " + marca + " está desligado.");
            return;
        }
        System.out.println(marca + " processando '" + tarefa + "' com " + ram + " GB de RAM e placa " + placa + ".");
    }

    @Override
    public String toString() {
        return "Computador " + marca + " | RAM: " + ram + " GB | Placa: " + placa + " | "
                + (ligado ? "ligado" : "desligado");
    }

    public String getMarca() { return marca; }
    public int getRam() { return ram; }
    public String getPlaca() { return placa; }
    public boolean isLigado() { return ligado; }
}
