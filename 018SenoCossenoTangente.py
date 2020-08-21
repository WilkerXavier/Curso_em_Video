import math

angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O ângulo de {} tem o Seno de {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o Cosseno de {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem a Tangente de {:.2f}".format(angulo, tangente))