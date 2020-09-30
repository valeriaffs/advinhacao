print("******************************************")
print("**********Jogo da Advinhação**************")
print("******************************************")

numero = 42
total_tentativas = 3
rodada = 1
nivel = 0

print("Nivel 1, você tem 20 tentativas")
print("Nivel 2, você tem 10 tentativas")
print("Nivel 3, você tem 5 tentativas")

nivel = int( input(" digite um nível "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
elif(nivel == 3):
    total_tentativas = 5 

for rodada in range(1, total_tentativas):
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
