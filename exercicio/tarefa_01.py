import random

# Função para criar a população inicial
def criar_pop(tam_pop, tam_genes):
    return [[random.randint(0, 1) for _ in range(tam_genes)] for _ in range(tam_pop)]

# Função para calcular a aptidão de um indivíduo
def calc_apt(individuo):
    return sum(individuo)

# Função para ordenar a população com base na aptidão
def ordenar(populacao):
    return sorted(populacao, key=calc_apt, reverse=True)

# Função para realizar o crossover entre dois indivíduos
def crossover(ind1, ind2):
    ponto_cross = random.randint(1, len(ind1) - 1)
    novo_ind1 = ind1[:ponto_cross] + ind2[ponto_cross:]
    novo_ind2 = ind2[:ponto_cross] + ind1[ponto_cross:]
    return novo_ind1, novo_ind2

# Função para realizar a mutação em um indivíduo
def mutacao(individuo, taxa_mut):
    for i in range(len(individuo)):
        if random.random() < taxa_mut:
            num_genes_mut = random.randint(1, 3)
            genes_mut = random.sample(range(len(individuo)), num_genes_mut)
            for gene in genes_mut:
                individuo[gene] = 1 if individuo[gene] == 0 else 0
    return individuo

# Solicitar parâmetros do usuário
tam_populacao = int(input("Tamanho da população inicial: "))
tam_genes = int(input("Tamanho dos genes dos indivíduos: "))
max_geracoes = int(input("Número máximo de gerações: "))
taxa_mutacao = float(input("Taxa de mutação (entre 0 e 1): "))

# Gerando população inicial
pop = criar_pop(tam_populacao, tam_genes)

# Execução do algoritmo genético
for geracao in range(max_geracoes):
    pop = ordenar(pop)
    if calc_apt(pop[0]) == tam_genes:
        print("Objetivo alcançado na geração", geracao)
        break
    
    # Seleção dos mais aptos
    pop = pop[:tam_populacao]
    
    # Cruzamento e mutação
    nova_pop = []
    while len(nova_pop) < tam_populacao:
        pai1, pai2 = random.choices(pop, k=2)
        filho1, filho2 = crossover(pai1, pai2)
        filho1 = mutacao(filho1, taxa_mutacao)
        filho2 = mutacao(filho2, taxa_mutacao)
        nova_pop.extend([filho1, filho2])
    
    pop = nova_pop

melhor_ind = ordenar(pop)[0]
print("Melhor indivíduo:", melhor_ind, "Aptidão:", calc_apt(melhor_ind))
