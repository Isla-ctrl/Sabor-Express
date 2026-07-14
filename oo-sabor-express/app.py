from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
##restaurante_mexicano = Restaurante('mexicano food', 'mexicano')
##restaurante_japones = Restaurante('Jaoa', 'Japonesa')

##restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('lais', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
