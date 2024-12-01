#Questão 12 - Construa uma tabela comparativa

import time
import random
import math

# --- Algoritmos de Busca ---

def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    bound = 1
    while bound < n and arr[bound] <= target:
        bound *= 2
    return binary_search(arr, bound // 2, min(bound, n) - 1, target)

# --- Função de Análise de Desempenho ---

def analyze_search_algorithms():
    sizes = [1000, 5000, 10000]
    algorithms = {
        "Binary Search": binary_search,
        "Interpolation Search": interpolation_search,
        "Jump Search": jump_search,
        "Exponential Search": exponential_search,
    }
    
    target = -1  # Elemento inexistente para análise de pior caso
    print(f"{'Tamanho':<10}{'Algoritmo':<20}{'Tempo (s)':<10}")
    print("-" * 40)
    
    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        for name, algo in algorithms.items():
            start_time = time.time()
            if name == "Binary Search" or name == "Exponential Search":
                algo(arr, 0, len(arr) - 1, target)
            else:
                algo(arr, target)
            duration = time.time() - start_time
            print(f"{size:<10}{name:<20}{duration:<10.6f}")

if __name__ == "__main__":
    print("\n### Tabela Comparativa de Algoritmos de Busca ###\n")
    analyze_search_algorithms()


