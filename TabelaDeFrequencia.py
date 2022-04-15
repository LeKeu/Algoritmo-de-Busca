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
    vetor = [n for n in range(1, 1001)]
    criarTabFreq(vetor)
    checarTabelaFreq(140)
