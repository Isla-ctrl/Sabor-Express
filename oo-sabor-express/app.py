from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.0, 'grande')
prato_bife = Prato('Bife a Parmegiana', 25.0, 'Bife com molho de tomate e queijo gratinado')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_bife)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
