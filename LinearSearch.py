def linSe(v, n):
    cntg = 0
    for i in range(len(v)):
        if v[i] == n:
            cntg += 1
            return i, cntg
        cntg += 1

    return -1, cntg


if __name__ == "__main__":
    vet = [n for n in range(1, 1001)]
    posic, i = linSe(vet, 1340)

    if posic > -1:
        print(f"Posição do elemento --> {posic}")
    else:
        print(f"Elemento não encontrado --> {posic}")

    print(f"vezes rodado --> {i}")