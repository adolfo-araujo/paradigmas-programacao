# Guia de execução dos exercícios

Execute os comandos a partir da **raiz do repositório**, salvo indicação de `cd`. É necessário ter pelo menos a linguagem correspondente instalada. Para Java, recomenda-se JDK; para C, GCC; para Python, Python 3.

## Exercícios em Python

```bash
python aulas/aula-02/imc/imc.py
python aulas/aula-04/disciplinas/disciplinas.py
python aulas/aula-04/fibonacci/fibonacci.py
python aulas/aula-05/areas/areaquad.py
python aulas/aula-05/areas/areas.py
python aulas/aula-06/eleicao-e-posto/ex01_eleicao.py
python aulas/aula-06/eleicao-e-posto/ex02_posto.py
```

Os programas de POO têm importação da pasta local `classe` e devem ser executados dentro do diretório do exercício:

```bash
cd aulas/aula-07/gato/python
python app.py
```

Repita o padrão em `aulas/aula-08/computador/python` e `aulas/aula-08/carro/python`.

## Exercícios em C

Entre na pasta e compile o arquivo escolhido. Exemplo:

```bash
cd aulas/aula-02/imc
gcc -std=c11 -Wall -Wextra imc.c -o imc
./imc
```

Outros arquivos C:

- `aulas/aula-04/disciplinas/disciplinas.c`
- `aulas/aula-04/fibonacci/fibonacci.c`
- `aulas/aula-05/areas/areaquad.c` e `areas.c`
- `aulas/aula-06/eleicao-e-posto/ex03_eleicao.c` e `ex04_posto.c`

Use os mesmos comandos trocando o nome do arquivo. No Windows (PowerShell), execute `./imc.exe` (ou `.\imc.exe`).

## Exercícios em Java

Exemplo com uma classe principal única:

```bash
cd aulas/aula-02/imc
javac -encoding UTF-8 Imc.java
java Imc
```

Também há `Disciplinas.java` e `Fibonacci.java` nas pastas da Aula 04.

Para cada projeto Java de POO (Gato, Computador, Carro):

```bash
cd aulas/aula-08/computador/java
javac -encoding UTF-8 -d bin src/classe/Computador.java src/App.java
java -cp bin App
```

Substitua `Computador.java` por `Gato.java` na pasta `aulas/aula-07/gato/java`, ou por `Carro.java` na pasta `aulas/aula-08/carro/java`.

## Validação automatizada

Na raiz do repositório, rode:

```bash
python scripts/validar.py
```

O verificador compila os exercícios C e Java e checa a sintaxe Python sem gerar artefatos dentro do repositório. A validação completa requer GCC e JDK disponíveis no PATH.
