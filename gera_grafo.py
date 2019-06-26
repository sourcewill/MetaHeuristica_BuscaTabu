# Por: William Rodrigues

from random import randint

#---------------------------------------------------------------------------------------------------

# Retorna uma matriz de adj de um grafo gerado com n cidades
# Usado para gerar casos de teste

# num_cidades : Número de cidades
# dist_min : distância mínima que uma cidade pode ter em relação a outra
# dist_max : distância máxima que uma cidade pode ter em relação a outra

def gera_grafo(num_cidades, dist_min, dist_max):

	matriz_adj = []

	#Inicializa toda matriz quadrada
	for _ in range(num_cidades):
		cidade = []
		for _ in range(num_cidades):
			cidade.append(0)
		matriz_adj.append(cidade)

	# Preenche a distância entre as cidades
	for i in range(num_cidades):
		for j in range(num_cidades):
			if i != j:
				aleatorio = randint(dist_min, dist_max)
				matriz_adj[i][j] = aleatorio
				matriz_adj[j][i] = aleatorio

	# Exibe grafo gerado
	print("\n")
	print(matriz_adj)

	# Salva o grafo gerado em um arquivo de texto
	arq = open("grafo_{}_cidades.txt".format(num_cidades), "w")
	arq.write(str(matriz_adj))
	arq.close()

	print("\n---> Arquivo 'grafo_{}_cidades.txt' criado no diretório atual.".format(num_cidades))

	return matriz_adj

#---------------------------------------------------------------------------------------------------

# Executa função geradora
gera_grafo(30, 1, 100)
