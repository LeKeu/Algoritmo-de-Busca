# Implementar os algoritmos de busca de dados apresentados, utilizando a linguagem de programação a sua escolha (1,0 pt).

# Para cada algoritmo, o trio terá que mostrar três casos de teste
# (considerando um vetor com mil elementos -> use uma função que gera valores de 1 a 1000 NÃO ALEATÓRIO):
# um caso que o elemento é encontrado e outro caso que o elemento não é encontrado (0,5 pt).

# Para cada algoritmo, um contador de comparações deve ser usado e, no final da busca,
# o valor do contador deve ser mostrado (0,5 pt).

import json


def criarTabFreq(v):
    freq = {}
    for n in v:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    with open("frequencia.txt", 'w') as f:
        f.write(json.dumps(freq))


def checarTabelaFreq(n):
    i = 0
    with open("frequencia.txt", 'r') as f:
        freq = json.loads(f.read())
        i += 1
        print("Valor encontrado") if str(n) in freq else print("Valor não encontrado")
        print(f"Vezes rodado --> {i}")


if __name__ == "__main__":
    vet = [n for n in range(1, 1001)]
    # 0  1   2   3   4   5   6   7   8   9
    checarTabelaFreq(40)
    checarTabelaFreq(333)
    checarTabelaFreq(609876)
