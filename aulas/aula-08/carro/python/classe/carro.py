# Aula 08 - Exercício 03 - Proj4 - Classe Carro (Python)


class Carro:
    VELOCIDADE_MAXIMA = 200   # km/h

    def __init__(self, marca, modelo, cor, ano, preco):
        # Atributos da classe
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.velocidade = 0   # estado interno do objeto (km/h)

    def acelerar(self, incremento=10):
        self.velocidade = min(self.VELOCIDADE_MAXIMA, self.velocidade + incremento)
        print(f"{self.modelo} acelerando... velocidade atual: {self.velocidade} km/h")

    def frear(self, decremento=10):
        if self.velocidade == 0:
            print(f"{self.modelo} já está parado.")
            return
        self.velocidade = max(0, self.velocidade - decremento)
        if self.velocidade == 0:
            print(f"{self.modelo} freou e parou.")
        else:
            print(f"{self.modelo} freando... velocidade atual: {self.velocidade} km/h")

    def __str__(self):
        preco = f"{self.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{self.marca} {self.modelo} | {self.cor} | {self.ano} | R$ {preco}"
