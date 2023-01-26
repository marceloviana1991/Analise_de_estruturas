def mat_rig(x, comprimento, angulo, i, j, rotula, caracteristicas):
    import math
    import operacoes_com_matrizes
    rotacao = []
    rigidez_local_local = []
    rigidez_local_global = []
    rigidez_global = []
    rigidez_global_aux = []
    # Dimensionamento da matriz de rigidez global
    for _ in range(len(x) * 3):
        rigidez_global_aux.append(0)
    for _ in range(len(x) * 3):
        rigidez_global.append(rigidez_global_aux.copy())
    for a in range(len(comprimento)):
        # Cálculo do vetor de espalhamento
        espalhamento = [
            3 * (i[a] + 1) - 3,
            3 * (i[a] + 1) - 2,
            3 * (i[a] + 1) - 1,
            3 * (j[a] + 1) - 3,
            3 * (j[a] + 1) - 2,
            3 * (j[a] + 1) - 1]
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
        if not(rotula[a][0]) and not(rotula[a][1]):
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
        elif rotula[a][0] and not(rotula[a][1]):
            rigidez_local_local[1][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[1][5] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[4][1] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][4] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 3
            rigidez_local_local[4][5] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][1] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][4] = -3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a] ** 2
            rigidez_local_local[5][5] = 3 * caracteristicas[a][2] * caracteristicas[a][1] / comprimento[a]
        elif not(rotula[a][0]) and rotula[a][1]:
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
        # Locação da matriz de rigidez local na matriz de rigidez global
        for b, d in enumerate(espalhamento):
            for c, e in enumerate(espalhamento):
                rigidez_global[d][e] = rigidez_local_global[b][c] + rigidez_global[d][e]
    return rigidez_global
