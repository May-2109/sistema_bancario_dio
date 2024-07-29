
def mostrarExtrato():
    global saldo
    print('\nSeu saldo atual é de R$ {:.2f}'.format(saldo))

def depositar():
    global saldo   
    valor = float(input('Informe o valor a depositar: '))
    saldo += valor
    print('\nValor de R$ {:.2f} depositado com sucesso!'.format(valor))
    return saldo

def sacar():
    global saldo, limite_saque
    if limite_saque < 3:
        limite_saque += 1
        valor = float(input('Informe o valor a sacar: '))
        if valor < saldo:
            saldo -= valor 
            print('\nValor de R$ {:.2f} sacado com sucesso!'.format(valor))
        elif valor > saldo:
            print("\nSaldo insuficiente!\nConsulte extrato.")
        return limite_saque
    else: 
        print('Limite de saques excedido! Entre em contato com o seu gerente.')

saldo = 0
valor = 0
limite_saque = 0

while True:
    menu = input("""\n
         ================ MENU ================
         
Informe a opção desejada:  
         
[e] Extrato
[d] Depositar
[s] Sacar
[q] Sair

""") 
    
    
    if menu == 'e':
        mostrarExtrato()
    elif menu == 'd':
        depositar()
    elif menu == 's':
        sacar()
    elif menu == 'q':
        print('\nObrigada por utilizar os nossos serviços.\nAté mais!!')
        break




