from modelos.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao):
        ##super - serve para chamar o construtor da classe pai, ou seja, a classe que eu estou herdando. No caso, a classe ItemCardapio
        super().__init__(nome, preco)
        self._descricao = descricao

    