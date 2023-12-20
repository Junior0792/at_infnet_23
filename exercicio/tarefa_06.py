def particionar_tres_vias(arr, baixo, alto, pivo1, pivo2):
    i = baixo
    j = baixo
    k = alto

    while j <= k:
        if arr[j] < pivo1:
            # Troca elementos menores que o primeiro pivô para a região dos menores
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif pivo1 <= arr[j] <= pivo2:
            # Elementos entre os dois pivôs permanecem na região do meio
            j += 1
        else:
            # Troca elementos maiores que o segundo pivô para a região dos maiores
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1

    return i, k


def quicksort_tres_vias(arr, baixo, alto):
    if baixo < alto:
        # Seleciona os pivôs inicial e final
        pivo1 = arr[baixo]
        pivo2 = arr[alto]

        if pivo1 > pivo2:
            pivo1, pivo2 = pivo2, pivo1

        # Particiona a lista em três partes
        menor, maior = particionar_tres_vias(arr, baixo + 1, alto - 1, pivo1, pivo2)

        # Coloca os pivôs na posição correta
        arr[baixo], arr[menor - 1] = arr[menor - 1], arr[baixo]
        arr[alto], arr[maior + 1] = arr[maior + 1], arr[alto]

        # Chama a ordenação recursiva para as três regiões
        quicksort_tres_vias(arr, baixo, menor - 1)
        quicksort_tres_vias(arr, menor, maior)
        quicksort_tres_vias(arr, maior + 1, alto)


# Exemplo de uso:
arr = [4, 2, 7, 3, 1, 6, 5]
print("Array antes da ordenação:", arr)
quicksort_tres_vias(arr, 0, len(arr) - 1)
print("Array depois da ordenação:", arr)

