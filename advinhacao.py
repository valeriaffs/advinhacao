print("******************************************")
print("**********Jogo da Advinhação**************")
print("******************************************")

numero = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_tentativas))
    chute = int (input("Digite um número: "))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if (acertou):
        print("Você acertou")
        break
    elif(maior):
        print("Você errou!  número foi maior que o número secreto")
    elif(menor):
        print("Você errou! número foi menor que o número secreto")
    rodada = rodada + 1

print("Fim do Jogo")
