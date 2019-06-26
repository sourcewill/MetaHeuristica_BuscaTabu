# Matriz quadrada com 11 cidades e as distâncias entre elas
cities1 = [
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],
    [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13],
    [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 25],
    [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22],
    [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 37],
    [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 84],
    [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 13],
    [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18],
    [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 38],
    [18, 12, 13, 25, 22, 37, 84, 13, 18, 38, 0]
]

# Matriz quadrada com 30 cidades e as distâncias entre elas
cities2 = [
    [0, 36, 96, 83, 62, 75, 84, 45, 69, 33, 36, 66, 53, 100, 1, 6, 10, 41, 89, 90, 4, 77, 7, 85, 83, 86, 58, 24, 98, 22], 
    [36, 0, 53, 26, 60, 94, 21, 30, 39, 8, 92, 82, 65, 77, 81, 68, 16, 16, 5, 17, 99, 97, 1, 56, 72, 21, 87, 86, 53, 83], 
    [96, 53, 0, 34, 85, 34, 75, 99, 7, 3, 71, 66, 4, 80, 100, 75, 68, 27, 53, 72, 22, 83, 77, 11, 46, 62, 20, 5, 60, 51], 
    [83, 26, 34, 0, 49, 8, 98, 92, 92, 40, 75, 71, 85, 54, 30, 64, 87, 24, 45, 12, 28, 85, 93, 95, 23, 69, 44, 35, 73, 25], 
    [62, 60, 85, 49, 0, 3, 19, 6, 88, 55, 88, 65, 72, 95, 44, 59, 96, 62, 52, 51, 96, 54, 17, 31, 33, 99, 46, 46, 70, 21], 
    [75, 94, 34, 8, 3, 0, 16, 10, 80, 21, 70, 80, 37, 33, 16, 69, 77, 62, 89, 77, 77, 17, 49, 65, 87, 68, 12, 67, 62, 47], 
    [84, 21, 75, 98, 19, 16, 0, 65, 9, 73, 29, 64, 75, 68, 85, 7, 57, 65, 47, 26, 96, 46, 46, 79, 2, 41, 50, 77, 80, 85], 
    [45, 30, 99, 92, 6, 10, 65, 0, 4, 66, 29, 97, 98, 19, 84, 66, 5, 34, 99, 31, 91, 64, 57, 14, 59, 43, 55, 59, 26, 18], 
    [69, 39, 7, 92, 88, 80, 9, 4, 0, 79, 61, 84, 59, 22, 19, 70, 84, 19, 45, 27, 46, 85, 43, 74, 30, 94, 60, 52, 99, 24], 
    [33, 8, 3, 40, 55, 21, 73, 66, 79, 0, 95, 42, 85, 77, 47, 86, 81, 77, 78, 93, 32, 73, 7, 58, 79, 54, 47, 60, 76, 11], 
    [36, 92, 71, 75, 88, 70, 29, 29, 61, 95, 0, 78, 63, 6, 77, 20, 62, 7, 35, 43, 7, 34, 59, 9, 31, 85, 74, 44, 59, 73], 
    [66, 82, 66, 71, 65, 80, 64, 97, 84, 42, 78, 0, 74, 63, 87, 87, 69, 16, 9, 23, 56, 90, 78, 55, 99, 30, 50, 23, 91, 82], 
    [53, 65, 4, 85, 72, 37, 75, 98, 59, 85, 63, 74, 0, 84, 46, 34, 38, 87, 38, 58, 74, 64, 20, 19, 3, 1, 5, 88, 97, 76], 
    [100, 77, 80, 54, 95, 33, 68, 19, 22, 77, 6, 63, 84, 0, 43, 72, 36, 98, 69, 45, 88, 40, 68, 4, 5, 70, 52, 16, 81, 11], 
    [1, 81, 100, 30, 44, 16, 85, 84, 19, 47, 77, 87, 46, 43, 0, 62, 32, 82, 71, 56, 59, 75, 55, 86, 27, 82, 5, 100, 6, 62], 
    [6, 68, 75, 64, 59, 69, 7, 66, 70, 86, 20, 87, 34, 72, 62, 0, 42, 24, 2, 70, 70, 83, 98, 90, 96, 51, 51, 21, 63, 85], 
    [10, 16, 68, 87, 96, 77, 57, 5, 84, 81, 62, 69, 38, 36, 32, 42, 0, 27, 23, 95, 14, 61, 49, 76, 60, 28, 62, 95, 17, 98], 
    [41, 16, 27, 24, 62, 62, 65, 34, 19, 77, 7, 16, 87, 98, 82, 24, 27, 0, 84, 13, 20, 8, 52, 20, 47, 71, 1, 48, 54, 40], 
    [89, 5, 53, 45, 52, 89, 47, 99, 45, 78, 35, 9, 38, 69, 71, 2, 23, 84, 0, 24, 14, 49, 45, 18, 32, 40, 48, 14, 78, 26], 
    [90, 17, 72, 12, 51, 77, 26, 31, 27, 93, 43, 23, 58, 45, 56, 70, 95, 13, 24, 0, 90, 70, 42, 1, 47, 77, 65, 32, 9, 100], 
    [4, 99, 22, 28, 96, 77, 96, 91, 46, 32, 7, 56, 74, 88, 59, 70, 14, 20, 14, 90, 0, 85, 4, 86, 2, 25, 73, 100, 57, 62],
    [77, 97, 83, 85, 54, 17, 46, 64, 85, 73, 34, 90, 64, 40, 75, 83, 61, 8, 49, 70, 85, 0, 33, 98, 31, 51, 33, 62, 93, 17],
    [7, 1, 77, 93, 17, 49, 46, 57, 43, 7, 59, 78, 20, 68, 55, 98, 49, 52, 45, 42, 4, 33, 0, 60, 40, 18, 8, 54, 14, 72],
    [85, 56, 11, 95, 31, 65, 79, 14, 74, 58, 9, 55, 19, 4, 86, 90, 76, 20, 18, 1, 86, 98, 60, 0, 70, 49, 39, 1, 68, 53],
    [83, 72, 46, 23, 33, 87, 2, 59, 30, 79, 31, 99, 3, 5, 27, 96, 60, 47, 32, 47, 2, 31, 40, 70, 0, 64, 35, 28, 85, 65], 
    [86, 21, 62, 69, 99, 68, 41, 43, 94, 54, 85, 30, 1, 70, 82, 51, 28, 71, 40, 77, 25, 51, 18, 49, 64, 0, 24, 69, 61, 98], 
    [58, 87, 20, 44, 46, 12, 50, 55, 60, 47, 74, 50, 5, 52, 5, 51, 62, 1, 48, 65, 73, 33, 8, 39, 35, 24, 0, 93, 49, 62], 
    [24, 86, 5, 35, 46, 67, 77, 59, 52, 60, 44, 23, 88, 16, 100, 21, 95, 48, 14, 32, 100, 62, 54, 1, 28, 69, 93, 0, 1, 5], 
    [98, 53, 60, 73, 70, 62, 80, 26, 99, 76, 59, 91, 97, 81, 6, 63, 17, 54, 78, 9, 57, 93, 14, 68, 85, 61, 49, 1, 0, 30],
    [22, 83, 51, 25, 21, 47, 85, 18, 24, 11, 73, 82, 76, 11, 62, 85, 98, 40, 26, 100, 62, 17, 72, 53, 65, 98, 62, 5, 30, 0]
]

#---------------------------------------------------------------------------------------------------

# Retorna o indice do elemento anterior em um vetor circular
# Tendo como base o indice atual
def anterior_vet_circular(indice_atual, tam_vet):
    indice_anterior = indice_atual - 1
    if indice_anterior < 0:
        indice_anterior = tam_vet - 1
    return indice_anterior

#---------------------------------------------------------------------------------------------------

# Retorna o indice do próximo elemento em um vetor circular
# Tendo como base o indice atual
def proximo_vet_circular(indice_atual, tam_vet):
    indice_proximo = indice_atual + 1
    if indice_proximo == tam_vet:
        indice_proximo = 0
    return indice_proximo

#---------------------------------------------------------------------------------------------------

# Retorna o custo de um dado caminho no grafo, tendo como base sua matriz de adj
def calcula_custo_caminho(caminho, matriz_adj):
    distancia_total = 0
    for i in range(len(caminho)-1):
        distancia_total += matriz_adj[caminho[i]][caminho[i+1]]
    return distancia_total

#---------------------------------------------------------------------------------------------------

# Heurística: Vizinho mais próximo
def greedy_closest_neighbor(matriz_adj, initial=0):
    # Inicializa a rota com a cidade inicial e a distancia total com zero
    current = initial
    route = [current]
    total_distance = 0

    # Repita para o número de cidades - 1
    # A primeira cidade já foi adicionada na rota
    for _ in range(len(matriz_adj) - 1):

        # Pega a linha da matriz que representa os vizinhos da cidade atual (current)
        neighbours = matriz_adj[current]

        # Inicializa a menor distância com infinito
        best_neighbour = None
        best_distance = float("inf")

        # Para cada cidade vizinha da cidade corrente
        for idx in range(len(neighbours)):

            # Pega a distância da cidade atual para a cidade vizinha
            distance = neighbours[idx]

            # Se a cidade ainda não foi visitada e
            #  sua distância for maior que zero e
            #  sua distância for menor que a menor distância até o momento
            # então atualiza a cidade mais próxima da atual
            if idx not in route and distance > 0 and distance < best_distance:
                best_neighbour = idx
                best_distance = distance

        # Atualiza a cidade atual para o vizinho mais próxima
        # Adiciona o vizinho na rota e incrementa a distância total
        current = best_neighbour
        route.append(current)
        total_distance += best_distance

    # Ao final, conectar a última cidade na primeira cidade
    route.append(initial)
    total_distance += matriz_adj[current][initial]

    return (total_distance, route)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais próxima
def greedy_closest_insertion(matriz_adj):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(matriz_adj) - 3):

        vizinho_mais_proximo = None
        cidade_vizinho_mais_proximo = None
        melhor_distancia = float("inf")

        # Para cada cidade no ciclo:
        # Encontra o vizinho mais proximo de qualquer vértice do ciclo
        for indice_atual, cidade in enumerate(ciclo):

            # Para cada vizinho da cidade atual
            vizinhos = matriz_adj[cidade]
            for i in range(len(vizinhos)):

                distancia = vizinhos[i]

                if i not in ciclo and distancia > 0 and distancia < melhor_distancia:
                    cidade_vizinho_mais_proximo = cidade # Cidade que tem o vizinho mais próximo
                    indice_cidade_vizinho_mais_proximo = indice_atual # Indice no ciclo da cidade que tem o vizinho mais próximo
                    vizinho_mais_proximo = i # Vizinho mais próximo de todos os vértices do ciclo
                    melhor_distancia = distancia # Distancia do vizinho mais próximo

        # Encontra os índices no ciclo das cidades (anteriro e próxima)
        indice_anterior = anterior_vet_circular(indice_cidade_vizinho_mais_proximo, len(ciclo))
        indice_proximo = proximo_vet_circular(indice_cidade_vizinho_mais_proximo, len(ciclo))

        # Calcula o peso de adicionar o vértice na cidade anterior e próxima
        # Custo(V atual-->Vi) + Custo(Vi-->Vj) - Custo(V atual-->Vj)
        peso_anterior = matriz_adj[cidade_vizinho_mais_proximo][vizinho_mais_proximo] + matriz_adj[vizinho_mais_proximo][ciclo[indice_anterior]] - matriz_adj[cidade_vizinho_mais_proximo][ciclo[indice_anterior]]
        peso_proxima = matriz_adj[cidade_vizinho_mais_proximo][vizinho_mais_proximo] + matriz_adj[vizinho_mais_proximo][ciclo[indice_proximo]] - matriz_adj[cidade_vizinho_mais_proximo][ciclo[indice_proximo]]

        # Insere o vértice no ciclo onde for menos custoso
        if peso_anterior < peso_proxima:
            ciclo.insert(indice_anterior + 1, vizinho_mais_proximo)
        else:
            ciclo.insert(indice_cidade_vizinho_mais_proximo + 1, vizinho_mais_proximo)

    # Insere e completa o ciclo com o vértice inicial
    ciclo.append(ciclo[0])

    # Calcula a distancia
    distancia_total = calcula_custo_caminho(ciclo, matriz_adj)

    return (distancia_total, ciclo)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais distante
def greedy_further_insertion(matriz_adj):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(matriz_adj) - 3):

        vizinho_mais_distante = None
        cidade_vizinho_mais_distante = None
        maior_distancia = float("-inf")

        # Para cada cidade no ciclo:
        # Encontra o vizinho mais distante de qualquer vértice do ciclo
        for indice_atual, cidade in enumerate(ciclo):

            # Para cada vizinho da cidade atual
            vizinhos = matriz_adj[cidade]
            for i in range(len(vizinhos)):

                distancia = vizinhos[i]

                if i not in ciclo and distancia > 0 and distancia > maior_distancia:
                    cidade_vizinho_mais_distante = cidade # Cidade que tem o vizinho mais distante
                    indice_cidade_vizinho_mais_distante = indice_atual # Indice no ciclo da cidade que tem o vizinho mais distante
                    vizinho_mais_distante = i # Vizinho mais distante de todos os vértices do ciclo
                    maior_distancia = distancia # Distancia do vizinho mais distante

        # Encontra os índices no ciclo das cidades (anteriro e próxima)
        indice_anterior = anterior_vet_circular(indice_cidade_vizinho_mais_distante, len(ciclo))
        indice_proximo = proximo_vet_circular(indice_cidade_vizinho_mais_distante, len(ciclo))

        # Calcula o peso de adicionar o vértice na cidade anterior e próxima
        # Custo(V atual-->Vi) + Custo(Vi-->Vj) - Custo(V atual-->Vj)
        peso_anterior = matriz_adj[cidade_vizinho_mais_distante][vizinho_mais_distante] + matriz_adj[vizinho_mais_distante][ciclo[indice_anterior]] - matriz_adj[cidade_vizinho_mais_distante][ciclo[indice_anterior]]
        peso_proxima = matriz_adj[cidade_vizinho_mais_distante][vizinho_mais_distante] + matriz_adj[vizinho_mais_distante][ciclo[indice_proximo]] - matriz_adj[cidade_vizinho_mais_distante][ciclo[indice_proximo]]

        # Insere o vértice no ciclo onde for menos custoso
        if peso_anterior < peso_proxima:
            ciclo.insert(indice_anterior + 1, vizinho_mais_distante)
        else:
            ciclo.insert(indice_cidade_vizinho_mais_distante + 1, vizinho_mais_distante)

    # Insere e completa o ciclo com o vértice inicial
    ciclo.append(ciclo[0])

    # Calcula a distancia total
    distancia_total = calcula_custo_caminho(ciclo, matriz_adj)

    return (distancia_total, ciclo)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais barata
def greedy_cheapest_insertion(matriz_adj):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(matriz_adj) - 3):

        melhor_peso = float("inf")

        # Para cada cidade no ciclo
        for indice_atual, cidade in enumerate(ciclo):      

            # Encontra os índices no ciclo das cidades (anteriro e próxima)
            indice_anterior = anterior_vet_circular(indice_atual, len(ciclo))
            indice_proximo = proximo_vet_circular(indice_atual, len(ciclo))
            
            cidade_anterior = ciclo[indice_anterior]
            cidade_proxima = ciclo[indice_proximo]

            # Para cada "i" vizinho da cidade atual que ainda não está no ciclo
            vizinhos = matriz_adj[cidade]
            for i in range(len(vizinhos)):
                if i not in ciclo:

                    # Calcula o peso para inserir a cidade entre a anterior e a próxima
                    peso_anterior = matriz_adj[cidade][i] + matriz_adj[i][cidade_anterior] - matriz_adj[cidade][cidade_anterior]
                    peso_proxima = matriz_adj[cidade][i] + matriz_adj[i][cidade_proxima] - matriz_adj[cidade][cidade_proxima]

                    if peso_anterior < peso_proxima:
                        # Atualiza a melhor solução encontrada
                        if peso_anterior < melhor_peso:
                            melhor_peso = peso_anterior
                            cidade_inserir = i
                            melhor_sub_caminho = [cidade_anterior, i, cidade] # Usado apenas para print
                            indice_inserir = indice_anterior + 1
                    else:
                        # Atualiza a melhor solução encontrada
                        if peso_proxima < melhor_peso:
                            melhor_peso = peso_proxima    
                            cidade_inserir = i                    
                            melhor_sub_caminho = [cidade, i, cidade_proxima] # Usado apenas para print
                            indice_inserir = indice_atual + 1

        # Insere o vértice com menor custo encontrado
        ciclo.insert(indice_inserir, cidade_inserir)                

    # Insere e completa o ciclo com o vértice inicial
    ciclo.append(ciclo[0])

    # Calcula a distancia total
    distancia_total = calcula_custo_caminho(ciclo, matriz_adj)

    return (distancia_total, ciclo)

#---------------------------------------------------------------------------------------------------

# Gera a vizinhança de um atual estado, realizando trocas de elementos consecutivos
def vizinhanca_troca_consecutivos(solucao_atual):

    tam_vet = len(solucao_atual)
    vizinhanca = []

    for i in range(tam_vet-1):

        vetor_aux = solucao_atual[:]
        temp = vetor_aux[i+1]
        vetor_aux[i+1] = vetor_aux[i]
        vetor_aux[i] = temp

        #Trata vetor circular
        if i == 0:
            vetor_aux[tam_vet-1] = vetor_aux[0]

        if i == tam_vet-2:
            vetor_aux[0] = vetor_aux[tam_vet-1]

        vizinhanca.append(vetor_aux)

    return vizinhanca

#---------------------------------------------------------------------------------------------------

# Gera a vizinhança de um atual estado, realizando trocas de dois elementos quaisquer
def vizinhanca_troca_dois_quaisquer(solucao_atual):

    tam_vet = len(solucao_atual)
    vizinhanca = []

    for i in range(tam_vet-1):
        for j in range(tam_vet-1):
            if i != j:
                vetor_aux = solucao_atual[:]
                temp = vetor_aux[i]
                vetor_aux[i] = vetor_aux[j]
                vetor_aux[j] = temp

                #Trata vetor circular
                if i == 0 or j == 0:
                    vetor_aux[tam_vet-1] = vetor_aux[0]
                
                if vetor_aux not in vizinhanca:
                    vizinhanca.append(vetor_aux)

    return vizinhanca

#---------------------------------------------------------------------------------------------------

# Gera a vizinhança de um atual estado, realizando trocas de três elementos quaisquer
def vizinhanca_troca_tres_quaisquer(solucao_atual):

    tam_vet = len(solucao_atual)
    vizinhanca = []

    for i in range(tam_vet-1):
        for j in range(tam_vet-1):
            for k in range(tam_vet-1):
                if i != j != k != i:
                    vetor_aux = solucao_atual[:]
                    temp = vetor_aux[i]
                    vetor_aux[i] = vetor_aux[j]
                    vetor_aux[j] = vetor_aux[k]
                    vetor_aux[k] = temp

                    #Trata vetor circular
                    if i == 0 or j == 0 or k == 0:
                        vetor_aux[tam_vet-1] = vetor_aux[0]

                    if vetor_aux not in vizinhanca:
                        vizinhanca.append(vetor_aux)

    return vizinhanca

#---------------------------------------------------------------------------------------------------

# Meta-Heurística: Busca Tabu

# solucao_inicial : Solução inicial válida (gerada por uma heurística)
# matriz_adj : Matriz de adj de um grafo completo
# BTMax : Critério de parada por estagnação (número de interações sem melhorara na solução)
# tam_lista_tabu : Tamanho máximo que a lista tabu pode atingir

def busca_tabu(solucao_inicial, matriz_adj, BTMax, tam_lista_tabu):

    print("\n\nExecutando Busca Tabu...")

    solucao_atual = solucao_inicial
    melhor_solucao = solucao_atual
    custo_melhor_solucao = calcula_custo_caminho(melhor_solucao, matriz_adj)
    interacao = 0
    melhor_interacao = 0
    lista_tabu = []

    while((interacao - melhor_interacao) <= BTMax):
        
        interacao += 1
        melhor_custo_atual = float("inf")

        #Enocntra o melhor vizinho da solução e que não está na lista tabu
        vizinhanca = vizinhanca_troca_dois_quaisquer(solucao_atual)
        for vizinho in vizinhanca:
            if vizinho not in lista_tabu:
                custo_vizinho = calcula_custo_caminho(vizinho, matriz_adj)
                if custo_vizinho < melhor_custo_atual:
                    melhor_custo_atual = custo_vizinho
                    melhor_vizinho = vizinho

        # Controle do tamanho da lista tabu
        if len(lista_tabu) == tam_lista_tabu:
            lista_tabu.pop(0)
        lista_tabu.append(solucao_atual)

        solucao_atual = melhor_vizinho

        if melhor_custo_atual < custo_melhor_solucao:
            melhor_solucao = solucao_atual
            custo_melhor_solucao = melhor_custo_atual
            melhor_interacao = interacao
            print("Melhor custo ate o momento:", custo_melhor_solucao)        

    return (custo_melhor_solucao, melhor_solucao)

#---------------------------------------------------------------------------------------------------

# Executando Heurísticas
print("\nVizinho mais próximo:\n", greedy_closest_neighbor(cities1))
print("Inserção mais próxima:\n", greedy_closest_insertion(cities1))
print("Inserção mais distante:\n", greedy_further_insertion(cities1))
print("Inserção mais barata:\n", greedy_cheapest_insertion(cities1))

# Executando métodos de geração de vizinhança
#print("\n\nVizinhança (Troca de consecutivos)\n", vizinhanca_troca_consecutivos([1, 2, 3, 4, 1]))
#print("\n\nVizinhança (Troca de dois quaisquer)\n", vizinhanca_troca_dois_quaisquer([1, 2, 3, 4, 1]))
#print("\n\nVizinhança (Troca de tres quaisquer)\n", vizinhanca_troca_tres_quaisquer([1, 2, 3, 4, 1]))

# Gerando solução inicial com uma Heurística para usar na Busca Tabu
solucao_inicial = greedy_cheapest_insertion(cities1)[1]

# Executando Busca Tabu (Meta-Heurística)
print("\nBusca Tabu:\n", busca_tabu(solucao_inicial, cities1, 10, 5))

#---------------------------------------------------------------------------------------------------

# MELHORES RESULTADOS ECONTRADOS:

# cities1 (11 cidades) | BTMax = 10 | tam_lista_tabu = 5
# (253, [0, 8, 10, 1, 6, 2, 5, 9, 3, 4, 7, 0])

# cities2 (30 cidades) | BTMax = 1000 | tam_lista_tabu = 100
# (226, [7, 4, 5, 3, 1, 22, 0, 14, 26, 17, 21, 29, 9, 2, 27, 28, 16, 25, 12, 24, 20, 10, 13, 23, 19, 11, 18, 15, 6, 8, 7])


