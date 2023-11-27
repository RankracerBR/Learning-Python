import random

# Função para realizar o sorteio
def sorteio_participantes(numeros_participantes):
    numeros_sorteados = []
    ganhadores = set()

    while len(numeros_sorteados) < len(numeros_participantes):
        numero_sorteado = random.randint(1, len(numeros_participantes))

        if numero_sorteado not in numeros_sorteados:
            numeros_sorteados.append(numero_sorteado)

            if numero_sorteado not in ganhadores:
                ganhadores.add(numero_sorteado)
                print(f"Parabéns! O ganhador do brinde é o participante {numero_sorteado}")

numero_participantes = [i for i in range(1,5)]

sorteio_participantes(numero_participantes)