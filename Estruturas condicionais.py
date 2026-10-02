MAIOR_IDADE = 18 #Caracteres em letras maiúsculas, por convenção, para determinar constante. 
IDADE_ESPECIAL = 12


idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não as práticas.")
else:
    print("Ainda não pode tirar a CNH.")