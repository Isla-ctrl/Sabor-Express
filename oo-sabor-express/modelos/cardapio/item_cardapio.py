class ItemCardapio: 
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}" + (f" ({self.descricao})" if self.descricao else "")