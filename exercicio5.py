def n_positivos():
    positivo = 0

    while True:
        numero = int(input("Digite um número (ou um número negativo para sair): "))
        if numero < 0:
            break
        positivo += 1

    print(f"Você digitou {positivo} números positivos.")

n_positivos()