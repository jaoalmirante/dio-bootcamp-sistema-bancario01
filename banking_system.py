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
saque_list = []
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
        if numero_saques >= 3:
            print("Você ultrapassou o seu limite de saque!!")
            
        else:
            saque = float(input("Digite o valor que deseja sacar até 500 reais => "))
            if saque <= 500:
                if saldo >= saque:
                    saldo = saldo - saque
                    numero_saques = numero_saques + 1
                    saque_list.append(saque)
                else:
                    print("O seu saque não pode ser maior que o valor em conta!!")
            else:
                print("Você não pode sacar este valor")
            
        print(numero_saques)
        print(saldo)

        
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!!")