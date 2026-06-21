class Livro: #classe livro
    titulo = ""
    autor = ""
    ano = 0
    codigo = ""
    status = "Disponivel"

def Logo(): #função da logo
    #LLM UTILIZADA PARA REALIZAR A LOGO.
    #MOTIVO: NÃO IA CONSEGUIR FAZER UMA LOGO BONITA DESSAS NA MÃO
    print(r"""
        ██████╗ ██╗██████╗ ██╗     ██╗ ██████╗ ████████╗███████╗ ██████╗ █████╗
        ██╔══██╗██║██╔══██╗██║     ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
        ██████╔╝██║██████╔╝██║     ██║██║   ██║   ██║   █████╗  ██║     ███████║
        ██╔══██╗██║██╔══██╗██║     ██║██║   ██║   ██║   ██╔══╝  ██║     ██╔══██║
        ██████╔╝██║██████╔╝███████╗██║╚██████╔╝   ██║   ███████╗╚██████╗██║  ██║
        ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

        ██╗███╗   ██╗████████╗███████╗██╗     ██╗ ██████╗ ███████╗███╗   ██╗████████╗███████╗
        ██║████╗  ██║╚══██╔══╝██╔════╝██║     ██║██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔════╝
        ██║██╔██╗ ██║   ██║   █████╗  ██║     ██║██║  ███╗█████╗  ██╔██╗ ██║   ██║   █████╗
        ██║██║╚██╗██║   ██║   ██╔══╝  ██║     ██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝
        ██║██║ ╚████║   ██║   ███████╗███████╗██║╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗
        ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
    """)
    print(r"""
        ╔══════════════════════════════════════════════════════╗
        ║ A MELHOR MANEIRA DE CADASTRAR OS SEUS LIVROS         ║
        ╚══════════════════════════════════════════════════════╝
    """)
    print("___________________________________________________________________________________________________________")
    print("ESCOLHA A SUA OPÇÃO")
    print("___________________________________________________________________________________________________________")

def Menu(): #função do menu
    print("-------------------------")
    print("1 - Cadastrar livro")
    print("2 - Consultar livro")
    print("3 - Alterar dados")
    print("4 - Remover livro")
    print("5 - Listar todos")
    print("6 - Realizar empréstimo")
    print("7 - Realizar devolução")
    print("0 - Sair")
    print("-------------------------")

    op = int(input("Opção: "))
    return op

def sortc(livros): #função que cria uma uma lista nova com os livros em ordem por ano de lançamento
    lsort = []

    for i in range(len(livros)):
        lsort.append(livros[i])

    for i in range(len(lsort)):
        for j in range(i + 1, len(lsort)):
            if lsort[i].ano > lsort[j].ano:
                lsort[i], lsort[j] = lsort[j], lsort[i] #troca de posição
    return lsort

def Percorre(livros, codigo): #função que percorre a lista livros a procura de um codigo especifico
    for i in range(len(livros)):
        if livros[i].codigo == codigo:
            return i
    return -1

def PercorreAutor(livros, autor): #função que percorre a lista livros a procura de um autor especifico e coloca ele na lista laut
    laut = []

    for i in range(len(livros)): 
        if livros[i].autor == autor:
            laut.append(i)

    return laut

def Cadastrar(livros): #função que faz um cadastro de um livro

    while True: #verifica se o codigo ja existe
        codigo = input("Informe um codigo numerico para ser atribuido ao livro: ")
        if Percorre(livros, codigo) > -1:
            print("Codigo ja esta em utilização, insira outro codigo.")
        else:
            break

    livro = Livro()
    livro.codigo = codigo
    livro.titulo = input("Título: ")
    livro.autor = input("Autor: ")
    livro.ano = int(input("Ano de publicação: "))
    livro.status = "Disponivel"

    livros.append(livro)

    print("Livro cadastrado com sucesso.")

def Consultar(livros): #consulta a existencia de um livro

    while True:
        print("1 - Buscar por codigo")
        print("2 - Buscar por autor")

        op = int(input("Opção: "))

        if op == 1 or op == 2:
            break
        else:
            print("Insira uma opção valida")


    if op == 1: #buscar por codigo
        codigo = input("Codigo: ")
        print("-------------------------")

        i = Percorre(livros, codigo)

        if i >= 0:
            print("Título:", livros[i].titulo)
            print("Autor:", livros[i].autor)
            print("Ano:", livros[i].ano)
            print("Código:", livros[i].codigo)
            print("Status:", livros[i].status)
        else:
            print("Livro não encontrado")

    if op == 2: #imprimir todos os livros de um autor
        autor = input("Autor: ")
        print("-------------------------")

        laut = PercorreAutor(livros, autor)

        if len(laut) > 0:
            for i in range(len(laut)):
                j = laut[i]
                print("Título:", livros[j].titulo)
                print("Ano:", livros[j].ano)
                print("Código:", livros[j].codigo)
                print("Status:", livros[j].status)
                print("-------------------------")

        else:
            print("Livro não encontrado")

def Alterar(livros): #alterar as informações de um livro
    codigo = input("Código do livro: ")

    i = Percorre(livros, codigo)

    if i >= 0:
        livros[i].titulo = input("Novo título: ")
        livros[i].autor = input("Novo autor: ")
        livros[i].ano = int(input("Novo ano: "))

        print("Dados alterados.")
    else:
        print("Livro não encontrado")

def Remover(livros): #remover a existencia de um livro
    codigo = input("Código do livro: ")

    i = Percorre(livros, codigo)

    if i >= 0:
        livros.remove(livros[i])
        print("Livro removido.")
    else:
        print("Livro não encontrado")

def Listar(livros): #listar todos os livros em ordem cronologica
    sortcs = sortc(livros)
    for i in range(len(sortcs)):
        print(sortcs[i].titulo, "-", sortcs[i].ano)

def Emprestimo(livros): #mudar o status de um livro para "Emprestado"
    codigo = input("Código do livro: ")

    i = Percorre(livros, codigo)

    if i >= 0:
        if livros[i].status == "Disponivel":
            livros[i].status = "Emprestado"
            print("Empréstimo realizado com sucesso")
        else:
            print("Livro já emprestado")
    else:
        print("Livro não encontrado")

def Devolucao(livros): #mudar o status de um livro para "Disponivel"
    codigo = input("Código do livro: ")

    i = Percorre(livros, codigo)

    if i >= 0:
        if livros[i].status == "Emprestado":
            livros[i].status = "Disponivel"
            print("Devolução realizada.")
        else:
            while True:
                empop=input(("Livro não esta emprestado, gostaria de emprestar o livro? (SIM/NAO)"))
                if empop == "SIM" or empop == "NAO":
                    if empop == "SIM":
                        Emprestimo(livros)
                        break
                    else:
                        break
                else:
                    print('Reposda com "SIM" ou "NAO"')
    else:
        print("Livro não encontrado")

def Main(): #função principal do codigo, chama todas as outras
    livros = [] #lista de livros

    Logo()

    while True:
        op = Menu()

        if op <= 7 and op >=0:

            if op == 0:
                print('Muito obrigado por ter usado o programa "Biblioteca Inteligente"')
                break

            if op == 1:
                Cadastrar(livros)

            if op == 2:
                Consultar(livros)

            if op == 3:
                Alterar(livros)

            if op == 4:
                Remover(livros)

            if op == 5:
                Listar(livros)

            if op == 6:
                Emprestimo(livros)

            if op == 7:
                Devolucao(livros)

        else:
            print("Opção invalida, digite outra opção")

Main() #coluna principal do codigo