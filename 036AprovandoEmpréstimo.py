valorCasa = float(input("Qual é o valor da casa ? R$: "))
salario = float(input("Quanto é o seu salaria ? R$: "))
anos = int(input("Em quantos anos você quer pagar ? : "))

meses = anos * 12
prestacao = valorCasa / meses 
minimo = (salario * 30) / 100

print("Para pagar uma casa de {:.2f} em {} anos a pretação será de {:.2f}".format(valorCasa, anos, prestacao))

if prestacao <= minimo:
    print("Empretimo Aprovado")
else:
    print("Emprestimo Negado") 