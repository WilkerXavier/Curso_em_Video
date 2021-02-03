print("{:=^40}".format(" Lojinha "))

preco = float(input("Preço da compra R$:"))

print(''''Formas de Pagamento:
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão ''')

opcao = int(input("Qual opção ?: "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$:{:.2f} sem juros ".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input("Quantas parcelas ?: "))
    parcela =   total / totparcela
    print("Sua compra será parcelada em {} de R$:{:.2f} com juros".format(totparcela, parcela))
else:
    print("Opção inválida")

print("Sua compra de R$:{:.2f} vai custar R$:{:.2f} no final".format(preco, total))
