# Aula 07 - Proj2 - Classe Gato (Python, paradigma orientado a objetos)
#
# O gato funciona como uma MÁQUINA DE ESTADOS: ele está sempre em um estado
# (acordado, dormindo, brincando ou comendo) e cada método provoca uma transição.
# Os níveis de energia e fome decidem se a transição é permitida.


class Gato:
    ESTADOS = ("acordado", "dormindo", "brincando", "comendo")

    def __init__(self, nome, raca):
        # Atributos exigidos pela atividade
        self.nome = nome
        self.raca = raca
        # Atributos que controlam a máquina de estados
        self.estado = "acordado"
        self.energia = 100   # 0 a 100
        self.fome = 0        # 0 a 100

    def dormir(self):
        if self.estado == "dormindo":
            print(f"{self.nome} já está dormindo... zZz")
            return
        self.estado = "dormindo"
        self.energia = 100
        self.fome = min(100, self.fome + 10)
        print(f"{self.nome} se enrolou e dormiu. Energia recuperada: {self.energia}%")

    def brincar(self):
        if self.estado == "dormindo":
            print(f"{self.nome} está dormindo e acordou para brincar!")
        if self.energia < 30:
            print(f"{self.nome} está cansado demais para brincar (energia {self.energia}%). Precisa dormir.")
            return
        if self.fome > 70:
            print(f"{self.nome} está com muita fome (fome {self.fome}%). Precisa comer antes de brincar.")
            return
        self.estado = "brincando"
        self.energia -= 30
        self.fome = min(100, self.fome + 25)
        print(f"{self.nome} está brincando com o novelo! Energia: {self.energia}%  Fome: {self.fome}%")

    def comer(self):
        if self.fome == 0:
            print(f"{self.nome} cheirou a ração e foi embora: não está com fome.")
            return
        self.estado = "comendo"
        self.fome = max(0, self.fome - 50)
        self.energia = min(100, self.energia + 10)
        print(f"{self.nome} está comendo ração. Fome: {self.fome}%  Energia: {self.energia}%")

    def status(self):
        return (f"[{self.nome} | {self.raca}] estado: {self.estado}, "
                f"energia: {self.energia}%, fome: {self.fome}%")
