def diag_mom(comprimento, angulo, rotula, caracteristicas, restricoes_de_apoio, deslocabilidades, h, alfa, temperatura,
             cg, i, j):
    import math
    import operacoes_com_matrizes
    caso_0 = []
    caso_n = []
    aux = []
    rigidez_local_local = []
    rotacao = []
    rigidez_local_global = []
    diagrama_de_momento_fletor = []
    # Caso 0
    for a in range(len(comprimento)):
        tg = (temperatura[a][0] * (h[a] - cg[a]) + temperatura[a][1] * cg[a]) / h[a]
        ts = temperatura[a][0] - tg
        ti = temperatura[a][1] - tg
        if not(rotula[a][0]) and not(rotula[a][1]):
            caso_0.append(caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a])
            caso_0.append(- caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a])
        elif rotula[a][0] and not(rotula[a][1]):
            caso_0.append(0)
            caso_0.append(- 1.5 * caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a])
        elif not(rotula[a][0]) and rotula[a][1]:
            caso_0.append(1.5 * caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a])
            caso_0.append(0)
        else:
            caso_0.append(0)
            caso_0.append(0)
    # Casos n
    for a in range(len(restricoes_de_apoio) * 3):
        aux.append(0)
    for a in range(len(comprimento)):
        caso_n.append(aux.copy())
        caso_n.append(aux.copy())
    for a in range(len(comprimento)):
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
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 3] = rigidez_local_global[0][2]
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 2] = rigidez_local_global[1][2]
        caso_n[2 * (a + 1) - 2][3 * (i[a] + 1) - 1] = rigidez_local_global[2][2]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 3] = rigidez_local_global[0][5]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 2] = rigidez_local_global[1][5]
        caso_n[2 * (a + 1) - 1][3 * (i[a] + 1) - 1] = rigidez_local_global[2][5]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 3] = rigidez_local_global[3][2]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 2] = rigidez_local_global[4][2]
        caso_n[2 * (a + 1) - 2][3 * (j[a] + 1) - 1] = rigidez_local_global[5][2]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 3] = rigidez_local_global[3][5]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 2] = rigidez_local_global[4][5]
        caso_n[2 * (a + 1) - 1][3 * (j[a] + 1) - 1] = rigidez_local_global[5][5]
    for a in range(len(comprimento) * 2):
        aux = - caso_0[a]
        d = 0
        e = 0
        for b in restricoes_de_apoio:
            for c in b:
                if not(c):
                    aux = aux + deslocabilidades[d][0] * caso_n[a][e]
                    d = d + 1
                e = e + 1
        diagrama_de_momento_fletor.append(aux)
    return diagrama_de_momento_fletor


