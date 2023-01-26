def diag_cort(restricoes_de_apoio, rotula, caracteristicas, comprimento, angulo, deslocabilidades, i, j, recalque,
              vetor_dos_termos_de_carga):
    import math
    import operacoes_com_matrizes
    caso_0 = []
    caso_n = []
    rigidez_local_local = []
    rigidez_local_global = []
    rotacao = []
    diagrama_de_esforco_cortante = []
    recalque_local = []
    for _ in range(6):
        recalque_local.append(0)
    # Casos n
    aux = []
    for a in range(len(restricoes_de_apoio) * 3):
        aux.append(0)
    for a in range(len(caracteristicas)):
        caso_n.append(aux.copy())
        caso_n.append(aux.copy())
    for a in range(len(comprimento)):
        recalque_local[0] = [recalque[i[a]][0]]
        recalque_local[1] = [recalque[i[a]][1]]
        recalque_local[2] = [recalque[i[a]][2]]
        recalque_local[3] = [recalque[j[a]][0]]
        recalque_local[4] = [recalque[j[a]][1]]
        recalque_local[5] = [recalque[j[a]][2]]
        # Cálculo da matriz de transformação por rotação
        rotacao.clear()
        for _ in range(6):
            rotacao.append([0, 0, 0, 0, 0, 0])
        rotacao[0][0] = math.cos(angulo[a])
        rotacao[0][1] = math.sin(angulo[a])
        rotacao[1][0] = -math.sin(angulo[a])
        rotacao[1][1] = math.cos(angulo[a])
        rotacao[2][2] = 1
        rotacao[3][3] = math.cos(angulo[a])
        rotacao[3][4] = math.sin(angulo[a])
        rotacao[4][3] = -math.sin(angulo[a])
        rotacao[4][4] = math.cos(angulo[a])
        rotacao[5][5] = 1
        # Cálculo da matriz de rigez local no sistema de coordenadas locais
        rigidez_local_local.clear()
        for _ in range(6):
            rigidez_local_local.append([0, 0, 0, 0, 0, 0])
        rigidez_local_local[0][0] = caracteristicas[a][2] * caracteristicas[a][0] / comprimento[a]
        rigidez_local_local[0][3] = -caracteristicas[a][2] * caracteristicas[a][0] / comprimento[a]
        rigidez_local_local[3][0] = -caracteristicas[a][2] * caracteristicas[a][0] / comprimento[a]
        rigidez_local_local[3][3] = caracteristicas[a][2] * caracteristicas[a][0] / comprimento[a]
        if not (rotula[a][0]) and not (rotula[a][1]):
            rigidez_local_local[1][1] = 12 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][2] = 6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[1][4] = -12 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][5] = 6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[2][1] = 6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[2][2] = 4 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
            rigidez_local_local[2][4] = -6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[2][5] = 2 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
            rigidez_local_local[4][1] = -12 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][2] = -6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[4][4] = 12 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][5] = -6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][1] = 6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][2] = 2 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
            rigidez_local_local[5][4] = -6 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][5] = 4 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
        elif rotula[a][0] and not (rotula[a][1]):
            rigidez_local_local[1][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][5] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[4][1] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][4] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][5] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][5] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
        elif not (rotula[a][0]) and rotula[a][1]:
            rigidez_local_local[1][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][2] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[1][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[2][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[2][2] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
            rigidez_local_local[2][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[4][1] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][2] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[4][4] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
        # Cálculo da matriz de rigidez local no sistema de coordenadas globais
        rigidez_local_global.clear()
        rigidez_local_local = operacoes_com_matrizes.multiplicacao(rigidez_local_local, rotacao)
        rotacao = operacoes_com_matrizes.transposta(rotacao)
        rigidez_local_global = operacoes_com_matrizes.multiplicacao(rotacao, rigidez_local_local)
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 3] = rigidez_local_global[0][1]
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 2] = rigidez_local_global[1][1]
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 1] = rigidez_local_global[2][1]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 3] = rigidez_local_global[0][4]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 2] = rigidez_local_global[1][4]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 1] = rigidez_local_global[2][4]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 3] = rigidez_local_global[3][1]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 2] = rigidez_local_global[4][1]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 1] = rigidez_local_global[5][1]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 3] = rigidez_local_global[3][4]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 2] = rigidez_local_global[4][4]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 1] = rigidez_local_global[5][4]
        # Cálculo do vetor dos termos de carga local no sistema de coordenadas globais
        vetor_dos_termos_de_carga_local = operacoes_com_matrizes.multiplicacao(rigidez_local_global, recalque_local)
        caso_0.append(vetor_dos_termos_de_carga_local[1][0])
        caso_0.append(vetor_dos_termos_de_carga_local[4][0])
        vetor_dos_termos_de_carga.clear
    for a in range(len(caracteristicas) * 2):
        aux = -caso_0[a]
        d = 0
        e = 0
        for b in restricoes_de_apoio:
            for c in b:
                if not(c):
                    aux = aux + deslocabilidades[d][0] * caso_n[a][e]
                    d = d + 1
                e = e + 1
        diagrama_de_esforco_cortante.append(aux)
    recalque_vetor = []
    for a in recalque:
        for b in a:
            recalque_vetor.append(b)
    return diagrama_de_esforco_cortante

