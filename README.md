# Paradigmas de Linguagens de Programação | Atividades Práticas

<p align="center">
  <img alt="Linguagens de programação" src="https://img.shields.io/badge/Linguagens-C%20%7C%20Python%20%7C%20Java-2563eb" />
  <img alt="Disciplina" src="https://img.shields.io/badge/Disciplina-Paradigmas%20de%20Programa%C3%A7%C3%A3o-475569" />
  <img alt="Tipo de projeto" src="https://img.shields.io/badge/Tipo-Exerc%C3%ADcios%20Acad%C3%AAmicos-059669" />
</p>

Repositório de **exercícios práticos em C, Python e Java** desenvolvidos na disciplina de **Paradigmas de Linguagens de Programação**, do curso de Engenharia de Software da Universidade Veiga de Almeida (UVA).

O objetivo é praticar e comparar a implementação de problemas em diferentes linguagens, passando por **variáveis e tipos, estruturas de decisão e repetição, funções, recursividade e programação orientada a objetos**.

> **Escopo:** este repositório contém os códigos das atividades práticas do ZIP original, reorganizados por aula e assunto. Os PDFs de aula do professor não estão incluídos. As atividades teóricas das aulas iniciais não constavam do ZIP.

## Tecnologias

- **C** — funções, seleção, repetição e programação estruturada.
- **Python 3** — programação estruturada e orientação a objetos.
- **Java** — programas com `main`, classes, objetos e métodos.
- **Ferramentas para executar** — GCC (C), Python 3 e JDK (`javac`/`java`). Não há dependências externas nos exercícios apresentados.

## Atividades disponíveis

| Aula | Conteúdo | Linguagens | Código |
|:---:|---|---|---|
| 02 | Cálculo de IMC | C, Python, Java | [`imc/`](aulas/aula-02/imc/) |
| 04 | Seleção de disciplinas e relatório estatístico | C, Python, Java | [`disciplinas/`](aulas/aula-04/disciplinas/) |
| 04 | Sequência de Fibonacci com recursividade | C, Python, Java | [`fibonacci/`](aulas/aula-04/fibonacci/) |
| 05 | Área do quadrado e de outras figuras | C, Python | [`areas/`](aulas/aula-05/areas/) |
| 06 | Simulador de votação e atendimento de posto | C, Python | [`eleicao-e-posto/`](aulas/aula-06/eleicao-e-posto/) |
| 07 | Classe Gato com estado, energia e fome | Python, Java | [`gato/`](aulas/aula-07/gato/) |
| 08 | Classe Computador: ligar, desligar e processar | Python, Java | [`computador/`](aulas/aula-08/computador/) |
| 08 | Classe Carro: acelerar e frear | Python, Java | [`carro/`](aulas/aula-08/carro/) |

## Como executar

**Pré-requisitos:** Python 3, compilador GCC e/ou JDK, conforme o exercício escolhido.

### Exemplo em Python

A partir da raiz do repositório:

```bash
python aulas/aula-04/fibonacci/fibonacci.py
```

### Exemplo em C

Entre na pasta do exercício e compile:

```bash
cd aulas/aula-04/fibonacci
gcc -std=c11 -Wall -Wextra fibonacci.c -o fibonacci
./fibonacci
```

No Windows, execute `fibonacci.exe` em vez de `./fibonacci`, quando aplicável.

### Exemplo em Java

```bash
cd aulas/aula-04/fibonacci
javac -encoding UTF-8 Fibonacci.java
java Fibonacci
```

Os exemplos orientados a objetos possuem `app.py` ou `src/App.java`, com duas instâncias dos objetos. Para executar Java orientado a objetos, entre na pasta `java/` correspondente:

```bash
javac -encoding UTF-8 -d bin src/classe/Computador.java src/App.java
java -cp bin App
```

Veja [o guia completo de execução](docs/GUIA-DE-EXECUCAO.md) para os demais programas, incluindo os exercícios que solicitam entradas pelo teclado.

## Organização do repositório

```text
.
├── aulas/
│   ├── aula-02/imc/
│   ├── aula-04/{disciplinas,fibonacci}/
│   ├── aula-05/areas/
│   ├── aula-06/eleicao-e-posto/
│   ├── aula-07/gato/{python,java}/
│   └── aula-08/
│       ├── computador/{python,java}/
│       └── carro/{python,java}/
├── docs/
│   ├── GUIA-DE-EXECUCAO.md
│   ├── ORGANIZACAO.md
│   └── LEIA-ME-ORIGINAL.md
├── scripts/
│   └── validar.py
├── .github/workflows/validacao.yml
├── .gitignore
└── README.md
```

A organização preserva o conteúdo dos códigos originais. Os diretórios de projetos foram padronizados, sem alterar a lógica dos exercícios; arquivos temporários de IDE e compilação foram retirados do pacote.

## Verificação dos códigos

Foi incluído um script que confere a sintaxe dos programas Python e compila os exemplos C e Java em diretórios temporários. Se possuir as três ferramentas, execute:

```bash
python scripts/validar.py
```

Há também uma automação de validação em `.github/workflows/validacao.yml` para executar esses checks após o push. **Compilar não equivale a validar todos os cenários de entrada nem a comprovar cobertura de testes.**

## Aprendizados

- Compreender diferenças de sintaxe e organização entre C, Python e Java.
- Aplicar condicionais, laços, funções e recursividade.
- Modelar entidades com classes, atributos, métodos e instâncias.
- Praticar decomposição de problemas e organização de código-fonte.

## Autoria e contexto

Atividades acadêmicas organizadas para portfólio por **João Adolfo Martins Araújo**, estudante de Engenharia de Software na **Universidade Veiga de Almeida (UVA)**.

Os códigos são exemplos educacionais; não representam aplicações de produção. Materiais didáticos do professor não foram redistribuídos neste repositório.
