preco = float(input("Qual é o preço deste produto ? R$: "))
desconto = preco - (preco * 5 / 100)

print("O produto que custava {}, na promoção de 5% vai custar R$: {}".format(preco, desconto))