# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
# Crie um prgrama onde  João informe: cor, modelo, ano e valor da bicicleta vendida.
# Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("FON!!!")

    def parar(self):
        print("Skrrrrilll!")
        print("Bike travada")

    def correr(self):
        print("Vraaaul!")

    #def __str__(self):
    #    return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, preço = {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


#b1 = Bicicleta("Vermelha", "Caloi", 2010, 3000)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print("Especificações da bike: ", b1.cor, b1.modelo, b1.ano, b1.valor)
b2 = Bicicleta("Verde", "Monark", 2000, 1600)
print(b2)