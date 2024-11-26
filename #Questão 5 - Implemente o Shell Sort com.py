#Questão 5 - Implemente o Shell Sort com diferentes sequências de intervalo (ex.: Shell, Knuth, Hibbard). Compare os tempos de execução.

import time

def shell_sort(arr, gap_sequence):
    """
    Implementa o algoritmo Shell Sort com uma sequência de gaps fornecida.
    
    :param arr: Lista de elementos a ser ordenada.
    :param gap_sequence: Sequência de gaps (intervalos) a ser utilizada.
    :return: Lista ordenada.
    """
    n = len(arr)
    gaps = gap_sequence(n)

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    return arr


def shell_gap(n):
    """Gap sequence usada no algoritmo original de Shell: n//2, n//4, ..., 1"""
    gap = n // 2
    while gap > 0:
        yield gap
        gap //= 2


def knuth_gap(n):
    """Gap sequence de Knuth: (3^k - 1) / 2 até que seja menor que n"""
    gap = 1
    gaps = []
    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    return reversed(gaps)


def hibbard_gap(n):
    """Gap sequence de Hibbard: 2^k - 1 até que seja menor que n"""
    gap = 1
    k = 1
    gaps = []
    while gap < n:
        gaps.append(gap)
        k += 1
        gap = 2**k - 1
    return reversed(gaps)


def benchmark_shell_sort():
    """
    Compara o tempo de execução do Shell Sort usando diferentes sequências de gaps.
    """
    import random

    # Gerar uma lista aleatória de 10.000 elementos
    arr_size = 10000
    random.seed(0)
    original_list = [random.randint(1, arr_size) for _ in range(arr_size)]

    # Definir diferentes sequências de gaps para comparação
    sequences = {
        "Shell": shell_gap,
        "Knuth": knuth_gap,
        "Hibbard": hibbard_gap,
    }

    # Realizar benchmarks para cada sequência
    for name, gap_sequence in sequences.items():
        arr = original_list[:]
        start_time = time.time()
        shell_sort(arr, gap_sequence)
        end_time = time.time()
        print(f"{name} Sequence - Tempo de execução: {end_time - start_time:.5f} segundos")


# Executar benchmarks
if __name__ == "__main__":
    benchmark_shell_sort()

#Resultado do teste:
#Shell Sequence - Tempo de execução: 0.03499 segundos
#Knuth Sequence - Tempo de execução: 0.04208 segundos
#Hibbard Sequence - Tempo de execução: 0.04446 segundos