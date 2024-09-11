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
        deposito = int(input("Quanto você dejesa depositar? "))
        if deposito >= 0:
            saldo = deposito + saldo
        else:
            print("Voce não pode depositar valores negativos!!")
        print(saldo)
    elif opcao == 's':
        print("Saque")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!!")