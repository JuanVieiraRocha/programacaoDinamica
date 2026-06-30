import random as rd

def gerar_diretorias(quantidade_De_Diretorias):
    diretorias = []
    for i in range(quantidade_De_Diretorias):
        diretoria = (rd.randint(4, 12), [])
        diretorias.append(diretoria)
    return diretorias
def gerar_atividades(quantidade_De_Atividades):
    rd.seed(3)
    atividades = []
    for i in range(quantidade_De_Atividades):
        atividade = [rd.randint(1, 4), rd.randint(1, 3)]
        atividades.append(atividade)
    return atividades
def cria_tabela(linhas, colunas):
    matriz = []

    for _ in range(linhas):
        matriz.append( [0] * colunas )

    return matriz
            
diretorias = gerar_diretorias(4)
atividades = gerar_atividades(6)
tabela = cria_tabela(6, 4)
print(tabela, '\n',  diretorias, '\n', atividades)
i = 0
j = 0
for atividade in atividades:
    for diretoria in diretorias:
        horas_atividade = atividades[i][0]
        print(horas_atividade)
        peso_Atividade = atividades[i][1]
        print(peso_Atividade)
        if diretoria[0] < horas_atividade:
            tabela[i][j] = tabela[i-1][j]
        else:
            atual = peso_Atividade + tabela[i-1][j-horas_atividade]
            anterior = tabela[i -1][j]
            max(atual, anterior)
        i += 1
        j += 1
tabela[atividades, diretorias]