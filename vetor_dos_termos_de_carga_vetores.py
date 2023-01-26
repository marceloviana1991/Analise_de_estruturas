def vet_car(x, cargas_nodais, carregamento, comprimento, angulo, rotula, i, j):
    import math
    cargas = []
    vetor_local = [0, 0, 0, 0, 0, 0]
    vetor_dos_termos_de_carga = []
    carregamento_local = []
    for a in range(len(i)):
        carregamento_local.append([0, 0])
    # Conversão dos carregamentos que atuam nas barras para o sistema de coordenadas locais
    for a in range(len(i)):
        carregamento_local[a][0] = carregamento[a][0] * math.cos(angulo[a]) + carregamento[a][1] * math.sin(angulo[a])
        carregamento_local[a][1] = -carregamento[a][0] * math.sin(angulo[a]) + carregamento[a][1] * math.cos(angulo[a])
    # Dimensionamento do vetor dos termos de carga
    for a in range(len(x * 3)):
        vetor_dos_termos_de_carga.append([0])
    # Locação das cargas nodais em um pseudo vetor dos termos de carga
    for a in cargas_nodais:
        for b in a:
            cargas.append(b)
    for a in range(len(i)):
        # Cálculo do vetor dos termos de carga local
        if not(rotula[a][0]) and not(rotula[a][1]):
            vetor_local[0] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) -\
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.sin(angulo[a])
            vetor_local[1] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) +\
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.cos(angulo[a])
            vetor_local[2] = (carregamento_local[a][1] * comprimento[a] ** 2) / 12
            vetor_local[3] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) -\
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.sin(angulo[a])
            vetor_local[4] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) +\
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.cos(angulo[a])
            vetor_local[5] = -(carregamento_local[a][1] * comprimento[a] ** 2) / 12
        elif rotula[a][0] and not(rotula[a][1]):
            vetor_local[0] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((3 * carregamento_local[a][1] * comprimento[a]) / 8) * math.sin(angulo[a])
            vetor_local[1] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((3 * carregamento_local[a][1] * comprimento[a]) / 8) * math.cos(angulo[a])
            vetor_local[2] = 0
            vetor_local[3] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((5 * carregamento_local[a][1] * comprimento[a]) / 8) * math.sin(angulo[a])
            vetor_local[4] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((5 * carregamento_local[a][1] * comprimento[a]) / 8) * math.cos(angulo[a])
            vetor_local[5] = -(carregamento_local[a][1] * comprimento[a] ** 2) / 8
        elif not(rotula[a][0]) and rotula[a][1]:
            vetor_local[0] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((5 * carregamento_local[a][1] * comprimento[a]) / 8) * math.sin(angulo[a])
            vetor_local[1] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((5 * carregamento_local[a][1] * comprimento[a]) / 8) * math.cos(angulo[a])
            vetor_local[2] = (carregamento_local[a][1] * comprimento[a] ** 2) / 8
            vetor_local[3] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((3 * carregamento_local[a][1] * comprimento[a]) / 8) * math.sin(angulo[a])
            vetor_local[4] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((3 * carregamento_local[a][1] * comprimento[a]) / 8) * math.cos(angulo[a])
            vetor_local[5] = 0
        elif rotula[a][0] and rotula[a][1]:
            vetor_local[0] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.sin(angulo[a])
            vetor_local[1] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.cos(angulo[a])
            vetor_local[2] = 0
            vetor_local[3] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.cos(angulo[a]) - \
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.sin(angulo[a])
            vetor_local[4] = ((carregamento_local[a][0] * comprimento[a]) / 2) * math.sin(angulo[a]) + \
                             ((carregamento_local[a][1] * comprimento[a]) / 2) * math.cos(angulo[a])
            vetor_local[5] = 0
        # Locação do vetor dos termos de carga local no vetor dos termos de carga global
        vetor_dos_termos_de_carga[3 * (i[a] + 1) - 3][0] = vetor_local[0] + \
                                                           vetor_dos_termos_de_carga[3 * (i[a] + 1) - 3][0]
        vetor_dos_termos_de_carga[3 * (i[a] + 1) - 2][0] = vetor_local[1] + \
                                                           vetor_dos_termos_de_carga[3 * (i[a] + 1) - 2][0]
        vetor_dos_termos_de_carga[3 * (i[a] + 1) - 1][0] = vetor_local[2] + \
                                                           vetor_dos_termos_de_carga[3 * (i[a] + 1) - 1][0]
        vetor_dos_termos_de_carga[3 * (j[a] + 1) - 3][0] = vetor_local[3] + \
                                                           vetor_dos_termos_de_carga[3 * (j[a] + 1) - 3][0]
        vetor_dos_termos_de_carga[3 * (j[a] + 1) - 2][0] = vetor_local[4] + \
                                                           vetor_dos_termos_de_carga[3 * (j[a] + 1) - 2][0]
        vetor_dos_termos_de_carga[3 * (j[a] + 1) - 1][0] = vetor_local[5] + \
                                                           vetor_dos_termos_de_carga[3 * (j[a] + 1) - 1][0]
    # Soma do pseudo vetor com o vetor dos termos de carga
    for a in range(len(x * 3)):
        vetor_dos_termos_de_carga[a][0] = vetor_dos_termos_de_carga[a][0] + cargas[a]
    return vetor_dos_termos_de_carga
