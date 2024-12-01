#Questão 11 - Desenvolva o algoritmo Ternary Search

import time
import random

def ternary_search(arr, left, right, target):
    """Ternary Search Recursivo."""
    if left > right:
        return -1  # Elemento não encontrado

    # Dividindo a lista em três partes
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Comparando o elemento alvo com os pivôs
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search(arr, left, mid1 - 1, target)
    elif target > arr[mid2]:
        return ternary_search(arr, mid2 + 1, right, target)
    else:
        return ternary_search(arr, mid1 + 1, mid2 - 1, target)

def binary_search(arr, left, right, target):
    """Binary Search Recursivo."""
    if left > right:
        return -1  # Elemento não encontrado

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

def analyze_performance():
    """Analisa o desempenho do Ternary Search vs Binary Search."""
    list_sizes = [25, 50, 75]
    target = -1  # Elemento inexistente para análise de pior caso
    
    for size in list_sizes:
        test_list = sorted(random.sample(range(size * 10), size))
        print(f"\nTamanho da lista: {size}")
        
        # Teste com Ternary Search
        start = time.time()
        ternary_search(test_list, 0, len(test_list) - 1, target)
        ternary_duration = time.time() - start
        print(f"Ternary Search: {ternary_duration:.6f} segundos")
        
        # Teste com Binary Search
        start = time.time()
        binary_search(test_list, 0, len(test_list) - 1, target)
        binary_duration = time.time() - start
        print(f"Binary Search: {binary_duration:.6f} segundos")

if __name__ == "__main__":
    # Exemplo de uso
    test_list = [2, 3, 5, 10, 14, 18, 21, 27, 32, 39]
    target = 14

    print("Lista:", test_list)
    print(f"Ternary Search - Índice do {target}:", ternary_search(test_list, 0, len(test_list) - 1, target))
    print(f"Binary Search - Índice do {target}:", binary_search(test_list, 0, len(test_list) - 1, target))
    
    # Análise de desempenho
    print("\n### Análise de Desempenho ###")
    analyze_performance()
