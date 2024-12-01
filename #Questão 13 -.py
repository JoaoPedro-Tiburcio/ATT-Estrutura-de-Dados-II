#Questão 13 - Comparação de Algoritmos de Ordenação 

import time
import random
import math

# --- Algoritmos de Ordenação ---

# Variáveis globais para contar comparações
comparisons = 0

def reset_comparisons():
    global comparisons
    comparisons = 0

def shell_sort(arr):
    global comparisons
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def merge_sort(arr):
    global comparisons
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def selection_sort(arr):
    global comparisons
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr, low, high):
    global comparisons
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    global comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def bucket_sort(arr):
    global comparisons
    if len(arr) == 0:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index == len(arr):  # Avoid index out of range
            index -= 1
        buckets[index].append(num)

    for i in range(len(buckets)):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def radix_sort(arr):
    global comparisons
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    global comparisons
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# --- Função de Análise de Algoritmos de Ordenação ---

def analyze_sort_algorithms():
    sizes = [10, 15, 20]
    algorithms = {
        "Shell Sort": shell_sort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Bucket Sort": bucket_sort,
        "Radix Sort": radix_sort,
    }

    results = []

    for size in sizes:
        arr = random.sample(range(size * 10), size)
        for name, algo in algorithms.items():
            reset_comparisons()
            arr_copy = arr[:]
            start_time = time.time()
            if name == "Quick Sort":
                algo(arr_copy, 0, len(arr_copy) - 1)  # Passa low e high
            elif name == "Bucket Sort" or name == "Radix Sort":
                arr_copy = algo(arr_copy)  # Bucket e Radix retornam o array ordenado
            else:
                algo(arr_copy)  # Algoritmos que ordenam in-place
            duration = time.time() - start_time
            results.append((size, name, duration, comparisons))

    # Formatação simples da tabela
    print(f"{'Tamanho':<10}{'Algoritmo':<20}{'Tempo (s)':<15}{'Comparações':<15}")
    print("-" * 60)
    for size, name, duration, comp in results:
        print(f"{size:<10}{name:<20}{duration:<15.6f}{comp:<15}")

if __name__ == "__main__":
    print("\n### Tabela Comparativa de Algoritmos de Ordenação ###\n")
    analyze_sort_algorithms()
