import subprocess

restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False}, 
                {'nome' : 'Pizza seprema', 'categoria' : 'Italiana', 'ativo' : True},
                {'nome' : 'Feijoada', 'categoria' : 'Brasileira', 'ativo' : False}]

def exibir_nome_do_programa():
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def reiniciar():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida, digite um numero de 1 a 4, apenas!')
    reiniciar()

def exibir_subtitulo(texto):
    subprocess.run('cls', shell=True)
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    reiniciar()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        print(f'- {nome_restaurante} | {categoria}')

    reiniciar()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    #opcao_escolhida = int(input('Escolha uma opção: '))
    #match opcao_escolhida:
        #case 1:
            #print('Adicionar restaurante')
        #case 2:
            #print('Listar restaurantes')
        #case 3:
            #print('Ativar restaurante')
        #case 4:
            #print('Finalizar app')
        #case _:
            #print('Opção inválida!') #opcao de uso do match para cadeias de condicionais mais complexas (como um switch casa do python)

def main():
    subprocess.run('cls', shell=True)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()