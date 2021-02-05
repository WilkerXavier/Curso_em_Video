numero = int(input("Digite o fatorial: "))
count = numero
fatorial =  1

print("Calculando Fatorial de {}! = ".format(numero), end = '') 
while count > 0: 
    print("{}".format(count), end = '')
    print(" x " if count > 1 else " = ", end = '')
    fatorial *= count
    count -= 1
    

print("{}".format(fatorial))
