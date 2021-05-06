#menu principal
index=0
#casdatro=1

#CADASTRO DE CLIENTES
cliente_username = []
cliente_cpf = []
cliente_senha = []
cliente_email = []
cliente_limitecredito = []

# Lista de produtos
produtos_carrinho = []
produtos_total = [{'Pasta de dente': '500.00'}, {'Arroz 5 kg': '100.00'}, {'Feijão 1 kg': '500.00'}, {'Açucar 1 kg': '50.00'}]


def menu():
    opcao = "-1"

    while opcao != "0":
        print("""Menu:
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair""")
        opcao = input()

        if opcao == "1":
            print("Opção selecionada: Cadastro")
            
#cadastro de novos clientes

            cpf = input("Digite seu CPF: ")
            if not cpf in cliente_cpf:

                cliente_cpf.append(cpf)
                nome = input("Digite seu Nome: ")
                cliente_username.append(nome)
                senha = input("Digite sua senha: ")
                cliente_senha.append(senha)
                email = input("Digite seu email: ")
                cliente_email.append(email)
                cliente_limitecredito.append(1000.00) 
                print ("Parabéns, Cadastro concluido com sucesso!")

#verificar se o cliente já existe a partir do cpf
            else:    
                for cpf in cliente_cpf:
                        print("Cliente já cadastrado com o nome de: ", cliente_username)


        elif opcao == "2":
            print("Opção selecionada: Comprar")

#print (produtos_nome)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")

#Confirmação de compra
            cpf=input("Digite  o cpf: ")
            if cpf in cliente_cpf:
                
                senha = input("Digite  a senha: ")
                if senha in cliente_senha:
                    print ("Pagamento efutado com sucesso!")
                    cliente_limitecredito.clear()
                    
                else:
                        print ("Senha incorreta.")

#Verificação de CPF
            if not cpf in cliente_cpf:
                    print("CPF incorreto.")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")            
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")            
            print (type(produtos_total))

        elif opcao == "0":
            print("Saindo...")
            
        else:
            print("Opção inválida! Tente novamente.")

menu()
