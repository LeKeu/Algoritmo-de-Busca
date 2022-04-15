def binSe(v, n, menor, maior, k):
    if menor > maior:
        return -1, k

    meio = (menor + maior) // 2

    if v[meio] < n:
        return binSe(v, n, meio+1, maior, k+1)
    elif v[meio] > n:
        return binSe(v, n, menor, meio-1, k+1)
    else:
        k += 1
        return meio, k


if __name__ == "__main__":
    vetor = [n for n in range(1, 1001)]

    posic, i = binSe(vetor, 1789, 0, len(vetor) - 1, 0)

    if posic > -1:
        print(f"Posição do elemento --> {posic}")
    else:
        print(f"Elemento não encontrado --> {posic}")

    print(f"vezes rodado --> {i}")