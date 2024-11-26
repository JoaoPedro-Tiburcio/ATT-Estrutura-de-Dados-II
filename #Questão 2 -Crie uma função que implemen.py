#Questão 2 -Crie uma função que implemente o Interpolation Search e teste-a em listas ordenadas com intervalos uniformes e não uniformes. Compare com o Binary Search.

def interpolation_search(arr, value):
    """
    Implementa o algoritmo de Interpolation Search.
    
    :param arr: Lista ordenada de elementos.
    :param value: Valor a ser buscado.
    :return: Índice do valor encontrado ou -1 se não encontrado.
    """
    low = 0
    high = len(arr) - 1
    iterations = 0  # Para contar o número de iterações

    while low <= high and arr[low] <= value <= arr[high]:
        iterations += 1

        # Evita divisão por zero
        if arr[high] == arr[low]:
            if arr[low] == value:
                print(f"Interpolation Search encontrou em {iterations} iterações")
                return low
            break

        # Fórmula de interpolação para estimar a posição
        pos = low + ((value - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if pos < 0 or pos >= len(arr):
            break

        # Comparação do valor estimado com o valor procurado
        if arr[pos] == value:
            print(f"Interpolation Search encontrou em {iterations} iterações")
            return pos
        elif arr[pos] < value:
            low = pos + 1
        else:
            high = pos - 1

    print(f"Interpolation Search falhou após {iterations} iterações")
    return -1


def binary_search(arr, value):
    """
    Implementa o algoritmo de Binary Search.
    
    :param arr: Lista ordenada de elementos.
    :param value: Valor a ser buscado.
    :return: Índice do valor encontrado ou -1 se não encontrado.
    """
    low = 0
    high = len(arr) - 1
    iterations = 0  # Para contar o número de iterações

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == value:
            print(f"Binary Search encontrou em {iterations} iterações")
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Binary Search falhou após {iterations} iterações")
    return -1


# Função de teste para comparar os algoritmos
def test_search_algorithms():
    # Listas de teste
    uniform_list = list(range(10, 101, 10))  # [10, 20, 30, ... 100]
    non_uniform_list = [10, 15, 21, 30, 42, 55, 60, 78, 81, 95]

    # Valor a ser pesquisado
    target_value = 55

    print("Teste com lista de intervalos uniformes:")
    print("Interpolation Search:")
    interpolation_search(uniform_list, target_value)
    print("Binary Search:")
    binary_search(uniform_list, target_value)

    print("\nTeste com lista de intervalos não uniformes:")
    print("Interpolation Search:")
    interpolation_search(non_uniform_list, target_value)
    print("Binary Search:")
    binary_search(non_uniform_list, target_value)


# Executa os testes
test_search_algorithms()

#Resulatdo da execução
#Teste com lista de intervalos uniformes:
#Interpolation Search: #
#Interpolation Search falhou após 1 iterações
#Binary Search:
#Binary Search falhou após 3 iterações

#Teste com lista de intervalos não uniformes:
#Interpolation Search:
#Interpolation Search encontrou em 2 iterações
#Binary Search:
#Binary Search encontrou em 3 iterações