# Projeto4 – Classe Carro (Java)

Aula 08 – Exercício 04.

A classe `Carro` (em `src/classe/Carro.java`) tem os atributos **marca**, **modelo**, **cor**, **ano** e **preco**
e os métodos **acelerar()** e **frear()**, que alteram a velocidade (0 a 200 km/h).
Os dois métodos têm sobrecarga: podem ser chamados com ou sem o valor da variação.

`src/App.java` cria duas instâncias com dados diferentes (Gol e Corolla).

> O slide cita os arquivos como `Carro.py` e `App.py`, mas como o projeto é em Java
> eles foram criados como `Carro.java` e `App.java`.

## Como executar
No VS Code: abra esta pasta e execute `src/App.java`.

Pelo terminal, dentro desta pasta (`java/`):
```
javac -encoding UTF-8 -d bin src/classe/Carro.java src/App.java
java -cp bin App
```
