def comp_ang(x, y, i, j):
    import math
    comprimento = []
    angulo = []
    for a in range(len(i)):
        # Cálculo do comprimento da barra
        comprimento.append(math.sqrt((x[j[a]] - x[i[a]]) ** 2 + (y[j[a]] - y[i[a]]) ** 2))
        # Cálculo da inclunação da barra
        if (y[j[a]] - y[i[a]]) < 0:
            angulo.append(math.asin((y[j[a]] - y[i[a]]) / comprimento[a]))
        else:
            angulo.append(math.acos((x[j[a]] - x[i[a]]) / comprimento[a]))
    comprimento = tuple(comprimento)
    angulo = tuple(angulo)
    return comprimento, angulo
