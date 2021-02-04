somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemVelho = ''
totMulher20 = 0

for n in range(1, 5):
    print("----- {}ª Pessoa -----".format(n))
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F] : ")).strip().upper()

    somaIdade +=idade

    if n == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem: 
            maiorIdadeHomem = idade
            nomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1 

mediaIdade = somaIdade / 4

print("\nA média de idade do grupo é de {} anos".format(mediaIdade))
print("O Homem mais velho tem {} e se chama {} ".format(maiorIdadeHomem, nomeHomemVelho))
print("Ao todo são {} Mulheres com menos de 20 anos\n ".format(totMulher20))
