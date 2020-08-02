salario = float(input("Qual é o salario deste funcionário ? R$: "))
reajuste = salario + (salario * 15 / 100)

print("O funcionario que ganhava {}, com aumento de15%, passa a receber R$: {}".format(salario, reajuste))
