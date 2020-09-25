print("******************************************")
print("**********Jogo da Advinhação**************")
print("******************************************")

numero = 42
chute = int (input("Digite um número: "))

acertou = chute == numero
maior = chute > numero
menor = chute < numero

if (acertou):
    print("Você acertou")
elif(maior):
    print("Você errou!  número foi maior que o número secreto")
elif(menor):
    print("Você errou! número foi menor que o número secreto")
