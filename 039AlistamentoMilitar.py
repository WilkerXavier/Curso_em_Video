from datetime import date 

atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento

print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, atual))

if idade == 18:
    print("Você tem que se Alistar este ano")
elif idade < 18:
    saldo = 18 - idade
    print("Falta {} anos para você se alistar".format(saldo))
    ano = atual + saldo
    print("Seu alistamento sera em {}".format(ano))
else:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))