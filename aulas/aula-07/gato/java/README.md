# Projeto2 – Classe Gato (Java)

Aula 07 – Paradigma Orientado a Objetos.

A classe `Gato` (em `src/classe/Gato.java`) tem os atributos **nome** e **raça** e os métodos
**dormir()**, **brincar()** e **comer()**. Ela funciona como uma máquina de estados:
o gato está sempre em um estado (`ACORDADO`, `DORMINDO`, `BRINCANDO` ou `COMENDO`),
e os níveis de energia e fome decidem se cada transição é permitida
(ex.: com energia abaixo de 30% ele não brinca, precisa dormir).

`src/App.java` cria duas instâncias (Mingau e Frajola) e executa uma rotina com cada uma.

## Estrutura
- `src`: código-fonte
- `bin`: arquivos compilados (criados pelo comando; ignorados pelo Git)

## Como executar
No VS Code (Extension Pack for Java): abra esta pasta e execute `src/App.java`.

Pelo terminal, dentro desta pasta (`java/`):
```
javac -encoding UTF-8 -d bin src/classe/Gato.java src/App.java
java -cp bin App
```
