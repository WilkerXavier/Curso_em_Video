peso = float(input("Qual é o seu peso ?: "))
altura = float(input("Qual a sua altura ?: "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do Peso")
elif imc <= 25:
    print("Peso Ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")

print("Seu IMC é de {:.2f}".format(imc))