#Questão 19 -    - Crie gráficos para ilustrar como os algoritmos de ordenação (Merge Sort, Quick Sort, Selection Sort) reorganizam os elementos a cada etapa.

import matplotlib.pyplot as plt
import random
import time

# Função para mostrar o gráfico
def plot(arr, title):
    plt.clf()  # Limpa a figura antes de desenhar
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.pause(0.5)  # Pausa para mostrar a mudança

# --- Merge Sort (com visualização) ---
def merge_sort(arr, title="Merge Sort"):
    def merge(left, right):
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, title)
        merge_sort(right_half, title)

        arr[:] = merge(left_half, right_half)
        plot(arr, title)
    return arr

# --- Quick Sort (com visualização) ---
def quick_sort(arr, title="Quick Sort"):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    plot(arr, title)
    return arr

# --- Selection Sort (com visualização) ---
def selection_sort(arr, title="Selection Sort"):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plot(arr, title)
    return arr

# Função para testar e plotar os gráficos
def test_sorting_algorithms():
    arr = random.sample(range(1, 101), 10)  # Lista de 10 números aleatórios
    print("Original:", arr)

    # Visualizando Merge Sort
    plt.figure(figsize=(10, 6))
    merge_sort(arr.copy(), "Merge Sort")
    plt.show()

    # Visualizando Quick Sort
    arr = random.sample(range(1, 101), 10)  # Reinicializando a lista
    plt.figure(figsize=(10, 6))
    quick_sort(arr.copy(), "Quick Sort")
    plt.show()

    # Visualizando Selection Sort
    arr = random.sample(range(1, 101), 10)  # Reinicializando a lista
    plt.figure(figsize=(10, 6))
    selection_sort(arr.copy(), "Selection Sort")
    plt.show()

# Executando a função
test_sorting_algorithms()
