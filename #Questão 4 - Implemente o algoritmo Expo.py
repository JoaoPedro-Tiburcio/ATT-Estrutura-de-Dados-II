#Questão 4 - Implemente o algoritmo Exponential Search para localizar um elemento em uma lista ordenada.

def exponential_search(arr, value):
    """
    Implementa o algoritmo de Exponential Search.
    
    :param arr: Lista ordenada de elementos.
    :param value: Valor a ser buscado.
    :return: Índice do valor encontrado ou -1 se não encontrado.
    """
    if len(arr) == 0:
        return -1

    # Se o primeiro elemento é o alvo
    if arr[0] == value:
        return 0

    # Encontra o intervalo onde o elemento pode estar
    index = 1
    while index < len(arr) and arr[index] <= value:
        index *= 2

    # Realiza busca binária no intervalo identificado
    return binary_search_in_range(arr, value, index // 2, min(index, len(arr) - 1))


def binary_search_in_range(arr, value, low, high):
    """
    Busca binária para Exponential Search dentro de um intervalo específico.
    
    :param arr: Lista ordenada de elementos.
    :param value: Valor a ser buscado.
    :param low: Limite inferior do intervalo.
    :param high: Limite superior do intervalo.
    :return: Índice do valor encontrado ou -1 se não encontrado.
    """
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Teste para Exponential Search
if __name__ == "__main__":
    ordered_list = [10, 15, 21, 30, 42, 55, 60, 78, 81, 95]
    target_value = 55
    result = exponential_search(ordered_list, target_value)
    if result != -1:
        print(f"Exponential Search encontrou o valor {target_value} no índice {result}")
    else:
        print(f"Exponential Search não encontrou o valor {target_value}")



