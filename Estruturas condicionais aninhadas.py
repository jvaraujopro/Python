conta_normal = False
conta_universitaria = False

saldo = 3000
saque = 5000
cheque_especial = 1000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo + cheque_especial >= saque:
        print("Saque realizado com sucesso usando cheque especial!")
    else:
        print("Saldo insuficiente para realizar o saque.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

else:
    print("Tipo de conta inválido.")