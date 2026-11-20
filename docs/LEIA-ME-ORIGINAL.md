# PLP – Atividades das Aulas 02 a 08

Códigos das atividades práticas do final de cada aula. As respostas teóricas
(Aulas 01, 02 e 03) estão no documento "PLP – Respostas das Atividades Teóricas".

| Pasta | Atividade | Arquivos |
|---|---|---|
| Aula02_IMC | Cálculo do IMC em C, Python e Java (versões corrigidas do slide) | imc.c, imc.py, Imc.java |
| Aula04_Ex1_Disciplinas | Exercício 1: menu de disciplinas + relatório estatístico | disciplinas.c, disciplinas.py, Disciplinas.java |
| Aula04_Ex2_Fibonacci | Exercício 2: série de Fibonacci com recursividade | fibonacci.c, fibonacci.py, Fibonacci.java |
| Aula05_Areas | Função areaquad() e áreas de triângulo, círculo, losango, retângulo e trapézio | areaquad.c/.py, areas.c/.py |
| Aula06_Eleicao_e_Posto | Ex. 01 e 03: eleição (Python e C) · Ex. 02 e 04: posto RENALF (Python e C) | ex01_eleicao.py, ex02_posto.py, ex03_eleicao.c, ex04_posto.c |
| Aula07/Proj2 | Classe Gato em Python (máquina de estados) | classe/gato.py, app.py |
| Aula07/Projeto2 | Classe Gato em Java | src/classe/Gato.java, src/App.java |
| Aula08/Proj3 e Projeto3 | Classe Computador em Python e Java | classe/computador.py, src/classe/Computador.java |
| Aula08/Proj4 e Projeto4 | Classe Carro em Python e Java | classe/carro.py, src/classe/Carro.java |

## Como executar

**C** (na pasta do arquivo):
```
gcc disciplinas.c -o disciplinas
./disciplinas          (no Windows: disciplinas.exe)
```
Os textos dos programas em C estão sem acento para aparecerem certos no terminal do Windows.

**Python**:
```
python disciplinas.py
```
Nos projetos orientados a objetos, rode `python app.py` de dentro da pasta do projeto (Proj2, Proj3, Proj4).

**Java** – programas soltos (na pasta do arquivo):
```
javac -encoding UTF-8 Disciplinas.java
java Disciplinas
```
Projetos (Projeto2, Projeto3, Projeto4): abra a pasta no VS Code e clique em **Run** no `App.java`,
ou veja o README.md de cada projeto.

Os programas em Python e Java e os de C com menu aceitam vírgula ou ponto nos números reais (ex.: 9,5 ou 9.5). Em imc.c e areaquad.c, use ponto.
