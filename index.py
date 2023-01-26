import entrada
import comprimento_e_angulo_de_barra
import matriz_de_rigidez
import math
# Vetores
import vetor_dos_termos_de_carga_vetores
import deslocabilidades_vetores
import diagrama_de_momento_fletor_vetores
import diagrama_de_esforco_cortante_vetores
import diagrama_de_esforco_normal_vetores
# Recalque
import vetor_dos_termos_de_carga_recalque
import deslocabilidades_recalque
import diagrama_de_momento_fletor_recalque
import diagrama_de_esforco_cortante_recalque
import diagrama_de_esforco_normal_recalque
# Temperatura
import vetor_dos_termos_de_carga_temperatura
import deslocabilidades_temperatura
import diagrama_de_momento_fletor_temperatura
import diagrama_de_esforco_cortante_temperatura
import diagrama_de_esforco_normal_temperatura


x, y, restricoes_de_apoio, cargas_nodais, i, j, rotula, carregamento, caracteristicas, recalque, h, cg, alfa, \
temperatura = entrada.exemplo_4()

comprimento, angulo = comprimento_e_angulo_de_barra.comp_ang(x, y, i, j)
print("Comprimento")
print(comprimento)
print("Angulo")
print(angulo)
print("")
print("Vetores")
matriz_de_rigidez = matriz_de_rigidez.mat_rig(x, comprimento, angulo, i, j, rotula, caracteristicas)
# Vetores
vetor_dos_termos_de_carga_vetores = vetor_dos_termos_de_carga_vetores.vet_car(x, cargas_nodais, carregamento,
                                                                              comprimento, angulo, rotula, i, j)
deslocabilidades_vetores, reacoes_vetores = deslocabilidades_vetores.desloc(restricoes_de_apoio, matriz_de_rigidez,
                                                                            vetor_dos_termos_de_carga_vetores)
print("Deslocabilidades")
print(deslocabilidades_vetores)
print("Reações de apoio")
print(reacoes_vetores)
diagrama_de_momento_fletor_vetores = diagrama_de_momento_fletor_vetores.diag_mom(carregamento, comprimento, angulo,
                                                                                 rotula, caracteristicas,
                                                                                 restricoes_de_apoio,
                                                                                 deslocabilidades_vetores, i, j)
print("Diagrama de momento fletor")
print(diagrama_de_momento_fletor_vetores)
diagrama_de_esforco_cortante_vetores = diagrama_de_esforco_cortante_vetores.diag_cort(restricoes_de_apoio, rotula,
                                                                                      carregamento, caracteristicas,
                                                                                      comprimento, angulo,
                                                                                      deslocabilidades_vetores, i, j)
diagrama_de_esforco_normal_vetores = diagrama_de_esforco_normal_vetores.diag_nor(restricoes_de_apoio, rotula,
                                                                                 carregamento, caracteristicas,
                                                                                 comprimento, angulo,
                                                                                 deslocabilidades_vetores, i, j)
diagrama_de_esforco_normal_local_vetores = []
diagrama_de_esforco_cortante_local_vetores = []
b = 0
for a in range(len(i) * 2):
    diagrama_de_esforco_normal_local_vetores.append(diagrama_de_esforco_normal_vetores[a] * math.cos(angulo[b]) +
                                                    diagrama_de_esforco_cortante_vetores[a] * math.sin(angulo[b]))
    diagrama_de_esforco_cortante_local_vetores.append(-diagrama_de_esforco_normal_vetores[a] * math.sin(angulo[b]) +
                                                      diagrama_de_esforco_cortante_vetores[a] * math.cos(angulo[b]))
    if a % 2 == 1:
        b = b + 1
print("Diagrama de esfoço normal")
print(diagrama_de_esforco_normal_local_vetores)
print("Diagrama de esfoço cortante")
print(diagrama_de_esforco_cortante_local_vetores)
# Recalque
print("")
print("Recalque")
vetor_dos_termos_de_carga_recalque = vetor_dos_termos_de_carga_recalque.vet_car(matriz_de_rigidez, recalque)
deslocabilidades_recalque, reacoes_recalque = deslocabilidades_recalque.desloc(restricoes_de_apoio, matriz_de_rigidez,
                                                                               vetor_dos_termos_de_carga_recalque)
print("Deslocabilidades")
print(deslocabilidades_recalque)
print("Reações de apoio")
print(reacoes_recalque)
diagrama_de_momento_fletor_recalque = diagrama_de_momento_fletor_recalque.diag_mom(comprimento, angulo, rotula,
                                                                                   caracteristicas, restricoes_de_apoio,
                                                                                   deslocabilidades_recalque, i, j,
                                                                                   recalque,
                                                                                   vetor_dos_termos_de_carga_recalque)
print("Diagrama de momento fletor")
print(diagrama_de_momento_fletor_recalque)
diagrama_de_esforco_cortante_recalque = diagrama_de_esforco_cortante_recalque.diag_cort(restricoes_de_apoio, rotula,
                                                                                        caracteristicas, comprimento,
                                                                                        angulo,
                                                                                        deslocabilidades_recalque, i, j,
                                                                                        recalque,
                                                                                        vetor_dos_termos_de_carga_recalque)
diagrama_de_esforco_normal_recalque = diagrama_de_esforco_normal_recalque.diag_nor(restricoes_de_apoio, rotula,
                                                                                   caracteristicas, comprimento, angulo,
                                                                                   deslocabilidades_recalque, i, j,
                                                                                   recalque,
                                                                                   vetor_dos_termos_de_carga_recalque)
diagrama_de_esforco_normal_local_recalque = []
diagrama_de_esforco_cortante_local_recalque = []
b = 0
for a in range(len(i) * 2):
    diagrama_de_esforco_normal_local_recalque.append(diagrama_de_esforco_normal_recalque[a] * math.cos(angulo[b]) +
                                                     diagrama_de_esforco_cortante_recalque[a] * math.sin(angulo[b]))
    diagrama_de_esforco_cortante_local_recalque.append(-diagrama_de_esforco_normal_recalque[a] * math.sin(angulo[b]) +
                                                       diagrama_de_esforco_cortante_recalque[a] * math.cos(angulo[b]))
    if a % 2 == 1:
        b = b + 1
print("Diagrama de esfoço normal")
print(diagrama_de_esforco_normal_local_recalque)
print("Diagrama de esfoço cortante")
print(diagrama_de_esforco_cortante_local_recalque)
# Temperatura
print("")
print("Temperatura")
vetor_dos_termos_de_carga_temperatura = vetor_dos_termos_de_carga_temperatura.vet_car(x, angulo, rotula, i, j,
                                                                                      caracteristicas, h, alfa,
                                                                                      temperatura, cg)
deslocabilidades_temperatura, reacoes_temperatura = deslocabilidades_temperatura.desloc(restricoes_de_apoio,
                                                                                        matriz_de_rigidez,
                                                                                        vetor_dos_termos_de_carga_temperatura)
print("Deslocabilidades")
print(deslocabilidades_temperatura)
print("Reações de apoio")
print(reacoes_temperatura)
diagrama_de_momento_fletor_temperatura = diagrama_de_momento_fletor_temperatura.diag_mom(comprimento, angulo, rotula,
                                                                                         caracteristicas,
                                                                                         restricoes_de_apoio,
                                                                                         deslocabilidades_temperatura,
                                                                                         h, alfa, temperatura, cg, i, j)
print("Diagrama de momento fletor")
print(diagrama_de_momento_fletor_temperatura)
diagrama_de_esforco_cortante_temperatura = diagrama_de_esforco_cortante_temperatura.diag_cort(restricoes_de_apoio,
                                                                                              rotula, caracteristicas,
                                                                                              comprimento, angulo,
                                                                                              deslocabilidades_temperatura,
                                                                                              alfa, temperatura, cg, h,
                                                                                              i, j)
diagrama_de_esforco_normal_temperatura = diagrama_de_esforco_normal_temperatura.diag_nor(restricoes_de_apoio, rotula,
                                                                                         caracteristicas, comprimento,
                                                                                         angulo,
                                                                                         deslocabilidades_temperatura,
                                                                                         alfa, temperatura, cg, h, i, j)
diagrama_de_esforco_normal_local_temperatura = []
diagrama_de_esforco_cortante_local_temperatura = []
b = 0
for a in range(len(i) * 2):
    diagrama_de_esforco_normal_local_temperatura.append(diagrama_de_esforco_normal_temperatura[a] * math.cos(angulo[b])
                                                        + diagrama_de_esforco_cortante_temperatura[a] *
                                                        math.sin(angulo[b]))
    diagrama_de_esforco_cortante_local_temperatura.append(-diagrama_de_esforco_normal_temperatura[a] *
                                                          math.sin(angulo[b]) +
                                                          diagrama_de_esforco_cortante_temperatura[a] *
                                                          math.cos(angulo[b]))
    if a % 2 == 1:
        b = b + 1
print("Diagrama de esfoço normal")
print(diagrama_de_esforco_normal_local_temperatura)
print("Diagrama de esfoço cortante")
print(diagrama_de_esforco_cortante_local_temperatura)

# Combinado
print("")
print("Combinado")
deslocabilidades = []
for a in range(len(deslocabilidades_recalque)):
    deslocabilidades.append(deslocabilidades_vetores[a][0] - deslocabilidades_recalque[a][0] -
                            deslocabilidades_temperatura[a][0])
print("Deslocabilidades")
print(deslocabilidades)
reacoes = []
for a in range(len(reacoes_temperatura)):
    reacoes.append(reacoes_vetores[a][0] + reacoes_recalque[a][0] + reacoes_temperatura[a][0])
print("Reações de apoio")
print(reacoes)
diagrama_de_momento_fletor = []
for a in range(len(diagrama_de_momento_fletor_temperatura)):
    diagrama_de_momento_fletor.append(diagrama_de_momento_fletor_vetores[a] - diagrama_de_momento_fletor_recalque[a] -
                                      diagrama_de_momento_fletor_temperatura[a])
print("Diagrama de momento fletor")
print(diagrama_de_momento_fletor)
diagrama_de_esforco_normal = []
for a in range(len(diagrama_de_momento_fletor_temperatura)):
    diagrama_de_esforco_normal.append(diagrama_de_esforco_normal_local_vetores[a] -
                                      diagrama_de_esforco_normal_local_recalque[a] -
                                      diagrama_de_esforco_normal_local_temperatura[a])
print("Diagrama de esforço normal")
print(diagrama_de_esforco_normal)
diagrama_de_esforco_cortante = []
for a in range(len(diagrama_de_momento_fletor_temperatura)):
    diagrama_de_esforco_cortante.append(diagrama_de_esforco_cortante_local_vetores[a] -
                                        diagrama_de_esforco_cortante_local_recalque[a] -
                                        diagrama_de_esforco_cortante_local_temperatura[a])
print("Diagrama de esforço cortante")
print(diagrama_de_esforco_cortante)

