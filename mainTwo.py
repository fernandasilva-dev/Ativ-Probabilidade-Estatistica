import matplotlib.pyplot as plt

limiteInferior = []
limiteSuperior = []
quantidadeClasses = 6
quantidadeElementos = 50
fi = [0,0,0,0,0,0]

def mediaDistribuicao(limite_inferior, limite_superior, frequencia):
    somaProduto = 0
    somaFrequencia = 0
    for i in range(len(limite_inferior)):
        pontoMedio = (limite_superior[i] + limite_inferior[i]) / 2
        somaProduto += pontoMedio * frequencia[i]
        somaFrequencia += frequencia[i]
    media = somaProduto / somaFrequencia
    return media


def medianaDistribuicao(limite_inferior, limite_superior, frequencia):
    numElementos = 0
    for freq in frequencia:
        numElementos += freq

    somaFrequencia = 0

    for i in range(len(frequencia)):
        somaFrequencia += frequencia[i]
        if somaFrequencia >= numElementos / 2:
            intervaloMediana = (limite_inferior[i], limite_superior[i])
            if numElementos % 2 == 0:
                l = limite_inferior[i]
                F = somaFrequencia - frequencia[i]
                freqMediana = frequencia[i]
                amplitude = limite_superior[i] - limite_inferior[i]
                mediana = l + ((numElementos / 2 - F) / freqMediana) * amplitude
                return mediana
            else:
                return intervaloMediana


def modaDistribuicao(limite_inferior, limite_superior, frequencia):
    indiceModal = 0
    for i in range(1, len(frequencia)):
        if frequencia[i] > frequencia[indiceModal]:
            indiceModal = i

    L = limite_inferior[indiceModal]
    fModal = frequencia[indiceModal]

    amplitude = limite_superior[indiceModal] - limite_inferior[indiceModal]

    if indiceModal > 0:
        fAnterior = frequencia[indiceModal - 1]
    else:
        fAnterior = 0

    if indiceModal < len(frequencia) - 1:
        fPosterior = frequencia[indiceModal + 1]
    else:
        fPosterior = 0

    moda = L + ((fModal - fAnterior) / (2 * fModal - fAnterior - fPosterior)) * amplitude
    return moda


def desvioPadrao(limite_inferior, limite_superior, frequencia, media):
    somaProduto = 0
    somaFrequencia = 0
    for i in range(len(limite_inferior)):
        pontoMedio = (limite_inferior[i] + limite_superior[i]) / 2

        somaProduto += frequencia[i] * ((pontoMedio - media) ** 2)
        somaFrequencia += frequencia[i]

    variancia = somaProduto / somaFrequencia
    desvioP = variancia ** 0.5
    return desvioP


def percentil(limite_inferior, limite_superior, frequencia, p):
    N = 0
    for freq in frequencia:
        N += freq

    posicao = p * N / 100
    somaFAcumulada = 0

    for i in range(len(frequencia)):
        somaFAcumulada += frequencia[i]

        if somaFAcumulada >= posicao:
            L = limite_inferior[i]
            F = somaFAcumulada - frequencia[i]
            f = frequencia[i]
            h = limite_superior[i] - limite_inferior[i]

            percentil = L + ((posicao - F) / f) * h
            return percentil


def grafico(limite_inferior, limite_superior, frequencia):
    categoria = []
    for i in range(len(frequencia)):
        novosValores = str(limite_inferior[i]) + "|--" + str(limite_superior[i])
        categoria.append(novosValores)

    for i, valor in enumerate(frequencia):
        plt.text(i, valor + 0.2, str(valor), ha="center", fontsize=10)

    plt.bar(categoria, frequencia, color="purple")
    plt.title("Gráfico de Frequência", fontsize=16)
    plt.xlabel("Classes", fontsize=14)
    plt.ylabel("Frequencia", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

elementos = [61,65,43,53,55,51,58,55,59,56,
             52,53,62,49,68,51,50,67,62,64,
             53,56,48,50,61,44,64,53,54,55,
             48,54,57,41,54,71,57,53,46,48,
             55,46,57,54,48,63,49,55,52,51]
elementosOrdenados = sorted(elementos)

for i in range(quantidadeClasses):

    if i == 0:
        limiteInferior.append(elementosOrdenados[0])

    limiteSuperior.append(limiteInferior[i] + 5)

    if i == 5:
        break

    limiteInferior.append(limiteSuperior[i])

for i in range(quantidadeElementos):
    for j in range(6):
        if j < 5:
            if elementosOrdenados[i] >= limiteInferior[j] and elementosOrdenados[i] < limiteSuperior[j]:
                fi[j] += 1
        if j == 5:
            if elementosOrdenados[i] >= limiteInferior[j] and elementosOrdenados[i] <= limiteSuperior[j]:
                fi[j] += 1

media = mediaDistribuicao(limiteInferior, limiteSuperior, fi)
mediana = medianaDistribuicao(limiteInferior, limiteSuperior, fi)
moda = modaDistribuicao(limiteInferior, limiteSuperior, fi)
dPadrao = desvioPadrao(limiteInferior, limiteSuperior, fi, media)
percentil25 = percentil(limiteInferior, limiteSuperior, fi, 25)
percentil50 = percentil(limiteInferior, limiteSuperior, fi, 50)
percentil75 = percentil(limiteInferior, limiteSuperior, fi, 75)
decil10 = percentil(limiteInferior, limiteSuperior, fi, 10)
decil90 = percentil(limiteInferior, limiteSuperior, fi, 90)

print("    CLASSE    |  fi")
for i in range(len(fi)):
    if (limiteInferior[i] >= 1000 and limiteSuperior[i] >= 1000):
        print(limiteInferior[i], "|--", limiteSuperior[i], "|", fi[i])
    else:
        print(limiteInferior[i], " |--", limiteSuperior[i], " |", fi[i])

print("\nMedia: ", media)
print(f"Moda: {moda:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio Padrao: {dPadrao:.2f}")
print(f"Percentil 25: {percentil25:.2f}")
print(f"Percentil 50: {percentil50:.2f}")
print(f"Percentil 75: {percentil75:.2f}")
print(f"Decil 10: {decil10:.2f}")
print(f"Decil 90: {decil90:.2f}")

mostrarGrafico = grafico(limiteInferior, limiteSuperior, fi)
