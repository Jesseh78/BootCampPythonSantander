# Em Python, propriedades são uma forma elegante de controlar o acesso 
# aos atributos de uma classe. Elas permitem que você use métodos como se 
# fossem atributos, mantendo a encapsulação e permitindo validações/controlos.

class Foo:
    def __init__(self, x=None):
        # O atributo "_x" é uma convenção para indicar que ele é "protegido"
        # (ou seja, só deve ser acessado de dentro da classe).
        self._x = x

    @property
    def x(self):
        # Este método é um "getter".
        # Ele será chamado quando alguém acessar "foo.x" como se fosse um atributo.
        # Aqui podemos controlar o que será retornado.
        print("Acessando valor de x...")  # Mensagem para fins didáticos
        return self._x                    # Retorna o valor armazenado em _x

    @x.setter
    def x(self, value):
        # Este método é um "setter".
        # Ele será chamado quando alguém fizer "foo.x = algum_valor".
        # Serve para validar ou modificar o valor antes de armazená-lo.

        print("Atribuindo novo valor a x...")  # Mensagem para mostrar quando o setter é ativado
        
        # Validação: só aceita números (inteiros ou ponto flutuante).
        if not isinstance(value, (int, float)):
            raise ValueError("x deve ser um número.")  # Se não for número, lança erro
        
        # Se passar pela validação, armazena o valor no atributo protegido _x
        self._x = value

    @x.deleter
    def x(self):
        # Este método é um "deleter".
        # Ele será chamado quando fizermos "del foo.x".
        # Serve para limpar ou apagar o atributo.

        print("Deletando x...")  # Mensagem para mostrar que o deleter foi acionado
        del self._x              # Remove o atributo _x da instância

# === Testando a classe Foo ===

foo = Foo(10)       # Cria um objeto com _x = 10 (valor inicial)
print(foo.x)        # Chama o getter (equivalente a foo.x), imprime e retorna o valor de _x

foo.x = 20          # Chama o setter para alterar o valor de x para 20
print(foo.x)        # Chama novamente o getter, agora retornando 20

del foo.x           # Chama o deleter, que remove _x da instância

print(foo.x)        # ERRO! O getter tenta acessar _x, mas ele foi deletado.
# Isso gera AttributeError: 'Foo' object has no attribute '_x'
