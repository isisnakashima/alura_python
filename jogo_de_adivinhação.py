print("*********************************")
print("Bem vindos ao jogo de adivinhação")
print("*********************************")

numero_secreto= 54
chute=(int(input("Digite seu número: ")))

if chute < 54:
    print("Tente novamente, o número secreto é maior")
elif chute >= 55:
    print("Tente novamente, o número secreto é menor")
else:
    print("Parabéns, você acertou!!!!")

print("Fim do jogo!")
