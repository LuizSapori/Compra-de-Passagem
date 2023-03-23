# Pacote de Cores Colorama
from colorama import init, Fore , Back , Style
init(autoreset=True)

# 1 - VARIÁVEIS

PASSAGENS_DISPONIVEIS = 28
ASSENTO_VAZIO = ''
COMPRAR = 1
VER_ASSENTOS = 2
RESUMO_VENDAS = 3
SAIR = 4
JANELA = 'J'
CORREDOR = 'C'
DIREITA = 'D'
ESQUERDA = 'E'
ASSENTOS_COLUNA = PASSAGENS_DISPONIVEIS // 4

# 2 - CABEÇALHO

print()
print( Fore.BLUE + Back.BLACK + '     PPROJETO POCCOBUS     ')
print()

# 3 - MENU

def menu_passagem():
    print('*-------------------------------------*')
    print('  |    MENU - VENDA DE PASSAGENS    | ')
    print('*-------------------------------------*')
    print('[ 1 ] Comprar passagem')
    print('[ 2 ] Assentos disponíveis')
    print('[ 3 ] Resumo Vendas')
    print('[ 4 ] Sair')
    print('*-------------------------------------*')
    return int(input( Fore.BLUE + 'Selecione uma opção:  '))

# 4 FUNÇÔES P/ FUNCIONAMENTO

def assentos_vendidos(assentos):
    return True if assentos == 'X' else False

# Função seleção da posição J (E/D) ou C ((E/D) para compra de passagem. Seleção entre colunas.

def comprar_passagem(janela_direita,  corredor_direita, janela_esquerda, corredor_esquerda, total_vendido):
    while total_vendido <= PASSAGENS_DISPONIVEIS:

        print(Fore.BLUE + 'VENDA DE PASSAGENS')
        print()

        print(Fore.BLUE + 'ESCOLHA SEU ASSENTO: ')
        print()
        assentos_disponiveis()
        janela_ou_corredor = input(Fore.BLUE + ' Selecione Janela [ J ] ou Corredor [ C ]: ').upper()
        if janela_ou_corredor == JANELA:
            direira_ou_esquerda = input(Fore.BLUE + 'Janela direita [ D ] ou esquerda [ E ]: ').upper()
            if direira_ou_esquerda == DIREITA:
                continuar_passagem(janela_direita, total_vendido)
                total_vendido += 1
            elif direira_ou_esquerda == ESQUERDA:
                continuar_passagem(janela_esquerda, total_vendido)
                total_vendido += 1
            else:
                print(Fore.RED + 'Opção inválida!')

        elif janela_ou_corredor == CORREDOR:

            opcao_direira_ou_esquerda = input(Fore.BLUE + 'Corredor direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == DIREITA:
                continuar_passagem(corredor_direita, total_vendido)
            elif opcao_direira_ou_esquerda == ESQUERDA:
                continuar_passagem(corredor_direita, total_vendido)
            else:
                print(Fore.RED+ 'Opção inválida!')

        else:
            print(Fore.RED+ 'Opção inválida!')

        if total_vendido == 28:
            print(Fore.RED +'\n***** Todas as passagens foram vendidas! *****\n')
            break

        continuar = input('Deseja comprar outra passagem? [S/N]: ').upper()
        if continuar == 'S':
            continue
        else:
            break

        return total_vendido

#Função seleção da posição entre colunas.

def continuar_passagem(assentos, total_passagens):
    if todos_assentos_vendidos(assentos):
        print(Fore.RED + 'Todos os lugares estão ocupados!')

    print('Lugares disponíveis:')
    lista_posicoes_livres = busca_posicoes_livres(assentos)
    assentos_livres(lista_posicoes_livres)

    finalizou_compra = False
    while not finalizou_compra:
        continuar_compra = int(input(Fore.BLUE+ '\n Digite o número do assento desejado (1-7): '))
        if continuar_compra in lista_posicoes_livres:
            assentos[continuar_compra - 1] = 'X'
            total_passagens += 1
            finalizou_compra = True
        else:
            print('Opção invalida! Escolha novamente!')
            finalizou_compra = False

    print('\n Operação efetuada com sucesso!! \n')

    return total_passagens

#Função de estruturação dos assentos disponíveis e do mapa de ocupação do ônibus..

def assentos_disponiveis():
    print(Fore.GREEN+'   Lugares vagos [ ]' + Fore.RED + '   Lugares ocupados [X]\n')
    print('     1  2  3  4  5  6  7')

    print('    ', end='')
    for assentos in janela_direita:
        print(f'[{(assentos if assentos  else " ")}]', end='')
    print('   -> Janela Direita')

    print('    ', end='')
    for assentos in corredor_direita:
        print(f'[{(assentos  if assentos else " ")}]', end='')
    print('   -> Corredor Direito')

    print('    ', end='')
    for assentos in corredor_esquerda:
        print(f'[{assentos  if assentos  else " "}]', end='')
    print('   -> Corredor Esquerdo')

    print('    ', end='')
    for assentos  in janela_esquerda:
        print(f'[{(assentos  if assentos  else " ")}]', end='')
    print('   -> Janela Esquerda')

    print('    ', end='')


def resumo_vendas(total_vendido,total_passagens):
    print()
    print(f'O NÚMERO DE PASSAGENS VENDIDAS FORAM {total_vendido + total_passagens} restam {PASSAGENS_DISPONIVEIS - total_vendido-total_passagens} passagens!')


def todos_assentos_vendidos(assentos):
    return ASSENTO_VAZIO not in assentos

# Função determinação dos assentos livres e ocupados.

def busca_posicoes_livres(assentos):
    posicoes_livres = []
    for indice, assentos in enumerate(assentos, start=1):
        if not assentos_vendidos(assentos):
            posicoes_livres.append(indice)
    return posicoes_livres

def assentos_livres(assentos_livres):
    posicoes_livres = ' - '.join(str(numero_assentos ) for numero_assentos in assentos_livres)
    print(posicoes_livres)

# 5 FUNCIONAMENTO

#   Criando vetores

if __name__ == '__main__':
    # Criando colunas!!
    janela_direita = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    corredor_direita = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    janela_esquerda = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    corredor_esquerda = [ASSENTO_VAZIO] * ASSENTOS_COLUNA

    total_vendido = 0

    while True:
        opcao_menu = menu_passagem()

        if opcao_menu == COMPRAR:
            comprar_passagem(janela_direita,corredor_direita,janela_esquerda,corredor_esquerda,total_vendido)

        elif opcao_menu == VER_ASSENTOS:
            print('Ver assentos\n')
            assentos_disponiveis()

        elif opcao_menu == RESUMO_VENDAS:
            assentos_disponiveis()
            resumo_vendas(total_vendido,total_passagens=True)
            break

        elif opcao_menu == SAIR:
            break