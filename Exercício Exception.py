def validar_idade(idade):
    if idade < 0:
        raise Exception("Erro: Idade não pode ser negativa.")
    elif idade < 18:
        print("Menor de idade")
    else:
        print("Maior de idade")
try:
    entrada = int(input("Digite sua idade: "))
    validar_idade(entrada)
except ValueError:
    print("Erro: Por favor insira um número válido.")
except Exception as e:
    print(e)