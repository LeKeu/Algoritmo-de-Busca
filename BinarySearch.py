# Implementar os algoritmos de busca de dados apresentados, utilizando a linguagem de programação a sua escolha (1,0 pt).

# Para cada algoritmo, o trio terá que mostrar três casos de teste
# (considerando um vetor com mil elementos -> use uma função que gera valores de 1 a 1000 NÃO ALEATÓRIO):
# um caso que o elemento é encontrado e outro caso que o elemento não é encontrado (0,5 pt).

# Para cada algoritmo, um contador de comparações deve ser usado e, no final da busca,
# o valor do contador deve ser mostrado (0,5 pt).

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
    vet = [n for n in range(1, 1001)]
    #0  1   2   3   4   5   6   7   8   9
    t1 = binSe(vet, 250, 0, len(vet) - 1, 0)
    t2 = binSe(vet, 333, 0, len(vet) - 1, 0)
    t3 = binSe(vet, 6923, 0, len(vet) - 1, 0)

    print(f"Posição --> {t1[0]} || Vezes rodado --> {t1[1]}")
    print(f"Posição --> {t2[0]} || Vezes rodado --> {t2[1]}")
    print(f"Posição --> {t3[0]} || Vezes rodado --> {t3[1]}")