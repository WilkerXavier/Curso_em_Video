from random import randint
computador = randint(0, 10)

print("Adivinhe um número de 0 á 10.")

acertou = False
palpites = 1
while not acertou:
    jogador = int(input("Palpite: "))
    if jogador == computador:
        acertou = True
        print("Você acertou !!!")
        print("Você teve {} palpites para acertar".format(palpites)) 
    else:
        if computador > jogador:
            print("O número é maior !!!")
        elif computador < jogador:
            print("O número é menor !!!") 
    palpites += 1

print("Fim!")
