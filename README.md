# Sistema Bancário Simples

Este é um programa de sistema bancário simples em Python. Ele permite que o usuário faça depósitos, saques, visualize o extrato da conta e saia do sistema.

## Funcionalidades

- **Depósito:** Permite que o usuário deposite um valor em sua conta.
- **Saque:** Permite que o usuário saque um valor de sua conta, respeitando um limite diário de saques.
- **Extrato:** Exibe todas as transações (depósitos e saques) realizadas, além do saldo atual da conta.
- **Sair:** Encerra o programa.

## Como Funciona

### Menu Principal

O programa exibe um menu principal com as seguintes opções:

```text
|=========//=======|
|    [D] Depositar |
|    [S] Sacar     |
|    [E] Extrato   |
|    [Q] Sair      |
|========//========|
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

