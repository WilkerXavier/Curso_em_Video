sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos,\nInforme seu sexo novamente: ")).strip().upper()[0]

print("Sexo {} cadastrado com secesso".format(sexo))
