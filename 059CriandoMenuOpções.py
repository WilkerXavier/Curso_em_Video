n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opcao = 0 
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair''')
    opcao = int(input("Qual é a sua opção: "))

    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} e {} é: {}".format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print("A multiplicação de {} e {} é: {}".format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            print("O Maior é: {}".format(n1))
        else:
            print("O Maior é: {}".format(n2))
    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        print("Opção Invalida,\nTente Novamente...")
print("Fim !!!")
