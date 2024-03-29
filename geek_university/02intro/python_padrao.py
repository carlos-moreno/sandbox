import datetime
import math


def main():
    inicio = datetime.datetime.now()

    computar(fim=100_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")


def computar(fim, inicio=1):
    pos = inicio
    fator = 1_000 * 1_000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()

"""
Terminou em 13.01 segundos.
"""
