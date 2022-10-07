import random

print("******************")
print("Bem vindos ao Jogo")
print("******************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual é o nível de dificuldade?")
print("(1) para fácil, (2) para médio, (3) para difícil")

nivel = int(input("Digite a sua difículdade: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5
else:
    print("Digite um valor válido")

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    if numero_secreto == chute:
        print("Parábens, você acertou!")
        break
    else:
        if numero_secreto > chute:
            print("Tente novamente, o número secreto é maior")
        elif numero_secreto < chute:
            print("Tente novamente! O número é menor!")
    rodada = rodada + 1
    print("Obrigada por jogar!")
