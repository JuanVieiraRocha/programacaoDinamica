import random as rd

def gerar_diretorias(quantidade_De_Diretorias):
    diretorias = []
    for i in range(quantidade_De_Diretorias):
        diretoria = (rd.randint(4, 12), [])
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
        matriz.append( [0] * colunas )

    return matriz
            
diretorias = gerar_diretorias(4)
atividades = gerar_atividades(6)
tabela = cria_tabela(4, 6)
i = 0
j = 0
for i in range(3):
    for j in range(6):
        horas_atividade = atividades[j][0]
        peso_Atividade = atividades[j][1]

        horas_diretoria = diretorias[i][0]
        atividades_diretoria = diretorias[i][1]
        if  horas_diretoria < horas_atividade:
            tabela[i][j] = tabela[i-1][j]
            
        else:
            atual = peso_Atividade + tabela[i-1][j-horas_atividade]
            anterior = tabela[i -1][j]
            tabela[i][j] = max(atual, anterior)
            diretorias[i][1].append(atividades[j])
        print(f'diretoria ${diretorias[i]}, recebeu a atividade ${atividades[j]}. isso custou ${horas_atividade}. Agora a diretoria tem ${diretorias[i][0]} horas \n')
        print(diretorias[i][1])
print(tabela[0])
print(tabela[1])
print(tabela[2])
print(tabela[3])