import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print("Sua palvra secreta tem:", len(palavra_secreta),  "letras")  # o len mostra o tamanho da palvra
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} rodadas".format(6-erros))

        enforcou = erros == 6
        acertou = "__" not in letras_acertadas
        print(letras_acertadas)

        if erros == 6:
            break
        if "__" not in letras_acertadas:
            break

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    print("Fim do jogo")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou :)")


def imprime_mensagem_perdedor():
    print("Que pena, você perdeu :(")


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def inicializa_letras_acertadas(palavra):
    return ["__" for letra in palavra]
# usa a lista pq o tuple é imutável. para o tuple se usa ()


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def pede_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    # o strip remove todos os espaços em branco, antes ou depois da palavra

    return chute


if __name__ == "__main__":
    jogar()
