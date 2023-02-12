saldo = 0
LIMITE_SAQUE = 3
qnt_depositada = 0
LIMITE = 500
extrato = ""
qnt_diaria_saque = 0
while True:
    op = input('Qual operação deseja fazer?\n'
    '[Depositar/Sacar/Extrato/Sair] ')

    if op == 'D':
        valor = float(input('Valor a depositar: '))
        if valor <= 0:
            print('Este valor é invalido')
        else:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            qnt_depositada += 1

    elif op == 'S':
        valor = float(input('Quanto deseja sacar? '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = qnt_diaria_saque >= LIMITE_SAQUE

        if excedeu_saques:
            print('Você não pode mais sacar hoje. Volte amanha.')
        elif excedeu_saldo:
            print('Não será possível sacar por falta de saldo.')
        elif excedeu_limite:
            print('Você não pode sacar mais que R$500,00')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
        else:
            print('O valor informado é invalido')
    
    elif op == 'E':
        print('\n=================EXTRATO================')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('==========================================\n')
    
    elif op == 'Q':
        break

    else:
        print('Operação invalida!')