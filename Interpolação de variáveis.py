nome = "João Vitor"
idade = 18
profissão = "Estudante"
curso = "Ciência da Computação"
linguagem = "Python"

perfil = {"nome": "João Vitor", "idade": 18, "curso": "Ciência da Computação"}

print("Meu nome é %s tenho %d anos e curso %s." % (nome, idade, curso))

print("Meu nome é {} tenho {} anos e curso {}.".format(nome, idade, curso))

print("Meu nome é {0} tenho {1} anos e curso {2}. {0}".format(nome, idade, curso))

print("Meu nome é {nome} tenho {idade} anos e curso {curso}. {nome}".format(nome=nome, idade=idade, curso=curso))

print("Meu nome é {nome} tenho {idade} anos e curso {curso}. {nome}".format(**perfil))