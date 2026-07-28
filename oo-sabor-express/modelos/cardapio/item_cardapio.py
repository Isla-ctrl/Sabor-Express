from abc import ABC, abstractmethod

class ItemCardapio(ABC): 
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    ##abstractmethod é um decorador que indica que o método é abstrato, ou seja, ele não tem implementação na classe pai e deve ser implementado nas classes filhas. Isso força as classes filhas a implementarem o método, garantindo que todas as classes que herdam de ItemCardapio tenham o método aplicar_desconto. 
    @abstractmethod
    def aplicar_desconto(self):
        pass

    