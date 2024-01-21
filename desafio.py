print ("Bem vindo ao Banco X")
print ("Escolha a uma das opções 'd' para depósito, 's' para saque, 'e' para verificar o extrato ou 'sair'")



opcao = input ["Informe a opçao desejada: "]
opcao = s
deposito = 0
sacar = 0

while opcao != 'sair':
    if opcao == 'd':
        print ("você escolheu a opção depositar:")
        valor_deposito = float (input ("informe o valor a ser depositado"))
        deposito += valor_deposito
        print ("O valor depositado é de:" + valor_deposito)
    elif opcao == 's':
        print("Você escolheu a opção de saque:")
        valor_saque = float(input('Informe o valor que deseja sacar: '))
        if valor_saque <= deposito:
            sacar += valor_saque
            deposito -= valor_saque
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif opcao == 'e':
        print("Você escolheu a opção de ver o extrato:")
        extrato = deposito - sacar
        print("Saldo disponível:", extrato)

    opcao = input("Digite a próxima opção ('sair' para encerrar): ")

print("Obrigado por usar o Banco X. Até logo!")