print("*********************************")
print("Bem vindos ao jogo de adivinhação")
print("*********************************")

total_de_tentativas = 3
numero_secreto = 54

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute=(int(input("Digite o seu número entre 1 a 100: ")))
    print("Você digitou: ", chute)

    if chute == 54:
        print("Parábens, você acertou!")
        break
    else:
        if chute <= 53:
            print("Tente novamente, o número secreto é maior")
        elif chute >= 55:
            print("Tente novamente! O número é menor!")
    rodada = rodada  + 1

print("Obrigada por jogar!")
