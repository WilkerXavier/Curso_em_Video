frase = str(input("Digite a sua frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if  inverso == junto:
    print("A frase é um Palíntromo!")
else:
    print("Não é Palíntromo!")
