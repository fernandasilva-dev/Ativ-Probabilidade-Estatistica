def mediaDistribuicao(limite_inferior,limite_superior, frequencia):
    somaProduto = 0
    somaFrequencia = 0
    for i in range(len(limite_inferior)):
        pontoMedio = (limite_superior[i] + limite_inferior[i])/2
        somaProduto += pontoMedio * frequencia[i]
        somaFrequencia += frequencia[i]
    media = somaProduto / somaFrequencia
    return media
    
def medianaDistribuicao(limite_inferior,limite_superior, frequencia):
    numElementos = 0
    for freq in frequencia:
        numElementos += freq
    
    somaFrequencia = 0

    for i in range(len(frequencia)):
        somaFrequencia += frequencia[i]
        if somaFrequencia >= numElementos / 2:
            intervaloMediana = (limite_inferior[i],limite_superior[i])
            if numElementos % 2 == 0:
                l = limite_inferior[i]
                F = somaFrequencia - frequencia[i]
                freqMediana = frequencia[i]
                amplitude = limite_superior[i] - limite_inferior[i]
                mediana = l + ((numElementos / 2 - F) / freqMediana) * amplitude
                return mediana
            else:
                return intervaloMediana

def modaDistribuicao(limite_inferior,limite_superior,frequencia):
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

def desvioPadrao(limite_inferior,limite_superior,frequencia,media):
    somaProduto = 0
    somaFrequencia = 0
    for i in range(len(limite_inferior)):
        pontoMedio = (limite_inferior[i] + limite_superior[i]) / 2

        somaProduto += frequencia[i] * ((pontoMedio - media)**2)
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



limite_inferior = [300,400,500,600,700,800,900,1000,1100]
limite_superior = [400,500,600,700,800,900,1000,1100,1200]

frequencia = [14,46,58,76,68,62,48,22,6]

media = mediaDistribuicao(limite_inferior,limite_superior,frequencia)
mediana = medianaDistribuicao(limite_inferior,limite_superior,frequencia)
moda = modaDistribuicao(limite_inferior,limite_superior,frequencia)
dPadrao = desvioPadrao(limite_inferior,limite_superior,frequencia,media)
percentil25 = percentil(limite_inferior, limite_superior, frequencia, 25)
percentil50 = percentil(limite_inferior, limite_superior, frequencia, 50)
percentil75 = percentil(limite_inferior, limite_superior, frequencia, 75)
decil10 = percentil(limite_inferior, limite_superior, frequencia, 10)
decil90 = percentil(limite_inferior, limite_superior, frequencia, 90)

print("    CLASSE    |  fi")
for i in range(len(frequencia)):
    if(limite_inferior[i] >= 1000 and limite_superior[i] >= 1000):
        print(limite_inferior[i],"|--",limite_superior[i],"|",frequencia[i])
    else:
        print(limite_inferior[i]," |--",limite_superior[i]," |",frequencia[i])

print("\nMedia: ", media)
print(f"Moda: {moda:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio Padrao: {dPadrao:.2f}")
print(f"Percentil 25: {percentil25:.2f}")
print(f"Percentil 50: {percentil50:.2f}")
print(f"Percentil 75: {percentil75:.2f}")
print(f"Decil 10: {decil10:.2f}")
print(f"Decil 90: {decil90:.2f}")