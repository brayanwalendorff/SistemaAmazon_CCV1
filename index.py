import os
from sys import breakpointhook
import time

index = 0
#CADASTRO DE CLIENTES
cliente_username = ["marquinhos"]
cliente_cpf = ["123"]
cliente_senha = ["123"]
cliente_email = ["mark@hotmail.com"] 
cliente_limitecredito = ["1000"]

# Lista de produtos
produtos_carrinho = []
escolha1 = ["Pasta de Dente R$ 500,00"]
escolha2 = ["Arroz 5kg R$ 100,00"]
escolha3 = ["Feijão 1kg R$ 400,00"]
escolha4 = ["Açucar 1kg R$ 200,00"]
produtos_total = [['Pasta de dente', '500.00'], ['Arroz 5 kg', '100.00'], ['Feijão 1 kg', '500.00'], ['Açucar 1 kg', '50.00']]
#produtos_nome = ['Pasta de dente', 'Arroz 5 kg', 'Feijão 1 kg', 'Açucar 1 kg']
#produtos_preco = [5.00, 10.00, 4.00, 2.00]
printscreen = (''' Lista de produtos disponíveis:\n
 1 - Pasta de Dente --- R$ 500,00
 2 - Arroz 5kg -------- R$ 100,00
 3 - Feijão 1kg ------- R$ 400,00
 4 - Açucar 1kg ------- R$ 200,00
 0 - Sair
            ''')

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

#def login():
   # cpf=input("\n Digite  o cpf: ")
    #if cpf in cliente_cpf:
       # senha = input("\n Digite  a senha: ")
        #if senha in cliente_senha:
    #else
        #print("Senha incorreta")
       # time.sleep(1)
       # os.system('cls')

def cadastro (cpf):
    #Caso o cliente não esteja cadastrado solicita os dados e armazena
    if not cpf in cliente_cpf:
        cliente_cpf.append(cpf)
        nome = input("\n Digite seu Nome: ")
        cliente_username.append(nome)

        #inicia uma verificação de senha de 6 digitos
        while True:
            senha = input("\n Digite sua senha de 6 dígitos: ")
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

def compras():
    print(printscreen)
    escolha=-1
    credtotal = 1000
    
    while escolha !="0":

        print("\n Seu Saldo atual é igual a: ", credtotal)
        escolha=input("\n Escolha uma opção: ")
        if escolha == "0":
            escolha = input("\n Deseja encerrar a compra? 0 =  Sim,  1 - Não")
            time.sleep(3)
            cliente_limitecredito.append(credtotal)
            os.system('cls')

        if escolha == "1":
            print("\n Adicionando produto a sacola...")
            time.sleep(2)
            print("\n Produto adicionado com sucesso!!")
            credtotal = credtotal - 500
            produtos_carrinho.append(escolha1)
            print(printscreen)
        

        if escolha == "2":
            print("\n Adicionando produto a sacola...")
            time.sleep(2)
            print("\n Produto adicionado com sucesso!!")
            credtotal = credtotal - 100
            produtos_carrinho.append(escolha2)
            print(printscreen)
        

        if escolha == "3":
            print("\n Adicionando produto a sacola...")
            time.sleep(2)
            print("\n Produto adicionado com sucesso!!")
            credtotal = credtotal - 400
            produtos_carrinho.append(escolha3)
            print(printscreen)
    

        if escolha == "4":
            print("\n Adicionando produto a sacola...")
            time.sleep(2)
            print("\n Produto adicionado com sucesso!!")
            credtotal = credtotal - 500
            produtos_carrinho.append(escolha4)
            print(printscreen)
            
        
        if credtotal <= 0:
            print("\n Seu limite estourou...")
            print("\n Pague sua fatura antes de voltar as compras. \n")
            time.sleep(4)
            break

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
            cpf = input("\n Digite seu CPF: ")
            #Verificar CPF se é valido ou não
            if cpf_validate(cpf):
                print('\n CPF válido.')
                cadastro(cpf)
                time.sleep(1)
                os.system('cls')
            else:
                print('\n CPF inválido.')
                time.sleep(1)
                os.system('cls')
                
        elif opcao == "2":
            os.system('cls')
            print("\n Opção selecionada: Comprar \n")
            cpf=input("\n Digite  o cpf: ")
            if cpf in cliente_cpf:
                senha = input("\n Digite  a senha: ")
                if senha in cliente_senha:
                    print("\n Login efetuado com Sucesso!!! \n")
                    compras()
                else:
                    print("\n Senha incorreta")
                    time.sleep(1)
                    os.system('cls')
                
            else:
                print("\n CPF INVALIDO")
                time.sleep(1)
                os.system('cls')
            
        elif opcao == "3":
            os.system('cls')
            print("\n Opção selecionada: Mostrar carrinho \n")
            print (produtos_carrinho)

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
                    produtos_carrinho.clear()
                else:
                        print ("\n Senha incorreta. \n")

            #Verificação de CPF
            if not cpf in cliente_cpf:
                    print("\n CPF incorreto.")

        elif opcao == "5":
            os.system('cls')
            print("\n Opção selecionada: Consultar cliente \n")            
            procurarcliente = input("\n Digite o cpf do cliente a ser procurado: ")
            print("\n \n \n Buscando cliente....Aguarde \n \n \n")
            time.sleep(5)
        
            if procurarcliente in cliente_cpf:
                print('\n Cliente foi encontrado!')
                print(cliente_username)
                time.sleep(2)
                os.system('cls')
            else:
                print('\n O cliente nao foi encontrado. Verifique o CPF!')
                time.sleep(2)
                os.system('cls')

        elif opcao == "6":
            os.system('cls')
            print("\n Opção selecionada: Mostrar produtos \n")  
            print(printscreen)            
            print('\n')
            input('Pressione enter para retornar ao MENU...')
            os.system('cls')

        elif opcao == "0":
            print("\n \n \n Fechando programa...Obrigado!")
            time.sleep(2)
            os.system('cls')
            
        else:
            print("\n Opção inválida! Tente novamente. \n")
            time.sleep(2)
            os.system('cls')

menu()
