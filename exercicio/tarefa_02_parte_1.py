
def calcular_troco_minimo_recursivo(valor_troco, tipos_de_moedas):
    # Se o troco for zero, não são necessárias moedas
    if valor_troco == 0:
        return 0, []

    menor_qtd_moedas = float('inf')  # Inicialização da menor quantidade de moedas como infinito
    melhor_combinacao = None  # Inicialização da melhor combinação de moedas como nula

    # Para cada tipo de moeda disponível, procuramos a melhor combinação
    for tipo_moeda in sorted(tipos_de_moedas, reverse=True):
        if tipo_moeda <= valor_troco:
            # Chamada recursiva para calcular o troco do valor restante
            qtd_moedas, combinacao_resto = calcular_troco_minimo_recursivo(valor_troco - tipo_moeda, tipos_de_moedas)
            qtd_moedas += 1  # Adicionamos uma moeda do tipo atual

            # Verificamos se esta combinação é melhor que a anterior
            if qtd_moedas < menor_qtd_moedas:
                menor_qtd_moedas = qtd_moedas
                melhor_combinacao = [tipo_moeda] + combinacao_resto

    return menor_qtd_moedas, melhor_combinacao

# Valores utilizados para demonstrar o cálculo do troco mínimo
valor_da_compra = 37
tipos_de_moedas_usadas = [1, 5, 10, 21, 25]

# Chamada da função para calcular o troco mínimo
qtd_min_moedas, combinacao_usada = calcular_troco_minimo_recursivo(valor_da_compra, tipos_de_moedas_usadas)

# Impressão dos resultados
print(f"Número mínimo de moedas: {qtd_min_moedas}")
print(f"Conjunto de moedas utilizado: {combinacao_usada}")
