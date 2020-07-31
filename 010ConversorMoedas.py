real = float(input("Quanto de dinheiro voçê tem na carteira ? R$: "))
dolar = real / 5.20
euro = real / 6.15

print("Com R$:{} voçê pode comprar US$: {:.2f}".format(real, dolar))
print("Com R$:{} voçê pode comprar EUR: {:.2f}".format(real, euro))