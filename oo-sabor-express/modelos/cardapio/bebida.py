from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
            return self._nome

    def aplicar_desconto(self):
        desconto = 0.05
        self._preco -= self._preco * desconto
