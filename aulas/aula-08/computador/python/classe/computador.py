# Aula 08 - Exercício 01 - Proj3 - Classe Computador (Python)


class Computador:
    def __init__(self, marca, ram, placa):
        # Atributos da classe
        self.marca = marca
        self.ram = ram          # memória RAM em GB
        self.placa = placa      # placa de vídeo
        self.ligado = False     # estado interno do objeto

    def ligar(self):
        if self.ligado:
            print(f"O computador {self.marca} já está ligado.")
        else:
            self.ligado = True
            print(f"Ligando o computador {self.marca}... Sistema iniciado com {self.ram} GB de RAM.")

    def desligar(self):
        if not self.ligado:
            print(f"O computador {self.marca} já está desligado.")
        else:
            self.ligado = False
            print(f"Desligando o computador {self.marca}... Até logo!")

    def processar(self, tarefa):
        if not self.ligado:
            print(f"Não é possível processar '{tarefa}': o computador {self.marca} está desligado.")
            return
        print(f"{self.marca} processando '{tarefa}' com {self.ram} GB de RAM e placa {self.placa}.")

    def __str__(self):
        situacao = "ligado" if self.ligado else "desligado"
        return f"Computador {self.marca} | RAM: {self.ram} GB | Placa: {self.placa} | {situacao}"
