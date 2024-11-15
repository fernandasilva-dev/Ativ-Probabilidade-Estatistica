limiteInferior = []
limiteSuperior = []
quantidadeClasses = 6
quantidadeElementos = 50
fi = [0,0,0,0,0,0]

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
'''
contador = 1
for i in range(quantidadeElementos):
    if i == 49:
        if elementosOrdenados[i] != elementosOrdenados[i-1]:
            fi.append(contador)
        if elementosOrdenados[i] == elementosOrdenados[i - 1]:
            contador += 1

        break
    if elementosOrdenados[i] != elementosOrdenados[i+1]:
        fi.append(contador)
        contador = 1
    if elementosOrdenados[i] == elementosOrdenados[i+1]:
        contador += 1
'''

for i in range(quantidadeElementos):
    for j in range(6):
        if j < 5:
            if elementosOrdenados[i] >= limiteInferior[j] and elementosOrdenados[i] < limiteSuperior[j]:
                fi[j] += 1
        if j == 5:
            if elementosOrdenados[i] >= limiteInferior[j] and elementosOrdenados[i] <= limiteSuperior[j]:
                fi[j] += 1
print(elementosOrdenados)
print(fi)
print("-"*23)
print("|    CLASSES   |  fi  |")

for i in range(quantidadeClasses):
    print("-" * 23)
    print(f"|   {limiteInferior[i]} |- {limiteSuperior[i]}   |  {fi[i]}  |")
