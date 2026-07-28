from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
