menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        print("Depósito")
        deposito = float(input("Quanto você dejesa depositar? "))
        if deposito >= 0:
            saldo = deposito + saldo
        else:
            print("Voce não pode depositar valores negativos!!")
        print(saldo)
    elif opcao == 's':
        print("Saque")
        saques_restantes = LIMITE_SAQUES
        if saques_restantes == 0:
            print("Você ultrapassou o seu limite de saque!!")
            
        else:
            saque = float(input("Digite o valor que deseja sacar até 500 reais"))
            if saque <= 500:
                saldo = saldo - saque
            else:
                print("Você não pode sacar este valor")
            saques_restantes = saques_restantes - 1
        print(saques_restantes)
        print(saldo)

        
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!!")