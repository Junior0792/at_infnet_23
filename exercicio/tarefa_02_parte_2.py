
def calcular_menor_numero_moedas_programacao_dinamica(valor_troco, tipos_de_moedas):
    # Cria uma tabela para armazenar o número mínimo de moedas para cada valor de troco
    tabela_dp = [float('inf')] * (valor_troco + 1)
    tabela_dp[0] = 0  # O troco de 0 requer 0 moedas

    # Percorre todos os valores de troco de 1 até o valor desejado
    for i in range(1, valor_troco + 1):
        # Para cada valor de troco, verifica todas as moedas disponíveis
        for moeda in tipos_de_moedas:
            if moeda <= i:
                # Atualiza a tabela com o menor número de moedas necessário para o valor de troco atual
                tabela_dp[i] = min(tabela_dp[i], tabela_dp[i - moeda] + 1)

    return tabela_dp[valor_troco]  # Retorna o menor número de moedas necessário para o valor de troco desejado

moedas_algoritmos = [1, 5, 10, 21, 25]
valor_compra = 37
qtd_moedas = calcular_menor_numero_moedas_programacao_dinamica(valor_compra, moedas_algoritmos)

print(f"Número mínimo de moedas: {qtd_moedas}")
