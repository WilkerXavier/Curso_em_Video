numero = int(input("Digite o numero da tabuada: "))

for count in range(1, 11):
    multiplica = numero * count
    print("{} x {} = {}".format(numero, count, multiplica))
