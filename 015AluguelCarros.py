dias = int(input("Quantos dias alugado ? "))
km = float(input("Quantos km rodados ? "))

diaria = dias * 60
rodados = km * 0.15
pagar = diaria + rodados

print("O total a pagar é de R$:{:.2f}".format(pagar))