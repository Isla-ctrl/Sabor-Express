class Prato:
    def __init__(self, nome: str, preco: float, descricao: str = None):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}" + (f" ({self.descricao})" if self.descricao else "")