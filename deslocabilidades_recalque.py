def desloc(restricoes_de_apoio, matriz_de_rigidez, vetor_dos_termos_de_carga):
    import operacoes_com_matrizes
    restricoes_vetor = []
    vetor_dos_termos_de_carga_fixo = []
    vetor_dos_termos_de_carga_livre = []
    matriz_de_rigidez_livre_livre = []
    matriz_de_rigidez_fixo_livre = []
    aux = []
    aux2 = []
    reacoes = []
    for a in restricoes_de_apoio:
        for b in a:
            restricoes_vetor.append(b)
    for a, b in enumerate(vetor_dos_termos_de_carga):
        if restricoes_vetor[a]:
            vetor_dos_termos_de_carga_fixo.append(b)
        else:
            vetor_dos_termos_de_carga_livre.append(b[0])
    for a, b in enumerate(matriz_de_rigidez):
        aux.clear()
        aux2.clear()
        for c, d in enumerate(b.copy()):
            if not(restricoes_vetor[a]) and not(restricoes_vetor[c]):
                aux.append(d)
            if restricoes_vetor[a] and not(restricoes_vetor[c]):
                aux2.append(d)
        if not(restricoes_vetor[a]):
            matriz_de_rigidez_livre_livre.append(aux.copy())
        if restricoes_vetor[a]:
            matriz_de_rigidez_fixo_livre.append(aux2.copy())
    deslocabilidades = operacoes_com_matrizes.sistemas_lineares(matriz_de_rigidez_livre_livre,
                                                                vetor_dos_termos_de_carga_livre)
    aux = operacoes_com_matrizes.multiplicacao(matriz_de_rigidez_fixo_livre, deslocabilidades)
    for a in aux:
        reacoes.append(a)
    for a in range(len(reacoes)):
        reacoes[a][0] = (reacoes[a][0] - vetor_dos_termos_de_carga_fixo[a][0]) * - 1
    return deslocabilidades, reacoes

