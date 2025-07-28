# Quando uma classe "filha" herda apenas uma classe "pai".

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")

#m1 = Motocicleta("azul", "Abc-1234", 2)
#m1.ligar_motor

#c1 = Carro("preto", "Adb-4321", 4)
#c1.ligar_motor

ca1 = Caminhao("Verde", "cba-1234", 8, True)
print(ca1)
ca1.ligar_motor()
ca1.esta_carregado()
