def adc_linha ():
    texto=input("Digite o Texto que deseja anotar: ")

    arquivo = open('arqText.txt', 'a+')
    arquivo.write(' ' + texto)
    arquivo.close()

    leitura=open('arqText.txt', 'r')
    print(leitura.read())
    leitura.close()
    opc_texto()


def edt_linha ():
    # Abrir o arquivo para leitura
    with open('arqText.txt', 'r') as leitura:
        linhas = leitura.readlines()

    # Exibir as linhas atuais
    print("Conteúdo atual do arquivo:")
    for i, linha in enumerate(linhas):
        print(f"{i + 1}: {linha.strip()}")

    # Perguntar qual linha o usuário deseja editar
    linha_num = int(input("Digite o número da linha que deseja editar: ")) - 1

    # Substituir o conteúdo dessa linha
    novo_texto = input("Digite o novo texto para essa linha: ")
    linhas[linha_num] = novo_texto + '\n'

    # Reescrever o arquivo com o novo conteúdo
    with open('arqText.txt', 'w') as arquivo:
        arquivo.writelines(linhas)

    # Mostrar o conteúdo atualizado
    print("Conteúdo atualizado do arquivo:")
    with open('arqText.txt', 'r') as leitura:
        print(leitura.read())
    opc_texto()


def ltr_texto ():
    leitura = open('arqText.txt', 'r')
    print(leitura.read())
    leitura.close()
    opc_texto()

def opc_texto ():
    print('1- Ler Texto')
    print('2- Editar Texto')
    print('3- Adicionar Texto')
    opc = int(input("Digite o numero da ação de deseja: "))

    if opc == 1:
        ltr_texto()
    if opc == 2:
        edt_linha()
    if opc == 3:
        adc_linha()


opc_texto()

