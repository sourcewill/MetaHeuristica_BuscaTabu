# Matriz quadrada com 11 cidades e as distâncias entre elas
cities = [
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
def greedy_closest_neighbor(cities, initial=0):
    # Inicializa a rota com a cidade inicial e a distancia total com zero
    current = initial
    route = [current]
    total_distance = 0

    # Repita para o número de cidades - 1
    # A primeira cidade já foi adicionada na rota
    for _ in range(len(cities) - 1):

        # Pega a linha da matriz que representa os vizinhos da cidade atual (current)
        neighbours = cities[current]

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
    total_distance += cities[current][initial]

    return (total_distance, route)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais próxima
def greedy_closest_insertion(cities):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(cities) - 3):

        vizinho_mais_proximo = None
        cidade_vizinho_mais_proximo = None
        melhor_distancia = float("inf")

        # Para cada cidade no ciclo:
        # Encontra o vizinho mais proximo de qualquer vértice do ciclo
        for indice_atual, cidade in enumerate(ciclo):

            # Para cada vizinho da cidade atual
            vizinhos = cities[cidade]
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
        peso_anterior = cities[cidade_vizinho_mais_proximo][vizinho_mais_proximo] + cities[vizinho_mais_proximo][ciclo[indice_anterior]] - cities[cidade_vizinho_mais_proximo][ciclo[indice_anterior]]
        peso_proxima = cities[cidade_vizinho_mais_proximo][vizinho_mais_proximo] + cities[vizinho_mais_proximo][ciclo[indice_proximo]] - cities[cidade_vizinho_mais_proximo][ciclo[indice_proximo]]

        # Insere o vértice no ciclo onde for menos custoso
        if peso_anterior < peso_proxima:
            ciclo.insert(indice_anterior + 1, vizinho_mais_proximo)
        else:
            ciclo.insert(indice_cidade_vizinho_mais_proximo + 1, vizinho_mais_proximo)

    # Insere e completa o ciclo com o vértice inicial
    ciclo.append(ciclo[0])

    # Calcula a distancia
    distancia_total = calcula_custo_caminho(ciclo, cities)

    return (distancia_total, ciclo)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais distante
def greedy_further_insertion(cities):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(cities) - 3):

        vizinho_mais_distante = None
        cidade_vizinho_mais_distante = None
        maior_distancia = float("-inf")

        # Para cada cidade no ciclo:
        # Encontra o vizinho mais distante de qualquer vértice do ciclo
        for indice_atual, cidade in enumerate(ciclo):

            # Para cada vizinho da cidade atual
            vizinhos = cities[cidade]
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
        peso_anterior = cities[cidade_vizinho_mais_distante][vizinho_mais_distante] + cities[vizinho_mais_distante][ciclo[indice_anterior]] - cities[cidade_vizinho_mais_distante][ciclo[indice_anterior]]
        peso_proxima = cities[cidade_vizinho_mais_distante][vizinho_mais_distante] + cities[vizinho_mais_distante][ciclo[indice_proximo]] - cities[cidade_vizinho_mais_distante][ciclo[indice_proximo]]

        # Insere o vértice no ciclo onde for menos custoso
        if peso_anterior < peso_proxima:
            ciclo.insert(indice_anterior + 1, vizinho_mais_distante)
        else:
            ciclo.insert(indice_cidade_vizinho_mais_distante + 1, vizinho_mais_distante)

    # Insere e completa o ciclo com o vértice inicial
    ciclo.append(ciclo[0])

    # Calcula a distancia total
    distancia_total = calcula_custo_caminho(ciclo, cities)

    return (distancia_total, ciclo)

#---------------------------------------------------------------------------------------------------

# Heurística: Inserção mais barata
def greedy_cheapest_insertion(cities):

    ciclo = [0, 1, 2] # Ciclo inicial

    # Executa o número de cidades-3 vezes (pois o ciclo ja inicia com 3 cidades)
    for _ in range(len(cities) - 3):

        melhor_peso = float("inf")

        # Para cada cidade no ciclo
        for indice_atual, cidade in enumerate(ciclo):      

            # Encontra os índices no ciclo das cidades (anteriro e próxima)
            indice_anterior = anterior_vet_circular(indice_atual, len(ciclo))
            indice_proximo = proximo_vet_circular(indice_atual, len(ciclo))
            
            cidade_anterior = ciclo[indice_anterior]
            cidade_proxima = ciclo[indice_proximo]

            # Para cada "i" vizinho da cidade atual que ainda não está no ciclo
            vizinhos = cities[cidade]
            for i in range(len(vizinhos)):
                if i not in ciclo:

                    # Calcula o peso para inserir a cidade entre a anterior e a próxima
                    peso_anterior = cities[cidade][i] + cities[i][cidade_anterior] - cities[cidade][cidade_anterior]
                    peso_proxima = cities[cidade][i] + cities[i][cidade_proxima] - cities[cidade][cidade_proxima]

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
    distancia_total = calcula_custo_caminho(ciclo, cities)

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
            #print("Melhor custo ate o momento:", custo_melhor_solucao)        

    return (custo_melhor_solucao, melhor_solucao)

#---------------------------------------------------------------------------------------------------

# Executando Heurísticas
print("\nVizinho mais próximo:\n", greedy_closest_neighbor(cities))
print("Inserção mais próxima:\n", greedy_closest_insertion(cities))
print("Inserção mais distante:\n", greedy_further_insertion(cities))
print("Inserção mais barata:\n", greedy_cheapest_insertion(cities))

# Executando métodos de geração de vizinhança
print("\n\nVizinhança (Troca de consecutivos)\n", vizinhanca_troca_consecutivos([1, 2, 3, 4, 1]))
print("\n\nVizinhança (Troca de dois quaisquer)\n", vizinhanca_troca_dois_quaisquer([1, 2, 3, 4, 1]))
print("\n\nVizinhança (Troca de tres quaisquer)\n", vizinhanca_troca_tres_quaisquer([1, 2, 3, 4, 1]))

# Gerando solução inicial com uma Heurística para usar na Busca Tabu
solucao_inicial = greedy_cheapest_insertion(cities)[1]

# Executando Busca Tabu (Meta-Heurística)
print("\nBusca Tabu:\n", busca_tabu(solucao_inicial, cities, 10, 5))

