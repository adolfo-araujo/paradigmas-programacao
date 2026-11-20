# Projeto3 – Classe Computador (Java)

Aula 08 – Exercício 02.

A classe `Computador` (em `src/classe/Computador.java`) tem os atributos **marca**, **ram** e **placa**
e os métodos **ligar()**, **desligar()** e **processar()**. O computador só processa uma tarefa se estiver ligado.

`src/App.java` cria duas instâncias com dados diferentes (Dell e Lenovo).

## Como executar
No VS Code: abra esta pasta e execute `src/App.java`.

Pelo terminal, dentro desta pasta (`java/`):
```
javac -encoding UTF-8 -d bin src/classe/Computador.java src/App.java
java -cp bin App
```
