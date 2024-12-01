#Questão 3 - 

import math

def jump_search(arr, value):
    """
    Implementa o algoritmo de Jump Search para encontrar um elemento em uma lista ordenada.
    
    :param arr: Lista ordenada de elementos.
    :param value: Valor a ser buscado.
    :return: Índice do valor encontrado ou -1 se não encontrado.
    """
    n = len(arr)
    step = int(math.sqrt(n))  # Tamanho do salto ideal
    prev = 0

    # Saltar blocos até encontrar um intervalo que possa conter o valor
    while arr[min(step, n) - 1] < value:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Valor não encontrado

    # Busca linear dentro do bloco identificado
    for idx in range(prev, min(step, n)):
        if arr[idx] == value:
            return idx

    return -1  # Valor não encontrado


# Teste para o Jump Search
if __name__ == "__main__":
    ordered_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    target_value = 15
    result = jump_search(ordered_list, target_value)
    if result != -1:
        print(f"Jump Search encontrou o valor {target_value} no índice {result}")
    else:
        print(f"Jump Search não encontrou o valor {target_value}")

