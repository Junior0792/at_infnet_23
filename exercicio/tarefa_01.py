import random

# Função para gerar um indivíduo aleatório
def gerar_individuo(tamanho):
    return [random.randint(0 , 1) for _ in range(tamanho)]

# Função para gerar a população inicial
def gerar_populacao_inicial(tamanho_populacao, tamanho_individuo):
    return [gerar_individuo(tamanho_individuo) for _ in range(tamanho_populacao)]

# Função para calcular a aptidão de um indivíduo
def calcular_aptidao(individuo):
    return sum(individuo)

# Função para realizar o crossover entre dois indivíduos
def crossover(individuo1, individuo2):
    ponto_crossover = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    filho2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]
    return filho1, filho2

# Função para realizar a mutação em um indivíduo
def mutacao(individuo):
    qtd_genes_mutacao = random.randint(1, 3)
    for _ in range(qtd_genes_mutacao):
        indice = random.randint(0, len(individuo) - 1)
        individuo[indice] = 1 if individuo[indice] == 0 else 0

# Função para ordenar a população com base na aptidão
def ordenar_populacao(populacao):
    return sorted(populacao, key=calcular_aptidao, reverse=True)

# Parâmetros do algoritmo genético
tamanho_populacao = 20
tamanho_individuo = 6
max_geracoes = 1000

# Gerar população inicial
populacao = gerar_populacao_inicial(tamanho_populacao, tamanho_individuo)

for geracao in range(max_geracoes):
    # Calcular aptidão
    aptidoes = [calcular_aptidao(individuo) for individuo in populacao]

    # Verificar se a função objetivo foi alcançada
    if max(aptidoes) == tamanho_individuo:
        print(f"Função objetivo alcançada na geração {geracao + 1}")
        break

    # Selecionar os indivíduos mais aptos
    populacao = ordenar_populacao(populacao)[:tamanho_populacao]

    # Realizar crossover
    nova_populacao = []
    for _ in range(tamanho_populacao // 2):
        pai1, pai2 = random.sample(populacao, 2)
        filho1, filho2 = crossover(pai1, pai2)
        nova_populacao.extend([filho1, filho2])

    # Aplicar mutação
    for individuo in nova_populacao[:len(nova_populacao) // 2]:
        if random.random() < 0.005:  # Probabilidade de mutação de 0,5%
            mutacao(individuo)

    # Atualizar população
    populacao = nova_populacao

# Ordenar a população final antes de encerrar
populacao = ordenar_populacao(populacao)
print("População final ordenada:")
for individuo in populacao:
    print(individuo, "Aptidão:", calcular_aptidao(individuo))
