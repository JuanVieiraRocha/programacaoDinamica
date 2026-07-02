import random as rd


def gerar_diretorias(quantidade_de_diretorias, pessoas_por_diretoria=4, horas_por_pessoa=4):
    diretorias = []
    for _ in range(quantidade_de_diretorias):
        capacidade = pessoas_por_diretoria * horas_por_pessoa
        diretorias.append([capacidade, []])
    return diretorias


def gerar_atividades(quantidade_de_atividades, horas_minima=1, horas_maxima=4):
    atividades = []
    for _ in range(quantidade_de_atividades):
        atividade = [rd.randint(horas_minima, horas_maxima), 1]
        atividades.append(atividade)
    return atividades


def cria_tabela(linhas, colunas):
    return [[0] * colunas for _ in range(linhas)]


def selecionar_atividades(atividades, capacidade):
    quant_atv = len(atividades)
    tabela = cria_tabela(quant_atv + 1, capacidade + 1)

    for i in range(1, quant_atv + 1):
        horas_atividade = atividades[i - 1][0]
        valor_atividade = atividades[i - 1][1]
        for j in range(1, capacidade + 1):
            if horas_atividade > j:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = max(
                    tabela[i - 1][j],
                    valor_atividade + tabela[i - 1][j - horas_atividade],
                )

    horas_restantes = capacidade
    atividades_escolhidas = []

    for i in range(quant_atv - 1, -1, -1):
        if tabela[i][horas_restantes] != tabela[i + 1][horas_restantes]:
            atividade = atividades[i]
            atividades_escolhidas.append(atividade)
            horas_restantes -= atividade[0]

    atividades_escolhidas.reverse()
    return tabela, tabela[quant_atv][capacidade], atividades_escolhidas


def distribuir_atividades_equilibradas(atividades, capacidades):
    diretorias = []
    for capacidade in capacidades:
        diretorias.append([0, []])

    atividades_ordenadas = sorted(atividades, key=lambda item: (-item[0], item[1]))

    for atividade in atividades_ordenadas:
        horas_atividade = atividade[0]
        melhor_indice = None
        melhor_score = None

        for indice, diretoria in enumerate(diretorias):
            horas_usadas = diretoria[0]
            if horas_usadas + horas_atividade <= capacidades[indice]:
                cargas_futuras = [d[0] for d in diretorias]
                cargas_futuras[indice] += horas_atividade
                score = (max(cargas_futuras) - min(cargas_futuras), max(cargas_futuras), indice)

                if melhor_score is None or score < melhor_score:
                    melhor_score = score
                    melhor_indice = indice

        if melhor_indice is not None:
            diretorias[melhor_indice][0] += horas_atividade
            diretorias[melhor_indice][1].append(atividade)

    return diretorias


# Cada diretoria tem 3 pessoas e cada pessoa cede 4 horas -> 12 horas de capacidade
pessoas_por_diretoria = 3
horas_por_pessoa = 4
quantidade_de_diretorias = 2

capacidades = [pessoas_por_diretoria * horas_por_pessoa] * quantidade_de_diretorias

# Atividades de exemplo: cada atividade tem custo em horas e valor 1 (para maximizar a quantidade)
atividades = [
    [2, 1],
    [5, 1],
    [5, 1],
    [4, 1],
    [3, 1],
    [1, 1],
    [2, 1],
    [4, 1],
]

print("Atividades disponíveis:", atividades)

resultado = distribuir_atividades_equilibradas(atividades, capacidades)

for indice, diretoria in enumerate(resultado, start=1):
    capacidade = capacidades[indice - 1]
    horas_usadas = diretoria[0]
    atividades_alocadas = diretoria[1]
    tabela, quantidade_maxima, atividades_escolhidas = selecionar_atividades(atividades_alocadas, capacidade)

    print(f"Diretoria {indice}: capacidade = {capacidade} horas")
    print(f"Horas usadas = {horas_usadas}")
    print(f"Quantidade máxima de atividades = {quantidade_maxima}")
    print(f"Atividades alocadas = {atividades_alocadas}")
    print("Tabela da mochila:")
    for linha_idx, linha in enumerate(tabela):
        print(f"{linha_idx}: {linha}")
    print()

cargas = [diretoria[0] for diretoria in resultado]
print("Carga final das diretorias:", cargas)
print("Diferença de horas entre as diretorias:", max(cargas) - min(cargas))
