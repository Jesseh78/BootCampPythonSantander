# Quando a classe "filha" herda de várias classes "pai".
class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamiferio(Animal):
    def __init__(self, cor, **kw):
        self.cor = cor
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamiferio):
    pass

class Gato(Mamiferio):
    pass

class Leao(Mamiferio):
    pass

class Ornitorrinco(Mamiferio, Ave):
    pass


gato = Gato(n_patas = 4, cor = "Laranja")
print(gato)

perry = Ornitorrinco(n_patas = 2, cor = "Verde", cor_bico = "Laranja")
print(perry)