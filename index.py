#menu principal

index=0
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
            index=cadastro()
#CADASTRO DE CLIENTES

#cliente_username = []
#cliente_cpf = []
#cliente_senha = []
#cliente_email = []
#cliente_limitecredito = []

#dados_cliente = [cliente_username, cliente_cpf, cliente_senha, cliente_email, cliente_limitecredito]
#while True:

   # nome = input("Digite seu nome: ")
  #  cliente_username.append(nome)

    #cpf = input("Digite seu CPF: ")
    #if cpf in cliente_cpf:
     #   print ("Cliente já cadastrado")
      #  break
    #else:
    #    cliente_cpf.append(cpf)

    #senha = input("Digite sua senha: ")
    #cliente_senha.append(senha)
    #email = input("Digite seu email: ")
    #cliente_email.append(email)
    #limitecredito = input("Digite seu limite de crédito: ")
    #cliente_limitecredito.append(limitecredito) 
    #print ("Parabéns, Cadastro concluido com sucesso!")
    

#print (dados_cliente)

# Lista de Produtos

        elif opcao == "2":
            print("Opção selecionada: Comprar") 
            cpf=input("Digite  o cpf: ")  
            senha= input("Digite  a senha: ")  
            comprar(cpf,senha)

        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")            
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")            
            mostra_produtos()

        elif opcao == "0":
            print("Saindo...")
            
        else:
            print("Opção inválida! Tente novamente.")

menu()
