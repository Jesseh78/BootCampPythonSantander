class Cachorro:
    def __init__(self, nome, raca, acordado=True):
        self.nome = nome
        self.raca = raca
        self.acordado = acordado

    def latir(self):
        print("AUAU")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

    def __del__(self):
        print(f"Removendo cachorro {self.nome}")

# Criação dos objetos fora da classe
c1 = Cachorro("Madona", "Collie")
c2 = Cachorro("Bob", "Buldog", False)

# Exibição
print(c1)
print(c2)
