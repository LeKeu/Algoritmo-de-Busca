# Implementar os algoritmos de busca de dados apresentados, utilizando a linguagem de programação a sua escolha (1,0 pt).

# Para cada algoritmo, o trio terá que mostrar três casos de teste
# (considerando um vetor com mil elementos -> use uma função que gera valores de 1 a 1000 NÃO ALEATÓRIO):
# um caso que o elemento é encontrado e outro caso que o elemento não é encontrado (0,5 pt).

# Para cada algoritmo, um contador de comparações deve ser usado e, no final da busca,
# o valor do contador deve ser mostrado (0,5 pt).

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
    # 0  1   2   3   4   5   6   7   8   9
    posic, i = linSe(vet, 1340)
    t1 = 40
    t2 = 333
    t3 = 6794

    print(f"{t1}: Posição --> {linSe(vet, t1)[0]} || Vezes rodado --> {linSe(vet, t1)[1]}")
    print(f"{t2}: Posição --> {linSe(vet, t2)[0]} || Vezes rodado --> {linSe(vet, t2)[1]}")
    print(f"{t3}: Posição --> {linSe(vet, t3)[0]} || Vezes rodado --> {linSe(vet, t3)[1]}")