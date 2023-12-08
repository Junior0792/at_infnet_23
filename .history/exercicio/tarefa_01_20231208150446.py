import random

# Função para criar a população inicial
def criar_populacao(tamanho_populacao, tamanho_genes):
    return [[random.randint(0, 1) for _ in range(tamanho_genes)] for _ in range(tamanho_populacao)]

# Função para calcular a aptidão de um indivíduo
def calcular_aptidao(individuo):
    return sum(individuo)

# Função para ordenar a população com base na aptidão
def ordenar_populacao(populacao):
    return sorted(populacao, key=calcular_aptidao, reverse=True)

# Função para realizar o crossover entre dois indivíduos
def crossover(individuo1, individuo2):
    ponto_crossover = random.randint(1, len(individuo1) - 1)
    novo_individuo1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    novo_individuo2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]
    return novo_individuo1, novo_individuo2

# Função para realizar a mutação em um indivíduo
def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            num_genes_mutados = random.randint(1, 3)
            genes_mutados = random.sample(range(len(individuo)), num_genes_mutados)
            for gene in genes_mutados:
                individuo[gene] = 1 if individuo[gene] == 0 else 0
    return individuo

# Parâmetros do algoritmo
tamanho_populacao = 20
tamanho_genes = 6
geracoes_maximas = 1000
taxa_mutacao = 0.005

# Gerando população inicial
populacao = criar_populacao(tamanho_populacao, tamanho_genes)

# Execução do algoritmo genético
for geracao in range(geracoes_maximas):
    populacao = ordenar_populacao(populacao)
    if calcular_aptidao(populacao[0]) == tamanho_genes:
        print("Objetivo alcançado na geração", geracao)
        break
    
    # Seleção dos mais aptos
    populacao = populacao[:tamanho_populacao]
    
    # Cruzamento e mutação
    nova_populacao = []
    while len(nova_populacao) < tamanho_populacao:
        pai1, pai2 = random.choices(populacao, k=2)
        filho1, filho2 = crossover(pai1, pai2)
        filho1 = mutacao(filho1, taxa_mutacao)
        filho2 = mutacao(filho2, taxa_mutacao)
        nova_populacao.extend([filho1, filho2])
    
    populacao = nova_populacao

melhor_individuo = ordenar_populacao(populacao)[0]
print("Melhor indivíduo:", melhor_individuo, "Aptidão:", calcular_aptidao(melhor_individuo))
