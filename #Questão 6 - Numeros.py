#Questão 6 - Numeros

def merge_sort_numbers(arr):
    """
    Implementa o algoritmo de Merge Sort para ordenar uma lista de números inteiros.
    
    :param arr: Lista de números inteiros a ser ordenada.
    :return: Lista ordenada de números inteiros.
    """
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    mid = len(arr) // 2
    left_half = merge_sort_numbers(arr[:mid])
    right_half = merge_sort_numbers(arr[mid:])

    # Combina as metades ordenadas
    return merge_numbers(left_half, right_half)


def merge_numbers(left, right):
    """
    Combina duas listas de números inteiros ordenadas.
    
    :param left: Primeira metade ordenada.
    :param right: Segunda metade ordenada.
    :return: Lista combinada e ordenada.
    """
    sorted_list = []
    i = j = 0

    # Combina até que uma das listas se esgote
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Adiciona o restante dos elementos
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list


# Teste para Merge Sort com números inteiros
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    sorted_numbers = merge_sort_numbers(numbers)
    print(f"Lista ordenada (números): {sorted_numbers}")
