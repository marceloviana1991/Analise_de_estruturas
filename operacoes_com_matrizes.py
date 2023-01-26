def multiplicacao(a, b):
    c = []
    matriz_aux = []
    p1 = len(a[0])
    p2 = len(b)
    if p1 != p2:
        return print("As matrizes não são multiplicaveis!")
    else:
        p = p1
        m = len(a)
        n = len(b[0])
        for i in range(m):
            for j in range(n):
                aux = 0
                for k in range(p):
                    aux = aux + a[i][k] * b[k][j]
                matriz_aux.append(aux)
            c.append(matriz_aux.copy())
            matriz_aux.clear()
        return c


def transposta(a):
    m = len(a)
    n = len(a[0])
    b = []
    vetor_aux = []
    if m < n:
        for i in range(m):
            vetor_aux.append(0)
        for i in range(n):
            b.append(vetor_aux.copy())
        for i in range(m):
            for j in range(n):
                b[j][i] = a[i][j]
        return b
    else:
        for i in range(m):
            vetor_aux.append(0)
        for i in range(n):
            b.append(vetor_aux.copy())
        for i in range(m):
            for j in range(n):
                b[j][i] = a[i][j]
        return b


def sistemas_lineares(a, b):
    c = []
    dimensao = []
    for _ in range(len(b) + 1):
        dimensao.append(0)
    for _ in range(len(b)):
        c.append(dimensao.copy())

    for i in range(len(b)):
        for j in range(len(b)):
            c[i][j] = a[i][j]
        c[i][len(b)] = b[i]

    for j in range(len(b) - 1):
        for i in range(j + 1, len(b)):
            if abs(c[j][j]) < abs(c[i][j]):
                for s in range(len(b) + 1):
                    aux = c[j][s]
                    c[j][s] = c[i][s]
                    c[i][s] = aux
        for i in range(j + 1, len(b)):
            if not(c[i][j] == 0) and not(c[j][j] == 0):
                m = -c[i][j] / c[j][j]
            else:
                m = 0
            for s in range(len(b) + 1):
                c[i][s] = c[i][s] + m * c[j][s]
    x = []
    for i in range(len(b)):
        x.append([0])
    for i in range(len(b) - 1, -1, -1):
        aux = 0
        for j in range(len(b) - 1, i, -1):
            aux = aux + c[i][j] * x[j][0]
        if not(c[i][i] == 0) and not((c[i][len(b)] - aux) == 0):
            x[i][0] = (c[i][len(b)] - aux) / c[i][i]
        else:
            x[i][0] = 0
    return x
