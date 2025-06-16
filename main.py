menu = """
========================
       MENU BANCÁRIO
========================
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

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("❌ Valor inválido. Digite um valor maior que zero.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))

            if valor <= 0:
                print("❌ Valor inválido. Digite um valor maior que zero.")
            elif valor > saldo:
                print("❌ Saldo insuficiente.")
            elif valor > limite:
                print(f"❌ O valor excede o limite de R$ {limite:.2f} por saque.")
            elif numero_saques >= LIMITE_SAQUES:
                print("❌ Limite de saques diários atingido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

    elif opcao == "e":
        print("\n====== EXTRATO ======")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("======================")

    elif opcao == "q":
        print("✅ Obrigado por utilizar o sistema bancário. Até logo!")
        break

    else:
        print("❌ Opção inválida. Por favor, escolha uma opção válida.")

    print("\n")  # Separador visual entre as operações
