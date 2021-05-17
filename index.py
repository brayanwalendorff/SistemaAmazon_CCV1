import os
import time

index = 0
#CADASTRO DE CLIENTES
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = [] 
cliente_limitecredito = []

# Lista de produtos
produtos_carrinho = []
produtos_total = [{'Pasta de dente': '500.00'}, {'Arroz 5 kg': '100.00'}, {'Feijão 1 kg': '500.00'}, {'Açucar 1 kg': '50.00'}]
produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg']
produtos_preco = [5.00, 10.00, 4.00, 2.00]


total_carrinho = []


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def cadastro (cpf):
    #Caso o cliente não esteja cadastrado solicita os dados e armazena
    if not cpf in cliente_cpf:
        cliente_cpf.append(cpf)
        time.sleep(3)
        os.system('cls')
        nome = input("\n Digite seu Nome: ")
        cliente_username.append(nome)

        #inicia uma verificação de senha de 6 digitos
        while True:
            senha = input("\n Digite sua senha: ")
            tamanho_senha = len(list(senha))
            if tamanho_senha == 6:
                cliente_senha.append(senha)
                break
            else:
                print("\n Senha não corresponde aos requisitos \n")

        email = input("\n Digite seu email: ")
        cliente_email.append(email)
        cliente_limitecredito.append(1000.00) 
        
        print ("\n Parabéns, Cadastro concluido com sucesso! \n")
        return True

#verificar se o cliente já existe a partir do cpf
    else:    
        for cpf in cliente_cpf:
            print("\n Cliente já cadastrado com o nome de: ", cliente_username)
        return True
        
#Verificando o parametro senhas


def menu():
    opcao = "-1"

    while opcao != "0":
        print('''\n Menu: \n
 1 - Cadastro
 2 - Comprar
 3 - Mostrar carrinho
 4 - Pagar conta
 5 - Consultar cliente
 6 - Mostrar produtos
 0 - Sair''')
        opcao = input("\n Selecione uma opção: ")

        #cadastro de novos clientes
        if opcao == "1":
            os.system('cls')
            print("\n Opção selecionada: Cadastro \n")
            cpf = input(" Digite seu CPF: ")
            #Verificar CPF se é valido ou não
            if cpf_validate(cpf):
                print('\n CPF válido.')
                cadastro(cpf)
                time.sleep(3)
                os.system('cls')
            else:
                print('\n CPF inválido.')
                time.sleep(3)
                os.system('cls')
                
        elif opcao == "2":
            os.system('cls')
            print("\n Opção selecionada: Comprar \n")
            print(''' Lista de produtos disponíveis:\n
 1 - Pasta de Dente --- R$ 5,00
 2 - Arroz 5kg -------- R$ 10,00
 3 - Feijão 1kg ------- R$ 4,00
 4 - Açucar 1kg ------- R$ 2,00
            ''')
            listacompra = int(input('\n Digite o número do produto desejado: '))
            if listacompra > 0 and listacompra <=4:
                print("teste")
                
            else:
                print(' Código de produto inválido')
                time.sleep(3)
                os.system('cls')
            
        elif opcao == "3":
            os.system('cls')
            print("\n Opção selecionada: Mostrar carrinho \n")

        elif opcao == "4":
            os.system('cls')
            print("\n Opção selecionada: Pagar conta \n")

            #Confirmação de compra
            cpf=input("\n Digite  o cpf: ")
            if cpf in cliente_cpf:
                
                senha = input("\n Digite  a senha: ")
                if senha in cliente_senha:
                    print ("\n Pagamento efutado com sucesso! \n")
                    cliente_limitecredito.clear()
                    
                else:
                        print ("\n Senha incorreta. \n")

            #Verificação de CPF
            if not cpf in cliente_cpf:
                    print("\n CPF incorreto.")

        elif opcao == "5":
            os.system('cls')
            print("\n Opção selecionada: Consultar cliente \n")            
            procurarcliente = input('Digite o cpf do cliente a ser procurado: ')
        
            if procurarcliente in cliente_cpf:
                print('\n Cliente foi encontrado!')
                print(cliente_username)
            else:
                print('\n O cliente nao foi encontrado. Verifique o CPF!')
                

        elif opcao == "6":
            os.system('cls')
            print("\n Opção selecionada: Mostrar produtos \n")  
            print(''' Lista de produtos disponíveis:\n
 1 - Pasta de Dente --- R$ 5,00
 2 - Arroz 5kg -------- R$ 10,00
 3 - Feijão 1kg ------- R$ 4,00
 4 - Açucar 1kg ------- R$ 2,00
            ''')            
            print('\n')
            input('Pressione enter para retornar ao MENU...')
            os.system('cls')

        elif opcao == "0":
            os.system('cls')
            print("Fechando programa...Obrigado!")
            time.sleep(3)
            
        else:
            print("\n Opção inválida! Tente novamente. \n")

menu()
