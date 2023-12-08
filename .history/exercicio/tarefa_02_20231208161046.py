def troco_guloso(valor, moedas):
    # Se o valor do troco for zero, não são necessárias moedas
    if valor == 0:
        return 0
    
    min_moedas = float('inf')  # Inicializa o número mínimo de moedas com um valor muito grande
    
    for moeda in moedas:
        if moeda <= valor:
            # Chama recursivamente a função para calcular o número mínimo de moedas
            # necessário para o troco restante após usar uma moeda atual
            qtd_moedas = 1 + troco_guloso(valor - moeda, moedas)
            
            # Atualiza o número mínimo de moedas, se necessário
            if qtd_moedas < min_moedas:
                min_moedas = qtd_moedas
                
    return min_moedas

# Input dos valores
troco = int(input("Digite o valor do troco: "))
moedas_algorithia = list(map(int, input("Digite os valores das moedas separados por espaço: ").split()))

# Chama a função para encontrar o número mínimo de moedas usando o algoritmo guloso recursivo
print("Número mínimo de moedas usando o algoritmo guloso recursivo:", troco_guloso(troco, moedas_algorithia))
