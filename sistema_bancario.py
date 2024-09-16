from time import sleep

def menu():
    print(
"""
|=========////=========|
|    [D] Depositar     |
|    [S] Sacar         |
|    [E] Extrato       |
|    [C] Criar User    |
|    [NC]Conta Corrente|
|    [LC]Listar contas |  
|    [Q] Sair          | 
|=========////=========|
""")
def tempo_analise_da_conta():
    print("Analisando sua conta...")
    sleep(1)

def sacar(*, saldo, saque, limite_saque, numero_de_saques):
    print(f"Você tem R${saldo:.2f} na sua conta")
    if saldo > 0:
        saque = float(input("Digite o valor para realizar o saque: "))
        if limite_saque == 0:
            return saldo, limite_saque, numero_de_saques, "Você atingiu o limite diário de saques..."
        elif saque <= 0:
            return saldo, limite_saque, numero_de_saques, "Não é possível realizar saques com números negativos ou zero"
        elif saque > saldo:
            return saldo, limite_saque, numero_de_saques, f"O valor do saque de R${saque:.2f} é maior que o valor do seu saldo R${saldo:.2f}"
        elif saque > 500:
            return saldo, limite_saque, numero_de_saques, "Não é possível realizar saques acima de R$500,00 reais."
        else:
            numero_de_saques += 1
            saldo -= saque
            limite_saque -= 1
            extrato.append({'tipo': 'Saque', 'valor': saque})
            print(f"Limites de saque restantes: {limite_saque}")
            return saldo, limite_saque, numero_de_saques, f"Você sacou R${saque:.2f} com sucesso"
    elif saldo == 0:
        return saldo, limite_saque, numero_de_saques, "Você não possui saldo na conta."
    else:
        return saldo, limite_saque, numero_de_saques, "SEU SALDO ESTÁ NEGATIVO!!!"

def deposito(saldo, valor,/):
    valor = float(input("Quanto deseja depositar na sua conta?: "))
    if valor > 0:
            saldo += valor
            extrato.append({'tipo': 'deposito', 'valor' : valor})
            return saldo , valor , f"Depósito de R${valor:.2f} realizado com sucesso!"
    else:
            print("Digite um valor válido para depositar...")

def func_extrato(saldo , / , * , extrato):

    print("Extrato")
    print("-=-" * 10)
    print(f"Total de saques: {numero_saques}")
    if not extrato:
            return "Nenhum extrato realizado"
    else:
        for transacao in extrato:
            print(f"{transacao['tipo']}: R${transacao['valor']:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        print("-=-" * 10)

def criar_usuario():
    print("-=-" * 10)
    print("Bem vindo ao cadastro de Conta")
    print("-=-" * 10)
    cadastro = {}
    cpf = input("Digite seu cpf(apenas numeros): ").replace('.', '').replace('-', '')
    cpf_existente = any(usuario.get('CPF') == cpf for usuario in usuarios)
    if cpf_existente:
        print("ESTE CPF JÁ FOI CADASTRADO")
        return 
    else:
        cadastro['CPF'] = cpf
        usuarios.append(cadastro)
        print("CPF cadastrado!")
    nome = str(input("Digite seu Nome:"))
    cadastro['Nome'] = nome
    data_nasc = input("Digite sua data de nastimento (dd-mm-aaaa): ")
    cadastro['Data de Nascimento'] = data_nasc
    print("-=-" * 10)    
    print("Digite seu endereço")
    print("-=-" * 10)
    endereco = {"Rua" : "" , "Bairro" : "" , "Cidade" : "" , "Estado" : ""}
    endereco["Rua"] = input("Rua: ")
    endereco["Bairro"] = input("Bairro: ")
    endereco["Cidade"] = input("Cidade: ")
    endereco["Estado"] = input("Estado/Sigla: ")
    cadastro['Endereco'] = endereco

def criar_conta_corrente():
    global numero_conta_sequencial
    
    cpf = input("Digite o CPF do usuário para associar a conta: ").replace('.', '').replace('-', '')
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        conta = {
            'agencia': AGENCIA,
            'numero_conta': numero_conta_sequencial,
            'usuario': usuario_encontrado['CPF'],

        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']}")
        
        numero_conta_sequencial += 1
    else:
        print("Usuário não encontrado. Verifique o CPF e tente novamente.")

def listar_contas(contas):
    for conta in contas:
        print("-=-" * 10)
        print(f"""
Agência:{conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']}
        """)
    print("-=-" * 10)

usuarios = []
extrato = []
contas = []
cadastro = {}
saldo = 0 
saque = 0
valor = 0
numero_conta_sequencial = 1
numero_saques = 0
LIMITE_SAQUE = 3
AGENCIA = "0001"

while True:
    menu()
    opcao = str(input("Digite uma opção: ").upper())

    if opcao == 'D':
        tempo_analise_da_conta()
        saldo , valor , mensagem = deposito(saldo,valor)
        print(mensagem)

    elif opcao == 'S':
        tempo_analise_da_conta()
        saldo, LIMITE_SAQUE, numero_saques, mensagem = sacar(saldo=saldo, saque=saque, 
        limite_saque=LIMITE_SAQUE, numero_de_saques=numero_saques)
        print(mensagem)

    elif opcao == "E":
        func_extrato(saldo, extrato=extrato)
        
    elif opcao == "C":
        criar_usuario()

    elif opcao == "NC":
        criar_conta_corrente()

    elif opcao == "LC":
        listar_contas(contas)

    elif opcao == "Q":
        print("Saindo... Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação invalida, por favor selecione uma opção válida.")