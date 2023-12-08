def particionar_tres_vias(arr, baixo, alto):
    # Verifica e troca a ordem dos elementos baixo e alto, se necessário
    if arr[baixo] > arr[alto]:
        arr[baixo], arr[alto] = arr[alto], arr[baixo]

    # Define os pivôs
    pivô1 = arr[baixo]
    pivô2 = arr[alto]

    # Inicialização dos índices para particionamento
    esquerda = baixo + 1
    direita = alto - 1
    i = baixo + 1

    while i <= direita:
        if arr[i] < pivô1:
            arr[i], arr[esquerda] = arr[esquerda], arr[i]
            esquerda += 1
            i += 1
        elif arr[i] > pivô2:
            arr[i], arr[direita] = arr[direita], arr[i]
            direita -= 1
        else:
            i += 1

    # Coloca os pivôs em suas posições corretas
    arr[esquerda - 1], arr[baixo] = arr[baixo], arr[esquerda - 1]
    arr[direita + 1], arr[alto] = arr[alto], arr[direita + 1]

    return esquerda - 1, direita + 1


def quicksort_tres_vias(arr, baixo, alto):
    if baixo < alto:
        esquerda, direita = particionar_tres_vias(arr, baixo, alto)
        quicksort_tres_vias(arr, baixo, esquerda - 1)
        quicksort_tres_vias(arr, esquerda + 1, direita - 1)
        quicksort_tres_vias(arr, direita + 1, alto)


# Entrada dos dados
n = int(input("Digite o tamanho da lista: "))
lista = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))

# Chamada da função de ordenação
quicksort_tres_vias(lista, 0, n - 1)

# Saída dos dados ordenados
print("Lista ordenada:", lista)
