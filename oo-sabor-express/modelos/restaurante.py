from modelos.avaliacao import Avaliacao

class Restaurante: ## classe de um objeto (molde)
    restaurantes = []

    ## o uso do caracter _ é uma boa prática de mercado já que eu protejo as minhas variaveis, evitando que usem elas no escopo global e quebre o código

    def __init__(self, nome, categoria): ## init é o construtor, ele da os valores iniciais para a instancia em especifico. e o self é justamente quem aponta para a instancia(objeto em especifico)
        self._nome = nome.title() ## title() Transforma a primeira letra em maiusculo
        self._categoria = categoria.upper() ## upper() transforma todas as letras em maiusculas
        self._ativo = False 
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod ## boas práticas para apontar que um método é de uma classe e não de uma instância
    def listar_restaurantes(cls): ## o cls aponta para a própria classe, é uma boa prática para não quebrar a linguagem. Pois se eu decicir mudar a o nome da minha classe, só preciso fazer isso na linha 1, já que no método o cls se adapta automaticamente.
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avalição'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') ## aqui estou usando o 'ativo' como uma função disfarçada de variavel por conta do @property. Dessa forma não preciso chamar o 'ativo' como um método 'ativo()'

    @property ## serve para criar uma função que finge ser uma variavel, se passando por um atributo dinâmico.
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo ## o not sempre nega o estado em que ele esta, sempre vai colocar o contrario do que ele é

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media