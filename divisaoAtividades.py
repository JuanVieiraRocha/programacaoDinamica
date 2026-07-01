import random as rd

def gerar_diretorias(quantidade_De_Diretorias):
    diretorias = []
    for i in range(quantidade_De_Diretorias):
        diretoria = [rd.randint(4, 12), []]
        diretorias.append(diretoria)
    return diretorias
def gerar_atividades(quantidade_De_Atividades):
    atividades = []
    for i in range(quantidade_De_Atividades):
        atividade = [rd.randint(1, 4), rd.randint(1, 3)]
        atividades.append(atividade)
    return atividades
def cria_tabela(linhas, colunas):
    matriz = []

    for _ in range(linhas):
        matriz.append( [0] * colunas)

    return matriz

diretoria_horas = 12

atividades = [
    [2, 8],
    [5, 3],
    [5, 9],
    [4,10],
    [8,11],
]


# diretorias = gerar_diretorias(4)
# print(diretorias)
# atividades = gerar_atividades(6)
print(atividades)
quant_atv = len(atividades)
tabela = cria_tabela(quant_atv+1, diretoria_horas+1)

# i = 0
# j = 0
for i in range(1, quant_atv+1):
    horas_atividade = atividades[i-1][0]
    peso_atividade  = atividades[i-1][1]
    for j in range(1, diretoria_horas+1):
        if horas_atividade > j:
            tabela[i][j] = tabela[i-1][j]
        else:
            tabela[i][j] = max(tabela[i-1][j], peso_atividade + tabela[i-1][j-horas_atividade])
for i in tabela:
    print(i)

horas_restantes = diretoria_horas
# print(tabela[4][12])
for i in range(quant_atv-1, -1, -1):
    if tabela[i][horas_restantes] != tabela[i+1][horas_restantes]:
        print(f"atividade escolhida:{i+1}")
        horas_restantes = horas_restantes - atividades[i][0]




#     for j in range(quant_atv):
#         horas_atividade = atividades[j][0]
#         peso_Atividade = atividades[j][1]

#         horas_diretoria = diretorias[i][0]
#         atividades_diretoria = diretorias[i][1]
#         if  horas_diretoria < horas_atividade:
#             tabela[i][j] = tabela[i-1][j]
            
#         else:
#             atual = peso_Atividade + tabela[i-1][j-horas_atividade]
#             anterior = tabela[i -1][j]
#             tabela[i][j] = max(atual, anterior)
#             diretorias[i][1].append(atividades[j])
#         # print(f'diretoria ${diretorias[i]}, recebeu a atividade ${atividades[j]}. isso custou ${horas_atividade}. Agora a diretoria tem ${diretorias[i][0]} horas \n')
#         # print(f"aq {diretorias[i][1]}")
# print(tabela[0])
# print(tabela[1])
# print(tabela[2])
# print(tabela[3])