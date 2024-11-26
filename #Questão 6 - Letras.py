#Questão 6 - Letras

# merge_sort_strings.py

def merge_sort_strings(arr):
    """
    Implementa o algoritmo de Merge Sort para ordenar uma lista de strings em ordem alfabética.
    
    :param arr: Lista de strings a ser ordenada.
    :return: Lista ordenada de strings.
    """
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    mid = len(arr) // 2
    left_half = merge_sort_strings(arr[:mid])
    right_half = merge_sort_strings(arr[mid:])

    # Combina as metades ordenadas
    return merge_strings(left_half, right_half)


def merge_strings(left, right):
    """
    Combina duas listas de strings ordenadas.
    
    :param left: Primeira metade ordenada.
    :param right: Segunda metade ordenada.
    :return: Lista combinada e ordenada.
    """
    sorted_list = []
    i = j = 0

    # Combina até que uma das listas se esgote
    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():  # Comparação alfabética, ignorando maiúsculas/minúsculas
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Adiciona o restante dos elementos
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list


# Teste para Merge Sort com strings
if __name__ == "__main__":
    strings = ["Banana", "apple", "Orange", "grape", "Mango"]
    sorted_strings = merge_sort_strings(strings)
    print(f"Lista ordenada (strings): {sorted_strings}")
