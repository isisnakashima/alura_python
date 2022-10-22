import jogoForca
import jogoPonto

print("**************************")
print("***Bem vindo aos jogos!***")
print("**************************")

print("(1) Forca, (2) Adivinhação")

jogo = int(input("Digite a opção que você deseja: "))

if jogo == 1:
    print("Jogando forca")
    jogoForca.jogar()

elif jogo == 2:
    print("Jogando adivinhação")
    jogoPonto.jogar()

else:
    print("Digite uma opção válida")
