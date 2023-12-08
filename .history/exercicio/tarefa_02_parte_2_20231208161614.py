def troco_programacao_dinamica(valor, moedas):
    # Inicializa uma lista para armazenar o número mínimo de moedas para cada valor de troco
    qtd_moedas = [float('inf')] * (valor + 1)
    qtd_moedas[0] = 0  # Para o troco zero, não são necessárias moedas
    
    # Itera sobre todos os valores de troco de 1 até o valor desejado
    for i in range(1, valor + 1):
        # Para cada valor de troco, percorre todas as moedas disponíveis
        for moeda in moedas:
            if moeda <= i:
                # Atualiza o número mínimo de moedas necessário para o valor de troco atual
                qtd_moedas[i] = min(qtd_moedas[i], 1 + qtd_moedas[i - moeda])
    
    return qtd_moedas[valor]

# Input dos valores
troco = int(input("Digite o valor do troco: "))
moedas_algorithia = list(map(int, input("Digite os valores das moedas separados por espaço: ").split()))

# Chama a função para encontrar o número mínimo de moedas usando programação dinâmica
print("Número mínimo de moedas usando programação dinâmica:", troco_programacao_dinamica(troco, moedas_algorithia))
