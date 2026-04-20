AGENDA = {}

AGENDA['Teste'] = {
    'telefone': '99999-9999',
    'email': 'yago@email.com',
    "endereco": 'Rua A, 123',
}

AGENDA['Teste2'] = {
    'telefone': '99999-9999',
    'email': 'teste2@email.com',
    "endereco": 'Rua b, 123',
}

def mostar_contatos():
    if len(AGENDA) > 0 :
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>>> Agenda vazia!')


def buscar_contato(contato):
    try:    
        print('Nome:', contato )
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]['endereco'])
        print('-----------------------------')
    except KeyError:    
        print(f'Contato {contato} não encontrado!')        



def captar_detales_contato():
    telefone = int(input('Digite o telefone do contato: '))
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')    
    return telefone, email, endereco # Retorna os detalhes do contato como uma tupla para ser usada na função incluir_editar_contato()



def incluir_editar_contato(contato,telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'Contato {contato} excluído com sucesso!')
    except KeyError:    
        print(f'Contato {contato} não encontrado!')
    except Exception as e:
        print('Ocorreu um erro insperado ao excluir contato!')
       #print(e) Opcional para ver o erro real      


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA: 
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n') # Escreve o nome do contato
        print('Agenda exportada com sucesso!')        
    except:
        print('Ocorreu algum erro inesperado ao exportar contatos!')     

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco) # Passa os detalhes do contato como argumentos separados para a função incluir_editar_contato()
        print('Contatos importados com sucesso!')

    except FileNotFoundError:
        print(f'Arquivo {nome_do_arquivo} não encontrado!')
    except Exception as e:
        print('Ocorreu um erro inesperado ao importar contatos!')
        print(e) # Opcional para ver o erro real                


def salvar():
    exportar_contatos('basededados.csv') # 

def carregar():
    try:
        with open('basededados.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

        AGENDA[nome] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }  
        print('Contatos carregados com sucesso!')
        print(f'>>>>>> {len(AGENDA)} contatos carregados.')  
           
    except FileNotFoundError:
        print(f'Arquivo {nome_do_arquivo} não encontrado!')
    except Exception as e:
        print('Ocorreu um erro inesperado ao importar contatos!')
        print(e) # Opcional para ver o erro real    


def imprimir_menu(): 
    print('--- AGENDA DE CONTATOS ---')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print('-----------------------------')

# INICIO DO PROGRAMA
carregar()
while True: #Identação do while
    try:    
        imprimir_menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1 :
            mostar_contatos()   

        elif opcao == 2 : 
            contato = input('Digite o nome do contato: ')
            buscar_contato(contato)  
        elif opcao == 3:
            contato = input('Digite o nome do contato: ')
            try:
                AGENDA[contato]
                print(f'Contato {contato} já existe')  
            except KeyError:
                print(f'Adicionando contato {contato} na agenda...')
                telefone, email, endereco = captar_detales_contato() # Recebe os detalhes do contato como uma tupla
                incluir_editar_contato(contato, telefone, email, endereco) # Passa os detalhes do contato como argumentos separados para a função incluir_editar_contato()
                print(f'Contato {contato} adicionado com sucesso!')    
        elif opcao == 4:
            contato = input('Digite o nome do contato: ')
            try:
                AGENDA[contato]
                print(f'Contato {contato} encontrado, editando contato...')
                telefone, email, endereco = captar_detales_contato() # Recebe os detalhes do contato como uma tupla
                incluir_editar_contato(contato, telefone, email, endereco) # Passa os detalhes do contato como argumentos separados para a função incluir_editar_contato()
                print(f'Contato {contato} editado com sucesso!')
            except KeyError:
                print(f'Contato {contato} não encontrado, não é possível editar contato inexistente!')

        elif opcao == 5 :
            contato = input('Digite o nome do contato: ')
            excluir_contato(contato)
        elif opcao == 6 :
            nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
            exportar_contatos(nome_do_arquivo)
        elif opcao == 7 :
            nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
            importar_contatos(nome_do_arquivo)    
        elif opcao == 0 :
            print('Fechando agenda...') 
            break
    except ValueError:
        print('Digite um número válido para a opção do menu!')    
