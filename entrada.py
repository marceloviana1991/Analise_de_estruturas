def exemplo_1():
    # Pontos
    x = (0, 6, 8, 10, 14, 16, 19)
    y = (0, 0, 0, 0, 0, 0, 0)
    restricoes_de_apoio = (
        (True, True, False),
        (True, True, False),
        (False, False, False),
        (True, True, False),
        (True, True, False),
        (False, False, False),
        (True, True, False)
    )
    recalque = (
        (0, 0, 0),
        (0, -0.03, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, -0.021, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    cargas_nodais = (
        (0, 0, 0),
        (0, 0, 0),
        (0, -75, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, -75, 0),
        (0, 0, 0)
    )
    # Barras
    i = (0, 1, 2, 3, 4, 5)
    j = (1, 2, 3, 4, 5, 6)
    rotula = (
        (False, False),
        (False, False),
        (False, False),
        (False, False),
        (False, False),
        (False, False)
    )
    carregamento = (
        (0, -20),
        (0, -20),
        (0, -20),
        (0, -20),
        (0, -20),
        (0, -20)
    )
    # A, I, E
    caracteristicas = (
        (0.12, 0.0036, 25 * 10 ** 6),
        (0.12, 0.0036, 25 * 10 ** 6),
        (0.12, 0.0036, 25 * 10 ** 6),
        (0.12, 0.0036, 25 * 10 ** 6),
        (0.12, 0.0036, 25 * 10 ** 6),
        (0.12, 0.0036, 25 * 10 ** 6)
    )
    # Altura da seção transversal
    h = (0.6, 0.6, 0.6, 0.6, 0.6, 0.6)
    cg = (0.3, 0.3, 0.3, 0.3, 0.3, 0.3)  # Zero na aresta inferior
    alfa = (10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5)
    # Superior, inferior
    temperatura = (
        (25, 25),
        (40, 25),
        (40, 25),
        (40, 15),
        (15, 40),
        (15, 40)
    )
    return x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, temperatura


"""
 MARTHA, L. F.
 Análise de Estruturas Conceitos e Métodos Básicos.
 1 ed. Rio de Janeiro: Elsevier, 2010.
 Capítulo 8
"""


def exemplo_2():
    # Pontos
    x = (0, 3, 6, 9, 12)
    y = (0, 0, 0, 0, 0)
    restricoes_de_apoio = (
        (True, True, False),
        (False, False, False),
        (False, True, False),
        (False, False, False),
        (False, True, False)
    )
    recalque = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, -0.03, 0)
    )
    cargas_nodais = (
        (0, 0, 0),
        (0, -40, 0),
        (0, 0, 0),
        (0, -40, 0),
        (0, 0, 0)
    )
    # Barras
    i = (0, 1, 2, 3)
    j = (1, 2, 3, 4)
    rotula = (
        (False, False),
        (False, False),
        (False, False),
        (False, False)
    )
    carregamento = (
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0)
    )
    # A, I, E
    caracteristicas = (
        (0.01, 0.001, 10 ** 8),
        (0.01, 0.001, 10 ** 8),
        (0.01, 0.001, 10 ** 8),
        (0.01, 0.001, 10 ** 8)
    )
    # Altura da seção transversal
    h = (0.6, 0.6, 0.6, 0.6)
    cg = (0.3, 0.3, 0.3, 0.3)  # Zero na aresta inferior
    alfa = (10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5)
    # Superior, inferior
    temperatura = (
        (50, 0),
        (50, 0),
        (50, 0),
        (50, 0)
    )
    return x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, temperatura


def exemplo_3():
    # Pontos
    x = (0, 4, 10)
    y = (0, 3, 3)
    restricoes_de_apoio = (
        (True, True, False),
        (False, False, False),
        (True, True, False)
    )
    recalque = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    cargas_nodais = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    # Barras
    i = (0, 1)
    j = (1, 2)
    rotula = (
        (False, False),
        (False, False)
    )
    carregamento = (
        (0, 0),
        (0, 0)
    )
    # A, I, E
    caracteristicas = (
        (0.12, 3.6 * 10 ** - 3, 10 ** 8),
        (0.12, 3.6 * 10 ** - 3, 10 ** 8)
    )
    # Altura da seção transversal
    h = (0.6, 0.6)
    cg = (0.3, 0.3)  # Zero na aresta inferior
    alfa = (1.2 * 10 ** -5,1.2 * 10 ** -5)
    # Superior, inferior
    temperatura = (
        (0, 12),
        (0, 12)
    )
    return x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, temperatura


def exemplo_4():
    # Pontos
    x = (0, 0, 4)
    y = (0, 2, 2)
    restricoes_de_apoio = (
        (True, True, True),
        (False, False, False),
        (False, True, False)
    )
    recalque = (
        (0, -0.01, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    cargas_nodais = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    # Barras
    i = (0, 1)
    j = (1, 2)
    rotula = (
        (False, False),
        (False, False)
    )
    carregamento = (
        (0, 0),
        (0, 0)
    )
    # A, I, E
    caracteristicas = (
        (0.02, 5.1 * 10 ** -5, 2 * 10 ** 8),
        (0.02, 5.1 * 10 ** -5, 2 * 10 ** 8)
    )
    # Altura da seção transversal
    h = (0.6, 0.6)
    cg = (0.3, 0.3)  # Zero na aresta inferior
    alfa = (10 ** -5, 10 ** -5)
    # Superior, inferior
    temperatura = (
        (0, 0),
        (0, 0)
    )
    return x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, temperatura


def exemplo_5():
    # Pontos
    x = (0, 0, 0, 6, 6, 6)
    y = (0, 3, 6, 6, 3, 0)
    restricoes_de_apoio = (
        (False, True, False),
        (False, False, False),
        (False, False, False),
        (False, False, False),
        (False, False, False),
        (True, True, True)
    )
    recalque = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    cargas_nodais = (
        (0, 0, 0),
        (-20, 0, 0),
        (-20, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0)
    )
    # Barras
    i = (0, 1, 2, 3, 4, 1)
    j = (1, 2, 3, 4, 5, 4)
    rotula = (
        (False, False),
        (False, False),
        (False, True),
        (True, False),
        (False, False),
        (False, True)
    )
    carregamento = (
        (0, 0),
        (0, 0),
        (0, -12),
        (0, 0),
        (0, 0),
        (0, 0)
    )
    # A, I, E
    caracteristicas = (
        (0.12, 0.0016, 6 * 10 ** 7),
        (0.12, 0.0016, 6 * 10 ** 7),
        (0.12, 0.0016, 6 * 10 ** 7),
        (0.12, 0.0016, 6 * 10 ** 7),
        (0.12, 0.0016, 6 * 10 ** 7),
        (0.12, 0.0016, 6 * 10 ** 7)
    )
    # Altura da seção transversal
    h = (0.4, 0.4, 0.4, 0.4, 0.4, 0.4)
    cg = (0.3, 0.3, 0.3, 0.3, 0.3, 0.3)  # Zero na aresta inferior
    alfa = (10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5, 10 ** -5)
    # Superior, inferior
    temperatura = (
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0)
    )
    return x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, temperatura
