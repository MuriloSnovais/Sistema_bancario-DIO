from time import sleep


menu = """
|=========//=======|
|    [D] Depositar |
|    [S] Sacar     |
|    [E] Extrato   |
|    [Q] Sair      |
|========//========|
Opção:
"""
def tempo_analise_da_conta():
    print("Analisando sua conta...")
    sleep(1)
saldo = 0 
limite = 500
extrato = []
saque = 0
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu).upper()

    if opcao == 'D':
        tempo_analise_da_conta()
        valor = float(input("Quanto deseja depositar na sua conta?: "))
        if valor <= 0:
            valor -= valor
            print("Digite um valor válido para depositar...")
        elif valor > 0:
            saldo += valor
            extrato.append({'tipo': 'deposito', 'valor' : valor})
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            

    elif opcao == 'S':
        tempo_analise_da_conta()
        print(f"Você tem R${saldo:.2f} na sua conta")
        if saldo > 0:
            saque = float(input("Digite o valor para realizar o saque: "))
            if LIMITE_SAQUE == 0:
                print("Você atingiu o limite diarios de saques...")
            elif saque <= 0:
                print("Não é posssivel realizar saques com numeros negativos ou zero")
            elif saque > saldo:
                print("TRANSAÇÃO CANCELADA")
                print(f"O valor do saque de R${saque:.2f} é maior que o valor do seu saldo R${saldo:.2f}")
            elif saque > 500:
                print("Não é possivel realizar saques acima de R$500,00 reais.")
            elif saque <= saldo:
                numero_saques += 1
                print(f"Você sacou R${saque:.2f} com sucesso")
                saldo -= saque
                LIMITE_SAQUE -= 1
                print(f"Saldo Na conta: R${saldo:.2f}")
                extrato.append({'tipo': 'Saque', 'valor': saque})
                print(f"limites de saque faltando {LIMITE_SAQUE}")  

        elif saldo == 0:
            print("Você não possui saldo na conta.")

        elif saldo <= -1:
            print("SEU SALDO ESTA NEGATIVO!!!")
    
    elif opcao == "E":
        print("Extrato")
        print("-=-" * 10)
        print(f"Total de saques: {numero_saques}")
        if extrato == []:
            print("Nenhum extrato realizado")
        else:
            for transacao in extrato:
                print(f"{transacao['tipo']}: R${transacao['valor']:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        print("-=-" * 10)
    
    elif opcao == "Q":
        print("Saindo... Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação invalida, por favor selecione uma opção válida.")