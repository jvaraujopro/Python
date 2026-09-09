#while is a loop 
while True:
    try:
        nota = int(input("A nota dos meus amigos hoje é: "))
        if nota >= 9:
            print("Eu amo vocês!")
        elif nota >= 7:
            print("Vocês são legais!")
        elif nota >= 5:
            print("precisamos conversar!")
        else:
            print("Vou excluir nosso grupo")
    except ValueError:
        print("Por favor insira um número válido.")
    

