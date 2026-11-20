// Aula 07 - Projeto2 - Classe Gato (Java, paradigma orientado a objetos)
//
// O gato funciona como uma MÁQUINA DE ESTADOS: ele está sempre em um estado
// (ACORDADO, DORMINDO, BRINCANDO ou COMENDO) e cada método provoca uma transição.
// Os níveis de energia e fome decidem se a transição é permitida.
package classe;

public class Gato {

    public enum Estado { ACORDADO, DORMINDO, BRINCANDO, COMENDO }

    // Atributos exigidos pela atividade (encapsulados)
    private String nome;
    private String raca;

    // Atributos que controlam a máquina de estados
    private Estado estado = Estado.ACORDADO;
    private int energia = 100;   // 0 a 100
    private int fome = 0;        // 0 a 100

    public Gato(String nome, String raca) {
        this.nome = nome;
        this.raca = raca;
    }

    public void dormir() {
        if (estado == Estado.DORMINDO) {
            System.out.println(nome + " já está dormindo... zZz");
            return;
        }
        estado = Estado.DORMINDO;
        energia = 100;
        fome = Math.min(100, fome + 10);
        System.out.println(nome + " se enrolou e dormiu. Energia recuperada: " + energia + "%");
    }

    public void brincar() {
        if (estado == Estado.DORMINDO) {
            System.out.println(nome + " está dormindo e acordou para brincar!");
        }
        if (energia < 30) {
            System.out.println(nome + " está cansado demais para brincar (energia " + energia + "%). Precisa dormir.");
            return;
        }
        if (fome > 70) {
            System.out.println(nome + " está com muita fome (fome " + fome + "%). Precisa comer antes de brincar.");
            return;
        }
        estado = Estado.BRINCANDO;
        energia -= 30;
        fome = Math.min(100, fome + 25);
        System.out.println(nome + " está brincando com o novelo! Energia: " + energia + "%  Fome: " + fome + "%");
    }

    public void comer() {
        if (fome == 0) {
            System.out.println(nome + " cheirou a ração e foi embora: não está com fome.");
            return;
        }
        estado = Estado.COMENDO;
        fome = Math.max(0, fome - 50);
        energia = Math.min(100, energia + 10);
        System.out.println(nome + " está comendo ração. Fome: " + fome + "%  Energia: " + energia + "%");
    }

    public String status() {
        return "[" + nome + " | " + raca + "] estado: " + estado.name().toLowerCase()
                + ", energia: " + energia + "%, fome: " + fome + "%";
    }

    // Getters
    public String getNome() { return nome; }
    public String getRaca() { return raca; }
    public Estado getEstado() { return estado; }
}
