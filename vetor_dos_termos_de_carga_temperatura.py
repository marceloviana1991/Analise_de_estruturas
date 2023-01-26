def vet_car(x, angulo, rotula, i, j, caracteristicas, h, alfa, temperatura, cg):
    import math
    vetor_local = [0, 0, 0, 0, 0, 0]
    vetor_dos_termos_de_carga = []
    for a in range(len(x) * 3):
        vetor_dos_termos_de_carga.append([0])
    for a in range(len(i)):
        tg = (temperatura[a][0] * (h[a] - cg[a]) + temperatura[a][1] * cg[a]) / h[a]
        ts = temperatura[a][0] - tg
        ti = temperatura[a][1] - tg
        # Cálculo do vetor dos termos de carga local
        if not(rotula[a][0]) and not(rotula[a][1]):
            vetor_local[0] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[1] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[2] = caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a]
            vetor_local[3] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[4] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[5] = - caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a]
        elif rotula[a][0] and not(rotula[a][1]):
            vetor_local[0] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[1] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[2] = 0
            vetor_local[3] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[4] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[5] = - 1.5 * caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a]
        elif not(rotula[a][0]) and rotula[a][1]:
            vetor_local[0] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[1] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[2] = 1.5 * caracteristicas[a][2] * caracteristicas[a][1] * alfa[a] * (ti - ts) / h[a]
            vetor_local[3] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[4] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[5] = 0
        elif rotula[a][0] and rotula[a][1]:
            vetor_local[0] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[1] = caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
            vetor_local[2] = 0
            vetor_local[3] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.cos(angulo[a])
            vetor_local[4] = - caracteristicas[a][2] * caracteristicas[a][0] * alfa[a] * tg * math.sin(angulo[a])
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
    return vetor_dos_termos_de_carga
