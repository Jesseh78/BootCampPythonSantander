
# Programação Orientada a Objetos (POO)

## O que é Orientação a Objetos?

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código com base em **objetos**, que são instâncias de **classes**. Esse modelo simula elementos do mundo real, tornando o código mais modular, reutilizável, organizado e fácil de manter.

A POO se baseia em quatro pilares principais:

- **Abstração:** foco apenas nos detalhes essenciais.
- **Encapsulamento:** ocultação de detalhes internos de um objeto.
- **Herança:** capacidade de uma classe herdar características de outra.
- **Polimorfismo:** objetos podem se comportar de maneiras diferentes dependendo do contexto.

---

## Definição de Classes e Objetos

### Classe

Uma **classe** é uma estrutura que define um tipo de objeto. Ela funciona como um molde, onde são definidos os **atributos** (dados) e **métodos** (funções) que os objetos daquele tipo terão.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

### Objeto

Um **objeto** é uma instância concreta de uma classe. Quando criamos um objeto, estamos usando o molde da classe para gerar algo utilizável no programa.

```python
p1 = Pessoa("Maria", 30)
p1.apresentar()  # Saída: Olá, meu nome é Maria e tenho 30 anos.
```

---

## Construtores e Destrutores

### Construtor

O **construtor** é um método especial usado para inicializar os objetos criados a partir de uma classe. Em Python, o método `__init__` é o construtor padrão.

```python
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        print(f"O livro '{self.titulo}' foi criado.")
```

### Destrutor

O **destrutor** é um método chamado automaticamente quando um objeto é destruído (ou sai de escopo). Em Python, usamos o método `__del__`.

```python
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        print(f"O livro '{self.titulo}' foi criado.")
    
    def __del__(self):
        print(f"O livro '{self.titulo}' foi removido da memória.")
```

> **Nota:** Em Python, o coletor de lixo gerencia a memória automaticamente. O `__del__` pode ser útil em casos específicos, como fechar arquivos ou conexões.

---

## Resumo

| Conceito        | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| POO             | Paradigma baseado em objetos que facilita a modelagem de sistemas reais. |
| Classe          | Modelo para criar objetos, com atributos e métodos.                      |
| Objeto          | Instância concreta de uma classe.                                        |
| Construtor      | Método que inicializa o objeto no momento da criação. (`__init__`)       |
| Destrutor       | Método executado quando o objeto é destruído. (`__del__`)                |
