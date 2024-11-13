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
                h = limite_superior[i] - limite_inferior[i]
                mediana = l + ((numElementos / 2 - F) / freqMediana) * h
                return mediana
            else:
                return intervaloMediana

def modaDistribuicao(frequencia,limite_inferior,limite_superior):
    frequenciaMax = -1
    moda = ()
    
    for i in range(len(frequencia)):
        if frequencia[i] > frequenciaMax:
            frequenciaMax = frequencia[i]
            moda = (limite_inferior[i],limite_superior[i])

    return moda

def desvioPadrao():
    desvio = 0
    


limite_inferior = [300,400,500,600,700,800,900,1000,1100]
limite_superior = [400,500,600,700,800,900,1000,1100,1200]

frequencia = [14,46,58,76,68,62,48,22,6]

media = mediaDistribuicao(limite_inferior,limite_superior,frequencia)
mediana = medianaDistribuicao(limite_inferior,limite_superior,frequencia)
moda = modaDistribuicao(limite_inferior,limite_superior,frequencia)

print("Media: ", media)
print("Moda: ", moda)
print(f"Mediana: {mediana:.2f}")