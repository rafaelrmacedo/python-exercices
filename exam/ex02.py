secreta = 'computador'
descobrir = len(secreta) * '-'
tentativas = 0

while tentativas != 6 or descobrir == secreta:
    print(f"Tentativa n° {tentativas + 1}")
    letra = input("Digite uma letra: ")
    letra.lower()

    for x in range(0, len(secreta)):
        if secreta[x] == letra:
            descobrir = descobrir[0:x] + letra + descobrir[x+1:]
            print(descobrir)

    if len(letra) > 1:
        print("Mais de uma letra! Digite novamente.")

    if letra not in secreta:
        tentativas += 1
        print("Letra incorreta!")
        print(f"Tentativas: {tentativas} \n")

    if tentativas == 6:
        print("Perdeu!")
        break

    if descobrir == secreta:
        print("PARABÉNS!")
        break



print(descobrir)
