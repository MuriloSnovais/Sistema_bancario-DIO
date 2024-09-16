# Banco Digital Simples - Versão 2.0

Este é um projeto simples de um banco digital desenvolvido em Python. Ele permite que os usuários realizem operações bancárias básicas como depósitos, saques e consultas de extrato, além de criar novas contas de usuário e contas correntes.

## Funcionalidades Principais

- **Depositar:** Permite ao usuário depositar valores na conta.
- **Sacar:** O usuário pode realizar saques de até R$500,00, com limite de 3 saques diários.
- **Extrato:** Exibe todas as transações feitas na conta, como depósitos e saques.
- **Criar Usuário:** Cadastra um novo usuário no sistema, validando se o CPF já existe.
- **Criar Conta Corrente:** Cria uma nova conta corrente vinculada a um usuário existente. O número da conta é gerado automaticamente e a agência é sempre "0001".

## Novidades na Versão 2.0

- Adicionada a funcionalidade de **criação de conta corrente**, onde:
  - O número da agência é fixo (0001).
  - O número da conta é sequencial.
  - Um usuário pode ter mais de uma conta corrente.
- Melhorias na verificação de **CPF já existente** ao criar um usuário.
  
O programa exibe um menu principal com as seguintes opções:

```text
"""
|=========////=========|
|    [D] Depositar     |
|    [S] Sacar         |
|    [E] Extrato       |
|    [C] Criar User    |
|    [NC]Conta Corrente|  
|    [Q] Sair          | 
|=========////=========|
"""
```
## Opções do Menu

### Depósito (`D`)

- O usuário é solicitado a informar o valor a ser depositado.
- O valor é adicionado ao saldo da conta e registrado no extrato.
- Caso o valor seja inválido (menor ou igual a zero), o programa solicita um valor válido.

### Saque (`S`)

- O usuário é informado sobre o saldo disponível.
- O saque só é permitido se:
  - O saldo for suficiente.
  - O valor solicitado for menor ou igual a R$500,00.
  - O limite diário de saques (3) não for excedido.
- O valor sacado é subtraído do saldo e registrado no extrato.

### Extrato (`E`)

- Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.
- Se não houver transações, uma mensagem informativa é exibida.
  
### Criar Usuário (`C`)

- O sistema solicita que o usuário informe seu CPF, nome, data de nascimento e endereço.
- O CPF é validado para garantir que não foi cadastrado anteriormente.
- Caso o CPF já esteja registrado, uma mensagem de erro será exibida, e o cadastro será interrompido.
- Um usuário só é criado se o CPF for único.

### Criar Conta Corrente (`NC`)

- O sistema cria uma nova conta corrente vinculada a um usuário existente.
- Cada conta corrente é composta por:
  - Agência (fixo: "0001")
  - Número da conta (sequencial, iniciando em 1)
  - CPF do usuário
- Um usuário pode ter mais de uma conta corrente.
- O sistema armazena as contas em uma lista.


### Sair (`Q`)

- Encerra o programa.

## Como Executar

1. Clone ou baixe este repositório.
2. Execute o programa usando o Python:
3. Siga as instruções do menu para interagir com o sistema bancário.

## Requisitos
- Python 3.x

## Licença
Este projeto é de domínio público e não possui uma licença específica.

   ```bash
Esse README fornece uma visão geral simples e direta do que o programa faz e como ele funciona. Você pode adaptá-lo conforme necessário!
