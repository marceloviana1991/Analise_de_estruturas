def vet_car(matriz_de_rigidez, recalque):
    vetor_dos_termos_de_carga = []
    recalque_vetor = []
    for a in recalque:
        for b in a:
            recalque_vetor.append(b)
    for a in range(len(recalque_vetor)):
        aux = 0
        for b in range(len(recalque_vetor)):
            aux = aux + matriz_de_rigidez[a][b] * recalque_vetor[b]
        vetor_dos_termos_de_carga.append([aux])
    return vetor_dos_termos_de_carga
