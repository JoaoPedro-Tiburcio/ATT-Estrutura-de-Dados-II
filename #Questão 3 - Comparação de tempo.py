#Questão 3 - Comparação de tempo

import time
import random
import math

# Função Jump Search
def jump_search(arr, value):
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

# Função Binary Search
def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Valor não encontrado

# Função para medir o tempo de execução
def measure_time(search_function, arr, value):
    start_time = time.time()
    search_function(arr, value)
    end_time = time.time()
    return end_time - start_time

# Listas de tamanhos variados
sizes = [10, 105, 1240, 20000, 103050]
results = []

for size in sizes:
    # Criar lista ordenada aleatória
    arr = sorted(random.sample(range(size * 10), size))
    value = arr[size // 2]  # Valor a ser buscado está no meio da lista

    # Medir tempo de execução para Jump Search
    jump_time = measure_time(jump_search, arr, value)
    
    # Medir tempo de execução para Binary Search
    binary_time = measure_time(binary_search, arr, value)
    
    results.append((size, jump_time, binary_time))

# Exibir resultados
for size, jump_time, binary_time in results:
    print(f"Tamanho da lista: {size}")
    print(f"Tempo de Jump Search: {jump_time:.10f} segundos")
    print(f"Tempo de Binary Search: {binary_time:.10f} segundos")
    print()
